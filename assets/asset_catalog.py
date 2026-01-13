from __future__ import annotations

import json
from dataclasses import dataclass
from enum import StrEnum
from pathlib import Path
from typing import Dict, Iterable, List, Optional

import numpy as np


class AssetKind(StrEnum):
    STRUCTURE = "Structure"
    PROP = "Prop"
    ITEM = "Item"
    CREATURE = "Creature"
    DEED = "Deed"
    LIGHT = "Light"
    OTHER = "Other"


@dataclass(frozen=True)
class AssetListItem:
    asset_id: int
    name: str
    kind: AssetKind


@dataclass(frozen=True)
class MeshPart:
    mesh_id: int
    texture_id: Optional[int]
    transform: np.ndarray  # 4x4
    source_render_id: int
    target_bone: Optional[str]


@dataclass(frozen=True)
class AssembledAsset:
    asset_id: int
    name: str
    kind: AssetKind
    render_ids: List[int]
    skeleton_id: Optional[int]
    parts: List[MeshPart]


class AssetCatalog:
    """
    Catalog of assembled in-game assets built from COBJECTS + RENDER records.

    This intentionally hides low-level cache categories from the UI.
    """

    def __init__(self, asset_manager) -> None:
        self._asset_manager = asset_manager
        self._kind_index: Dict[AssetKind, List[int]] = {k: [] for k in AssetKind}
        self._name_cache: Dict[int, str] = {}
        self._kind_cache: Dict[int, AssetKind] = {}

        self._index_cobjects()

    def list_kinds(self) -> List[AssetKind]:
        return [k for k in AssetKind if self._kind_index.get(k)]

    def count_by_kind(self, kind: AssetKind) -> int:
        return len(self._kind_index.get(kind, []))

    def iter_asset_ids(self, kind: AssetKind) -> Iterable[int]:
        return iter(self._kind_index.get(kind, []))

    def search(self, *, kind: AssetKind, query: str, limit: int = 500) -> List[AssetListItem]:
        q = (query or "").strip().lower()
        out: List[AssetListItem] = []
        for asset_id in self._kind_index.get(kind, []):
            name = self._get_name(asset_id)
            if not q or q in name.lower() or q in str(asset_id):
                out.append(AssetListItem(asset_id=asset_id, name=name, kind=kind))
                if len(out) >= limit:
                    break
        return out

    def assemble(self, asset_id: int) -> Optional[AssembledAsset]:
        cobj = self._asset_manager.load_cobject(asset_id)
        if not cobj:
            return None

        name = self._get_name(asset_id)
        kind = self._get_kind(asset_id)
        render_ids = list(getattr(cobj, "render_ids", []) or [])
        skeleton_id = getattr(cobj, "skeleton_id", None)

        parts: List[MeshPart] = []
        for rid in render_ids:
            parts.extend(self._flatten_render_to_parts(render_id=rid, parent_xform=np.identity(4, dtype=np.float32)))

        return AssembledAsset(
            asset_id=asset_id,
            name=name,
            kind=kind,
            render_ids=render_ids,
            skeleton_id=skeleton_id,
            parts=parts,
        )

    # ---------------------------------------------------------------------
    # Indexing
    # ---------------------------------------------------------------------
    def _index_cobjects(self) -> None:
        # Uses AssetManager's disk index; avoids O(n) directory crawling here.
        cobject_ids = self._asset_manager.list_assets("cobject")
        for asset_id in cobject_ids:
            kind = self._get_kind(asset_id)
            self._kind_index.setdefault(kind, []).append(asset_id)

        for k in self._kind_index:
            self._kind_index[k] = sorted(self._kind_index[k])

    def _get_kind(self, asset_id: int) -> AssetKind:
        cached = self._kind_cache.get(asset_id)
        if cached is not None:
            return cached

        src = self._asset_manager.get_source_path("cobject", asset_id)
        kind = AssetKind.OTHER
        if src:
            # arcane_dump/COBJECTS/<CATEGORY>/<id>.json
            category = Path(src).parent.name.upper()
            kind = {
                "STRUCTURE": AssetKind.STRUCTURE,
                "ASSETSTRUCTURE": AssetKind.STRUCTURE,
                "STATIC": AssetKind.PROP,
                "ITEM": AssetKind.ITEM,
                "KEY": AssetKind.ITEM,
                "RUNE": AssetKind.CREATURE,
                "DEED": AssetKind.DEED,
                "LIGHT": AssetKind.LIGHT,
            }.get(category, AssetKind.OTHER)

        self._kind_cache[asset_id] = kind
        return kind

    def _get_name(self, asset_id: int) -> str:
        cached = self._name_cache.get(asset_id)
        if cached is not None:
            return cached

        src = self._asset_manager.get_source_path("cobject", asset_id)
        name = f"Asset {asset_id}"
        if src and Path(src).exists():
            try:
                with open(src, "r", encoding="utf-8") as f:
                    data = json.load(f)
                name = data.get("obj_name") or data.get("name") or name
            except Exception:
                name = name

        self._name_cache[asset_id] = name
        return name

    # ---------------------------------------------------------------------
    # Assembly
    # ---------------------------------------------------------------------
    def _flatten_render_to_parts(self, *, render_id: int, parent_xform: np.ndarray) -> List[MeshPart]:
        render = self._asset_manager.load_render(render_id)
        if not render:
            return []

        xform = parent_xform @ self._render_transform(render)
        target_bone = getattr(render, "render_target_bone", None) or None

        mesh_ids: List[int] = []
        try:
            mesh_set = render.render_template.template_mesh.mesh_set  # type: ignore[attr-defined]
            for m in mesh_set:
                mid = int(m.polymesh_id)
                if mid > 0:
                    mesh_ids.append(mid)
        except Exception:
            mesh_ids = []

        texture_id: Optional[int] = None
        try:
            tex_set = render.render_texture_set  # type: ignore[attr-defined]
            if tex_set:
                # Prefer first texture entry for now
                tex = tex_set[0]
                texture_id = int(tex.texture_data.texture_id)  # type: ignore[attr-defined]
        except Exception:
            texture_id = None

        parts: List[MeshPart] = [
            MeshPart(
                mesh_id=mid,
                texture_id=texture_id,
                transform=xform,
                source_render_id=render_id,
                target_bone=target_bone,
            )
            for mid in mesh_ids
        ]

        # Recurse children renders if present
        child_ids: List[int] = []
        try:
            child_ids = [int(x) for x in getattr(render, "render_children", []) or []]
        except Exception:
            child_ids = []

        for cid in child_ids:
            parts.extend(self._flatten_render_to_parts(render_id=cid, parent_xform=xform))

        return parts

    @staticmethod
    def _render_transform(render) -> np.ndarray:
        m = np.identity(4, dtype=np.float32)

        # Scale
        try:
            sx, sy, sz = render.render_scale  # type: ignore[attr-defined]
            m = m @ np.array(
                [
                    [sx, 0.0, 0.0, 0.0],
                    [0.0, sy, 0.0, 0.0],
                    [0.0, 0.0, sz, 0.0],
                    [0.0, 0.0, 0.0, 1.0],
                ],
                dtype=np.float32,
            )
        except Exception:
            pass

        # Translation
        try:
            has_loc = bool(getattr(render, "render_has_loc", 0))
            if has_loc:
                tx, ty, tz = render.render_loc  # type: ignore[attr-defined]
                t = np.identity(4, dtype=np.float32)
                t[0, 3] = float(tx)
                t[1, 3] = float(ty)
                t[2, 3] = float(tz)
                m = m @ t
        except Exception:
            pass

        return m

