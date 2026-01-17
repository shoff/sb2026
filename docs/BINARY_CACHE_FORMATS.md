# BINARY_CACHE_FORMATS

Evidence-backed notes on **binary cache entry** formats as consumed by `ArcFileCache::binary_load_fn` targets.

> Scope: this file currently documents the two binary formats we can concretely decode in this pass (`ArcImage`, `ArcMesh`). Additional `binary_load_fn` targets are resolved (see `ASSET_LOADER_DISPATCH_SPEC.md`) but their per-entry binary schemas are still pending.

## 1) Common framing: `ArcFileCache_BinaryLoadAll`

`FUN_007dad20(file_cache)` iterates binary entries; for each:

- calls `thunk_FUN_007db270(file_cache, entry_stream)` to obtain a decompressed byte-stream wrapper
- then calls `file_cache->binary_load_fn(entry_id, stream)` (indirect)

**Evidence**: `FUN_007dad20` decomp and `FUN_007db270` decomp.

## 2) `ArcImage` binary entry (confirmed)

### 2.1 Loader entrypoint

- `binary_load_fn` thunk: `LAB_004212f1`
- Resolved target: `FUN_0058efb0` (`get_xrefs_from(0x004212f1) → FUN_0058efb0`)

### 2.2 Constructed runtime type

`FUN_0058efb0` constructs an object with vtable `PTR_LAB_015490f0` and then uses `ArcImage::Load` logging strings downstream (see `FUN_0058dd50` referencing `ArcImage.cpp` at `0x016d50f4`).

RTTI string `. ?AVArcImage@@` exists at `0x016d5018`.

### 2.3 Observed binary field reads (schema)

`FUN_0058efb0` reads fields from the provided binary stream `param_3` in this order:

- `u32` → store at `obj+0x38`
- `u32` → store at `obj+0x3c`
- `u32` → store at `obj+0x40`
- `u32` → store at `obj+0xf0`
- `u32` → store at `obj+0x54`
- `bool` → store at `obj+0x4f`
- `bool` → store at `obj+0x4a`
- `u32 len`:
  - if `len == 0`: `*(obj+0x5c)=0`
  - else allocate `len` bytes and read `len` bytes into `*(obj+0x5c)`

It also sets the `ArcCacheID` on the object via `thunk_FUN_00512610(obj,&id)` which stores two dwords at `obj+0x10` (see `FUN_00512610`).

**Evidence**: `FUN_0058efb0` decomp; `FUN_00512610` decomp.

### 2.4 Interpretation notes (partially inferred; needs confirmation)

- The triple `u32` at `0x38/0x3c/0x40` likely correspond to dimensions / format metadata used by `ArcImage::TextureGLInit` (`FUN_00590a90`) which reads width/height and selects GL formats.
- The blob at `obj+0x5c` likely corresponds to raw image data or a compressed payload; exact meaning is not yet confirmed without tracing the later usage of `obj+0x5c`.

## 3) `ArcMesh` binary entry (confirmed)

### 3.1 Loader entrypoint

- `binary_load_fn` thunk: `LAB_004097fa`
- Resolved target: `FUN_005a33e0` (`get_xrefs_from(0x004097fa) → FUN_005a33e0`)

### 3.2 Constructed runtime type

`FUN_005a33e0` allocates `0x108` bytes and calls `FUN_005a88b0(obj,1)` (constructor for the mesh object), then fills vertex/index arrays.

`ArcMesh.cpp` source path string exists at `0x016d63fc`.

### 3.3 Observed binary field reads (high-level schema)

`FUN_005a33e0` reads (non-exhaustive; only what is clearly evidenced in the decomp):

- A string into `obj + 0x48` via `thunk_FUN_005453a0(obj+0x12, stream)`
- A float via `thunk_FUN_007e1740(stream)` stored at `obj[0x31]` (field offset `0xC4`)
- Several `Vector3`-like triples read via `thunk_FUN_00837c70(&tmp, stream)` stored into consecutive fields (likely bounding volumes / transforms)
- Two booleans stored at `obj+0x42` and `obj+0x43`
- **Vertex positions**:
  - `count = thunk_FUN_007e1700(stream)`
  - allocate `count * 12` bytes via `thunk_FUN_005ac9e0(obj+0x19, count, &tmp)`
  - loop `count` times reading 3 floats and writing 12 bytes each
- **Vertex normals**:
  - `count = thunk_FUN_007e1700(stream)`
  - allocate `count * 12` bytes via `thunk_FUN_005ac9e0(obj+0x1f, count, &tmp)`
  - loop `count` times reading 3 floats
- **Texture coordinates**:
  - `count = thunk_FUN_007e1700(stream)`
  - allocate `count * 8` bytes via `thunk_FUN_005ae160(obj+0x1c, count, &tmp)`
  - loop `count` times reading 2 floats and writing 8 bytes each
- Optional additional `Vector3` array when `obj+0x43` is true (guarded block)
- **Indices**:
  - `count = thunk_FUN_007e1700(stream)`
  - resize an internal `u16` array at `obj+0x25/0x26` to `count`
  - loop `count` times: `u16 = thunk_FUN_007e16d0(stream)` and store
- Additional per-submesh / per-material structures follow (reads of nested arrays via `thunk_FUN_007e1720` etc), still pending full unpacking.

**Evidence**: `FUN_005a33e0` decomp.

### 3.4 Confirmed CPU-side vertex element widths (from `ArcMesh::Get*`)

Independent of the binary loader, `ArcMesh::Get*` functions confirm the in-memory element sizes:

- `ArcMesh::GetVertexPosition` (`FUN_005a43a0`): element size `0x0c` (float3)
- `ArcMesh::GetVertexNormal` (`FUN_005a4460`): element size `0x0c` (float3)
- `ArcMesh::GetTextureCoord` (`FUN_005a4530`): element size `0x08` (float2)

These use pointer ranges within the object:

- positions: `[obj+0x64 .. obj+0x68)` (start/end pointers, stride 12)
- texcoords: `[obj+0x70 .. obj+0x74)` (start/end pointers, stride 8)
- normals: `[obj+0x7c .. obj+0x80)` (start/end pointers, stride 12)

**Evidence**: `FUN_005a43a0`, `FUN_005a4460`, `FUN_005a4530` decomp.

