from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, List, Optional, Tuple

from rendering.runtime_render_payload import (
    ByteMemoryReader,
    DispatchParseRequest,
    ImmediateSubmissionRequest,
    MemorySegment,
    RuntimeRenderParser,
    DISPATCH_VTABLE_ADDR,
)

U32 = int


@dataclass(frozen=True)
class DumpSegment:
    base_address: int
    data: bytes

    def to_json_obj(self) -> dict:
        return {
            "base_address": f"0x{self.base_address:08x}",
            "data_hex": self.data.hex(),
        }


def _u32_le(data: bytes, offset: int) -> int:
    return int.from_bytes(data[offset : offset + 4], "little", signed=False)


def _scan_for_u32_value(segments: Iterable[MemorySegment], value: int) -> List[int]:
    hits: List[int] = []
    for seg in segments:
        data = seg.data
        base = seg.base_address
        limit = len(data) - 4
        i = 0
        while i <= limit:
            if _u32_le(data, i) == value:
                hits.append(base + i)
            i += 4
    return hits


def _slice_segment(seg: MemorySegment, start: int, size: int) -> Optional[DumpSegment]:
    seg_start = seg.base_address
    seg_end = seg.base_address + len(seg.data)
    end = start + size
    if start < seg_start or end > seg_end:
        return None
    offset = start - seg_start
    return DumpSegment(base_address=start, data=seg.data[offset : offset + size])


def _collect_minimal_segments(
    segments: List[MemorySegment],
    dispatch_addr: int,
    payload_ptr: int,
    positions_ptr: int,
    normals_ptr: int,
    uvs_ptr: int,
    vertex_count: int,
    stride_pos: int,
    stride_norm: int,
    stride_uv: int,
) -> List[DumpSegment]:
    wanted: List[Tuple[int, int]] = []

    wanted.append((dispatch_addr, 0x40))
    if payload_ptr != 0:
        wanted.append((payload_ptr, 0x80))

    if positions_ptr != 0 and vertex_count > 0:
        wanted.append((positions_ptr, vertex_count * stride_pos))
    if normals_ptr != 0 and vertex_count > 0:
        wanted.append((normals_ptr, vertex_count * stride_norm))
    if uvs_ptr != 0 and vertex_count > 0:
        wanted.append((uvs_ptr, vertex_count * stride_uv))

    wanted = sorted(set(wanted), key=lambda x: x[0])

    dumps: List[DumpSegment] = []
    for start, size in wanted:
        chosen: Optional[DumpSegment] = None
        for seg in segments:
            chosen = _slice_segment(seg, start, size)
            if chosen is not None:
                dumps.append(chosen)
                break
    return dumps


def dump_runtime_dispatch_candidates(
    segments: Iterable[MemorySegment],
    output_dir: str,
    max_candidates: int = 50,
) -> List[str]:
    seg_list = list(segments)
    reader = ByteMemoryReader(seg_list)
    parser = RuntimeRenderParser()

    candidates = _scan_for_u32_value(seg_list, DISPATCH_VTABLE_ADDR)[:max_candidates]

    out = Path(output_dir)
    out.mkdir(parents=True, exist_ok=True)

    written: List[str] = []

    for dispatch_addr in candidates:
        dispatch_obj = parser.parse_dispatch_object(
            request=DispatchParseRequest(reader=reader, address=dispatch_addr)
        )
        if dispatch_obj is None:
            continue

        submission = parser.parse_immediate_submission(
            request=ImmediateSubmissionRequest(reader=reader, dispatch_address=dispatch_addr)
        )
        if submission is None:
            continue

        payload = submission.payload
        stride_pos = 12
        stride_norm = 12
        stride_uv = 8

        dump_segments = _collect_minimal_segments(
            segments=seg_list,
            dispatch_addr=dispatch_addr,
            payload_ptr=dispatch_obj.render_payload_ptr,
            positions_ptr=payload.positions_ptr,
            normals_ptr=getattr(payload, "normals_ptr", 0),
            uvs_ptr=payload.uvs_ptr,
            vertex_count=submission.vertex_count,
            stride_pos=stride_pos,
            stride_norm=stride_norm,
            stride_uv=stride_uv,
        )

        dump_obj = {
            "dispatch_address": f"0x{dispatch_addr:08x}",
            "segments": [s.to_json_obj() for s in dump_segments],
        }

        file_path = out / f"runtime_dispatch_0x{dispatch_addr:08x}.json"
        file_path.write_text(json.dumps(dump_obj, indent=2), encoding="utf-8")
        written.append(str(file_path))

    return written
