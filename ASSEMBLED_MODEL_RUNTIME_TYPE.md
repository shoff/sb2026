# Assembled Model Runtime Type (Render Chain)

## Render Chain (Immediate Path)

- **Indirect dispatch table**: `0x015498A0` (entry `+0x28` → `0x015498C8`).
- **Slot +0x28 target**: `0x00408F99` (`thunk_FUN_005b6760`) → `FUN_005b6760`.
- **Immediate helper**: `FUN_005b6790` → `thunk_FUN_005aadc0` (`FUN_005aadc0`).

### Evidence (callsite + dispatch)

- **Indirect callsite**: `0x0045C3D6` in `FUN_0045c3a0` (scan artifact `sb.exe_B6_indirect_calls_015498C8_and_slot28.md`).
  - Instruction: `CALL dword ptr [EDX + 0x28]`.
  - Object pointer at callsite: `ESI` (function parameter `param_1` in decompile).
  - Vtable slot used: `+0x28`, which maps to table entry `0x015498C8` → `0x00408F99` → `FUN_005b6760`.

### Dispatch chain (proven)

```
FUN_0045c3a0 (callsite 0x0045c3d6; vtable slot +0x28)
  -> 0x00408F99 (thunk_FUN_005b6760)
  -> FUN_005b6760
     -> (**(code **)(**(int **)(this + 0x14) + 0x2C))(param_1,param_2,param_3)
        -> 0x0040B979 (thunk_FUN_005b6790)
        -> FUN_005b6790
           -> thunk_FUN_005aadc0(this_00, *(char *)(this + 0x11))
```

### Immediate-path object fields (from FUN_005b6790/FUN_005b6760)

- `this + 0x14` → object used for the vcall that leads to immediate draw helper.
- `this + 0x10` → flag gate (must be non-zero to take immediate path).
- `this + 0x11` → byte argument passed into `FUN_005aadc0`.

## Unnamed Immediate Render Dispatch Object (Vtable 0x015498A0)

- **Vtable base**: `0x015498A0` (label `PTR_LAB_015498a0`)
- **RTTI heuristic**: COL pointer at `0x01593840`, no RTTI-like type strings found.
- **Role**: Immediate render dispatch object (DispatchCarrier == ImmediateSubmitNode).

### Viewer-facing layout (proven)

- `+0x10` → immediate enable gate.
- `+0x11` → byte argument passed into `FUN_005aadc0`.
- `+0x14` → RenderPayload pointer passed as `this_00` into `FUN_005aadc0`.

### RenderPayload (immediate path)

- Layout: see `RENDER_PAYLOAD_LAYOUT.md`.
- Proven pointers from `FUN_005aadc0`:
  - `RenderPayload+0x64` → positions (float3 array).
  - `RenderPayload+0x70` → UVs (float2 array).
  - `RenderPayload+0x7C` → normals (float3 array).

### Constructor evidence (vtable writes + layout linkage)

- `FUN_005b5b00` `0x005b5b5f`: `MOV [ESI], 0x015498A0` with `ESI` offsets `{0x10,0x11,0x14}`.
- `FUN_005b5d20` `0x005b5d69`: `MOV [ESI], 0x015498A0` with `ESI` offsets `{0x10,0x11,0x14}`.
- `FUN_005b5e30` `0x005b5e81`: `MOV [ESI], 0x015498A0` with `ESI` offsets `{0x10,0x11,0x14}`.
- `FUN_005b6fe0` `0x005b7031`: `MOV [EDI], 0x015498A0` with `EDI` offsets `{0x10,0x11,0x14}`.

### Constructor field writes (scan)

- `sb_immediate_dispatch_ctor_writes.json` lists no additional field writes beyond the vtable assignment; no extra offsets are confirmed.
