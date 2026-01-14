# MODULE_OWNERSHIP_MAP

Evidence-backed ownership map across `sb.exe`, `Core.dll`, `Math.dll`, and `Skin.dll`.

> Status: `sb.exe` and `Core.dll` are evidence-backed in this pass. `Math.dll` and `Skin.dll` sections are **pending** until those modules are active in Ghidra for the same evidence sweep (exports/RTTI/strings/XREFs).

## sb.exe

### Primary responsibilities

- **Game runtime + entity system** (large `Arc*` type surface)
- **Asset cache orchestration and load pipelines** (text + binary caches)
- **Rendering orchestration** (OpenGL function string imports seen; shader proc resolution previously confirmed via `wglGetProcAddress` path in earlier notes)

### Root managers/singletons (evidence-backed examples)

- **Config/init**: `FUN_0088aad0`
  - Initializes cache roots:
    - `cache/Text/` (`0x016e0ef8`)
    - `cache/Binary/` (`0x01716070`)
- **Cache manager globals**: assigned in `FUN_0091d6b0`
  - `DAT_017737d8`, `DAT_017737f4`, `DAT_017737f8` (and others) are set to newly constructed cache manager objects.

### Key RTTI/class names (sample evidence)

- `ArcCacheObj` RTTI: `0x016c4178` (and multiple `ResPoolByID<...>` RTTI entries under `0x01732fd0..0x01733728`)
- `ArcFileCache` RTTI: `0x01704c78`

### Key evidence anchors

- **Cache roots**: `cache/Text/` @ `0x016e0ef8`, `cache/Binary/` @ `0x01716070`
- **ArcFileCache**:
  - Source path: `...\\ObjectServer\\ArcFileCache.cpp` @ `0x01704d58`
  - Logs: `ArcFileCache::LoadFromDisk...` @ `0x01704e60`, `0x01704eb8`
  - Load/index functions (by decomp evidence):
    - `FUN_007da440` (LoadFromDisk-like loop; builds name → open/decode → insert)
    - `FUN_007dd520` (directory enumeration/index building)
    - `FUN_007db270` (uncompress read path)
    - `FUN_007dc900` (compress write path)
    - `FUN_007dad20` (binary-load dispatch loop; logs missing binary loader)

## Core.dll

### Primary responsibilities (confirmed)

- **Core utilities**: strings, tokenization, threading/synchronization, memory management
- **IO abstractions**: file/stream interfaces; endian streams
- **Crypto**: Blowfish + related interfaces
- **WPak container IO**

### Root managers/singletons and entrypoints (examples)

- `core::MemoryManager` constructor exported (`??0MemoryManager@core@@...`) and class present via RTTI (`list_exports`, `list_classes` in Core.dll pass)
- `core::WPakFile::TryOpen` exported (`?TryOpen@WPakFile@core@@...`) and associated error strings

### Evidence anchors

- **Exports** (partial):
  - `core::BlowfishEncryption` (`?Encrypt/?Decrypt/?Reset`)
  - `core::WPakFile::*`, `core::TextWPakFile::*`
- **RTTI/class names** (partial):
  - `core::String`, `StringTokenizer`, `Thread`, `Mutex`, `RWLock`, `MemoryManager`
  - `IOBinStreamInterface`/`IOTextStreamInterface`, `EncryptedStream`
  - `WPakFile`, `TextWPakFile`, `TextWPakFileDecorator`
- **Logging strings**:
  - `core::WPakFile::Open: Error opening wpak file for reading`
  - `...Can't find internal file ...`

## Math.dll (pending)

### Status

- Pending: switch active Ghidra program to `Math.dll` so we can extract:
  - exports (if any), RTTI/class names, math primitives ownership, SIMD/trig tables, matrix/quaternion ops, and any “manager” style entrypoints.

## Skin.dll (pending)

### Status

- Pending: switch active Ghidra program to `Skin.dll` so we can extract:
  - skinning pipeline ownership (bone palette building, CPU/GPU skinning path), vertex stream variants, and the glue between `ArcSkeleton`/`ArcMotion` and render submission.

