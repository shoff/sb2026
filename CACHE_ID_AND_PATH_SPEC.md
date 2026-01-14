# CACHE_ID_AND_PATH_SPEC

This document is **evidence-backed**. Every claim is anchored to an `sb.exe` function, RTTI/type name, string constant, or XREF chain.

## 1) `ArcCacheID` runtime representation (confirmed)

### 1.1 Memory layout

- **Size**: 8 bytes (two 32-bit words)
- **Store (low/high)**: `FUN_00511910(void *this, u32 low, u32 high)` writes:
  - `*(u32*)this = low`
  - `*(u32*)(this+4) = high`
- **Copy**: `FUN_00511ba0(void *this, u32* src)` copies the same two dwords.
- **Zero init**: `FUN_00511790(u32* out)` sets both dwords to 0.

**Evidence**: `FUN_00511790`, `FUN_00511910`, `FUN_00511ba0` decompilation.

### 1.2 Canonical filename encoding: 20-digit decimal (confirmed)

- **20-digit decimal parse**: `FUN_00511d00(void *out_u64, int ascii_ptr)` parses **exactly 0x14 (20) characters**, assumes digits, and accumulates as base-10 into a `uint64`.
  - This matches a fixed-width decimal ID string used as a filename prefix.

**Evidence**: `FUN_00511d00` loop bound `while (iVar2 < 0x14)` and decimal accumulation.

### 1.3 Formatting hint: `"%0.20I64u"` (confirmed as a constant)

- `FUN_00511ec0(String *dst)` formats the **ArcCacheID value** (two dwords at `this+0/this+4`) using the constant format string `"%0.20I64u"` at `0x016cda90`.
- `FUN_00511cd0(String *dst)` is a thunk that delegates to `FUN_00511ec0`.

**Evidence**: `FUN_00511ec0` disassembly shows:
- `MOV EAX,[ECX+4]` and `MOV ECX,[ECX]` then pushes both as varargs before the formatting call, alongside `0x016cda90`.

## 2) Parsing `ArcCacheID` from strings (confirmed)

### 2.1 General-purpose parse: decimal or `X`-prefixed hex

`FUN_00549120(String *src, void *out_u64)`:

- If `src` is empty → returns 0.
- If first char is **not** `'X'` (`0x58`):
  - Consumes the **leading run** of decimal digits (`core::SSIsdigit`)
  - Interprets them as base-10 into `uint64`
- If first char **is** `'X'`:
  - Consumes the **leading run** of hex digits after `'X'` (`core::SSIsXDigit`)
  - Interprets them as base-16 into `uint64`
- Writes the result via `FUN_00511910(out, low32, high32)`.

**Evidence**: `FUN_00549120` decompilation (digit vs xdigit branches).

### 2.2 Normalization for dashed hex strings: `"X...-..."` (confirmed)

`FUN_00548e60(String *src, void *out_u64)`:

- If `src` does **not** start with `'X'`, it forwards to `FUN_00549120(src,out)`.
- If `src` starts with `'X'`, it searches backward for `'-'` (`0x2d`).
  - If no dash found: uses `src` as-is.
  - If dash found:
    - Builds a new string:
      - prefix = `src[0:dash_index]`
      - suffix = `src[dash_index+1:end]`
      - inserts a run of `"0"` characters between prefix and suffix (padding count computed as `(dash_index - len(src)) + 0x0e`)
    - Passes the normalized string to `FUN_00549120(normalized,out)`

**Evidence**: `FUN_00548e60` decompilation (dash search, prefix/suffix substrings, pad loop, final call to `FUN_00549120`).

## 3) Cache root strings and where they come from (confirmed)

- `cache/Text/` string constant at `0x016e0ef8`
- `cache/Binary/` string constant at `0x01716070`
- `FUN_0088aad0` (config init) assigns these into a config object:
  - `thunk_FUN_00546850(param_1 + 0x6f, s_cache_Text__016e0ef8)`
  - `thunk_FUN_00546850(param_1 + 0x75, s_cache_Binary__01716070)`

**Evidence**: `FUN_0088aad0` decompilation; XREFs to `0x016e0ef8` and `0x01716070`.

## 4) Evidence-backed cache resolution rules (partial; still expanding)

### 4.1 Texture cache directory construction (confirmed structure, unresolved semantics of each segment)

`FUN_007da120(this, out_path_string, ?, mode)` appends a base root then multiple path components:

- If `mode == 1`: appends `(String*)&DAT_01aa308c`
- Else if `mode == 2`: conditionally appends `(String*)&DAT_01aa73d8` (guarded by `DAT_01aa73f0`)
- Else: appends `(String*)&DAT_01aa30a4` and conditionally appends one of two constant strings based on `this+0x6c`.
- Then appends:
  - a folder name from a table: `(&PTR_s_Textures_0170508c)[*(int*)(this+0x6c)]`
    - **String evidence**: `"Textures"` at `0x017051b0` (the table XREFs this string)
  - `'/'`
  - a **per-index bucket character** from a byte table at `0x01705088`, indexed by `this+0x6c`
    - **Evidence**: `FUN_007da120` disassembly does `MOV EDX,[0x01705088]; MOV AL, byte ptr [ECX + EDX]`
  - `CALL 0x00404aed` with `ECX = ArcCacheID*` and `out String*`
    - `0x00404aed` thunks to `FUN_00511cd0` → `FUN_00511ec0`, which formats the **actual ID value** to the 20-digit decimal string via `"%0.20I64u"` (see §1.3).
  - another suffix from table: `(&PTR_DAT_017050c8)[*(int*)(this+0x6c)]`

**Evidence**: `FUN_007da120` decompilation; `list_strings` shows `Textures` and `tmcoorpksezzvad`.

> What’s still missing: proving which `mode` corresponds to **Text vs Binary** root (the roots in `FUN_007da120` are config strings, not the literal `cache/Text/` constant), and mapping each `type_index` to a concrete asset category beyond the confirmed `ArcImage`/`ArcMesh` cases.

### 4.2 Cache directory indexing: enumerate files and parse ID from filename prefix (confirmed)

`FUN_007dd520(param_1)`:

- Builds a directory/pattern string starting from `(String*)&DAT_01aa308c` and appending additional segments (including the `Textures`/`tmcoorpksezzvad` tables).
- Enumerates files using:
  - `FUN_0051a960(find_ctx, pattern_ascii, out_name_string)` → `findfirst`
  - `FUN_0051a9f0(find_ctx, out_name_string)` → `findnext`
- For each returned filename, converts it to ASCII (`FUN_005454c0`) and parses a `uint64` from the first 20 characters via:
  - `FUN_00511d00(out_cache_id_u64, (int)(ascii_string + 1))`

**Evidence**: `FUN_007dd520`, `FUN_0051a960`, `FUN_0051a9f0`, `FUN_00511d00` decompilation.

## 5) Cache table lookup & insertion (confirmed, but object types still unnamed)

### 5.1 Lookup by `ArcCacheID` (confirmed)

`FUN_005b72d0(this, out_ptr, cache_id_u64_ptr)` calls `FUN_00440db0(this, &tmp, cache_id_u64_ptr)`:

- If a node is found, it updates internal linked-list pointers at offsets `+0x24/+0x28` (LRU-like behavior) and returns a referenced pointer via `out_ptr`.

**Evidence**: `FUN_005b72d0` and `FUN_00440db0` decompilation (hash-probe + LRU relink).

### 5.2 Insert/update by key (confirmed)

On a miss with a valid loader (`this+0x1c`), `FUN_00440db0` calls `FUN_00441c70(this, out_ptr, node_ptr)` which:

- Probes/allocates a slot in the underlying hash table (`FUN_004416c0` / `FUN_00441650`)
- Inserts `node_ptr` into the table and LRU list

**Evidence**: `FUN_00440db0` calls `FUN_00441c70`; `FUN_00441c70` decompilation.

## 6) Implementation-grade pseudocode (only what is fully proven so far)

### 6.1 ParseArcCacheIDString(s) → u64

```text
// Evidence: FUN_00548e60 + FUN_00549120 + FUN_00511910
ParseArcCacheIDString(s):
  if s starts with 'X' and contains '-':
    (prefix, suffix) = split on last '-'
    zeros_to_insert = (dash_index - len(s)) + 0x0e
    s_norm = prefix + ("0" * zeros_to_insert) + suffix
    return ParseHexAfterX(s_norm)   // base16 over xdigits
  else if s starts with 'X':
    return ParseHexAfterX(s)        // base16 over xdigits
  else:
    return ParseLeadingDecimalDigits(s) // base10 over leading digit run
```

### 6.2 ParseCacheIdFromFilenamePrefix20(ascii_ptr) → u64

```text
// Evidence: FUN_00511d00 (20-digit decimal)
ParseCacheIdFromFilenamePrefix20(p):
  id = 0
  for i in 0..19:
    id = id*10 + (p[i] - '0')
  return id
```

## 7) Outstanding unknowns (actively being pursued)

- The **exact** `ResolveCacheIdToPath(id, type)` logic for *general assets* (mesh/skeleton/motion/render/etc.), including:
  - Text vs Binary preference / fallback order
  - Extension probing rules
  - Namespace / folder routing rules per asset type
- The concrete “open asset stream” functions that bridge `ArcCacheID` → filesystem open (we have table lookup & directory enumeration, but still need the per-type disk open path).

