# Shadowbane Asset Viewer - Quick Start Guide

## Installation (One-Time Setup)

Already done! Dependencies are installed in `viewer_env/`.

## Running the Viewer

**Option 1: Using the launch script** (easiest)
```bash
cd /Users/stevenhoff/dev/shadowbane
./run_viewer.sh
```

**Option 2: Manual**
```bash
cd /Users/stevenhoff/dev/shadowbane
source viewer_env/bin/activate
export PYTHONPATH="$(pwd):$PYTHONPATH"
python shadowbane_viewer/main.py
```

## How to View 3D Assets

### 1. View a Mesh

1. In the **Asset Browser** (left panel), expand the "Meshes" category
2. Click on any mesh ID (e.g., `100`, `101`, `1000`)
3. The mesh will appear in the 3D viewport with a texture applied

### 2. Camera Controls

- **Rotate**: Left-click and drag
- **Pan**: Middle-click and drag (or Shift + Left-click)
- **Zoom**: Mouse wheel up/down
- **Reset Camera**: Press `R` key

### 3. Change Textures

1. With a mesh loaded, expand the "Textures" category
2. Click on any texture ID
3. The texture will be applied to the current mesh

### 4. Search Assets

- Use the search box at the top of the Asset Browser
- Type an asset ID to filter (e.g., type "100" to find all IDs containing 100)

## Recommended Assets to Try

### Good Starting Meshes
- **100-110**: Simple props (pillars, rocks)
- **1000-1100**: Character body parts
- **10000-10010**: Complex objects

### Interesting Textures
- **1-100**: Various game textures
- **1000-2000**: Character textures
- **10000+**: Environment textures

## Keyboard Shortcuts

- `R` - Reset camera (re-frames current mesh)
- `Ctrl+O` - Open cache file (coming soon)
- `Ctrl+Q` - Quit application

## Menu Options

### File Menu
- **Open Cache File**: Load from .cache files (coming soon)
- **Export Asset**: Export to OBJ/GLTF (Phase 4)
- **Exit**: Close application

### View Menu
- **Asset Browser**: Toggle left panel
- **Timeline**: Toggle bottom panel (Phase 3)

## What You're Seeing

- **Left Panel**: Asset Browser with 50,000+ game assets
- **Center**: 3D viewport with OpenGL rendering
- **Bottom**: Animation timeline (placeholder - coming in Phase 3)
- **Status Bar**: FPS counter and status messages

## Performance

- Target: 60 FPS for most meshes
- FPS shown in status bar (bottom)
- If FPS drops below 30, try a smaller mesh

## Troubleshooting

### "No module named 'arcane'"
```bash
export PYTHONPATH="/Users/stevenhoff/dev/shadowbane:$PYTHONPATH"
```

### OpenGL errors
Make sure you're running on macOS 10.13+ with OpenGL 3.3 support.

### Mesh appears black
Try selecting a different texture from the Textures category.

### Window is blank
The shader might have failed to compile. Check the console output for errors.

## Tips

1. **Start small**: Try mesh 100-200 first before complex meshes
2. **Experiment**: Try different texture combinations
3. **Use search**: Filter assets by ID for quick access
4. **Reset often**: Press 'R' to re-frame meshes if you lose sight of them
5. **FPS check**: Watch the status bar to see rendering performance

## What's Next

- **Phase 3**: Skeletal animation playback (coming next!)
- **Phase 4**: Export to OBJ, GLTF, FBX formats
- **Phase 5**: Polish, optimization, and additional features

## Need Help?

Check the full documentation:
- `README.md` - Complete feature list
- `PHASE1_COMPLETE.md` - Asset browser details
- `PHASE2_COMPLETE.md` - 3D rendering details

Enjoy exploring the Shadowbane assets! 🎮
