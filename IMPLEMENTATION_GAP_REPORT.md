# IMPLEMENTATION_GAP_REPORT

This report compares **confirmed `sb.exe` behavior (via decompilation evidence)** against the current Python viewer implementation in this repo.

## 1) High-signal mismatches (confirmed)

### 1.1 Original client uses text asset formats; viewer consumes JSON dumps

- **`sb.exe` evidence**:
  - `ArcMesh` is parsed from text tokens/sections (`FUN_005a12e0`) and can be saved as text (`FUN_005a2d50`).
  - `ArcMotion` is parsed from text (`FUN_005b9d00`).
  - `ArcSkeleton` is parsed from text (`FUN_005d5d90`).
  - Render graphs include tag blocks like `<BEGINMESHSET>` (`FUN_005d30d0`) and `<BEGINTEXTURESET>` (`FUN_005c6e40`).
- **Repo reality**:
  - The viewer loads `arcane_dump/**/*.json` via `assets/asset_manager.py` + `arcane/*.py` JSON loaders.

**Impact**: We cannot directly “replay” the original client’s file readers on the dumped dataset; we must instead reproduce the **assembly semantics** using the JSON fields available in the dump.

### 1.2 Render objects in `sb.exe` have mesh sets + texture sets + material knobs; viewer only extracts `polymesh_id` + a single texture id

- **`sb.exe` evidence**:
  - Mesh sets are explicit (`<BEGINMESHSET>`, `ArcMeshSet`) and can contain multiple `ArcSinglePolyMesh` entries (`FUN_005d30d0`, `FUN_005b7760`).
  - Texture sets are explicit (`<BEGINTEXTURESET>`, `ArcTextureSet`) and are allocated/stored on the render object (`FUN_005c6e40` stores at `this+0xE8`).
  - Material-ish fields exist, including:
    - `DETAILTEXTURE` (`FUN_005d30d0` stores a cache-id at `+0x10`)
    - `SPECULARMAP` (`FUN_005d30d0`)
    - `SHININESS` float (`FUN_005d30d0` stores at `+0x18`)
    - `CULLFACE`, `LIGHTTWOSIDE`, `CLIPMAP` ints (various offsets in `FUN_005d30d0`)
  - DOUBLESIDED is a per-mesh-entry flag byte at `+0x11` (set in `FUN_005d30d0`, written by `FUN_005b62b0`).
- **Repo reality**:
  - `assets/asset_catalog.py` currently flattens a render into `MeshPart(mesh_id, texture_id, transform)` and picks a single `texture_id` from `render.render_texture_set.texture_data.texture_id` if present, otherwise `None`.

**Impact**: Creatures/items that depend on:
- texture set selection,
- multi-mesh meshsets,
- per-part flags (doublesided/decals), or
- render-state knobs (cullface/lighttwoside),

may render incorrectly or inconsistently even if geometry is present.

### 1.3 Texture-set selection propagation is not implemented

- **`sb.exe` evidence**:
  - Selecting a texture set index updates an internal index and propagates to children (`FUN_005c8170` recurses through child render objects).
- **Repo reality**:
  - No equivalent “texture set selection index” exists in the viewer; parts are rendered with a single chosen texture.

**Impact**: Any asset that relies on texture set variants (e.g., different skins) cannot be represented faithfully yet.

## 2) Concrete fix plan (repo-side) based on confirmed behavior

These steps are intentionally scoped to what we can implement against the JSON dumps without fabricating file readers.

### 2.1 Extend `MeshPart` to carry render flags and (optional) texture-set index

- **Where**: `assets/asset_catalog.py`
- **Add fields** (if available from JSON dump):
  - `is_doublesided: bool`
  - `is_decal: bool`
  - `texture_set_index: Optional[int]`
  - `detail_texture_id/specular_texture_id/shininess` (only if present in dump schema)

**Rationale**: Mirrors `sb.exe` per-entry DOUBLESIDED flag (`FUN_005d30d0` / `FUN_005b62b0`) and renderobject material knobs (`FUN_005d30d0`).

### 2.2 Implement renderobject “texture set selection” as a viewer-side parameter

- **Where**:
  - UI: `ui/asset_catalog.py` (inspector control)
  - Runtime: `ui/opengl_viewport.py` and `assets/asset_catalog.py`
- **Behavior**:
  - User picks an integer `texture_set_index`
  - Catalog assembly selects that texture set when flattening
  - Propagate to child renders (mirroring `FUN_005c8170`)

### 2.3 Render-state support (minimal)

- **Where**: `rendering/mesh_renderer.py` and/or `rendering/shader_manager.py`
- **Implement**:
  - Basic double-sided toggle: disable culling when a part is doublesided/decal.
  - (Optional) cullface control if dump provides equivalent.

## 3) Gaps that still require more decompilation (cannot be solved by repo changes alone yet)

- **ID resolution / cache ID format** (`ArcCacheID`):
  - We need the exact encoding/normalization and path mapping rules to compare against JSON dump conventions.
- **GPU upload / vertex attribute layout in the original client**:
  - We have text mesh parsing but not the render backend’s VAO/VBO layout code path yet.
- **“Assembled model” canonical runtime type**:
  - Need the exact class that renderer consumes after resolving meshsets/texturesets/hardpoints.

