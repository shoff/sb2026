# Project Information

Canonical index for the Shadowbane Asset Viewer project structure, components, patterns, and architecture.

## Inconsistencies

- ⚠️ **Monolithic `.cache` header size**: `sb.exe` writer path (`FUN_007dcba0`) writes a **0x10-byte** header (4×u32) + directory records, while some disk-backed notes in the repo describe a **0x28-byte** header. This must be reconciled against a real `Mesh.cache`/`Textures.cache` file from disk.

## Architecture Overview

The Shadowbane Asset Viewer is a desktop application built with PyQt6 and PyOpenGL for viewing, animating, and exporting game assets from Shadowbane (2002 MMORPG). The application follows a modular architecture with clear separation of concerns:

- **UI Layer**: PyQt6 widgets for user interface
- **Rendering Layer**: OpenGL 3.3 Core Profile for 3D graphics
- **Animation Layer**: Skeletal animation system with GPU skinning
- **Asset Layer**: Asset loading and management from arcane_dump folders
- **Export Layer**: OBJ and GLTF format exporters

## Asset Management

### Asset Types

The application supports the following asset types loaded from `arcane_dump/` folders:

- **Meshes** (24,387): 3D geometry with vertices, normals, UVs, bone indices/weights
- **Textures** (9,681): JPG images requiring mirror and 180° rotation transformation
- **Skeletons** (104): Bone hierarchies with bind poses (up to 43 bones)
- **Motions** (1,504): Animation frame data with position, rotation (quaternion), scale per bone
- **Renders** (32,713): Render configuration data
- **CObjects** (10,332): Composite object definitions (assembled in-game assets), stored under `arcane_dump/COBJECTS/<CATEGORY>/`.

### Asset Loading

- Assets are loaded on-demand via `AssetManager` class
- `AssetManager` builds a disk index at startup to resolve `asset_id -> file path` (handles nested `COBJECTS/` categories)
- Assets are cached in memory after first load
- Texture images are loaded from `TEXTURE/` and may be `.tga` (current dump format) or `.jpg`
- Dependencies: `arcane/` package for binary format parsers (ArcMesh, ArcSkeleton, ArcMotion, etc.)

### Asset Manager Location

`assets/asset_manager.py` - Central registry for loading and caching all asset types.

### Assembled Asset Catalog

- The UI browses assembled assets (COBJECTS → RENDER → MESH/TEXTURE) via `assets/asset_catalog.py`
- The catalog classifies assets primarily from `arcane_dump/COBJECTS/<CATEGORY>/` (e.g., `ITEM`, `STRUCTURE`, `RUNE`)

### Original Client Asset System (sb.exe) — Confirmed Reverse-Engineering Notes

- **Cache roots**: the original client uses both `cache/Text/` and `cache/Binary/`.
  - **Evidence**: `FUN_0088aad0` sets config fields from string constants `s_cache_Text__016e0ef8` and `s_cache_Binary__01716070`.
- **Central miss-load engine**: `ArcFileCache` is the core “miss-load” mechanism for many assets.
  - **Evidence**:
    - RTTI `.?AVArcFileCache@@` (`0x01704c78`) and source path `...\\ObjectServer\\ArcFileCache.cpp` (`0x01704d58`)
    - Miss-load loop `FUN_007da440` (build path from `ArcCacheID` → call `open_decode_fn` → set id → insert)
- **`ArcFileCache` loader indirections (resolved)**:
  - **BuildPathFromID**: vtable slot `+8` resolves to `FUN_007da120`.
    - **Evidence**: ctor `FUN_007d8c50` sets vtable `0x0155a97c`; XREF from `0x0155a984` (`vtable+8`) to `FUN_007da120`.
  - **open_decode_fn / binary_load_fn**:
    - `binary_load_fn` stored at `this+0x50` by `FUN_007d8c50` ctor arg
    - `open_decode_fn` stored at `this+0x84` by `FUN_007da010(cache, fn)`
    - Both wired per cache subtype in `FUN_0091d6b0` (see `ASSET_LOADER_DISPATCH_SPEC.md`).
- **Monolithic `*.cache` container (selection, write, lookup) — proven**:
  - **Container selection**: `FUN_007dba30` appends `PTR_s_Textures_0170508c[this->subtype]` + `".cache"` (`0x01704f08`) to build the monolithic container filename.
  - **Header+directory writer**: `FUN_007dcba0` writes a 0x10-byte header (4×u32) and then 0x14-byte directory records containing `(ArcCacheID low32/high32, stream_off, uncompressed_size, compressed_size)`.
  - **Directory lookup**: `FUN_007db8f0` performs **binary search** over directory entries (`[this+0x54, this+0x58)`, stride `0x18`) comparing by full `ArcCacheID` (two dwords).
  - **Entry point**: `FUN_007d8fb0` opens the `*.cache` file, reads/updates directory state, and invokes the writer/lookup helpers.
- **Text formats (parsers/writers exist in `sb.exe`)**:
  - **Meshes**: `ArcMesh` is parsed from tokenized text with `_VERTICES_` and `_INDICES_`.
    - **Evidence**: `FUN_005a12e0` (parser) and `FUN_005a2d50` (writer), `ArcMesh.cpp` string `016d63fc`.
  - **Motions**: `ArcMotion` is parsed from tokenized text and logs `Reading ArcMotion from text %s`.
    - **Evidence**: `FUN_005b9d00`, `ArcMotion.cpp` string `016d6cc8`.
  - **Skeletons**: `ArcSkeleton` is parsed from tokenized text and references motion IDs; validates motion existence.
    - **Evidence**: `FUN_005d5d90` (parser) and `FUN_005d8152` (ValidateMotions), `ArcSkeleton.cpp` string `016d7bb8`.
  - **Mesh/texture sets**: tag blocks such as `<BEGINMESHSET>` and `<BEGINTEXTURESET>` exist.
    - **Evidence**: `FUN_005d30d0` handles `<BEGINMESHSET>`; `FUN_005c6e40` handles `<BEGINTEXTURESET>`.
- **Render binding**:
  - `ArcObj` binds renderobjects via cache-id tokens `RENDEROBJECT` and `RENDEROBJECTLOWDETAIL`.
    - **Evidence**: `FUN_004d16a0` stores cache-id into `this+0xB8` and `this+200`.
  - Texture-set selection propagates recursively to child render objects.
    - **Evidence**: `FUN_005c8170` recurses child pointers and applies a texture-set index.
  - **Texture GPU upload**: `ArcImage::TextureGLInit` is implemented in `FUN_00590a90` and performs `glTexImage*` upload + `glTexParameteri`/`glPrioritizeTextures`.
    - **Evidence**: `FUN_00590a90` contains `ArcImage::TextureGLInit - texture upload` string `0x016d5474`.
  - **Mesh CPU vertex element sizes (confirmed)**:
    - position: float3 (12 bytes) via `FUN_005a43a0`
    - normal: float3 (12 bytes) via `FUN_005a4460`
    - uv: float2 (8 bytes) via `FUN_005a4530`
- **Immediate render payload layout (confirmed)**:
  - `RenderPayload+0x64` → positions pointer (float3 array) used by `glVertex3f` in `FUN_005aadc0`.
  - `RenderPayload+0x70` → UV pointer (float2 array) used by `glTexCoord2f` in `FUN_005aadc0`.
  - `RenderPayload+0x7C` → normals pointer (float3 array) used by `glNormal3f` in `FUN_005aadc0`.

### Original Client Modules — Ownership (confirmed)

- **Core.dll**
  - **Primary responsibilities**: core utilities (threading/synchronization, memory mgmt, file/stream IO abstractions, encryption, wpak container IO)
  - **Evidence**:
    - **Exports**: `core::BlowfishEncryption` (`?Encrypt/?Decrypt/?Reset`), `core::WPakFile::*`, `core::TextWPakFile::*` (via `list_exports`)
    - **RTTI/class names**: `core::String`, `StringTokenizer`, `Thread`, `Mutex`, `RWLock`, `MemoryManager`, `IOBinStreamInterface`/`IOTextStreamInterface`, `EncryptedStream`, `WPakFile` (via `list_classes`)
    - **Logging strings**: `core::WPakFile::Open: Error opening wpak file for reading`, `...Can't find internal file ...` (via `list_strings` filter `Pak`)

## Authentication and Authorization

Not applicable - this is a desktop application with no authentication requirements.

## Code Organization

### Directory Structure

```
sb2026/
├── main.py                    # Application entry point
├── requirements.txt           # Python dependencies
├── ui/                        # User interface components
│   ├── main_window.py         # Main application window
│   ├── asset_browser.py       # Asset tree view widget
│   ├── opengl_viewport.py     # 3D rendering viewport
│   ├── animation_timeline.py   # Animation controls widget
│   └── export_dialog.py       # Export options dialog
├── rendering/                 # OpenGL rendering system
│   ├── camera.py              # Orbit camera controller
│   ├── shader_manager.py      # GLSL shader compilation
│   ├── mesh_renderer.py       # Mesh → GPU buffer conversion
│   ├── texture_manager.py     # Texture loading and OpenGL binding
│   └── shaders/               # GLSL shader source files
│       ├── basic.vert/frag    # Static mesh shaders
│       └── skinned.vert/frag  # Animated mesh shaders
├── animation/                 # Skeletal animation system
│   ├── interpolation.py       # Lerp, slerp, quaternion math
│   ├── skeletal_animator.py   # Bone transform calculations
│   └── animation_controller.py # Playback state machine
├── export/                    # Asset export functionality
│   ├── obj_exporter.py        # OBJ/MTL format export
│   └── gltf_exporter.py       # GLTF 2.0 format export
├── assets/                    # Asset loading and management
│   └── asset_manager.py       # Central asset loader
└── utils/                     # Utility functions
    └── math_utils.py          # Math helper functions
```

### Module Responsibilities

- **main.py**: Application initialization, signal connections, event loop
- **ui/**: All PyQt6 widgets and window management
- **rendering/**: OpenGL rendering pipeline, shaders, camera
- **animation/**: Skeletal animation math and playback control
- **export/**: File format exporters (OBJ, GLTF)
- **assets/**: Asset loading from disk and caching
- **utils/**: Shared utility functions

## Configuration

### Environment Setup

- **Python Version**: 3.8 or higher (tested with 3.12)
- **PYTHONPATH**: Must include parent directory for `arcane/` package imports
- **Asset Path**: `arcane_dump/` folder in parent directory (relative to `main.py`)

### Dependencies

- **PyQt6** (>=6.6.0): GUI framework
- **PyOpenGL** (>=3.1.7): OpenGL bindings
- **PyOpenGL-accelerate** (>=3.1.7): OpenGL acceleration
- **NumPy** (>=1.26.0): Matrix math operations
- **Pillow** (>=10.1.0): Image loading and processing
- **pygltflib** (>=1.16.0): GLTF export support
- **trimesh** (>=4.0.5): 3D mesh utilities

### External Dependencies

- **arcane/**: Custom package for Shadowbane binary format parsing (located in parent directory)

## Data Models

### Asset Data Structures

Assets are represented as classes from the `arcane/` package:

- **ArcMesh**: Vertex data, normals, UVs, bone indices/weights, triangle indices
- **ArcSkeleton**: Bone hierarchy, bind pose matrices, bone names
- **ArcMotion**: Frame data with per-bone transforms (position, quaternion rotation, scale)
- **ArcTexture**: Image data (JPG format)
- **ArcRender**: Render configuration
- **ArcCObject**: Composite object definitions

### Rendering Data Structures

- **Mesh buffers**: VBO/VAO for vertex data, EBO for indices
- **Texture objects**: OpenGL texture IDs
- **Bone matrices**: 4x4 transformation matrices (up to 128 bones)
- **Animation state**: Current frame, playback speed, loop flag

## External Service Integrations

Not applicable - this is a standalone desktop application with no external service dependencies.

## File Naming Conventions

- **Python files**: Lowercase with underscores (e.g., `asset_manager.py`, `main_window.py`)
- **Shader files**: Lowercase with dots (e.g., `basic.vert`, `skinned.frag`)
- **Documentation**: Uppercase with underscores (e.g., `PROJECT_SUMMARY.md`, `PHASE1_COMPLETE.md`)

## Key Architectural Patterns

### Component Communication

- **Signals and Slots**: PyQt6 signal/slot mechanism for decoupled component communication
- **Asset Selection Flow**: Asset Browser → Main Window → Viewport/Animation Controller
- **Animation Flow**: Timeline → Animation Controller → Skeletal Animator → Viewport

### Rendering Pipeline

1. Asset loaded via `AssetManager`
2. Mesh data converted to GPU buffers via `MeshRenderer`
3. Texture loaded and bound via `TextureManager`
4. Shader compiled and bound via `ShaderManager`
5. Camera transforms calculated via `Camera`
6. Bone matrices calculated via `SkeletalAnimator` (if animated)
7. OpenGL draw call executed in `OpenGLViewport`

### Animation Pipeline

1. Motion data loaded from `AssetManager`
2. Frame interpolation via `Interpolation` utilities
3. Bone transforms calculated via `SkeletalAnimator`
4. Skinning matrices uploaded to GPU
5. Vertex shader performs GPU skinning
6. Deformed mesh rendered

## Known Limitations

1. **GLTF Animation Export**: Full skeletal animation export to GLTF not yet implemented (static pose only)
2. **Texture Embedding**: Textures are referenced by path in exports, not embedded
3. **Batch Export**: Can only export one asset at a time
4. **Skeleton Attachments**: CObject/Render attachment rules and hierarchy-driven transforms are not yet fully reconstructed from the original client
5. **Max Bones**: Shader limited to 128 bones (sufficient for all Shadowbane skeletons)
6. **OpenGL Version**: Requires OpenGL 3.3 Core Profile support

## Naming Conventions

- **Classes**: PascalCase (e.g., `AssetManager`, `MainWindow`)
- **Functions/Methods**: snake_case (e.g., `load_mesh`, `set_frame`)
- **Variables**: snake_case (e.g., `asset_id`, `current_mesh_id`)
- **Constants**: UPPER_SNAKE_CASE (e.g., `MAX_BONES`)
- **Private methods**: Leading underscore (e.g., `_connect_signals`, `_on_asset_selected`)

## Project Status

### Phase Completion

- **Phase 1**: ✅ Complete - Asset browser, UI framework, asset loading
- **Phase 2**: ✅ Complete - 3D rendering, camera controls, texture display
- **Phase 3**: ✅ Complete - Skeletal animation, timeline, playback
- **Phase 4**: ✅ Complete - OBJ/GLTF export

### Current State

All major features are implemented and tested. The application is production-ready for viewing and exporting Shadowbane assets.

## Rendering System

### OpenGL Configuration

- **Version**: OpenGL 3.3 Core Profile
- **Anti-aliasing**: 4x MSAA
- **Shaders**: GLSL vertex and fragment shaders
- **Lighting**: Blinn-Phong (ambient + diffuse + specular)

### Shader Programs

- **Basic Shader**: Static mesh rendering with texture mapping
- **Skinned Shader**: Animated mesh rendering with GPU vertex skinning (up to 4 bones per vertex)

### Camera System

- **Type**: Orbit camera
- **Controls**: 
  - Left-click drag: Rotate
  - Middle-click drag: Pan
  - Scroll wheel: Zoom
  - R key: Reset to default view
- **Auto-framing**: Automatically frames mesh on load

## Testing

### Test Files

- `test_animation.py`: Animation system verification
- `test_export.py`: Export functionality verification

### Test Coverage

- Animation playback and interpolation
- Export format validation
- Blender import compatibility

## Usage Patterns

### Typical Workflow

1. Launch application via `main.py`
2. Browse assets in Asset Browser (left panel)
3. Select mesh to load into viewport
4. Optionally select skeleton and motion for animation
5. Use timeline controls to play/pause/scrub animation
6. Export asset via File → Export Asset (Ctrl+E)

### Keyboard Shortcuts

- `Ctrl+O`: Open cache file (placeholder)
- `Ctrl+E`: Export asset
- `Ctrl+Q`: Quit application
- `R`: Reset camera
- `Spacebar`: Play/pause animation (when timeline is active)

## Version Control

### Git Structure

- Project root: `sb2026/`
- Python package structure with `__init__.py` files
- Documentation in root directory
- Dependencies in `requirements.txt`
