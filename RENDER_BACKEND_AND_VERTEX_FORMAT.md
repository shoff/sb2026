# RENDER_BACKEND_AND_VERTEX_FORMAT

Evidence-backed renderer binding notes: where asset runtime types become GPU resources, and what vertex formats are implied/confirmed.

> Status: **partial but materially advanced**. Texture upload (`ArcImage`) and mesh submission paths for the fixed-function pipeline are confirmed (client arrays + `glDrawElements`, plus immediate-mode fallback). The remaining gap is the assembled-model type + skinning variants and whether any shader-attribute (`glVertexAttribPointerARB`) path is used for skinned draws.

## 1) Texture upload path (confirmed): `ArcImage::TextureGLInit`

### 1.1 Entry point and evidence

- `FUN_00590a90` contains logging strings:
  - `ArcImage::TextureGLInit - texture upload` (`0x016d5474`)
  - `ArcImage::TextureGLInit - texparam/env` (`0x016d54a8`)
  - `ArcImage::TextureGLInit: _glImage %s is NULL.` (`0x016d5508`)

`get_xrefs_to(0x016d5474)` points to `FUN_00590a90`.

### 1.2 GL calls observed

`FUN_00590a90` calls (direct imports):

- `glTexImage2D` / `glTexImage1D`
- `glTexParameteri`
- `glTexEnvi`
- `glPrioritizeTextures`
- `glGetTexLevelParameteriv` (conditionally, for memory sizing)
- `glPixelStorei`

It selects internal format and pixel format based on image flags and dimensions (see the large branch selecting values like `0x1907`, `0x1908`, `0x8057`, `0x803c`, etc).

**Evidence**: `FUN_00590a90` decomp.

## 2) CPU-side mesh vertex element widths (confirmed): `ArcMesh::Get*`

These functions prove the **CPU representation** of `ArcMesh` vertex attributes as separate arrays (SoA), including element widths:

- `FUN_005a43a0` (`ArcMesh::GetVertexPosition`):
  - element size `0x0c` (float3)
  - returns `positions_start + index * 0x0c`
- `FUN_005a4460` (`ArcMesh::GetVertexNormal`):
  - element size `0x0c` (float3)
  - returns `normals_start + index * 0x0c`
- `FUN_005a4530` (`ArcMesh::GetTextureCoord`):
  - element size `0x08` (float2)
  - returns `uv_start + index * 0x08`

**Evidence**: `FUN_005a43a0`, `FUN_005a4460`, `FUN_005a4530` decomp.

## 3) Binary mesh decode confirms index type (partial but strong)

`FUN_005a33e0` reads an index array as `u16` values from the binary stream using `thunk_FUN_007e16d0` and stores into an internal `u16` vector.

**Evidence**: `FUN_005a33e0` decomp (loop storing `(short)uVar12` into a 2-byte stride array).

## 4) Draw submission: fixed-function mesh path (confirmed)

### 4.1 Immediate mode draw (debug/fallback) for `ArcMesh`

`FUN_005aadc0(this, flag)` draws a strip using:

- `glBegin(5)` (mode `GL_TRIANGLE_STRIP`)
- per-vertex:
  - `glNormal3f` from normals array at `this+0x7c`
  - `glTexCoord2f` from uv array at `this+0x70`
  - `glVertex3f` from positions array at `this+0x64`
- `glEnd()`

**Evidence**: `FUN_005aadc0` decomp.

### 4.2 Client-array draw via `glDrawElements` (per-range and per-batch)

`FUN_005a0780(param_1)` iterates a list at `param_1+0xa0..0xa4` and calls:

- `glDrawElements(mode, count, 0x1403, index_ptr)`
  - index type `0x1403` = `GL_UNSIGNED_SHORT`
  - `mode` is read from a table `DAT_016d6168 + primitive_id*4`

`FUN_005a07f0(param_1)` batches up to 64 draw calls of the same mode and submits them via:

- `thunk_FUN_009655c0(mode, counts[], 0x1403, index_ptrs[], n)`

**Evidence**: `FUN_005a0780` and `FUN_005a07f0` decomp.

### 4.3 Vertex pointer binding for the client-array path (confirmed call shape)

`FUN_005a0960(param_1)` issues a pointer-binding call with the signature:

- `(size=3, type=0x1406, stride=0, ptr=*(param_1+0x64))`
  - `0x1406` = `GL_FLOAT`

This matches the canonical `glVertexPointer(3, GL_FLOAT, 0, positions_ptr)` binding for `ArcMesh` positions.

**Evidence**: `FUN_005a0960` disassembly shows pushing `3, 0x1406, 0, *(param+0x64)` then calling an IAT slot.

## 5) Still required (pending)

- Identify where **normals** and **texcoords** are bound for the client-array path (the `glNormalPointer` / `glTexCoordPointer` equivalents) and prove their pointer/stride values.
- Determine whether any **VBO** path exists (vs raw client arrays).
- Recover the final vertex declaration variants for **skinned** meshes and the bone palette upload/binding path.

## 6) Skinned vertex variants (placeholder; MCP-required)

> Fill this section from `Skin.dll` + `sb.exe` render binding evidence.

- **Variant A: static mesh (confirmed pieces)**
  - position: float3 (CPU arrays) (`ArcMesh` accessors)
  - normal: float3 (CPU arrays) (`ArcMesh` accessors)
  - uv: float2 (CPU arrays) (`ArcMesh` accessors)
  - indices: `GL_UNSIGNED_SHORT` (confirmed `glDrawElements(..., 0x1403, ...)`)
- **Variant B: skinned mesh (to fill)**
  - bone indices:
  - bone weights:
  - max influences:
  - packing (u8/u16/float):
  - binding API (client arrays vs `glVertexAttribPointerARB` vs other):
  - palette upload mechanism:
  - draw function(s) used:

## 7) Evidence blocks to drop in (template)

- **Skinned attribute bind**
  - Function:
  - Attributes:
  - Evidence:
- **Bone palette upload**
  - Function:
  - Buffer/uniform target:
  - Evidence:

