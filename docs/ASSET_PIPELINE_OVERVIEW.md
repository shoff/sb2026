# ASSET_PIPELINE_OVERVIEW

This document is **evidence-only**: every statement is backed by a concrete string / function from `sb.exe` decompilation via Ghidra MCP.

## Scope (confirmed so far)

- **Cache roots**: the client has distinct `cache/Text/` and `cache/Binary/` roots (how they are rooted on disk is config-driven).
- **Text-driven asset formats** (confirmed by parsers and/or writers in `sb.exe`):
  - Meshes (`ArcMesh`)
  - Motions/animations (`ArcMotion`)
  - Skeletons (`ArcSkeleton`)
  - Render objects / render templates (keyword- and tag-driven)
  - Mesh sets (`ArcMeshSet`) and single poly meshes (`ArcSinglePolyMesh`)
  - Texture sets (`ArcTextureSet`) and textures (`ArcTexture` / animated texture blocks)

## Canonical cache roots / subtrees (confirmed)

### Root strings

- `cache/Text/`
  - **Evidence**: `s_cache_Text__016e0ef8` referenced by `FUN_0088aad0` (initializes config; sets string into a config field).
- `cache/Binary/`
  - **Evidence**: `s_cache_Binary__01716070` referenced by `FUN_0088aad0` (initializes config; sets string into a config field).

### Known subpaths / templates

- `cache/Text/TerrainAlpha/a%s`
  - **Evidence**: string `s_cache_Text_TerrainAlpha_a_s_016e1bfc` referenced by `FUN_00651b90`.
- `Cache/Text/Visual/` and `v%s.vfx`
  - **Evidence**:
    - string `s_Cache_Text_Visual__01752120` referenced by `FUN_00b51700`
    - string `s_Object_added_to_cache_text_visua_017520e8` includes `... as v%s.vfx` and is logged by `FUN_00b51700`
- `cache/Text/Dungeon/`
  - **Evidence**: string `s_cache_Text_Dungeon__01752370` (seen in strings list; XREFs not yet traced in this pass).

## Asset type inventory table (partial; evidence-backed)

| Category | Storage form | Recognizable tokens / tags | Entrypoint / parser functions (evidence) | Produced runtime object (evidence) | Dependencies / linkage (evidence) |
|---|---|---|---|---|---|
| Mesh | Text (line-based keywords + sections) | `USEFACENORMALS`, `STRIPIFY`, `USETANGENTBASIS`, `USEMIRROREDNORMALMAP`, `_VERTICES_`, `_INDICES_` | `FUN_005a12e0` parses; `FUN_005a2d50` writes/saves | `ArcMesh` (`C:\\...\\ArcMesh.cpp` string @ `016d63fc`) | May generate edge/shared-edge data (`FUN_005a7bd0`); computes normals (`FUN_005a49b0`) |
| Mesh set | Text tag blocks | `<BEGINMESHSET> ... <ENDMESHSET>` | `FUN_005b7970` writes wrapper; `FUN_005b7760` parses `<BEGINSINGLEPOLYMESH>` inside mesh sets | `ArcMeshSet` RTTI string `.?AVArcMeshSet@@` @ `016d6b00` | Contains `ArcSinglePolyMesh` entries (`FUN_005b7760`) |
| Single poly mesh | Text tag blocks | `<BEGINSINGLEPOLYMESH>` / `<ENDSINGLEPOLYMESH>`, `ID: %s`, `ID: DECAL`, `DOUBLESIDED: TRUE` | `FUN_005b62b0` writes; refresh/resolve by ID in `FUN_005b6450` (logs `ArcSinglePolyMesh::CacheRefresh`) | `ArcSinglePolyMesh` RTTI @ `016d6940` | Linked/selected via render-object parsing (see Render object section) |
| Skeleton | Text (sectioned, token-driven) | `_VERSION`, `_NAME`, `_MOTION`, `_UNITS`, `_ROOT`, `_BONEDATA`, `_HIERARCHY`, etc. | `FUN_005d5d90` parses; `FUN_005d8152` validates motions | `ArcSkeleton` (`C:\\...\\ArcSkeleton.cpp` string @ `016d7bb8`) | References motions by ID (on `_MOTION`, parses an index + ID string into a cache-id structure) |
| Motion / animation | Text (token-driven) | `_FULLY_SPECIFIED`, `_DEGREES`, `_RADIANS`, `_TARGETFRAME`, `_SOUND`, `_SHEATH`, `_RESETLOC`, `_LEAVEGROUND`, `_SMOOTHED`, etc. | `FUN_005b9d00` parses and logs `Reading ArcMotion from text %s` | `ArcMotion` (`C:\\...\\ArcMotion.cpp` string @ `016d6cc8`) | May perform smoothing post-pass (`FUN_005bb740` logs smoothing) |
| Texture | Text (animated texture blocks) + image lookup | `<BEGINANIMATEDTEXTURE>` / `<ENDANIMATEDTEXTURE>`, `FRAMETIMER`, `FRAMERAND` | `FUN_005e0170` writes/saves texture; `FUN_005dd4d0` resolves referenced image/template and logs on failure | `ArcTexture` (`C:\\...\\ArcTexture.cpp` string @ `016d7e94`) | Uses an “image template” / ID lookup (`FUN_005dd4d0` calls `thunk_FUN_005e2630(...)` and logs `Failed_to_find_image___TemplateI...`) |
| Texture set | Text tag blocks | `<BEGINTEXTURESET>` / `<ENDTEXTURESET>` | `FUN_005c6e40` recognizes `<BEGINTEXTURESET>` and allocates a 0x34-byte object (constructed via `thunk_FUN_005e33c0`) | `ArcTextureSet` RTTI @ `016d8438` | Owned by the enclosing render object (stored at `this+0xe8` in `FUN_005c6e40`) |
| Render template / object keywords | Text (keyword-based) | `FORWARDVECTOR`, `TRACKINGNAME`, `MAXTRACKINGDISTANCE`, `RENDEROBJECT`, `RENDEROBJECTLOWDETAIL`, `BEGINHARDPOINTS` | `FUN_004d16a0` handles `ArcRenderTemplate::ParseKeyword` error path and multiple `ArcObj` tokens including `RENDEROBJECT*` | `ArcRenderTemplate` RTTI @ `016d7900`; `ArcRenderObject` RTTI @ `016cde28` | `ArcObj` stores renderobject references as cache-IDs (parsed via `thunk_FUN_00548e60` + `thunk_FUN_00511ba0`) |
| Render object parse & material-ish knobs | Text (keyword-based) | `<BEGINMESHSET>`, `DETAILTEXTURE`, `SPECULARMAP`, `SHININESS`, `CULLFACE`, `LIGHTTWOSIDE`, etc. | `FUN_005d30d0` handles `<BEGINMESHSET>` and multiple render/material tokens; `FUN_005c6e40` handles `<BEGINTEXTURESET>`, `TARGETBONE`, `SCALE`, `ORIENT`, etc. | Likely `ArcRenderObject` (source path `ArcRenderObject.cpp` @ `016d7028`) | Connects meshset and per-mesh flags (e.g., DOUBLESIDED sets a flag on a mesh entry) |

## Dispatch / “manager” architecture (confirmed fragments)

- **Config initialization** sets cache roots + other defaults.
  - **Evidence**: `FUN_0088aad0` sets `cache/Text/` and `cache/Binary/`.
- **Shader function dispatch** is resolved at runtime via `wglGetProcAddress`.
  - **Evidence**: `FUN_00965ec0`.

## Open questions (not yet resolved from decompilation)

- Exact on-disk layout beneath `cache/Binary/` for meshes/textures/materials (we have the root string but have not yet traced binary readers).
- How `ArcCacheID` strings are encoded (format, namespace, case rules) and how they map to concrete files.
- The full “assembled model” runtime object type: which class represents the resolved render graph that the renderer consumes.
- GPU upload points in the original client (we’ve only confirmed shader proc resolution so far).

## Evidence index (functions referenced here)

- `FUN_0088aad0`: initializes config strings including `cache/Text/` and `cache/Binary/`
- `FUN_00965ec0`: loads ARB shader function pointers via `wglGetProcAddress`
- `FUN_005a12e0`: parses `ArcMesh` text format (keywords + `_VERTICES_`/`_INDICES_`)
- `FUN_005a2d50`: writes/saves mesh file (prints vertices/indices)
- `FUN_005b7760`: parses meshset; recognizes `<BEGINSINGLEPOLYMESH>`
- `FUN_005b62b0`: writes single polymesh tag block
- `FUN_005b6450`: `ArcSinglePolyMesh::CacheRefresh` (ID resolution / cache lookup failure path)
- `FUN_005b9d00`: parses `ArcMotion` text format (token list) and logs
- `FUN_005d5d90`: parses `ArcSkeleton` text format (token list) and parses motion references
- `FUN_005d8152`: validates skeleton motions; logs missing motion IDs
- `FUN_005e0170`: writes/saves texture (animated texture wrapper)
- `FUN_005dd4d0`: resolves texture image/template; logs failure if missing
- `FUN_004d16a0`: parse keyword handler including `ArcRenderTemplate` FORWARDVECTOR and `ArcObj` renderobject tokens
- `FUN_005c6e40`: parses render object properties including `<BEGINTEXTURESET>`, `TARGETBONE`, `SCALE`, `ORIENT`, VP params
- `FUN_005d30d0`: parses render object properties including `<BEGINMESHSET>`, texture/material knobs, and DOUBLESIDED behavior

