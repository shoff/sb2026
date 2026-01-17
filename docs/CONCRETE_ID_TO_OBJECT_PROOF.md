# CONCRETE_ID_TO_OBJECT_PROOF

Evidence-backed end-to-end proof of:

`ArcCacheID` → `BuildPathFromID` → `open_decode_fn`/`binary_load_fn` → constructed runtime type → (at least one) render-facing API.

This repo **does include** `./cache/*.cache` monolithic containers (e.g. `Mesh.cache`, `Textures.cache`) and we can cite concrete on-disk directory entries and offsets.

## 0) Disk-backed note (repo cache format)

This repo’s `cache/` directory contains **monolithic `.cache` containers** (e.g. `cache/Mesh.cache`, `cache/Textures.cache`), not per-asset `^\d{20}` filenames.

Disk-backed ID proofs are therefore expressed as:

`cache/<Type>.cache` + `(directory record key → zlib stream offset/size)` rather than `cache/<Type>/<bucket>/<20digit>.<ext>`.

**Evidence**: `DISK_BACKED_ID_PATH_PROOFS.md`.

## 0.2 Disk-verified: Variant B container layout + 5 worked examples (Mesh + Textures)

These worked examples are taken directly from the real `./cache/Mesh.cache` and `./cache/Textures.cache` files in this repo, using the Variant B layout documented in `CACHE_CONTAINER_FORMATS.md`:

- header: 0x28 bytes (10×u32), includes `count_plus_1`, `data_off`, `file_size`
- directory: entries at `0x28`, stride `0x14`, with a 4-byte pad between entries (pad absent after last)
- entry fields: `u32 key`, `u32 stream_off`, `u32 usize`, `u32 csize`, `u32 pad0`
- payload begins exactly at `data_off` and is zlib for these examples (`0x78 ??` header)

**Record-key model (locked for Mesh.cache / Textures.cache)**:

- Stored directory key is **u32** (`key`), not an `ArcCacheID` u64.
- The on-disk directory stride is `0x14` bytes, but the **last record’s** trailing 4 bytes are not a real pad; they overlap the first payload dword at `data_off`.

### Worked example 1 — Mesh.cache key=101 → zlib stream → ArcMesh decoder

- **File**: `cache/Mesh.cache` size `0x02381f4c` (37,232,460)
- **Header**: `count_plus_1=24387` ⇒ `record_count=24386`, `data_off=0x0007714c`, `base_key=100`
- **Directory entry**:
  - idx = 0
  - dir_entry_off = `0x00000028`
  - bytes (0x14):

```text
00000028  65 00 00 00 cc 77 07 00 fc 0b 00 00 8d 06 00 00
00000038  00 00 00 00
```

  - parsed: `key=101`, `stream_off=0x000777cc`, `usize=3068`, `csize=1677`, `pad0=0`
- **Payload**: `file[0x000777cc:...]` begins with `78 da ...` (zlib)
- **Inflate**: zlib-decompressed size **3068 == usize** ✅
- **Decoder mapping (sb.exe)**: `ArcMesh → FUN_005a33e0`

### Worked example 2 — Mesh.cache key=202 → zlib stream → ArcMesh decoder

- **File**: `cache/Mesh.cache`
- **Directory entry**:
  - idx = 4
  - dir_entry_off = `0x00000078`
  - bytes (0x14):

```text
00000078  ca 00 00 00 e4 90 07 00 02 10 00 00 dd 08 00 00
00000088  00 00 00 00
```

  - parsed: `key=202`, `stream_off=0x000790e4`, `usize=4098`, `csize=2269`, `pad0=0`
- **Payload**: `file[0x000790e4:...]` begins with `78 da ...` (zlib)
- **Inflate**: zlib-decompressed size **4098 == usize** ✅
- **Decoder mapping (sb.exe)**: `ArcMesh → FUN_005a33e0`

### Worked example 3 — Textures.cache key=10 → zlib stream → ArcImage decoder

- **File**: `cache/Textures.cache` size `0x66c4435c` (1,724,138,332)
- **Header**: `count_plus_1=9680` ⇒ `record_count=9679`, `data_off=0x0002f450`, `base_key=1`
- **Directory entry**:
  - idx = 0
  - dir_entry_off = `0x00000028`
  - bytes (0x14):

```text
00000028  0a 00 00 00 03 2a 03 00 1a 00 04 00 2e cc 00 00
00000038  00 00 00 00
```

  - parsed: `key=10`, `stream_off=0x00032a03`, `usize=262170`, `csize=52270`, `pad0=0`
- **Payload**: `file[0x00032a03:...]` begins with `78 9c ...` (zlib)
- **Inflate**: zlib-decompressed size **262170 == usize** ✅
- **Decoder mapping (sb.exe)**: `ArcImage → FUN_0058efb0`

### Worked example 4 — Textures.cache key=100 → zlib stream → ArcImage decoder

- **File**: `cache/Textures.cache`
- **Directory entry**:
  - idx = 1
  - dir_entry_off = `0x0000003c`
  - bytes (0x14):

```text
0000003c  64 00 00 00 31 f6 03 00 1a 00 03 00 32 15 00 00
0000004c  00 00 00 00
```

  - parsed: `key=100`, `stream_off=0x0003f631`, `usize=196634`, `csize=5426`, `pad0=0`
- **Payload**: `file[0x0003f631:...]` begins with `78 9c ...` (zlib)
- **Inflate**: zlib-decompressed size **196634 == usize** ✅
- **Decoder mapping (sb.exe)**: `ArcImage → FUN_0058efb0`

### Worked example 5 — Textures.cache key=9785 → zlib stream → ArcImage decoder

- **File**: `cache/Textures.cache`
- **Directory entry**:
  - idx = 9673
  - dir_entry_off = `0x0002f3dc`
  - bytes (0x14):

```text
0002f3dc  39 26 00 00 1a 9f be 66 1a 00 03 00 bc eb 01 00
0002f3ec  00 00 00 00
```

  - parsed: `key=9785`, `stream_off=0x66be9f1a`, `usize=196634`, `csize=125884`, `pad0=0`
- **Payload**: `file[0x66be9f1a:...]` begins with `78 9c ...` (zlib)
- **Inflate**: zlib-decompressed size **196634 == usize** ✅
- **Decoder mapping (sb.exe)**: `ArcImage → FUN_0058efb0`

## 0.1 Proven in `sb.exe`: `.cache` container selection + directory lookup primitive

### Container selection

`FUN_007dba30(this, out_path)` selects the container filename by:

- `out_path += PTR_s_Textures_0170508c[ this->subtype ]`
- `out_path += ".cache"` (string at `0x01704f08`)

### Directory lookup (lookup, not insert)

`FUN_007db8f0(this, &arc_cache_id)` performs **binary search** over the in-memory directory vector at `[this+0x54, this+0x58)` with element stride `0x18`, comparing by the full `ArcCacheID` (two dwords).

**Evidence**:

- `FUN_007db8f0` decomp shows the standard mid-point loop with `thunk_FUN_00511b20` / `thunk_FUN_00511bd0` comparisons.
- `FUN_007d8fb0` invokes `FUN_007db8f0` during `.cache` processing, establishing it as the primary directory search primitive for this cache container implementation.

## 1) Proven: how a 20-digit decimal filename prefix becomes `ArcCacheID` (uint64)

`FUN_007dc1c0` (directory indexing for an `ArcFileCache` subtype) enumerates files and for each filename:

- Calls `thunk_FUN_00511d00(out_id, (int)(filename_ascii + 1))`, which parses the first 20 digits into a 64-bit `ArcCacheID` value.

**Evidence**: `FUN_007dc1c0` decomp:

- `thunk_FUN_00511d00(auStack_24,(int)(pAVar2 + 1));`

and the previously recovered `FUN_00511d00` loop (20-digit decimal parser).

## 2) Proven: `BuildPathFromID` is `FUN_007da120` (vtable slot +8)

### 2.1 Target resolution

- `FUN_007d8c50` sets `this->vtable = 0x0155a97c`
- `get_xrefs_to(0x007da120)` shows **From `0x0155a984` [DATA]**
- `0x0155a984 == 0x0155a97c + 0x08` ⇒ vtable slot +8 points to `FUN_007da120`

### 2.2 The 20-digit string formatting rule (critical)

Inside `FUN_007da120`, the cache ID is converted to a string by:

- calling thunk `0x00404aed` with `ECX = id` and `out_string`
- `0x00404aed` thunks to `FUN_00511cd0` which calls `FUN_00511ec0`
- `FUN_00511ec0` disassembly proves it formats the `ArcCacheID` object’s two dwords with:
  - format string `"%0.20I64u"` at `0x016cda90`
  - pushes `[this+4]` and `[this+0]` as args before formatting call

**Evidence**:

- `FUN_007da120` disassembly around `0x007da1e9..0x007da202`
- `FUN_00511ec0` disassembly shows:
  - `MOV EAX,[ECX+4]` and `MOV ECX,[ECX]` then pushes both into formatting

## 3) Proven: `open_decode_fn` and `binary_load_fn` resolution (type_index 0 and 1 examples)

All instances are constructed in `FUN_0091d6b0` (see `ASSET_LOADER_DISPATCH_SPEC.md`), which wires:

- `binary_load_fn` via ctor arg to `thunk_FUN_007d8c50`
- `open_decode_fn` via `thunk_FUN_007da010(cache, fn)`

We resolve the concrete targets using `get_xrefs_from(LAB_xxx) → FUN_xxx [UNCONDITIONAL_CALL]`.

### 3.1 ArcImage (type_index 0)

From `FUN_0091d6b0`:

- `DAT_01aa7c90 = thunk_FUN_007d8c50(..., &LAB_004212f1, 0);`
- `thunk_FUN_007da010(DAT_01aa7c90, &LAB_00426a30);`

Resolved targets:

- `open_decode_fn`: `LAB_00426a30` → `FUN_0058eb90`
- `binary_load_fn`: `LAB_004212f1` → `FUN_0058efb0`

### 3.2 ArcMesh (type_index 1)

From `FUN_0091d6b0`:

- `DAT_01aa7ca8 = thunk_FUN_007d8c50(..., &LAB_004097fa, 1);`
- `thunk_FUN_007da010(DAT_01aa7ca8, &LAB_00414038);`

Resolved targets:

- `open_decode_fn`: `LAB_00414038` → `FUN_005a3e20`
- `binary_load_fn`: `LAB_004097fa` → `FUN_005a33e0`

## 4) Proven: runtime type + `ArcCacheID` storage location in the constructed object

`FUN_00512610(obj,&id)` stores the `ArcCacheID` into `obj+0x10`:

- `FUN_00512610(this, param_1)` calls `thunk_FUN_00511ba0((this+0x10), param_1)`

**Evidence**: `FUN_00512610` decomp.

## 5) Proven: ArcImage decode and GL upload path

### 5.1 Text/stream decode

`FUN_0058eb90` constructs an `ArcImage` and calls:

- `thunk_FUN_00512610(obj,&id)` (stores ID at `obj+0x10`)
- `thunk_FUN_0058dd50(obj, path_string)` → `ArcImage::Load(...)`

`FUN_0058dd50` logs `ArcImage::Load...` and calls a policy vtable method to load image data.

**Evidence**:

- `FUN_0058dd50` decomp includes strings:
  - `ArcImage::Load: No policy class defined...` (`0x016d50b0`)
  - `ArcImage.cpp` path (`0x016d50f4`)

### 5.2 Render-facing GPU upload (texture)

`FUN_00590a90` implements `ArcImage::TextureGLInit` (by strings + behavior) and calls:

- `glTexImage2D` / `glTexImage1D`
- `glTexParameteri`
- `glPrioritizeTextures`

It also logs `ArcImage::TextureGLInit - texture upload` (`0x016d5474`) and other TextureGLInit phase markers.

**Evidence**: `FUN_00590a90` decomp and `get_xrefs_to(0x016d5474)`.

## 6) Proven: ArcMesh binary decode and CPU-side vertex element widths

### 6.1 Binary decode

`FUN_005a33e0` constructs the mesh object (`FUN_005a88b0`) and reads:

- positions as float3 array
- normals as float3 array
- texcoords as float2 array
- indices as u16 array

**Evidence**: `FUN_005a33e0` decomp.

### 6.2 CPU-side vertex attribute sizes (directly proven)

`ArcMesh::GetVertexPosition/Normal/TextureCoord` confirm the array element widths:

- position: 12 bytes (float3) via `FUN_005a43a0`
- normal: 12 bytes (float3) via `FUN_005a4460`
- uv: 8 bytes (float2) via `FUN_005a4530`

**Evidence**: `FUN_005a43a0`, `FUN_005a4460`, `FUN_005a4530` decomp.

## 7) Remaining steps to satisfy the strict “stop condition”

To fully satisfy “take a concrete ArcCacheID string/prefix and show its full path to a file on disk”, we still need one **concrete** cache filename from a real install cache (or a `.cache` container inventory) so we can cite:

- the exact 20-digit filename present on disk
- the exact `type_index` bucket directory it lives under (so we can show the *real* directory string from `DIR_BY_TYPE[type_index]` and `BUCKET_CHAR_BY_TYPE[type_index]`)
- the exact suffix string from `SUFFIX_BY_TYPE[type_index]`

The mapping functions are fully recovered. For this repo’s cache layout, the remaining tightener is proving whether the container directory record `key` is the full `ArcCacheID` (low-only) or a separate 32-bit identifier mapped to `ArcCacheID` elsewhere.

## 8) Disk-backed examples (concrete on-disk offsets)

### 8.1 ArcImage from `cache/Textures.cache` (binary path)

- **Disk path**: `cache/Textures.cache`
- **Entry key**: 10 (`id20=00000000000000000010`)
- **Zlib stream**: `stream_off=0x32a03`, `csize=52270`, `usize=262170`

**Decoder + runtime type (sb.exe)**:

- `binary_load_fn` resolves to `FUN_0058efb0` (via `FUN_0091d6b0` wiring: `LAB_004212f1` → `FUN_0058efb0`)
- `FUN_0058efb0` constructs **ArcImage** and sets `ArcCacheID` at `obj+0x10` via `FUN_00512610`

### 8.2 ArcMesh from `cache/Mesh.cache` (binary path)

- **Disk path**: `cache/Mesh.cache`
- **Entry key**: 101 (`id20=00000000000000000101`)
- **Zlib stream**: `stream_off=0x777cc`, `csize=1677`, `usize=3068`

**Decoder + runtime type (sb.exe)**:

- Mesh `binary_load_fn` resolves to `FUN_005a33e0` (via `FUN_0091d6b0` wiring: `LAB_004097fa` → `FUN_005a33e0`)
- `FUN_005a33e0` constructs **ArcMesh** and fills vertex arrays (confirmed by `ArcMesh::Get*` methods operating on those arrays).


