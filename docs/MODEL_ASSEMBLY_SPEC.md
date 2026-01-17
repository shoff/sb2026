# MODEL_ASSEMBLY_SPEC

This spec documents the **client-side (“sb.exe”) model assembly rules** that have been confirmed via decompilation. It is intentionally implementation-grade (fields, offsets, pseudocode) and avoids inference.

## 1) Confirmed building blocks

### 1.1 `ArcMesh` (text mesh)

- **Parser**: `FUN_005a12e0` (token-driven line parsing; section state machine)
- **Writer**: `FUN_005a2d50` (emits options + `VERTICES`/`INDICES`)
- **Key tokens (evidence)**:
  - `USEFACENORMALS` (`s_USEFACENORMALS__016d6520`)
  - `STRIPIFY` (`s_STRIPIFY__016d6514`)
  - `USETANGENTBASIS` (`s_USETANGENTBASIS__016d6500`)
  - `USEMIRROREDNORMALMAP` (`s_USEMIRROREDNORMALMAP__016d64e4`)
  - `_VERTICES_` (`s__VERTICES__016d64d4`)
  - `_INDICES_` (`s__INDICES__016d64c8`)

### 1.2 `ArcMeshSet` (text tag wrapper)

- **Writer**: `FUN_005b7970`
  - emits `<BEGINMESHSET>` then `thunk_FUN_005b80d0(this,param_1)` then `<ENDMESHSET>`
- **Contains**: one or more polymesh entries (see below)

### 1.3 `ArcSinglePolyMesh` (text tag block + cache refresh)

- **Writer**: `FUN_005b62b0`
  - always emits `<BEGINSINGLEPOLYMESH>` and `<ENDSINGLEPOLYMESH>`
  - emits either:
    - `ID: %s` (`s_ID___s_016d69d8`) when it has a non-empty ID, or
    - `ID: DECAL` (`s_ID___DECAL_016d69c8`)
  - optional `DOUBLESIDED: TRUE` (`s_DOUBLESIDED__TRUE_016d69b0`) if a flag byte at `this+0x11` is set
- **ID-resolution / cache lookup**: `FUN_005b6450` logs `ArcSinglePolyMesh::CacheRefresh: Can't find mesh %s` (`016d6a00`)

### 1.4 `ArcTextureSet` (text tag block)

- **Tags**:
  - `<BEGINTEXTURESET>` string `016d73f4`
  - `<ENDTEXTURESET>` string `016d8470`
- **Creation**: `FUN_005c6e40` recognizes `<BEGINTEXTURESET>` and allocates a `0x34`-byte object constructed by `thunk_FUN_005e33c0`, then stores it at `this + 0xE8`.

### 1.5 `ArcTexture` (text “animated texture” wrapper + image/template binding)

- **Writer**: `FUN_005e0170`
  - logs `___TEXTURE_FILE___%s_saved` using `ArcTexture.cpp` path string `016d7e94`
  - writes:
    - `<BEGINANIMATEDTEXTURE>` (`016d82dc`)
    - `FRAMETIMER: %g` (`016d82c8`)
    - `FRAMERAND: %lu` (`016d82b4`)
    - iterates children and calls a virtual `+0x34` method on each
    - `<ENDANIMATEDTEXTURE>` (`016d8298`)
- **Binding to an image/template**: `FUN_005dd4d0`
  - calls `thunk_FUN_005e2630(param_1, &local_14, puVar2)` and logs `Failed_to_find_image___TemplateI...` on failure.

## 2) Confirmed render-object fields and parse rules

There are *at least* two distinct keyword parsers that participate in render/model assembly:

- `FUN_005c6e40`: recognizes `<BEGINTEXTURESET>` and other render-related knobs (target bone, scale, orient, VP params).
- `FUN_005d30d0`: recognizes `<BEGINMESHSET>` and multiple “material-ish” knobs (detail texture, specular map, shininess, cullface, etc.).

### 2.1 Fields observed in `FUN_005c6e40` (offsets are relative to `this`)

These are **direct assignments** observed in the decompiled code:

- **Target bone name**:
  - Token: `TARGETBONE` (`s_TARGETBONE__016d740c`)
  - Assignment: `core::String::operator=((String *)(this + 0x98), <value>)`
  - Post-step: `thunk_FUN_005c3620((int)this)` called immediately after setting
- **Scale (vector3)**:
  - Token: `SCALE` (`s_SCALE__016cb9e8`)
  - Assignments:
    - `*(float *)(this + 0x8c) = x`
    - `*(float *)(this + 0x90) = y`
    - `*(float *)(this + 0x94) = z`
- **Orientation-ish (4 floats)**:
  - Token: `ORIENT` (`s_ORIENT__016d73e8`)
  - Assignments:
    - `*(float *)(this + 0x7c) = a` (defaults to `1.0` if absent)
    - `*(float *)(this + 0x80) = b`
    - `*(float *)(this + 0x84) = c`
    - `*(float *)(this + 0x88) = d`
- **Texture set creation**:
  - Token: `<BEGINTEXTURESET>` (`016d73f4`)
  - Allocation: `operator_new(0x34)` → constructed via `thunk_FUN_005e33c0`
  - Stored: `*(int **)(this + 0xE8) = <new TextureSet*>`

`FUN_005c6e40` also parses numerous booleans and VP-related params (`VPNAME`, `VPPARAM`, etc.) and stores them into flags/collections; these need a deeper pass to extract stable layouts.

### 2.2 Fields observed in `FUN_005d30d0` (offsets are relative to an internal target object pointer)

`FUN_005d30d0` is a token-dispatcher that assigns to many offsets like `+0x10`, `+0x18`, `+0x1c`, etc. In decompilation, this target pointer appears as `local_14`; the layout below is still valid because it is assigned consistently.

- **Mesh set creation / ownership**
  - Token: `<BEGINMESHSET>` (`s_<BEGINMESHSET>_016d79b4`)
  - Allocation: `operator_new(0x34)` then `thunk_FUN_005d45b0(...)`
  - Stored: `*(... + 0x1c) = <new MeshSet*>`
- **Detail texture cache-id**
  - Token: `DETAILTEXTURE` (`s_DETAILTEXTURE__016d7940`)
  - Parses token into a cache-id using `thunk_FUN_00548e60` + `thunk_FUN_00511ba0`
  - Stored at: `(... + 0x10)`
- **Specular map cache-id**
  - Token: `SPECULARMAP` (`s_SPECULARMAP__016d7930`)
  - Parses a cache-id into `(... + 0x10)` as well in the shown region (needs a deeper pass to disambiguate whether there are multiple slots or shared storage)
- **Shininess**
  - Token: `SHININESS` (`s_SHININESS__016d7920`)
  - Stored at: `(... + 0x18)` as `float`
- **Cullface / render-state like ints**
  - Token: `CULLFACE` (`s_CULLFACE__016d7954`) stored at `(... + 0x48)` as `int`
  - Token: `LIGHTTWOSIDE` (`s_LIGHTTWOSIDE__016d7960`) stored at `(... + 0x44)` as `int`
  - Token: `CLIPMAP` (`s_CLIPMAP__016d7970`) stored at `(... + 0x40)` as `int`

#### DOUBLESIDED handling (behavioral rule)

- Token: `DOUBLESIDED` (`s_DOUBLESIDED__016d6960`)
- Behavior: when true, the parser finds a mesh entry via:
  - `thunk_FUN_00535630(*(void **)(... + 0x1c), ...)` then `thunk_FUN_005d4710(...)`
  - then sets `*(undefined1 *)(entry + 0x11) = 1`
- **Interpretation (evidence-backed)**: the polymesh entry has a byte at `+0x11` controlling DOUBLESIDED; this matches `ArcSinglePolyMesh` writer `FUN_005b62b0` which emits `DOUBLESIDED: TRUE` when `*(char *)(this+0x11) != 0`.

## 3) Confirmed object→render binding (IDs)

`ArcObj` parsing in `FUN_004d16a0` binds render IDs as cache IDs:

- `RENDEROBJECT` token:
  - Parses value into a cache-id and stores into `this + 0xB8`
  - **Evidence**: `FUN_004d16a0` handles `s_RENDEROBJECT__016cb788` and calls `thunk_FUN_00511ba0((void *)((int)this + 0xb8), ...)`
- `RENDEROBJECTLOWDETAIL` token:
  - Parses value into a cache-id and stores into `this + 200`
  - **Evidence**: `FUN_004d16a0` handles `s_RENDEROBJECTLOWDETAIL__016cb72c` and calls `thunk_FUN_00511ba0((void *)((int)this + 200), ...)`

## 4) Assembly pseudocode (only what is directly supported by decompilation so far)

### 4.1 Parse-time (text → intermediate objects)

```text
ArcObj::ParseKeyword(line):
  if token == "RENDEROBJECT":
    this.renderobject_id = ParseArcCacheID(value)
  if token == "RENDEROBJECTLOWDETAIL":
    this.renderobject_lowdetail_id = ParseArcCacheID(value)
  if token == "<BEGINHARDPOINTS>":
    ensure this.hardpoints_parser exists and delegate parsing

RenderObject::ParseKeyword(line):
  if token == "<BEGINMESHSET>":
    this.meshset = new ArcMeshSet()
  if token == "<BEGINTEXTURESET>":
    this.textureset = new ArcTextureSet()
  if token == "DETAILTEXTURE":
    this.detail_texture_id = ParseArcCacheID(value)
  if token == "SPECULARMAP":
    this.specular_map_id = ParseArcCacheID(value)    // slot mapping not fully recovered yet
  if token == "SHININESS":
    this.shininess = float(value)
  if token == "DOUBLESIDED":
    resolve mesh entry and set entry.doublesided_flag (byte at +0x11)
```

### 4.2 Run-time selection (texture sets)

- Selecting a texture set index on a render object updates `this+0xE0` and propagates to children.
  - **Evidence**: `FUN_005c8170` sets `*(uint *)(this+0xE0)` and recurses into child pointers in array `this+0x3c..this+0x40`.

## 5) Missing pieces (required for full reassembly spec, not yet recovered)

- The exact **mesh vertex layout** and how it maps to GPU buffers in the original client (we have text mesh parse/save but not renderer upload).
- How `ArcTextureSet` enumerates texture slots and how they bind to a render pass.
- How the `ArcRenderObject`/`ArcRenderTemplate` graph is traversed into final draw calls and state blocks.
- Where and how `ArcCacheID` is resolved to filesystem paths (we have cache root constants but not the ID→path algorithm yet).

