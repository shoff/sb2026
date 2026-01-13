"""
Asset Catalog Widget - Browse assembled in-game assets (COBJECTS-based).
"""

from __future__ import annotations

from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QListWidget,
    QListWidgetItem,
    QLineEdit,
    QTextEdit,
    QLabel,
)

from assets.asset_catalog import AssetCatalog, AssetKind, AssembledAsset


class AssetCatalogWidget(QWidget):
    """
    UI for browsing assembled assets:
    - Left: categories (kind)
    - Center: asset list + search
    - Right: inspector (composition summary)
    """

    assembled_asset_selected = pyqtSignal(object)  # AssembledAsset

    def __init__(self, asset_manager, parent=None):
        super().__init__(parent)

        self._catalog = AssetCatalog(asset_manager)
        self._current_kind: AssetKind | None = None

        root = QHBoxLayout()
        root.setContentsMargins(0, 0, 0, 0)
        root.setSpacing(6)

        # Left: kinds
        left = QVBoxLayout()
        left.addWidget(QLabel("Categories"))
        self.kind_list = QListWidget()
        self.kind_list.currentItemChanged.connect(self._on_kind_changed)
        left.addWidget(self.kind_list, 1)

        # Center: search + assets
        center = QVBoxLayout()
        self.search_box = QLineEdit()
        self.search_box.setPlaceholderText("Search by name or ID...")
        self.search_box.textChanged.connect(self._refresh_assets)
        center.addWidget(self.search_box)
        self.asset_list = QListWidget()
        self.asset_list.currentItemChanged.connect(self._on_asset_changed)
        center.addWidget(self.asset_list, 1)

        # Right: inspector
        right = QVBoxLayout()
        right.addWidget(QLabel("Inspector"))
        self.inspector = QTextEdit()
        self.inspector.setReadOnly(True)
        self.inspector.setLineWrapMode(QTextEdit.LineWrapMode.NoWrap)
        right.addWidget(self.inspector, 1)

        root.addLayout(left, 1)
        root.addLayout(center, 2)
        root.addLayout(right, 2)
        self.setLayout(root)

        self._populate_kinds()

    def _populate_kinds(self) -> None:
        self.kind_list.clear()
        for kind in self._catalog.list_kinds():
            count = self._catalog.count_by_kind(kind)
            item = QListWidgetItem(f"{kind.value} ({count})")
            item.setData(Qt.ItemDataRole.UserRole, kind)
            self.kind_list.addItem(item)

        if self.kind_list.count() > 0:
            self.kind_list.setCurrentRow(0)

    def _on_kind_changed(self, current: QListWidgetItem | None, previous: QListWidgetItem | None) -> None:
        _ = previous
        if not current:
            return
        self._current_kind = current.data(Qt.ItemDataRole.UserRole)
        self._refresh_assets()

    def _refresh_assets(self) -> None:
        if self._current_kind is None:
            return

        self.asset_list.clear()
        query = self.search_box.text()
        for item in self._catalog.search(kind=self._current_kind, query=query, limit=1000):
            li = QListWidgetItem(f"{item.asset_id}  {item.name}")
            li.setData(Qt.ItemDataRole.UserRole, item.asset_id)
            self.asset_list.addItem(li)

        if self.asset_list.count() == 0:
            self.inspector.setPlainText("no matches")

    def _on_asset_changed(self, current: QListWidgetItem | None, previous: QListWidgetItem | None) -> None:
        _ = previous
        if not current:
            return

        asset_id = current.data(Qt.ItemDataRole.UserRole)
        if not isinstance(asset_id, int):
            return

        assembled = self._catalog.assemble(asset_id)
        if not assembled:
            self.inspector.setPlainText(f"assemble failed|id={asset_id}")
            return

        self.inspector.setPlainText(self._format_inspector(assembled))
        self.assembled_asset_selected.emit(assembled)

    @staticmethod
    def _format_inspector(asset: AssembledAsset) -> str:
        lines: list[str] = []
        lines.append(f"id={asset.asset_id}")
        lines.append(f"name={asset.name}")
        lines.append(f"kind={asset.kind.value}")
        if asset.skeleton_id is not None:
            lines.append(f"skeleton_id={asset.skeleton_id}")
        lines.append(f"render_ids={asset.render_ids}")
        lines.append(f"parts={len(asset.parts)}")
        for i, p in enumerate(asset.parts[:200]):
            lines.append(
                f"  part[{i}] mesh={p.mesh_id} tex={p.texture_id} render={p.source_render_id} bone={p.target_bone}"
            )
        if len(asset.parts) > 200:
            lines.append(f"  ... {len(asset.parts) - 200} more parts ...")
        return "\n".join(lines)

