# DISK_BACKED_ID_PATH_PROOFS

Disk-backed proofs using the repo’s real `cache/` directory.

## 0) Ground truth: what exists on disk under `/cache`

`cache/` contains **13 container files** (no per-asset files):

- `cache/CObjects.cache`
- `cache/CZone.cache`
- `cache/Dungeon.cache`
- `cache/Mesh.cache`
- `cache/Motion.cache`
- `cache/Palette.cache`
- `cache/Render.cache`
- `cache/Skeleton.cache`
- `cache/Sound.cache`
- `cache/TerrainAlpha.cache`
- `cache/Textures.cache`
- `cache/Tile.cache`
- `cache/Visual.cache`

**Evidence**: OS-level directory listing (PowerShell) and `python` directory enumeration.

### 0.1 Important correction re: “20-digit filenames”

There are **0 filenames** in `cache/` matching `^\d{20}` because the cache in this repo is stored as **monolithic `.cache` containers**, not as `20-digit-id.ext` files on disk.

However, the 20-digit decimal representation is still **the canonical ID string format** in the client (`"%0.20I64u"`), and we can prove disk-backed ID resolution as:

`(container file path, entry key) → (zlib stream offset, compressed size, decompressed bytes) → (binary_load_fn decoder) → (runtime type)`

## 1) Container entry directory record format (proven empirically)

Both `cache/Mesh.cache` and `cache/Textures.cache` contain a directory region whose entries can be parsed as:

`u32 key, u32 stream_off, u32 uncompressed_size, u32 compressed_size, u32 reserved`

Validation rule:

- At `stream_off`, the data begins with `0x78` (zlib header)
- `zlib.decompress(file[stream_off : stream_off+compressed_size])` yields exactly `uncompressed_size` bytes (confirmed for `Textures.cache`, and for the sampled `Mesh.cache` entries)

## 2) At least 10 disk-backed ID→(path, offset, sizes) proofs

> `id20` is the 20-digit decimal form of the **u32 key** zero-extended to u64 (`%0.20I64u` semantics).

### 2.1 `Mesh.cache` (ArcMesh binary payloads)

- `cache/Mesh.cache` key=101 id20=`00000000000000000101` dir_off=0x28 stream_off=0x777cc csize=1677 usize=3068
- `cache/Mesh.cache` key=102 id20=`00000000000000000102` dir_off=0x3c stream_off=0x77e5c csize=2733 usize=5322
- `cache/Mesh.cache` key=103 id20=`00000000000000000103` dir_off=0x50 stream_off=0x7890c csize=464 usize=760
- `cache/Mesh.cache` key=201 id20=`00000000000000000201` dir_off=0x64 stream_off=0x78adc csize=1539 usize=3012
- `cache/Mesh.cache` key=202 id20=`00000000000000000202` dir_off=0x78 stream_off=0x790e4 csize=2269 usize=4098
- `cache/Mesh.cache` key=301 id20=`00000000000000000301` dir_off=0x8c stream_off=0x799c4 csize=2332 usize=5256
- `cache/Mesh.cache` key=302 id20=`00000000000000000302` dir_off=0xa0 stream_off=0x7a2e4 csize=2341 usize=5256
- `cache/Mesh.cache` key=351 id20=`00000000000000000351` dir_off=0xb4 stream_off=0x7ac0c csize=103 usize=226

### 2.2 `Textures.cache` (ArcImage binary payloads)

- `cache/Textures.cache` key=10 id20=`00000000000000000010` dir_off=0x28 stream_off=0x32a03 csize=52270 usize=262170
- `cache/Textures.cache` key=100 id20=`00000000000000000100` dir_off=0x3c stream_off=0x3f631 csize=5426 usize=196634
- `cache/Textures.cache` key=1000 id20=`00000000000000001000` dir_off=0x50 stream_off=0x40b63 csize=539346 usize=4194330
- `cache/Textures.cache` key=10000 id20=`00000000000000010000` dir_off=0x64 stream_off=0xc4635 csize=33314 usize=65562
- `cache/Textures.cache` key=100000 id20=`00000000000000100000` dir_off=0x78 stream_off=0xcc857 csize=94522 usize=196634
- `cache/Textures.cache` key=10001 id20=`00000000000000010001` dir_off=0x8c stream_off=0xe3991 csize=34508 usize=65562
- `cache/Textures.cache` key=100010 id20=`00000000000000100010` dir_off=0xa0 stream_off=0xec05d csize=77944 usize=196634
- `cache/Textures.cache` key=100011 id20=`00000000000000100011` dir_off=0xb4 stream_off=0xff0d5 csize=76842 usize=196634

## 3) Five fully worked examples (ID → location → decoder → runtime type)

### Example 1 (ArcImage / Textures.cache)

- **Disk path**: `cache/Textures.cache`
- **Entry key**: 10 (`id20=00000000000000000010`)
- **Directory record location**: `dir_off=0x28`
- **Zlib stream**: `stream_off=0x32a03`, `csize=52270`, `usize=262170`
- **Payload sanity**: decompressed payload begins with u32s like `0x00000100, 0x00000100, 0x00000004, ...` (consistent with a structured binary header).

**Decode proof (sb.exe)**:

- This cache subtype is wired in `FUN_0091d6b0` with `binary_load_fn` thunk `LAB_004212f1` → `FUN_0058efb0`.
- `FUN_0058efb0` constructs an `ArcImage` and reads typed fields from the binary stream.
- It sets the object’s `ArcCacheID` storage at `obj+0x10` via `FUN_00512610`.

### Example 2 (ArcImage / Textures.cache)

- **Disk path**: `cache/Textures.cache`
- **Entry key**: 100 (`id20=00000000000000000100`)
- **Directory record location**: `dir_off=0x3c`
- **Zlib stream**: `stream_off=0x3f631`, `csize=5426`, `usize=196634`

Decoder: `FUN_0058efb0` → **ArcImage** (same wiring as Example 1).

### Example 3 (ArcMesh / Mesh.cache)

- **Disk path**: `cache/Mesh.cache`
- **Entry key**: 101 (`id20=00000000000000000101`)
- **Directory record location**: `dir_off=0x28`
- **Zlib stream**: `stream_off=0x777cc`, `csize=1677`, `usize=3068`
- **Payload sanity**: decompressed payload begins with floats (e.g. `0x40fdd8dd`), consistent with vertex-like data.

**Decode proof (sb.exe)**:

- Mesh cache subtype is wired in `FUN_0091d6b0` as `type_index=1` with `binary_load_fn` thunk `LAB_004097fa` → `FUN_005a33e0`.
- `FUN_005a33e0` constructs the mesh runtime object and fills vertex arrays.

### Example 4 (ArcMesh / Mesh.cache)

- **Disk path**: `cache/Mesh.cache`
- **Entry key**: 102 (`id20=00000000000000000102`)
- **Directory record location**: `dir_off=0x3c`
- **Zlib stream**: `stream_off=0x77e5c`, `csize=2733`, `usize=5322`

Decoder: `FUN_005a33e0` → **ArcMesh** (same wiring as Example 3).

### Example 5 (ArcMesh / Mesh.cache)

- **Disk path**: `cache/Mesh.cache`
- **Entry key**: 202 (`id20=00000000000000000202`)
- **Directory record location**: `dir_off=0x78`
- **Zlib stream**: `stream_off=0x790e4`, `csize=2269`, `usize=4098`

Decoder: `FUN_005a33e0` → **ArcMesh** (same wiring as Example 3).

## 4) What still needs tightening (strictly evidence-backed)

- Prove whether the directory record **key** is truly the `ArcCacheID` (low-only) or a separate 32-bit identifier that is *mapped* to `ArcCacheID` elsewhere.
  - Current evidence: the repo’s cache containers do not store 20-digit filenames; keys are stored as `u32` in the directory.

