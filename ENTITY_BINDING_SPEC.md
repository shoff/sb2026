# ENTITY_BINDING_SPEC

This document captures **entity → asset binding** behavior confirmed in `sb.exe` decompilation. It focuses on how the runtime “object loader” path instantiates entities and attaches renderable components.

## 1) ArcObjectLoader call sites (confirmed)

The following functions reference `C:\\ArcanePrime\\Main_Branch\\Shadowbane\\Source\\ArcObjectLoader.cpp` (`01719340`) and log object-loader events:

- **`FUN_0089f160`**:
  - Logs: `ArcObjectLoader::Run__Failed_to_m...` (`017193bc`)
  - Called on a path that resolves an object/template and then configures properties (position/orientation/flags).
- **`FUN_0089f900`**:
  - Logs: `Processing Request for Character` (`017194a0`)
  - Logs: `ArcObjectLoader::LoadCharacter() - No Race Rune found ...` (`01719414`)
  - Performs substantial post-instantiation configuration of the character object (multiple subsystems invoked).

> Evidence: both functions embed the ArcObjectLoader.cpp file path string and line numbers in their logging blocks.

## 2) Character load / instantiate path (partial trace)

### 2.1 High-level order (confirmed by `FUN_0089f900`)

`FUN_0089f900(int *request)` (name inferred by behavior; symbol is `FUN_0089f900`) performs:

1. **Log request start**:
   - `Processing Request for Character` (uses ArcObjectLoader.cpp path `01719340`)
2. **Resolve a base “character object”**:
   - `local_14 = thunk_FUN_0048bde0(piVar9[0x34])` (some lookup using a request field)
3. **Iterate a list of “runes” / parts**:
   - Loops over `local_14[0x1df]` entries, calling `thunk_FUN_0091cb40(...)`
   - If a required entry is missing (`local_1c == 0.0`), logs:
     - `!!!!!!!!!!ArcObjectLoader::LoadCharacter() - No Race Rune found ...` (`01719414`)
4. **Post-load configuration** (many calls, evidence is direct function calls):
   - Applies transforms/orientation:
     - `thunk_FUN_00459d70(...)`
     - `thunk_FUN_004cc390(...)` (quaternion set)
   - Sets flags/state:
     - `thunk_FUN_004d5080(...,'\x01')`
     - `thunk_FUN_004cc0f0(...)`, `thunk_FUN_004cc0c0(...)`
   - Conditional branch involving `thunk_FUN_004611d0(...) == 1` that modifies internal state, selects an item/slot (`0x37`), and clears a bit on a byte field `*(byte *)(local_14 + 0x8f) &= 0xFE`.

### 2.2 What this implies for binding (strictly evidence-based)

From the presence of:

- the “rune found / not found” behavior,
- repeated calls to “add/configure” functions during the loop, and
- the later conditional equipment/slot logic,

we can confirm that **character instantiation is not a single-model load**: it is an assembly process that depends on multiple referenced sub-assets (“runes”, attachments, gear) and results in a configured runtime object.

However, the exact asset IDs and the exact data structures for these rune references are **not yet fully recovered** in this pass.

## 3) Generic object run path (partial trace)

`FUN_0089f160(int *request)`:

- Resolves an object either from a cached pointer (`param_1[2]`) or via a lookup (`thunk_FUN_004c4680(DAT_01aa7c70, ...)`).
- If resolution fails, logs:
  - `ArcObjectLoader::Run__Failed_to_m...` (`017193bc`)
- If object has certain capability flags (checked via `thunk_FUN_004c9c80(..., 0x2000)` and other masks), applies scaling/transform and other properties.

This is consistent with a runtime “entity instance” object that carries capability flags and is configured from incoming instance data.

## 4) Outstanding required work to complete ENTITY_BINDING_SPEC

To make this implementation-grade for the viewer, we still need (from decompilation evidence):

- The **entity definition format** (where `TEMPLATE`, `INSTANCE`, `ArcObjectInfo` keyword parsing, etc. live) and which cache/text files they are read from.
  - We have string evidence for `ArcObjectInfo::ParseKeyword` error messages and `ArcObject.cpp` source path (`016cb61c`), but we have not yet traced the full parsing pipeline into instantiation.
- The binding from an entity instance to:
  - `ArcObj` / `ArcRenderObject` IDs (`RENDEROBJECT`, etc.)
  - Skeleton + motions for animated entities
  - Any per-entity render-state knobs (texture set selection, decals, etc.)

