# Render Backend and Vertex Format (Current Evidence)

## Immediate-mode submission chain

- `FUN_005b6760` performs a vcall at `+0x2C` on `*(this + 0x14)`.
- Table slot `0x015498C8` (`+0x28` in the `0x015498A0` dispatch table) resolves to `0x00408F99` (`thunk_FUN_005b6760`).
- The immediate path is taken in `FUN_005b6790` when `*(this + 0x10) != 0` and calls:
  - `thunk_FUN_005aadc0(this_00, *(char *)(this + 0x11))`.

## Dispatch object type

- **Unnamed Immediate Render Dispatch Object** (DispatchCarrier == ImmediateSubmitNode).
- Vtable `0x015498A0` with viewer-facing fields `+0x10/+0x11/+0x14`.
- Vtable writes: `0x005b5b5f`, `0x005b5d69`, `0x005b5e81`, `0x005b7031` with offsets `{0x10,0x11,0x14}` on the same base reg.

## Vertex format

No new vertex/index buffer layout evidence is exposed in the B6 indirect callsite scan. The only proven vertex element sizes remain:
- position: float3 (12 bytes) via `FUN_005a43a0`
- normal: float3 (12 bytes) via `FUN_005a4460`
- uv: float2 (8 bytes) via `FUN_005a4530`

## Immediate render payload (FUN_005aadc0)

- Primitive: `GL_TRIANGLE_STRIP` via `glBegin(5)` at `0x005aadc8`.
- Sources:
  - `RenderPayload+0x64` → positions pointer, used for `glVertex3f`.
  - `RenderPayload+0x70` → UV pointer, used for `glTexCoord2f`.
  - `RenderPayload+0x7C` → normals pointer, used for `glNormal3f`.
- Vertex count:
  - `param_1 != 0`: 8 vertices (`CMP EDI,0x40` with `EDI += 0x8`).
  - `param_1 == 0`: 4 vertices (`CMP EDI,0x20` with `EDI += 0x8`).
