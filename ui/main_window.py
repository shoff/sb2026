"""
Main Window - Primary application window with menu bar and docked panels.
"""

from PyQt6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QMenuBar, QMenu, QDockWidget, QLabel, QFileDialog, QMessageBox
)
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QAction
from pathlib import Path


class MainWindow(QMainWindow):
    """
    Main application window with menu bar, asset browser, viewport, and timeline.
    """

    # Signals
    asset_selected = pyqtSignal(str, int)  # (asset_type, asset_id)

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Shadowbane Asset Viewer")
        self.resize(1400, 900)

        # Initialize UI components
        self._create_menu_bar()
        self._create_central_widget()
        self._create_dock_widgets()

        # Status bar
        self.statusBar().showMessage("Ready")

    def _create_menu_bar(self):
        """Create menu bar with File, View, and Help menus."""
        menubar = self.menuBar()

        # File menu
        file_menu = menubar.addMenu("&File")

        # Open action (placeholder for now)
        open_action = QAction("&Open Cache File...", self)
        open_action.setShortcut("Ctrl+O")
        open_action.setStatusTip("Open a cache file")
        open_action.triggered.connect(self._on_open_cache)
        file_menu.addAction(open_action)

        file_menu.addSeparator()

        # Export action
        export_action = QAction("&Export Asset...", self)
        export_action.setShortcut("Ctrl+E")
        export_action.setStatusTip("Export current asset")
        export_action.setEnabled(False)  # Disabled until Phase 4
        export_action.triggered.connect(self._on_export_asset)
        file_menu.addAction(export_action)
        self.export_action = export_action

        file_menu.addSeparator()

        # Exit action
        exit_action = QAction("E&xit", self)
        exit_action.setShortcut("Ctrl+Q")
        exit_action.setStatusTip("Exit application")
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

        # View menu
        view_menu = menubar.addMenu("&View")

        # Toggle asset browser
        self.toggle_browser_action = QAction("Asset &Browser", self, checkable=True)
        self.toggle_browser_action.setChecked(True)
        self.toggle_browser_action.setStatusTip("Toggle asset browser panel")
        view_menu.addAction(self.toggle_browser_action)

        # Toggle timeline
        self.toggle_timeline_action = QAction("&Timeline", self, checkable=True)
        self.toggle_timeline_action.setChecked(True)
        self.toggle_timeline_action.setStatusTip("Toggle animation timeline panel")
        view_menu.addAction(self.toggle_timeline_action)

        # Help menu
        help_menu = menubar.addMenu("&Help")

        # About action
        about_action = QAction("&About", self)
        about_action.setStatusTip("About Shadowbane Asset Viewer")
        about_action.triggered.connect(self._on_about)
        help_menu.addAction(about_action)

    def _create_central_widget(self):
        """Create central widget (placeholder for now, will be OpenGL viewport)."""
        # For now, just a placeholder label
        # This will be replaced with OpenGLViewport in Phase 2
        central_widget = QWidget()
        layout = QVBoxLayout()

        placeholder = QLabel("3D Viewport (OpenGL)\nComing in Phase 2")
        placeholder.setAlignment(Qt.AlignmentFlag.AlignCenter)
        placeholder.setStyleSheet("""
            QLabel {
                background-color: #2b2b2b;
                color: #888;
                font-size: 18px;
                padding: 20px;
            }
        """)

        layout.addWidget(placeholder)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # Store reference for later replacement
        self.viewport_placeholder = placeholder

    def _create_dock_widgets(self):
        """Create docked panels for asset browser and timeline."""
        # Asset Browser (left dock)
        self.browser_dock = QDockWidget("Asset Browser", self)
        self.browser_dock.setAllowedAreas(
            Qt.DockWidgetArea.LeftDockWidgetArea |
            Qt.DockWidgetArea.RightDockWidgetArea
        )

        # Placeholder for asset browser (will be implemented next)
        browser_placeholder = QLabel("Asset Browser\nComing next...")
        browser_placeholder.setAlignment(Qt.AlignmentFlag.AlignCenter)
        browser_placeholder.setStyleSheet("padding: 20px;")
        self.browser_dock.setWidget(browser_placeholder)

        self.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, self.browser_dock)

        # Connect toggle action
        self.toggle_browser_action.triggered.connect(
            lambda checked: self.browser_dock.setVisible(checked)
        )
        self.browser_dock.visibilityChanged.connect(
            self.toggle_browser_action.setChecked
        )

        # Animation Timeline (bottom dock)
        self.timeline_dock = QDockWidget("Animation Timeline", self)
        self.timeline_dock.setAllowedAreas(
            Qt.DockWidgetArea.BottomDockWidgetArea |
            Qt.DockWidgetArea.TopDockWidgetArea
        )

        # Placeholder for timeline (will be implemented in Phase 3)
        timeline_placeholder = QLabel("Animation Timeline - Coming in Phase 3")
        timeline_placeholder.setAlignment(Qt.AlignmentFlag.AlignCenter)
        timeline_placeholder.setStyleSheet("padding: 10px;")
        self.timeline_dock.setWidget(timeline_placeholder)

        self.addDockWidget(Qt.DockWidgetArea.BottomDockWidgetArea, self.timeline_dock)

        # Connect toggle action
        self.toggle_timeline_action.triggered.connect(
            lambda checked: self.timeline_dock.setVisible(checked)
        )
        self.timeline_dock.visibilityChanged.connect(
            self.toggle_timeline_action.setChecked
        )

        # Set initial dock sizes
        self.browser_dock.setMinimumWidth(250)
        self.timeline_dock.setMinimumHeight(100)

    def set_asset_browser(self, browser_widget):
        """
        Replace placeholder with actual asset browser widget.

        Args:
            browser_widget: AssetBrowserWidget instance
        """
        self.browser_dock.setWidget(browser_widget)

    def set_viewport(self, viewport_widget):
        """
        Replace placeholder with actual OpenGL viewport.

        Args:
            viewport_widget: OpenGLViewport instance
        """
        self.viewport = viewport_widget
        self.setCentralWidget(viewport_widget)

    def set_timeline(self, timeline_widget):
        """
        Replace placeholder with actual animation timeline.

        Args:
            timeline_widget: AnimationTimelineWidget instance
        """
        self.timeline_dock.setWidget(timeline_widget)

    def set_asset_manager(self, asset_manager):
        """
        Set the asset manager reference.

        Args:
            asset_manager: AssetManager instance
        """
        self.asset_manager = asset_manager

    def enable_export(self, enabled: bool):
        """
        Enable or disable the export action.

        Args:
            enabled: Whether to enable export
        """
        self.export_action.setEnabled(enabled)

    def _on_open_cache(self):
        """Handle Open Cache File menu action."""
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Open Cache File",
            "",
            "Cache Files (*.cache);;All Files (*)"
        )

        if file_path:
            self.statusBar().showMessage(f"Opening {file_path}...")
            # TODO: Implement cache file loading in later phase
            QMessageBox.information(
                self,
                "Not Implemented",
                "Cache file loading will be implemented in a future phase.\n"
                "For now, assets are loaded from arcane_dump/ folders."
            )

    def _on_export_asset(self):
        """Handle Export Asset menu action."""
        # Import here to avoid circular dependency
        from ui.export_dialog import ExportDialog

        if not hasattr(self, 'viewport') or not hasattr(self, 'asset_manager'):
            QMessageBox.warning(
                self,
                "Export Error",
                "Viewport or asset manager not initialized."
            )
            return

        if not self.viewport.current_mesh_id:
            QMessageBox.warning(
                self,
                "No Mesh Loaded",
                "Please load a mesh before exporting."
            )
            return

        # Show export dialog
        dialog = ExportDialog(self.viewport, self.asset_manager, self)
        dialog.exec()

    def _on_about(self):
        """Handle About menu action."""
        QMessageBox.about(
            self,
            "About Shadowbane Asset Viewer",
            "<h2>Shadowbane Asset Viewer</h2>"
            "<p>A tool for viewing and exporting Shadowbane game assets.</p>"
            "<p>Features:</p>"
            "<ul>"
            "<li>3D mesh viewing with textures</li>"
            "<li>Skeletal animation playback</li>"
            "<li>Export to OBJ and GLTF formats</li>"
            "</ul>"
            "<p><small>Built with PyQt6 and PyOpenGL</small></p>"
        )

    def show_status_message(self, message: str, timeout: int = 3000):
        """
        Show a message in the status bar.

        Args:
            message: Message to display
            timeout: How long to show message (ms), 0 = permanent
        """
        self.statusBar().showMessage(message, timeout)
