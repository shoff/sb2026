from __future__ import annotations

"""Arcane COBJECT parser.

The Shadowbane *cobjects.cache* entries categorise all in-game 3D assets.
Each record starts with a *flag* that maps to the legacy types discovered in
`objects.cpp`:

    0x03  Static props (pillars, rocks,…)
    0x04  Static structures (buildings)
    0x05  Interactive structures (doors, gates,…)
    0x09  Items / equipment
    0x0D  Creatures / NPCs (runes)
    0x0F  Deeds (land-claim parchments)
    0x13  Particle / environment stubs

The exporter’s JSON format is not standardised across dumps; keys differ by
client build.  The goal is *robust ID extraction*, not perfect fidelity—any
field we don’t understand is preserved in `extras` for future research.
"""

from collections import OrderedDict
from typing import Any, Dict, List, Tuple
import re

__all__ = ["ArcCObject"]


class ArcCObject:
    """High-level view of a COBJECT entry."""

    _RENDER_KEYS = (
        "obj_render_object",
        "obj_render_object_high_detail",
        "obj_render_object_low_detail",
        "obj_render_template_id",
        "render_template_id",
        "asset_structure_template_id",
        "asset_template_id",
        "render_id",
    )
    _SKELETON_KEYS = (
        "obj_skeleton",
        "obj_skeleton_id",
        "skeleton_id",
    )
    _DECIMAL_ID = re.compile(r"^\d{4,8}$")

    # ------------------------------------------------------------------
    def __init__(self) -> None:  # noqa: D401
        self.flag: int | None = None
        self.name: str | None = None
        self.render_ids: List[int] = []
        self.skeleton_id: int | None = None
        self.inv_tex_id: int | None = None
        self.map_tex_id: int | None = None
        self.extras: Dict[str, Any] = {}

        self._raw: Dict[str, Any] | None = None

    # ------------------------------------------------------------------
    def load_json(self, data: Dict[str, Any]) -> None:  # noqa: D401
        self._raw = data

        self.flag = data.get("obj_type") or data.get("flag")
        self.name = data.get("obj_name") or data.get("name")

        # Skeleton
        for k in self._SKELETON_KEYS:
            if k in data and isinstance(data[k], int):
                self.skeleton_id = data[k]
                break

        # Render/template IDs
        ids: set[int] = set()
        for k in self._RENDER_KEYS:
            v = data.get(k)
            if isinstance(v, int):
                ids.add(v)
            elif isinstance(v, list):
                ids.update(i for i in v if isinstance(i, int))
        # Fallback heuristic: any key containing "render" and ending with _id
        for k, v in data.items():
            if (
                "render" in k.lower()
                and k.lower().endswith("id")
                and isinstance(v, int)
            ):
                ids.add(v)
        self.render_ids = sorted(ids)

        # Textures
        self.inv_tex_id = data.get("inv_tex") or data.get("invTex") or data.get("inventory_texture_id")
        self.map_tex_id = data.get("map_tex") or data.get("mapTex") or data.get("minimap_texture_id")

        # Preserve unknowns for debugging
        known_keys = {
            *self._RENDER_KEYS,
            *self._SKELETON_KEYS,
            "obj_type",
            "flag",
            "obj_name",
            "name",
            "inv_tex",
            "invTex",
            "inventory_texture_id",
            "map_tex",
            "mapTex",
            "minimap_texture_id",
        }
        self.extras = {k: v for k, v in data.items() if k not in known_keys}

    def save_json(self) -> Dict[str, Any]:
        out: Dict[str, Any] = OrderedDict()
        if self.flag is not None:
            out["flag"] = self.flag
        if self.name is not None:
            out["name"] = self.name
        out["render_ids"] = self.render_ids
        if self.skeleton_id is not None:
            out["skeleton_id"] = self.skeleton_id
        if self.inv_tex_id is not None:
            out["inv_tex_id"] = self.inv_tex_id
        if self.map_tex_id is not None:
            out["map_tex_id"] = self.map_tex_id
        if self.extras:
            out["extras"] = self.extras
        return out 