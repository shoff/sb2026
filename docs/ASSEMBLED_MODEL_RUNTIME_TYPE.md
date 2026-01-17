# ASSEMBLED_MODEL_RUNTIME_TYPE

Evidence-backed identification of the canonical runtime type representing an “assembled renderable” (the thing the renderer consumes after mesh/material/texture/skeleton assembly).

> Status: **partially proven**. `ArcRenderObject` is confirmed as a runtime composition object that owns a render-object tree and applies texture-set selection recursively. Mesh submission exists (fixed-function path), but the precise “ArcRenderObject → mesh rep(s) → draw” call chain still needs to be pinned down.

## 1) Candidate canonical assembled type: `ArcRenderObject` (confirmed composition role)

### 1.1 Identification evidence

- RTTI: `.?AVArcRenderObject@@` at `0x016cde28`
- Source path: `C:\ArcanePrime\Main_Branch\Shadowbane\Source\ArcRenderObject.cpp` at `0x016d7028`

**Evidence**: `list_strings` results and `get_xrefs_to()` for `0x016d7028` show multiple functions within the `0x005c....` range referencing the source path.

### 1.2 Confirmed fields / layout (partial; offsets are concrete)

From `FUN_005c5150(this, child_ptr)` (“add child” behavior):

- **Child vector storage**:
  - `this+0x3c` = begin ptr
  - `this+0x40` = end ptr
  - `this+0x44` = capacity ptr
  - (used as a `vector<void*>`-like structure; insertion grows these pointers)
- **Child back-pointer to parent**:
  - when inserted: `*(child + 200) = this`
  - i.e. `child+0xC8` is the parent pointer field

**Evidence**: `FUN_005c5150` decomp shows insertion into `this+0x3c/0x40/0x44` and `*(void **)(param_1 + 200) = this;`.

From `FUN_005c8170(this, texture_set_index)` (apply texture set recursively):

- **Selected texture-set index**:
  - `*(this+0xE0) = texture_set_index` (also writes 0 when no selection)
- **Texture-set collection pointer**:
  - `this+0xE8` points to an object that contains a vector at offsets `+0x24/+0x28` and stores the selected index at `+0x30`
  - bounds check uses: `*(this+0xE8)->(+0x28) - (+0x24) >> 2`

**Evidence**: `FUN_005c8170` decomp (writes `this+0xE0`; reads `*(this+0xE8)+0x24/0x28`, writes `*(this+0xE8)+0x30`).

From `FUN_005c0ab0(param_1, depth)` (tree-walk/debug print):

- Reads a string-like field at `param_1+0x98` and prints it.

**Evidence**: `FUN_005c0ab0` decomp uses `core::String::_PrivateGetCStringMethodUse_CSTR_MacroInstead((param_1+0x98), ...)`.

### 1.3 Confirmed “assembled” behaviors

- **Tree composition**:
  - `ArcRenderObject` owns a list of child render objects and enforces unique insertion (via `FUN_005c5150` + `thunk_FUN_005d25c0` search).
- **Recursive texture-set application**:
  - `FUN_005c8170` applies a texture-set index to `this` and then recurses across children using the child vector at `this+0x3c`.

This matches the “assembled renderable” role: a runtime object that combines multiple sub-objects and propagates material/texture selection rules.

## 2) Where mesh payloads and draw submission sit today (known, but link pending)

### 2.1 Mesh payload runtime type (confirmed)

- `ArcMesh` binary loader: `FUN_005a33e0`
- Fixed-function draw helpers exist:
  - `glDrawElements` loops: `FUN_005a0740` / `FUN_005a0780` / `FUN_005a07f0`
  - immediate mode draw: `FUN_005aadc0`

**Evidence**: decomp of those functions + imports for `glDrawElements`.

### 2.2 Missing “spine” proof (next step)

We still need to prove, with a call-chain + field layout:

- which field(s) on `ArcRenderObject` reference mesh instances (e.g. `ArcMeshRep`, `ArcMeshSet`, `RenderAction@ArcMesh`, etc.)
- how those mesh instances are chosen (meshset/part selection) and bound with textures
- the exact method on `ArcRenderObject` (or wrapper) that triggers the `glDrawElements` path

## 3) Immediate follow-up targets

- Find `ArcRenderObject::Render` / draw methods (likely near the `ArcRenderObject.cpp` string cluster) and trace to the `FUN_005a07xx` draw helpers.
- Locate `ArcMeshRep` usage within `ArcRenderObject` (RTTI `. ?AVArcMeshRep@@` at `0x016d6920`) to connect “render object” → “mesh rep” → draw.

## 4) Renderobject → mesh-part enumeration (pending; MCP-required)

- **Locate mesh/rep references on `ArcRenderObject`**
  - **Anchors**:
    - RTTI: `.?AVArcMeshRep@@` (`0x016d6920`)
    - RTTI: `.?AVRenderAction@ArcMesh@@` (`0x016d6188`)
    - Source path: `ArcRenderObject.cpp` (`0x016d7028`)
  - **Expected evidence**:
    - field offsets on `ArcRenderObject` that store mesh/meshrep pointers or a list of render-actions
    - per-part arrays (ranges, primitive modes, flags) with concrete offsets and element sizes
  - **To fill**:
    - `ArcRenderObject` fields: `+0x??` → `ArcMeshRep*` / `ArcMeshSet*` / draw ranges
    - per-part flags: `+0x??` (meaning + controlling render state)

## 5) Render submission chain (pending; MCP-required)

- **Prove the call chain from `ArcRenderObject` to draw**
  - **Known draw endpoints (already evidenced)**:
    - `FUN_005a0740` / `FUN_005a0780` / `FUN_005a07f0` → `glDrawElements(..., GL_UNSIGNED_SHORT, ...)`
    - `FUN_005aadc0` immediate-mode fallback (`glBegin(5)` triangle strip)
  - **Anchors to start from (once MCP is live)**:
    - XREFs to `glDrawElements` import (`EXTERNAL:0000018f`) → callsites → parents
    - XREFs to `ArcRenderObject.cpp` string (`0x016d7028`) → likely render traversal functions
  - **Expected evidence**:
    - render traversal function(s): `FUN_0x??????` (signature, loop structure)
    - texture/material bind points before drawing
    - mesh-part iteration order and state setup per part

## 6) Evidence blocks to drop in (template)

- **Render traversal entry**
  - Function:
  - Evidence:
  - Notes:
- **Mesh-part loop**
  - Function:
  - Fields/offsets:
  - Evidence:
- **Texture/material binding**
  - Function:
  - Fields/offsets:
  - Evidence:
- **Draw call handoff**
  - Function:
  - Draw helper reached:
  - Evidence:

