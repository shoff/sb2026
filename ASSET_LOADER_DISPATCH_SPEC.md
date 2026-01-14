# ASSET_LOADER_DISPATCH_SPEC

Evidence-backed spec for how `ArcFileCache` dispatches per-type loaders:

- `BuildPathFromID` (virtual, vtable slot `+8`)
- `open_decode_fn` (function pointer field `this+0x84`)
- `binary_load_fn` (function pointer field `this+0x50`)

This document is limited to what is **concretely proven** from `sb.exe` in this pass. Any remaining unknowns are explicitly labeled.

## 1) How we recover the function pointer targets (hard requirement)

### 1.1 `BuildPathFromID` (vtable slot +8)

- `FUN_007d8c50` (ArcFileCache ctor) sets the **final** vtable pointer:
  - `*(this+0x00) = 0x0155a97c` (see `FUN_007d8c50` disassembly)
- `get_xrefs_to(0x007da120)` reports **From `0x0155a984` [DATA]**
- `0x0155a984 == 0x0155a97c + 0x08` ⇒ vtable slot `+8` points to `FUN_007da120`

**Conclusion**: `ArcFileCache::BuildPathFromID` resolves to **`FUN_007da120`**.

### 1.2 `open_decode_fn` (field +0x84)

- `FUN_007d8c50` initializes `*(this+0x84)=0`
- `thunk_FUN_007da010(this, fn)` stores `fn` into `*(this+0x84)`
- All `ArcFileCache` instances are created in `FUN_0091d6b0`, which calls `thunk_FUN_007da010(cache, &LAB_xxx)`
- Each `&LAB_xxx` is a concrete thunk: `get_xrefs_from(LAB_xxx)` yields a **UNCONDITIONAL_CALL** to a concrete `FUN_...` implementation

### 1.3 `binary_load_fn` (field +0x50)

- `FUN_007d8c50(this, fn, type_index)` stores:
  - `*(this+0x50) = fn` (see `FUN_007d8c50` disassembly: `MOV [ESI+0x50],EAX`)
- All `ArcFileCache` instances are created in `FUN_0091d6b0`, which calls `thunk_FUN_007d8c50(..., &LAB_xxx, type_index)`
- Each `&LAB_xxx` is a concrete thunk: `get_xrefs_from(LAB_xxx)` yields a **UNCONDITIONAL_CALL** to a concrete `FUN_...` implementation

## 2) `BuildPathFromID(out, id, mode)` pseudocode (implementation-grade)

Evidence: `FUN_007da120` decomp + disassembly; `FUN_00511ec0` disassembly shows it formats `ArcCacheID` with `"%0.20I64u"` from the two dwords in the `ArcCacheID` object.

```text
// FUN_007da120 (vtable slot +8)
BuildPathFromID(out: String, id: ArcCacheID*, mode: int):
  if mode == 1:
    out += DAT_01aa308c          // String
  else if mode == 2:
    if DAT_01aa73f0 != 0:
      out += DAT_01aa73d8        // String
  else:
    out += DAT_01aa30a4          // String
    if mode == 0:
      t = this.type_index        // *(this+0x6c)
      if t == 3 || t == 10:
        out += DAT_01704c90
      else if t == 4 || t == 11:
        out += DAT_016d6350

  t = this.type_index
  out += DIR_BY_TYPE[t]          // base 0x0170508c (ptr table; first entry names "Textures")
  out += '/'
  out += BUCKET_CHAR_BY_TYPE[t]  // base *[0x01705088], indexed by t (byte table)
  out += ArcCacheID_ToString20(id)  // via thunk 0x00404aed → FUN_00511cd0 → FUN_00511ec0 ("%0.20I64u")
  out += SUFFIX_BY_TYPE[t]       // base 0x017050c8 (ptr table)
```

## 3) `ArcFileCache` instances and resolved handler targets (from `FUN_0091d6b0`)

### 3.1 Table: type_index → open_decode_fn → binary_load_fn

Each row is directly evidenced by the `FUN_0091d6b0` constructor calls plus `get_xrefs_from()` on the thunk label.

| `type_index` | `ArcFileCache` global | open_decode thunk → target | binary_load thunk → target | Produced runtime type |
|---:|---|---|---|---|
| 5 | `DAT_01aa7c74` | `LAB_00418075` → `FUN_005c2e50` | `LAB_00405c2c` → `FUN_005c2d30` | pending |
| 4 | `DAT_01aa7c6c` | `LAB_00415104` → `FUN_004ca8b0` | `LAB_00413647` → `FUN_004caa40` | pending |
| 0 | `DAT_01aa7c90` | `LAB_00426a30` → `FUN_0058eb90` | `LAB_004212f1` → `FUN_0058efb0` | **ArcImage** (confirmed) |
| 12 | `DAT_01aa7c98` | `LAB_0040fcef` → `FUN_0095cc50` | `LAB_0040413d` → `FUN_0095dc40` | pending |
| 13 | `DAT_01aa7ca0` | `LAB_00426a30` → `FUN_0058eb90` | `LAB_004212f1` → `FUN_0058efb0` | **ArcImage** (confirmed) |
| 1 | `DAT_01aa7ca8` | `LAB_00414038` → `FUN_005a3e20` | `LAB_004097fa` → `FUN_005a33e0` | **ArcMesh** (confirmed) |
| 6 | `DAT_01aa7cb8` | `LAB_00428290` → `FUN_009494c0` | `LAB_0040936d` → `FUN_009494f0` | pending |
| 8 | `DAT_01aa7cb0` | `LAB_0041c96d` → `FUN_00bb2db0` | `LAB_00428d30` → `FUN_00bb2f20` | pending |
| 7 | `DAT_01aa7cd0` | `LAB_00422ddb` → `FUN_005d5860` | `LAB_0041f0e1` → `FUN_005d59d0` | pending |
| 11 | `DAT_01aa7cc0` | `LAB_00419ca4` → `FUN_00653500` | `LAB_00426f03` → `FUN_00653300` | pending |
| 9 | `DAT_01aa7cc8` | `LAB_0041d4a3` → `FUN_006abfe0` | `LAB_0040d198` → `FUN_006a7fb0` | pending |
| 2 | `DAT_01aa7cd8` | `LAB_00419835` → `FUN_005b9ba0` | `LAB_00411db5` → `FUN_005b9a70` | pending |
| 14 | `DAT_01aa7ce0` | `LAB_0041fc44` → `FUN_006c6d00` | `LAB_00407c0c` → `FUN_006c62c0` | pending |

### 3.2 Confirmed produced runtime type evidence (examples)

#### ArcImage (type_index 0 and 13)

- `FUN_0058eb90` constructs an object whose subsequent load path logs:
  - `ArcImage::Load: No policy class defined...` (string `0x016d50b0`)
  - `C:\ArcanePrime\Main_Branch\Shadowbane\Source\ArcImage.cpp` (`0x016d50f4`)
- RTTI string `. ?AVArcImage@@` exists at `0x016d5018`

#### ArcMesh (type_index 1)

- `FUN_005a33e0` (binary_load_fn) constructs an object via `FUN_005a88b0` and populates vertex arrays.
- `ArcMesh.cpp` source path string exists at `0x016d63fc`
- `FUN_005a43a0` / `FUN_005a4460` / `FUN_005a4530` implement `ArcMesh::GetVertexPosition/Normal/TextureCoord` (strings `0x016d6640`, `0x016d6690`, `0x016d66dc`).

## 4) Known gaps

- For `type_index != {0,1,13}`, the handler addresses are resolved but the **produced runtime types** are still pending: we need to identify the constructed class for each target `FUN_...` (usually by RTTI/vtable + source-path strings) and then trace them forward into rendering usage.

