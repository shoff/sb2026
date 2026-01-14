# SKINNING_PIPELINE_SPEC

Evidence-backed skinning pipeline ownership and data flow.

> Status: **pending; MCP-required**.

## 1) Module fingerprint (to fill from Skin.dll)

- **Segments**:
  - (list_segments)
- **Exports**:
  - (list_exports)
- **Imports**:
  - (list_imports; include any GL / D3D / SIMD / CRT)
- **RTTI/class names**:
  - (list_classes)
- **Source paths**:
  - (list_strings filter: `C:\\ArcanePrime\\` / `.cpp`)
- **Key log/diagnostic strings**:
  - (list_strings filters: `skin`, `bone`, `weight`, `palette`, `influence`, `matrix`)

## 2) Skinning data structures (to fill)

- **Vertex influence representation**:
  - weights: (format/width/count)
  - bone indices: (format/width/count)
  - max influences per vertex: (value + evidence)
- **Skeleton binding inputs**:
  - skeleton ID reference type:
  - bind pose storage layout:
  - inverse bind pose storage layout:

## 3) Bone palette creation (to fill)

- **Entry points**:
  - function(s):
  - owning type(s):
- **Outputs**:
  - matrix array type/stride:
  - coordinate space used:
  - upload target (uniform array / constant buffer / client array):

## 4) CPU vs GPU skinning determination (to fill)

- **CPU skinning evidence** (if present):
  - loops multiplying vertices by bone matrices:
  - writeback location (temp buffer / mesh buffers):
- **GPU skinning evidence** (if present):
  - attribute binding for weights/indices:
  - bone palette upload near draw:
  - shader/ARB attribute path usage:

## 5) Skinned draw path (to fill)

- **Render submission entry**:
  - function(s):
  - call chain to draw:
- **Vertex format variants**:
  - static vs skinned:
  - any alternate packed formats:

## 6) Evidence blocks to drop in (template)

- **RTTI/type anchor**
  - String/addr:
  - XREFs:
  - Notes:
- **Palette builder**
  - Function:
  - Inputs/outputs:
  - Evidence:
- **Influence unpack/pack**
  - Function:
  - Formats:
  - Evidence:
- **Skinned draw binding**
  - Function:
  - GL calls/imports:
  - Evidence:

