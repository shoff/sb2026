# Render Payload Layout (Immediate Mode)

## Sources

- `FUN_005aadc0` disassembly and decompile.
- `sb_aadc0_renderpayload_offsets.json` (no offset uses captured; layout derived from disassembly).

## RenderPayload field map (immediate path)

| Offset | Size | Access | Category | Name | Meaning | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| `0x64` | 4 | LOAD | pointer | `positions_ptr` | Base pointer to float3 position array | `005aae05 MOV ECX,[ESI+0x64]` → `005aae08/005aae0c/005aae13/005aae15` |
| `0x70` | 4 | LOAD | pointer | `uvs_ptr` | Base pointer to float2 UV array | `005aadf1 MOV ECX,[ESI+0x70]` → `005aadf4/005aadfb/005aadff` |
| `0x7C` | 4 | LOAD | pointer | `normals_ptr` | Base pointer to float3 normal array | `005aaddb MOV EAX,[ESI+0x7c]` → `005aade0/005aade6/005aadeb` |

## Immediate-mode submission behavior

- Primitive: `GL_TRIANGLE_STRIP` (`005aadc8 PUSH 0x5` → `005aadca CALL glBegin`)
- Vertex count:
  - `param_1 != 0`: 8 vertices (`005aae23 CMP EDI,0x40` with `EDI += 0x8`)
  - `param_1 == 0`: 4 vertices (`005aae88 CMP EDI,0x20` with `EDI += 0x8`)
- Per-vertex sources:
  - Normal: `*(normals_ptr + i*12)` feeds `glNormal3f`
  - UV: `*(uvs_ptr + i*8)` feeds `glTexCoord2f`
  - Position: `*(positions_ptr + i*12)` feeds `glVertex3f`
