"""
Asset Browser Widget - Tree view for browsing game assets.
"""

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QTreeWidget, QTreeWidgetItem, QLineEdit
from PyQt6.QtCore import Qt, pyqtSignal
from typing import Optional


class AssetBrowserWidget(QWidget):
    """
    Widget displaying asset hierarchy in a tree view.
    """

    # Signals
    asset_selected = pyqtSignal(str, int)  # (asset_type, asset_id)

    def __init__(self, asset_manager, parent=None):
        super().__init__(parent)

        self.asset_manager = asset_manager

        # Create UI
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)

        # Search box
        self.search_box = QLineEdit()
        self.search_box.setPlaceholderText("Search assets...")
        self.search_box.textChanged.connect(self._on_search)
        layout.addWidget(self.search_box)

        # Tree widget
        self.tree = QTreeWidget()
        self.tree.setHeaderLabel("Assets")
        self.tree.itemClicked.connect(self._on_item_clicked)
        layout.addWidget(self.tree)

        self.setLayout(layout)

        # Populate tree
        self._populate_tree()

    def _populate_tree(self):
        """Populate tree with assets from asset manager."""
        self.tree.clear()

        # Define asset categories
        categories = [
            ("Meshes", "mesh", "MESH"),
            ("Textures", "texture", "TEXTURE"),
            ("Skeletons", "skeleton", "SKELETON"),
            ("Motions", "motion", "MOTION"),
            ("Renders", "render", "RENDER"),
            ("CObjects", "cobject", "COBJECTS"),
        ]

        for category_name, asset_type, folder_name in categories:
            # Create category node
            category_item = QTreeWidgetItem([category_name])
            category_item.setData(0, Qt.ItemDataRole.UserRole, {
                'type': 'category',
                'asset_type': asset_type
            })

            # Get asset IDs
            asset_ids = self.asset_manager.list_assets(asset_type)

            # Add asset items
            for asset_id in asset_ids:
                asset_item = QTreeWidgetItem([str(asset_id)])
                asset_item.setData(0, Qt.ItemDataRole.UserRole, {
                    'type': 'asset',
                    'asset_type': asset_type,
                    'asset_id': asset_id
                })
                category_item.addChild(asset_item)

            # Show count in category label
            category_item.setText(0, f"{category_name} ({len(asset_ids)})")

            self.tree.addTopLevelItem(category_item)

        # Expand all categories
        self.tree.expandAll()

    def _on_item_clicked(self, item: QTreeWidgetItem, column: int):
        """
        Handle tree item click.

        Args:
            item: Clicked item
            column: Column index
        """
        data = item.data(0, Qt.ItemDataRole.UserRole)

        if data and data['type'] == 'asset':
            asset_type = data['asset_type']
            asset_id = data['asset_id']

            # Emit signal
            self.asset_selected.emit(asset_type, asset_id)

            # Show in status (if main window is accessible)
            print(f"Selected {asset_type}: {asset_id}")

    def _on_search(self, text: str):
        """
        Filter assets based on search text.

        Args:
            text: Search query
        """
        if not text:
            # Show all items
            for i in range(self.tree.topLevelItemCount()):
                category = self.tree.topLevelItem(i)
                category.setHidden(False)
                for j in range(category.childCount()):
                    child = category.child(j)
                    child.setHidden(False)
            return

        # Filter items
        text = text.lower()

        for i in range(self.tree.topLevelItemCount()):
            category = self.tree.topLevelItem(i)
            visible_children = 0

            for j in range(category.childCount()):
                child = category.child(j)
                asset_text = child.text(0).lower()

                # Show if matches search
                matches = text in asset_text
                child.setHidden(not matches)

                if matches:
                    visible_children += 1

            # Hide category if no visible children
            category.setHidden(visible_children == 0)

    def refresh(self):
        """Refresh asset tree (reload from asset manager)."""
        self._populate_tree()

    def get_selected_asset(self) -> Optional[tuple]:
        """
        Get currently selected asset.

        Returns:
            Tuple of (asset_type, asset_id) or None if no selection
        """
        current_item = self.tree.currentItem()

        if not current_item:
            return None

        data = current_item.data(0, Qt.ItemDataRole.UserRole)

        if data and data['type'] == 'asset':
            return (data['asset_type'], data['asset_id'])

        return None
