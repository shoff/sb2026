# CACHE_CONTAINER_FORMATS

Evidence-backed specification of the **monolithic cache container** format used by the repo’s on-disk `cache/*.cache` files (e.g. `Mesh.cache`, `Textures.cache`), and the resolver path from a container entry to a decoded runtime object **where currently provable**.

This document is split into:

- **`sb.exe` container writer/reader (proven by decomp)**: how `sb.exe` selects a `*.cache` filename, writes its header+directory, and performs record lookup.
- **Disk-backed “repo cache” notes**: existing observations about `cache/*.cache` files (requires the actual files to be present to re-validate).

## Inconsistencies (resolved; record-key model locked)

- ✅ **Header size mismatch resolved**: there are **multiple on-disk variants** in `./cache/`.
  - `cache/Mesh.cache` and `cache/Textures.cache` are **Variant B**: **0x28-byte header** + directory entries whose **key is a u32** (plus a 4-byte pad between entries).
  - `sb.exe` also implements **Variant A**: **0x10-byte header** + directory entries keyed by full `ArcCacheID` (u64, lo32/hi32) with a binary-search lookup (`FUN_007db8f0`).
  - `cache/Dungeon.cache` and `cache/Palette.cache` in this repo are tiny **0x200-byte Variant A stubs** (created/recognized by the Variant A reader/writer path).

- ✅ **Mesh.cache / Textures.cache record-key model locked (Variant_B_0x28)**:
  - **Directory stride on disk**: `0x14` bytes
  - **Stored key on disk**: **u32** (`key`), not u64
  - **Fields per stride**: `key(u32), stream_off(u32), usize(u32), csize(u32), pad0(u32)`
  - **Note**: the `pad0` for the **last** record overlaps the payload start at `data_off` (i.e., there is no trailing pad after the last record).

## A.4 Keying mismatch vs proven `sb.exe` lookup primitive (must not be hand-waved)

- Proven `sb.exe` `.cache` lookup primitive `FUN_007db8f0` compares the search key as an **ArcCacheID-shaped u64** (two dwords) and binary-searches an in-memory table of **0x18-byte** entries.
- Disk-verified Variant_B_0x28 containers (`Mesh.cache`, `Textures.cache`) store a **u32 key** per record and do **not** store the u64 `(lo32,hi32)` in the directory.

**Evidence that the proven `sb.exe` `.cache` subsystem is Variant A only** (no Variant B reader/writer found via `.cache` string usage):

- The literal `".cache"` string exists at `0x01704f08` and has a single XREF:
  - `get_xrefs_to(0x01704f08)` → `0x007dbb14` in `FUN_007dba30`
- `FUN_007dba30` (the only proven builder that appends `".cache"`) is called from:
  - `FUN_007d8fb0` (Variant A open/compile path)
  - `FUN_007dbba0` (Variant A create/read path; creates 0x200 stubs when absent)
  - `FUN_007d98c0` (Variant A remove/rewrite path; calls `FUN_007dcba0`)

Therefore:

- For Variant_B_0x28 containers, there must exist either:
  - an **unrecovered second lookup path** in `sb.exe` that does not rely on `FUN_007dba30` / `0x01704f08`, or
  - an **upstream u64→u32 mapping** plus a distinct u32-key lookup routine (not yet located),
  - OR these repo Variant_B containers are not consumed by the proven `sb.exe` `.cache` subsystem.

## A) `sb.exe` monolithic `.cache` container (writer/lookup) — proven

### A.1 Container filename selection (cache subtype → `<Name>.cache`)

`FUN_007dba30(this, out_string)` builds the monolithic container filename by:

- appending the cache root directory
- appending a cache-type dependent string from `PTR_s_Textures_0170508c[ this->subtype ]`
- appending the literal suffix `".cache"` at `0x01704f08`

**Evidence**:

- `FUN_007dba30` decomp shows:
  - `thunk_FUN_00546ae0(out, (&PTR_s_Textures_0170508c)[*(int *)((int)this + 0x6c)]);`
  - `thunk_FUN_00546ae0(out, s__cache_01704f08);`

### A.2 Header + directory writer (what `sb.exe` writes)

`FUN_007dcba0(this)` writes the container header and directory to the active stream at `this+0x70`:

- seeks to offset 0 (`thunk_FUN_0051a880(stream, 0, 0)`)
- writes 4×u32 header
- writes `record_count` directory records (each 0x14 bytes)
- writes a zero-filled padding/terminator region if `this->data_end` exceeds the computed end-of-directory

**Header (0x10 bytes)** — four little-endian u32 values written in order:

```text
u32 record_count;     // (this->dir_end - this->dir_begin) / 0x18
u32 data_end;         // *(u32 *)(this + 0x74)
u32 data_end_dup;     // *(u32 *)(this + 0x78)
u32 data_cursor;      // *(u32 *)(this + 0x7c)
```

**Directory record (0x14 bytes)** — five little-endian u32 values:

```text
struct CacheDirRecord {
  u32 id_lo;              // ArcCacheID low32
  u32 id_hi;              // ArcCacheID high32
  u32 stream_off;         // offset of payload (relative to file start)
  u32 uncompressed_size;  // bytes after inflate (or raw)
  u32 compressed_size;    // bytes in file payload region
}
```

**Evidence**:

- `FUN_007dcba0` decomp:
  - writes `local_18 = (dir_end-dir_begin)/0x18` then serializes it via `thunk_FUN_007e1900(...); thunk_FUN_0051a510(stream,&local_14,4);`
  - per record, copies two dwords from the `ArcCacheID` object via `thunk_FUN_00511750` / `thunk_FUN_00511770` and then serializes the three u32 fields at `entry+8`, `entry+0xC`, `entry+0x10`

### A.3 Record lookup (binary search; no u32 transform observed here)

`FUN_007db8f0(this, arc_cache_id_u64_ptr)` performs **binary search** over the in-memory directory vector:

- range: `[this+0x54, this+0x58)` in steps of `0x18`
- comparison: `thunk_FUN_00511b20(entry, key)` and `thunk_FUN_00511bd0(entry, key)`

This is a standard “lower_bound” style loop, and it searches by the full `ArcCacheID` (two dwords), not by a separate u32 key computed from it (no such transform is present in this function).

**Evidence**:

- `FUN_007db8f0` decomp shows the `do { mid=(hi+lo)/2; ... } while (lo < hi)` loop with two comparisons per iteration.

## 1) On-disk inventory (repo)

`cache/` contains 13 `.cache` containers (no per-asset `^\d{20}` filenames):

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

## 2) Container header format (Variant B; disk-verified)

The following is **disk-verified** against the actual files in this repo:

- `cache/Mesh.cache` (size `0x02381f4c`)
- `cache/Textures.cache` (size `0x66c4435c`)

Variant B uses a fixed **0x28-byte header**, then a directory region, then the payload region. The payload begins exactly at `data_off` and the first payload bytes are the zlib header `0x78 ??` for zlib-compressed records.

Interpret the first 0x28 bytes as 10 little-endian u32 values:

| Offset | Field | Meaning (disk-backed) |
|---:|---|---|
| 0x00 | `count_plus_1` | Used as `record_count + 1` in Variant B parsing (`record_count = count_plus_1 - 1`). |
| 0x04 | `data_off` | Offset where payload region begins (confirmed: zlib header bytes start at `data_off`). |
| 0x08 | `file_size` | Equals the file length in bytes. |
| 0x0C | `sentinel` | Always `0xFFFFFFFF` in tested files. |
| 0x10 | `zero` | Always `0x00000000` in tested files. |
| 0x14 | `base_key` | Equals `min_key - 1` for tested files (e.g., Mesh: min key 101, base_key 100). |
| 0x18 | `data_off_dup` | Duplicate of `data_off`. |
| 0x1C | `hdr_u32_7` | Unknown (varies per container). |
| 0x20 | `hdr_u32_8` | Unknown (varies per container). |
| 0x24 | `hdr_u32_9` | Unknown (varies per container). |

### 2.1 Concrete header examples

#### `cache/Mesh.cache`

- `count_plus_1 = 0x5f43` (= 24387) ⇒ `record_count = 24386`
- `data_off = 0x7714c`
- `file_size = 0x2381f4c` (= 37,232,460)
- `base_key = 0x64` (= 100)

**First 0x40 bytes (hex)**:

```text
00000000  43 5f 00 00 4c 71 07 00 4c 1f 38 02 ff ff ff ff
00000010  00 00 00 00 64 00 00 00 4c 71 07 00 fc 0b 00 00
00000020  80 06 00 00 00 00 00 00 65 00 00 00 cc 77 07 00
00000030  fc 0b 00 00 8d 06 00 00 00 00 00 00 66 00 00 00
```

Notes:

- First directory entry begins at `0x28` (key=101).
- Payload begins at `data_off=0x7714c` and `file[data_off:data_off+2] == 0x78 0xda` (zlib).

#### `cache/Textures.cache`

- `count_plus_1 = 0x25d0` (= 9680) ⇒ `record_count = 9679`
- `data_off = 0x2f450`
- `file_size = 0x66c4435c` (= 1,724,138,332)
- `base_key = 0x1` (= 1)

**First 0x40 bytes (hex)**:

```text
00000000  d0 25 00 00 50 f4 02 00 5c 43 c4 66 ff ff ff ff
00000010  00 00 00 00 01 00 00 00 50 f4 02 00 1a 00 01 00
00000020  b3 35 00 00 00 00 00 00 0a 00 00 00 03 2a 03 00
00000030  1a 00 04 00 2e cc 00 00 00 00 00 00 64 00 00 00
```

Notes:

- First directory entry begins at `0x28` (key=10).
- Payload begins at `data_off=0x2f450` and `file[data_off:data_off+2] == 0x78 0x9c` (zlib).

#### `cache/Motion.cache`

- `count_plus_1 = 0x5df` (= 1503) ⇒ `record_count = 1502`
- `data_off = 0x757c`
- `base_key = 0x0f4241` (= 1,000,001) with first key observed `1,000,002`

## 3) Directory record format (Variant B; disk-verified)

### 3.1 Layout

Directory records begin at offset `0x28`.

Each entry is stored as **16 bytes of data** plus **4 bytes of padding** (always `0`) *between entries*, i.e. an effective stride of `0x14`:

```text
// data (0x10)
u32 key;
u32 stream_off;
u32 uncompressed_size;
u32 compressed_size;
// pad (0x04) — present between entries, absent after the last entry
u32 pad0; // usually 0x00000000
```

The **last entry has no trailing pad**. This is directly observable in both `Mesh.cache` and `Textures.cache`:

- The last entry begins at `data_off - 0x10`
- The 4 bytes that would be the “pad” at `data_off` are actually the first payload bytes (zlib header `0x78 ??`)

**Concrete proof**:

- `Mesh.cache`:
  - `record_count = 24386`
  - last entry start = `0x0007713c`
  - `data_off = 0x0007714c`
  - `data_off - last_entry_start = 0x10`
  - bytes at `data_off` begin with `78 da ...` (zlib)
- `Textures.cache`:
  - `record_count = 9679`
  - last entry start = `0x0002f440`
  - `data_off = 0x0002f450`
  - `data_off - last_entry_start = 0x10`
  - bytes at `data_off` begin with `78 9c ...` (zlib)

### 3.2 First 10 and last 10 entries (Mesh.cache)

See the computed offsets and the observed pad overlap at the last entry:

```text
Mesh.cache first_10:
  idx=     0 dir_off=0x00000028 key=       101 so=0x000777cc usize=     3068 csize=     1677 pad=0x00000000
  idx=     1 dir_off=0x0000003c key=       102 so=0x00077e5c usize=     5322 csize=     2733 pad=0x00000000
  idx=     2 dir_off=0x00000050 key=       103 so=0x0007890c usize=      760 csize=      464 pad=0x00000000
  idx=     3 dir_off=0x00000064 key=       201 so=0x00078adc usize=     3012 csize=     1539 pad=0x00000000
  idx=     4 dir_off=0x00000078 key=       202 so=0x000790e4 usize=     4098 csize=     2269 pad=0x00000000
  idx=     5 dir_off=0x0000008c key=       301 so=0x000799c4 usize=     5256 csize=     2332 pad=0x00000000
  idx=     6 dir_off=0x000000a0 key=       302 so=0x0007a2e4 usize=     5256 csize=     2341 pad=0x00000000
  idx=     7 dir_off=0x000000b4 key=       351 so=0x0007ac0c usize=      226 csize=      103 pad=0x00000000
  idx=     8 dir_off=0x000000c8 key=       361 so=0x0007ac74 usize=    66200 csize=    15798 pad=0x00000000
  idx=     9 dir_off=0x000000dc key=       382 so=0x0007ea2c usize=     5320 csize=     2707 pad=0x00000000

Mesh.cache last_10:
  idx= 24376 dir_off=0x00077088 key=   7000245 so=0x0237e3b4 usize=     4460 csize=     2653 pad=0x00000000
  idx= 24377 dir_off=0x0007709c key=   7000253 so=0x0237ee14 usize=     3068 csize=     1988 pad=0x00000000
  idx= 24378 dir_off=0x000770b0 key=   7000263 so=0x0237f5dc usize=     4410 csize=     2882 pad=0x00000000
  idx= 24379 dir_off=0x000770c4 key=   7000264 so=0x02380124 usize=     1758 csize=     1086 pad=0x00000000
  idx= 24380 dir_off=0x000770d8 key=   7000271 so=0x02380564 usize=     2736 csize=     1735 pad=0x00000000
  idx= 24381 dir_off=0x000770ec key=   7000281 so=0x02380c2c usize=     3286 csize=     1795 pad=0x00000000
  idx= 24382 dir_off=0x00077100 key=  77000101 so=0x02381334 usize=      910 csize=      303 pad=0x00000000
  idx= 24383 dir_off=0x00077114 key=  77000102 so=0x02381464 usize=      706 csize=      163 pad=0x00000000
  idx= 24384 dir_off=0x00077128 key=  77000103 so=0x0238150c usize=      226 csize=       78 pad=0x00000000
  idx= 24385 dir_off=0x0007713c key=  77000301 so=0x0238155c usize=     4400 csize=     2537 pad=0x56b5da78  (pad overlaps payload at 0x7714c)
```

### 3.3 First 10 and last 10 entries (Textures.cache)

```text
Textures.cache first_10:
  idx=     0 dir_off=0x00000028 key=        10 so=0x00032a03 usize=   262170 csize=    52270 pad=0x00000000
  idx=     1 dir_off=0x0000003c key=       100 so=0x0003f631 usize=   196634 csize=     5426 pad=0x00000000
  idx=     2 dir_off=0x00000050 key=      1000 so=0x00040b63 usize=  4194330 csize=   539346 pad=0x00000000
  idx=     3 dir_off=0x00000064 key=     10000 so=0x000c4635 usize=    65562 csize=    33314 pad=0x00000000
  idx=     4 dir_off=0x00000078 key=    100000 so=0x000cc857 usize=   196634 csize=    94522 pad=0x00000000
  idx=     5 dir_off=0x0000008c key=     10001 so=0x000e3991 usize=    65562 csize=    34508 pad=0x00000000
  idx=     6 dir_off=0x000000a0 key=    100010 so=0x000ec05d usize=   196634 csize=    77944 pad=0x00000000
  idx=     7 dir_off=0x000000b4 key=    100011 so=0x000ff0d5 usize=   196634 csize=    76842 pad=0x00000000
  idx=     8 dir_off=0x000000c8 key=    100012 so=0x00111cff usize=   196634 csize=   162644 pad=0x00000000
  idx=     9 dir_off=0x000000dc key=    100013 so=0x00139853 usize=   196634 csize=   158297 pad=0x00000000

Textures.cache last_10:
  idx=  9669 dir_off=0x0002f38c key=      9781 so=0x66bd0467 usize=    49178 csize=    32825 pad=0x00000000
  idx=  9670 dir_off=0x0002f3a0 key=      9782 so=0x66bd84a0 usize=    49178 csize=    29900 pad=0x00000000
  idx=  9671 dir_off=0x0002f3b4 key=      9783 so=0x66bdf96c usize=    49178 csize=    27127 pad=0x00000000
  idx=  9672 dir_off=0x0002f3c8 key=      9784 so=0x66be6363 usize=    49178 csize=    15287 pad=0x00000000
  idx=  9673 dir_off=0x0002f3dc key=      9785 so=0x66be9f1a usize=   196634 csize=   125884 pad=0x00000000
  idx=  9674 dir_off=0x0002f3f0 key=      9786 so=0x66c08ad6 usize=   196634 csize=   131963 pad=0x00000000
  idx=  9675 dir_off=0x0002f404 key=      9787 so=0x66c28e51 usize=    49178 csize=    33134 pad=0x00000000
  idx=  9676 dir_off=0x0002f418 key=      9788 so=0x66c30fbf usize=    49178 csize=    31467 pad=0x00000000
  idx=  9677 dir_off=0x0002f42c key=      9789 so=0x66c38aaa usize=    49178 csize=    21641 pad=0x00000000
  idx=  9678 dir_off=0x0002f440 key=      9790 so=0x66c3df33 usize=    49178 csize=    25641 pad=0x7ded9c78  (pad overlaps payload at 0x2f450)
```

## 3.4 Variant selection (repo inventory)

Classification (by disk header signature) of the repo’s `./cache/*.cache`:

- **Variant_B_0x28_u32 (data_off_dup==data_off)**: `CZone.cache`, `Mesh.cache`, `Motion.cache`, `Skeleton.cache`, `Sound.cache`, `TerrainAlpha.cache`, `Tile.cache`, `Textures.cache`, `Visual.cache`
- **Variant_B2_0x28_u32 (data_off_dup!=data_off)**: `CObjects.cache`, `Render.cache`
  - Both have a 0x28 header, zlib payload beginning at `data_off`, and the same 0x14-stride directory entries (`key, stream_off, usize, csize, pad0`) with last-entry pad overlap at `data_off`.
- **Variant_A_0x10_u64 (ArcCacheID directory)**: `Dungeon.cache` (0x200 stub), `Palette.cache` (0x200 stub)

## 4) Compression / payload encoding (disk-backed)

### 4.1 Zlib-compressed payloads

For most containers (e.g. `Mesh.cache`, `Textures.cache`, `Motion.cache`, `Skeleton.cache`, `Render.cache`):

- `file[stream_off] == 0x78` (zlib header)
- `zlib.decompress(file[stream_off : stream_off+compressed_size])` yields exactly `uncompressed_size` bytes

This holds for thousands of records (e.g. Mesh: 24386/24386 records zlib; Textures: 9679/9679 records zlib).

### 4.2 Raw/uncompressed payloads (Sound.cache)

`cache/Sound.cache` is mixed:

- Most records are **raw**: `stream_off` does not point to `0x78`, and `compressed_size == uncompressed_size`
- A small subset are zlib streams (6 records detected by the `0x78` header test)

## 5) Five concrete “ID → container → record → offset → decoder” walkthroughs

These are **disk-backed** through `cache/*.cache` directory records and **decoder-backed** through previously resolved `sb.exe` loader targets (from `FUN_0091d6b0` wiring).

> Note on “ArcCacheID”: the directory `key` is a 32-bit integer. We still need to prove (in `sb.exe`) the exact transform from `ArcCacheID` (low/high) to this `key`. Disk-backed keys appear to be numeric IDs that can be represented as 20-digit decimals via zero-padding.

### Walkthrough 1 — ArcMesh (binary) via `cache/Mesh.cache`, key=101

- **Container**: `cache/Mesh.cache`
- **Record**:
  - key = 101 (`id20=00000000000000000101`)
  - stream_off = `0x777cc`
  - compressed_size = 1677
  - uncompressed_size = 3068
- **Payload decode**:
  - zlib stream at `0x777cc` decompresses to 3068 bytes
- **Decoder (sb.exe)**:
  - mesh `binary_load_fn` resolved: `LAB_004097fa` → `FUN_005a33e0`
  - produced runtime type: `ArcMesh` (confirmed by `ArcMesh` RTTI + accessors and the loader itself)

### Walkthrough 2 — ArcMesh (binary) via `cache/Mesh.cache`, key=102

- `cache/Mesh.cache` key=102 (`id20=...102`) stream_off `0x77e5c` csize 2733 usize 5322
- decoder: `FUN_005a33e0` → `ArcMesh`

### Walkthrough 3 — ArcImage (binary) via `cache/Textures.cache`, key=10

- **Container**: `cache/Textures.cache`
- **Record**:
  - key = 10 (`id20=00000000000000000010`)
  - stream_off = `0x32a03`
  - compressed_size = 52270
  - uncompressed_size = 262170
- **Payload decode**:
  - zlib stream at `0x32a03` decompresses to 262170 bytes
- **Decoder (sb.exe)**:
  - image `binary_load_fn` resolved: `LAB_004212f1` → `FUN_0058efb0`
  - produced runtime type: `ArcImage` (confirmed by ArcImage RTTI + ArcImage.cpp strings + loader behavior)

### Walkthrough 4 — ArcImage (binary) via `cache/Textures.cache`, key=100

- `cache/Textures.cache` key=100 (`id20=...100`) stream_off `0x3f631` csize 5426 usize 196634
- decoder: `FUN_0058efb0` → `ArcImage`

### Walkthrough 5 — ArcMotion (binary) via `cache/Motion.cache`, key=1000002

- **Container**: `cache/Motion.cache`
- **Record**:
  - key = 1,000,002 (`id20=00000000000001000002`)
  - stream_off = `0x14ff4`
  - compressed_size = 5123
  - uncompressed_size = 12967
- **Payload decode**:
  - zlib stream decompresses to 12967 bytes
- **Decoder**: pending (requires confirming which `binary_load_fn` target corresponds to motions in `sb.exe` for this repo’s cache subtype wiring).

## 6) What’s still required to satisfy Phase 1 “no ambiguity”

To close the “ArcCacheID → container selection → record key transform → lookup function” requirements we must (with working Ghidra MCP):

- Locate the `sb.exe` code that opens `*.cache` containers (path includes the literal `.cache` suffix; `sb.exe` has a `".cache"` string constant).
- Identify the lookup primitive: given an `ArcCacheID` (two dwords), compute the directory record `key` and find the matching record.
- Prove whether `key` is:
  - `low32`, `high32`, `low32^high32`, endian-swapped, or a hash
  - and confirm which asset caches use which transform (if multiple).

