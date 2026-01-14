# CACHE_MISS_OPEN_CHAIN

Evidence-backed trace of the **cache miss** path(s) that turn an `ArcCacheID` into a concrete file/stream and then into a constructed runtime object.

> Scope note: the core “miss-load” mechanism for many assets goes through **`ArcFileCache`** (see §2). In this update, the three previously-indirect targets are now **concretely resolved** (see §4.2, §4.3, §5.3).

## 1) Proven primitives we build on

- **`ArcCacheID` compare/hash**
  - Hash: `FUN_00512210(u32* key)` → `key[1] ^ key[0]`
  - Equality: `FUN_00511b20(key_a, key_b)` compares two dwords
- **Cache roots**
  - `cache/Text/` at `0x016e0ef8`
  - `cache/Binary/` at `0x01716070`
  - Assigned in config init: `FUN_0088aad0`

## 2) `ArcFileCache` is a central miss-load mechanism (confirmed)

### 2.1 Identification evidence

- RTTI: `".?AVArcFileCache@@"` at `0x01704c78`
- Source path string: `C:\\ArcanePrime\\Main_Branch\\Shadowbane\\Source\\ObjectServer\\ArcFileCache.cpp` at `0x01704d58`
- Logging strings:
  - `ArcFileCache::LoadFromDisk: caught unknown exception while loading %s\n` at `0x01704e60`
  - `ArcFileCache::LoadFromDisk: caught exception %s while loading %s\n` at `0x01704eb8`

**Evidence**: `list_strings` filters `FileCache` / `ArcFileCache::`.

### 2.2 Global cache managers wired to file caches (confirmed)

`FUN_0091d6b0` constructs multiple cache managers and then assigns:

- `DAT_017737d8 = DAT_01aa7c94` (used as an asset cache manager elsewhere)
- `DAT_017737f4 = DAT_01aa7cdc`
- `DAT_017737f8 = DAT_01aa7ce4`

These managers are constructed by `FUN_00925f50(this, file_cache_ptr)` which stores:

- `this+0x1c = file_cache_ptr`

and initializes internal hash/LRU structures used by `thunk_FUN_00440db0` (see §3).

**Evidence**: `FUN_0091d6b0`, `FUN_00925f50` decomp; XREF write sites to `DAT_017737d8/…`.

## 3) Cache lookup + miss insert core (confirmed mechanics; partial miss-load)

### 3.1 Lookup + LRU behavior (hit path)

`thunk_FUN_00440db0`:

- Probes the hash table via `FUN_004416c0` / `FUN_00441650`
- On hit, re-links the found node in an LRU list using node fields at `+0x24/+0x28`
- Returns the node pointer via `param_1`

**Evidence**: `thunk_FUN_00440db0` decomp.

### 3.2 Miss behavior (key detail: indirect loader hook exists)

On a miss, `thunk_FUN_00440db0` checks `this+0x1c != 0` and performs an **indirect call** via `(**(code **)(**(int **)((int)this + 0x1c) + 4))();`.

This is a critical pivot: it indicates the cache manager is wired to a **secondary loader** object (stored at `this+0x1c`) that is consulted only when the table misses.

**Evidence**: `thunk_FUN_00440db0` decomp; it calls through `this+0x1c` only on miss.

> Work in progress: resolve the concrete function behind this vtable slot for each cache manager instance so we can provide absolute addresses for the miss-load function(s) (see §6).

## 4) Concrete miss-load chain inside `ArcFileCache::LoadFromDisk` (strongly evidenced)

`FUN_007da440(param_1)` (identified by ArcFileCache.cpp path string usage and behavior) performs:

1. **Ensure file index built**:
   - If `param_1[0x20] == 0` → calls `FUN_007dd520((int)param_1)` (directory enumeration & ID parsing)
2. **For each cache id** (iterating an internal list at `param_1[0x18]..param_1[0x19]`):
   - If not already present in an internal map:
     - Build a cache-id struct `local_24` from an entry (copies 8 bytes via `thunk_FUN_005117b0`)
     - Creates a filename/path string:
       - `(**(code **)(*param_1 + 8))(local_c0, &local_24, 1);`
       - This is an indirect call; it is the “**Build path from ID**” step.
     - Calls a per-cache “open+decode” function pointer:
       - `puVar4 = (undefined4 *)(*(code *)param_1[0x21])(out_handle, &local_24, local_c0);`
       - Then reads `local_30 = (int *)*puVar4` and checks for `NULL` to log corruption.
     - On success:
       - `thunk_FUN_00512610(local_30, &local_24);` (set object’s cache id)
       - `thunk_FUN_007d9ee0(param_1, local_30);` (insert/track in cache)
3. Logs “Finished” and (optionally) “Creating pak file …” depending on progress thresholds.

**Evidence**: `FUN_007da440` decomp; callsites use ArcFileCache.cpp path string `0x01704d58`.

### Key derived interfaces (evidence-backed)

- **BuildPathFromID**: virtual call at `(*param_1 + 8)` inside `FUN_007da440`
- **Open+Decode (per cache instance)**: function pointer call `(*(code*)param_1[0x21])(...)` inside `FUN_007da440`

### 4.1 Where the 3 indirections live in `ArcFileCache` (confirmed offsets)

From `FUN_007d8c50` (ArcFileCache ctor) disassembly:

- **vtable**: `*(this+0x00) = 0x0155a97c` (final vtable after base init)
- **binary_load_fn**: `*(this+0x50) = param_1` (from constructor arg)
- **open_decode_fn**: initialized to 0 (`*(this+0x84)=0`), then assigned by `FUN_007da010(this, fn)` which writes `*(this+0x84)=fn`

**Evidence**: `FUN_007d8c50` disassembly shows `MOV dword ptr [ESI + 0x50],EAX` and `MOV dword ptr [ESI],0x155a97c`; `FUN_007da010` (previously recovered) stores at `this+0x84`.

### 4.2 Resolved vtable slot `+8` target: `BuildPathFromID` (concrete)

#### 4.2.1 Proof of the target

- `FUN_007d8c50` sets `this->vtable = 0x0155a97c`
- `get_xrefs_to(0x007da120)` reports **From `0x0155a984` [DATA]**
- `0x0155a984 == 0x0155a97c + 0x08` ⇒ the vtable entry at `+8` points to `FUN_007da120`

**Conclusion**: `ArcFileCache::BuildPathFromID` (the virtual call at `(*this + 8)`) resolves to **`FUN_007da120`**.

#### 4.2.2 What `BuildPathFromID` builds (concrete rules)

`FUN_007da120(this, outString, ArcCacheID* id, int mode)` builds a path-ish **string key** by concatenating:

- **Root selection by `mode`**:
  - `mode == 1` ⇒ append `DAT_01aa308c` (String)
  - `mode == 2` ⇒ if `DAT_01aa73f0 != 0` append `DAT_01aa73d8` (String)
  - else ⇒ append `DAT_01aa30a4` (String), and if `mode == 0` also prepend one of:
    - `DAT_01704c90` if `this->type_index (this+0x6c)` is 3 or 10
    - `DAT_016d6350` if `this->type_index` is 4 or 11
- **Per-type directory**: append `(&PTR_s_Textures_0170508c)[type_index]` (array of string pointers)
- `'/'`
- **Per-type bucket letter**: append 1 byte from a table at `0x01705088`, indexed by `type_index`
  - evidence: `MOV EDX,[0x01705088]; MOV AL, byte ptr [ECX + EDX]`
- **ID string**: append the result of `ArcCacheID::ToString20(out)`:
  - `CALL 0x00404aed` with `ECX=id` and `PUSH &local_string`
  - `0x00404aed` is a thunk to `FUN_00511cd0`, which calls `FUN_00511ec0`
  - `FUN_00511ec0` disassembly shows it formats the **two dwords** from the `ArcCacheID` object via `"%0.20I64u"` (pushes `[this+4]` then `[this+0]`)
- **Per-type suffix**: append `(&PTR_DAT_017050c8)[type_index]` (array of string pointers; suffix/extension pattern)

**Evidence**: `FUN_007da120` decomp + disassembly; `FUN_00511ec0` disassembly (pushes low/high dwords into formatting call).

## 5) Binary cache stream read/write helpers (confirmed)

## 5) Binary cache stream read/write helpers (confirmed)

### 5.1 Read/uncompress (binary-open chain component)

`FUN_007db270(this, stream_ptr)`:

- Allocates buffers based on `stream_ptr+0x10` (size) and `stream_ptr+0x0c` (compressed size)
- If `this+0x6c != 8`, calls `FUN_00ccc950(...)` to uncompress into the output buffer
- Logs on uncompress failure using ArcFileCache.cpp path and format string `s__s_Error_uncompressing__s_01704e40`
- Returns a handle/wrapper created by `thunk_FUN_007e1540(...)` (stream wrapper around decompressed bytes)

**Evidence**: `FUN_007db270` decomp.

### 5.2 Write/compress + alignment

`FUN_007dc900(this, stream_ptr, out_len_ptr)`:

- Compresses input stream unless `this+0x6c == 8` (passthrough)
- Pads to 8-byte alignment (`uVar4 = -(int)local_8 & 7`)
- Writes compressed bytes + optional pad bytes to an IO stream at `this+0x70`

**Evidence**: `FUN_007dc900` decomp.

### 5.3 Dispatching binary loads for a cache type

`FUN_007dad20(file_cache)`:

- If `file_cache+0x50 == 0`, logs `No binary load function for %s` (`s_No_binary_load_function_for__s_01704e18`)
- Else iterates entries and calls:
  - `uVar3 = thunk_FUN_007db270(file_cache, entry_stream)` (uncompress)
  - `piVar4 = (int *)(*(code*)file_cache->binary_load_fn)(..., entry_id, uVar3)` (indirect)
  - and stores results via `thunk_FUN_004426c0(...)`

**Evidence**: `FUN_007dad20` decomp.

### 5.4 Resolved `open_decode_fn` and `binary_load_fn` targets (concrete)

All `ArcFileCache` instances are constructed in `FUN_0091d6b0`. For each:

- `binary_load_fn` is passed as the 2nd arg to `thunk_FUN_007d8c50(..., &LAB_xxx, type_index)`
- `open_decode_fn` is passed to `thunk_FUN_007da010(file_cache, &LAB_xxx)`

Each `&LAB_xxx` thunk is proven to transfer control to a concrete implementation via `get_xrefs_from(LAB_xxx) → FUN_xxx [UNCONDITIONAL_CALL]`.

Below are the resolved targets for the two “easy” asset types we can fully prove in this pass:

- **ArcImage** (confirmed)
  - `open_decode_fn`: `LAB_00426a30` → `FUN_0058eb90`
  - `binary_load_fn`: `LAB_004212f1` → `FUN_0058efb0`
  - Evidence for produced type: `FUN_0058dd50` logs `ArcImage::Load...` and references `ArcImage.cpp` (`0x016d50f4`), and RTTI string `. ?AVArcImage@@` exists at `0x016d5018`.
- **ArcMesh** (confirmed)
  - `open_decode_fn`: `LAB_00414038` → `FUN_005a3e20`
  - `binary_load_fn`: `LAB_004097fa` → `FUN_005a33e0`
  - Evidence for produced type: `ArcMesh.cpp` source path string `0x016d63fc` and `ArcMesh::GetVertex*` functions (`FUN_005a43a0`, `FUN_005a4460`, `FUN_005a4530`) operate on the produced object’s internal arrays.

## 6) Pseudocode (implementation-grade; limited to proven operations)

### 6.1 ArcFileCache_LoadFromDisk (miss-load loop)

```text
// Evidence: FUN_007da440
ArcFileCache_LoadFromDisk(cache):
  if cache.index_built_flag == 0:
    BuildIndexFromDisk(cache)                // FUN_007dd520

  for each id in cache.id_list:
    if not cache.has_loaded(id):
      path = cache.vtbl.BuildPathFromID(id, mode=1)   // indirect call (*cache+8)
      obj = cache.open_decode_fn(id, path)            // indirect call (cache+0x21)
      if obj == NULL:
        log "File corrupt"
        continue
      obj.cache_id = id                                // thunk_FUN_00512610
      cache.Insert(obj)                                // thunk_FUN_007d9ee0
```

### 6.2 ArcFileCache_BinaryLoadAll (per-type binary dispatch)

```text
// Evidence: FUN_007dad20 + FUN_007db270
ArcFileCache_BinaryLoadAll(cache):
  if cache.binary_load_fn == NULL:
    log "No binary load function"
    return

  for each entry in cache.binary_entries:
    stream = UncompressEntry(entry)                    // FUN_007db270
    obj = cache.binary_load_fn(entry.id, stream)        // indirect call
    cache.StoreBinaryLoaded(obj)
```

## 7) Immediate next evidence to collect (to satisfy “stop conditions”)

- Complete the full **ID → key/path → open → decode → runtime type** proof for one concrete ID pulled from an actual cache index (requires either a cache directory present on disk, or extraction from a `.cache` container build step).
- From confirmed produced types (`ArcMesh`, `ArcImage`), continue forward to:
  - the renderer-consumed assembled runtime type
  - draw submission and a confirmed vertex declaration (including skinning variants)

