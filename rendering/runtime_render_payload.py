from __future__ import annotations

import os
from dataclasses import dataclass
from typing import Iterable, Optional, Protocol

import numpy as np


DISPATCH_VTABLE_ADDR = 0x015498A0


@dataclass(frozen=True)
class MemorySegment:
    base_address: int
    data: bytes


@dataclass(frozen=True)
class ReadBytesRequest:
    address: int
    size: int


@dataclass(frozen=True)
class ReadScalarRequest:
    address: int


@dataclass(frozen=True)
class ReadArrayRequest:
    address: int
    count: int


class RuntimeMemoryReader(Protocol):
    def read_bytes(self, request: ReadBytesRequest) -> bytes:
        ...

    def read_u8(self, request: ReadScalarRequest) -> int:
        ...

    def read_u32(self, request: ReadScalarRequest) -> int:
        ...

    def read_f32_array(self, request: ReadArrayRequest) -> np.ndarray:
        ...


class ByteMemoryReader:
    def __init__(self, segments: Iterable[MemorySegment]) -> None:
        self._segments = list(segments)

    def read_bytes(self, request: ReadBytesRequest) -> bytes:
        segment, offset = self._locate(request.address, request.size)
        return segment.data[offset : offset + request.size]

    def read_u8(self, request: ReadScalarRequest) -> int:
        data = self.read_bytes(ReadBytesRequest(address=request.address, size=1))
        return int.from_bytes(data, byteorder="little", signed=False)

    def read_u32(self, request: ReadScalarRequest) -> int:
        data = self.read_bytes(ReadBytesRequest(address=request.address, size=4))
        return int.from_bytes(data, byteorder="little", signed=False)

    def read_f32_array(self, request: ReadArrayRequest) -> np.ndarray:
        data = self.read_bytes(ReadBytesRequest(address=request.address, size=request.count * 4))
        return np.frombuffer(data, dtype=np.float32)

    def _locate(self, address: int, size: int) -> tuple[MemorySegment, int]:
        for segment in self._segments:
            start = segment.base_address
            end = start + len(segment.data)
            if start <= address and address + size <= end:
                return segment, address - start
        raise ValueError(f"memory read miss|addr=0x{address:08x}|size=0x{size:x}")


@dataclass(frozen=True)
class DispatchParseRequest:
    reader: RuntimeMemoryReader
    address: int


@dataclass(frozen=True)
class PayloadParseRequest:
    reader: RuntimeMemoryReader
    address: int


@dataclass(frozen=True)
class ImmediateSubmissionRequest:
    reader: RuntimeMemoryReader
    dispatch_address: int


@dataclass(frozen=True)
class RuntimeDispatchObject:
    address: int
    vtable: int
    immediate_enabled: int
    immediate_arg: int
    render_payload_ptr: int


@dataclass(frozen=True)
class RuntimeRenderPayload:
    address: int
    positions_ptr: int
    uvs_ptr: int
    normals_ptr: int


@dataclass(frozen=True)
class RuntimeImmediateSubmission:
    dispatch: RuntimeDispatchObject
    payload: RuntimeRenderPayload
    vertex_count: int
    positions: np.ndarray
    normals: np.ndarray
    uvs: np.ndarray


class RuntimeRenderParser:
    def __init__(self) -> None:
        self._trace_enabled = os.getenv("RUNTIME_RENDER_TRACE", "0") == "1"

    def parse_dispatch_object(self, request: DispatchParseRequest) -> Optional[RuntimeDispatchObject]:
        vtable = request.reader.read_u32(ReadScalarRequest(address=request.address))
        if vtable != DISPATCH_VTABLE_ADDR:
            return None
        immediate_enabled = request.reader.read_u8(ReadScalarRequest(address=request.address + 0x10))
        immediate_arg = request.reader.read_u8(ReadScalarRequest(address=request.address + 0x11))
        render_payload_ptr = request.reader.read_u32(ReadScalarRequest(address=request.address + 0x14))
        if self._trace_enabled:
            print(
                "runtime_dispatch|addr=0x%08x|vtable=0x%08x|gate=0x%02x|arg=0x%02x|payload=0x%08x"
                % (
                    request.address,
                    vtable,
                    immediate_enabled,
                    immediate_arg,
                    render_payload_ptr,
                )
            )
            try:
                payload_head = request.reader.read_bytes(
                    ReadBytesRequest(address=render_payload_ptr, size=0x40)
                ).hex()
                print("runtime_payload_head|addr=0x%08x|bytes=%s" % (render_payload_ptr, payload_head))
            except Exception as exc:
                print(
                    "runtime_payload_head_err|addr=0x%08x|err=%s"
                    % (render_payload_ptr, exc)
                )
        return RuntimeDispatchObject(
            address=request.address,
            vtable=vtable,
            immediate_enabled=immediate_enabled,
            immediate_arg=immediate_arg,
            render_payload_ptr=render_payload_ptr,
        )

    def parse_payload(self, request: PayloadParseRequest) -> RuntimeRenderPayload:
        positions_ptr = request.reader.read_u32(ReadScalarRequest(address=request.address + 0x64))
        uvs_ptr = request.reader.read_u32(ReadScalarRequest(address=request.address + 0x70))
        normals_ptr = request.reader.read_u32(ReadScalarRequest(address=request.address + 0x7C))
        return RuntimeRenderPayload(
            address=request.address,
            positions_ptr=positions_ptr,
            uvs_ptr=uvs_ptr,
            normals_ptr=normals_ptr,
        )

    def parse_immediate_submission(self, request: ImmediateSubmissionRequest) -> Optional[RuntimeImmediateSubmission]:
        dispatch = self.parse_dispatch_object(
            DispatchParseRequest(reader=request.reader, address=request.dispatch_address)
        )
        if dispatch is None:
            return None
        if dispatch.immediate_enabled == 0:
            return None
        payload = self.parse_payload(PayloadParseRequest(reader=request.reader, address=dispatch.render_payload_ptr))
        vertex_count = 8 if dispatch.immediate_arg != 0 else 4
        positions = request.reader.read_f32_array(
            ReadArrayRequest(address=payload.positions_ptr, count=vertex_count * 3)
        ).reshape((vertex_count, 3))
        normals = request.reader.read_f32_array(
            ReadArrayRequest(address=payload.normals_ptr, count=vertex_count * 3)
        ).reshape((vertex_count, 3))
        uvs = request.reader.read_f32_array(
            ReadArrayRequest(address=payload.uvs_ptr, count=vertex_count * 2)
        ).reshape((vertex_count, 2))
        return RuntimeImmediateSubmission(
            dispatch=dispatch,
            payload=payload,
            vertex_count=vertex_count,
            positions=positions,
            normals=normals,
            uvs=uvs,
        )
