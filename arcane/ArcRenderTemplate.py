from __future__ import annotations

"""Arcane Render Template parser.

This module provides a permissive, forward-compatible loader for the RENDER
category JSON produced by the original Shadowbane client exporter.

The legacy C++ viewer (`RenderInfo` in objects.cpp) shows that each render
record can embed:

• A primary mesh id
• A list of child render ids (recursive assembly)
• An optional texture override id
• A `joint` string that declares where the mesh should attach when used as a
  child of a skeleton-driven COBJECT (e.g. Hair → joint "Head")
• Position / rotation / scale hints (currently only *pos* is used by the
  previewer – rotation/scale are TODO).

Because historical JSON dumps from different client versions vary wildly in
field naming, we don’t try to match a rigid schema.  Instead we walk the
entire document collecting integers behind any key that *looks* like a mesh
or render reference.

The heuristic rules are conservative and **must be validated** against the
running client via live disassembly.  If a future export introduces false
positives we can tighten the key filters without touching the broader
pipeline.
"""

from collections import OrderedDict
import re
from typing import Any, Dict, Generator, Iterable, List, Tuple

__all__ = ["ArcRenderTemplate"]


class ArcRenderTemplate:
    """In-memory representation of a render template."""

    # ---------------------------------------------------------------------
    # Heuristic keyword lists – tweak as we learn more from the client
    # ---------------------------------------------------------------------
    _MESH_KEYWORDS: Tuple[str, ...] = (
        "mesh",  # mesh_id, mesh, meshes
        "polymesh",  # polymesh_set, polymesh_id
    )
    _RENDER_ID_KEYWORDS: Tuple[str, ...] = (
        "render_children",
        "render_id",
        "render_template",  # sometimes render_template_id
    )

    # Regex to pick 8-digit numeric strings that *look* like dump filenames
    _DECIMAL_ID = re.compile(r"^\d{4,8}$")

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------
    def __init__(self) -> None:  # noqa: D401
        self.mesh_ids: List[int] = []
        self.child_render_ids: List[int] = []
        self.joint: str | None = None
        self.texture_id: int | None = None
        self.position: Tuple[float, float, float] | None = None

        # Keep the raw data around for potential debugging / round-trip
        self._raw: Dict[str, Any] | None = None

    # ------------------------------------------------------------------
    # JSON helpers
    # ------------------------------------------------------------------
    def load_json(self, data: Dict[str, Any]) -> None:  # noqa: D401
        """Populate fields from *data* dict."""
        self._raw = data

        # Joint name (exact key in export)
        self.joint = data.get("joint") or data.get("joint_name")

        # Position – exporter sometimes stores explicit offset
        self.position = (
            tuple(data.get("pos", ()))
            or tuple(data.get("position", ()))
            or None
        )

        # Texture override
        self.texture_id = self._first_int(
            data.get("texture_id"),
            data.get("tex_id"),
            data.get("override_texture"),
        )

        # Walk entire document looking for mesh / child ids
        mesh_ids: set[int] = set()
        child_ids: set[int] = set()
        for key, value in self._walk_items(data):
            if not key:
                continue
            lkey = key.lower()
            if self._looks_like_mesh_key(lkey):
                mesh_ids.update(self._ints_from(value))
            elif self._looks_like_child_key(lkey):
                child_ids.update(self._ints_from(value))
        # Avoid duplicates / overlaps
        self.mesh_ids = sorted(mesh_ids)
        self.child_render_ids = sorted(child_ids - mesh_ids)

    def save_json(self) -> Dict[str, Any]:
        """Minimal JSON representation (primarily for tests)."""
        out: Dict[str, Any] = OrderedDict()
        out["mesh_ids"] = self.mesh_ids
        out["child_render_ids"] = self.child_render_ids
        if self.joint is not None:
            out["joint"] = self.joint
        if self.texture_id is not None:
            out["texture_id"] = self.texture_id
        if self.position is not None:
            out["position"] = list(self.position)
        return out

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------
    @staticmethod
    def _ints_from(value: Any) -> List[int]:
        """Return *all* ints found inside *value* (recursing lists)."""
        ints: List[int] = []
        if isinstance(value, int):
            ints.append(value)
        elif isinstance(value, str) and ArcRenderTemplate._DECIMAL_ID.fullmatch(value):
            ints.append(int(value))
        elif isinstance(value, (list, tuple)):
            for item in value:
                ints.extend(ArcRenderTemplate._ints_from(item))
        return ints

    def _walk_items(self, obj: Any) -> Generator[Tuple[str, Any], None, None]:  # noqa: ANN401
        """Yield (key, value) pairs for every mapping in *obj*."""
        if isinstance(obj, dict):
            for k, v in obj.items():
                yield k, v
                yield from self._walk_items(v)
        elif isinstance(obj, (list, tuple)):
            for item in obj:
                yield from self._walk_items(item)

    @staticmethod
    def _looks_like_mesh_key(k: str) -> bool:
        return any(word in k for word in ArcRenderTemplate._MESH_KEYWORDS)

    @staticmethod
    def _looks_like_child_key(k: str) -> bool:
        return any(word in k for word in ArcRenderTemplate._RENDER_ID_KEYWORDS)

    @staticmethod
    def _first_int(*vals: Any) -> int | None:  # noqa: ANN401
        for v in vals:
            if isinstance(v, int):
                return v
            if isinstance(v, str) and v.isdigit():
                return int(v)
        return None 