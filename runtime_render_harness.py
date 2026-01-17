import json
import os
from dataclasses import dataclass
from pathlib import Path
from typing import List

from rendering.runtime_render_payload import (
    ByteMemoryReader,
    MemorySegment,
    RuntimeRenderParser,
    ImmediateSubmissionRequest,
)


@dataclass(frozen=True)
class SegmentDump:
    base_address: int
    data_hex: str


@dataclass(frozen=True)
class DispatchDump:
    dispatch_address: int
    segments: List[SegmentDump]


def _parse_int(value) -> int:
    if isinstance(value, int):
        return value
    if isinstance(value, str):
        return int(value, 0)
    raise ValueError(f"invalid int value|value={value}")


def _load_dump(path: Path) -> DispatchDump:
    with path.open("r", encoding="utf-8") as handle:
        payload = json.load(handle)

    dispatch_address = _parse_int(payload["dispatch_address"])
    segments = [
        SegmentDump(base_address=_parse_int(seg["base_address"]), data_hex=seg["data_hex"])
        for seg in payload["segments"]
    ]
    return DispatchDump(dispatch_address=dispatch_address, segments=segments)


def _build_segments(dump: DispatchDump) -> List[MemorySegment]:
    out: List[MemorySegment] = []
    for seg in dump.segments:
        raw = bytes.fromhex(seg.data_hex)
        out.append(MemorySegment(base_address=seg.base_address, data=raw))
    return out


def run(dump_path: str) -> None:
    os.environ["RUNTIME_RENDER_TRACE"] = "1"
    os.environ["RUNTIME_RENDER_NO_DRAW"] = "1"

    dump = _load_dump(Path(dump_path))
    reader = ByteMemoryReader(_build_segments(dump))
    parser = RuntimeRenderParser()

    submission = parser.parse_immediate_submission(
        ImmediateSubmissionRequest(reader=reader, dispatch_address=dump.dispatch_address)
    )
    if submission is None:
        print("runtime_harness|submission=None")
        return

    sample_count = min(3, submission.vertex_count)
    print(
        "runtime_harness|dispatch=0x%08x|payload=0x%08x|verts=%d|sample_positions=%s"
        % (
            submission.dispatch.address,
            submission.payload.address,
            submission.vertex_count,
            submission.positions[:sample_count].tolist(),
        )
    )


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("usage: python runtime_render_harness.py <dump.json>")
        raise SystemExit(2)
    run(sys.argv[1])
