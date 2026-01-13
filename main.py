#!/usr/bin/env python3
"""
Shadowbane Asset Viewer - Main Entry Point

A tool for viewing and exporting Shadowbane game assets with skeletal animation support.
"""

import sys
from pathlib import Path
from PyQt6.QtWidgets import QApplication

# Add parent directory to path for arcane imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from shadowbane_viewer.ui.main_window import MainWindow
from shadowbane_viewer.ui.asset_browser import AssetBrowserWidget
from shadowbane_viewer.ui.opengl_viewport import OpenGLViewport
from shadowbane_viewer.ui.animation_timeline import AnimationTimelineWidget
from shadowbane_viewer.assets.asset_manager import AssetManager


class ShadowbaneViewer:
    """
    Main application class.
    """

    def __init__(self):
        # Initialize Qt application
        self.app = QApplication(sys.argv)
        self.app.setApplicationName("Shadowbane Asset Viewer")
        self.app.setOrganizationName("Shadowbane")

        # Set dark theme (optional, but looks nice)
        self._set_dark_theme()

        # Initialize asset manager
        arcane_dump_path = Path(__file__).parent.parent / "arcane_dump"
        self.asset_manager = AssetManager(str(arcane_dump_path))

        # Create main window
        self.main_window = MainWindow()

        # Set asset manager reference
        self.main_window.set_asset_manager(self.asset_manager)

        # Create asset browser
        self.asset_browser = AssetBrowserWidget(self.asset_manager)
        self.main_window.set_asset_browser(self.asset_browser)

        # Create OpenGL viewport
        self.viewport = OpenGLViewport(self.asset_manager)
        self.main_window.set_viewport(self.viewport)

        # Create animation timeline
        self.timeline = AnimationTimelineWidget()
        self.main_window.set_timeline(self.timeline)

        # Connect signals
        self._connect_signals()

        # Show window
        self.main_window.show()
        self.main_window.show_status_message(
            f"Loaded assets from: {arcane_dump_path}",
            5000
        )

    def _connect_signals(self):
        """Connect signals between components."""
        # Asset browser selection -> main window
        self.asset_browser.asset_selected.connect(self._on_asset_selected)

        # Viewport FPS -> status bar
        self.viewport.fps_updated.connect(lambda fps:
            self.main_window.show_status_message(f"FPS: {fps:.0f}", 0)
        )

        # Viewport animation frame -> timeline
        self.viewport.frame_updated.connect(self.timeline.set_frame)

        # Timeline controls -> animation controller
        self.timeline.play_requested.connect(self._on_play_animation)
        self.timeline.pause_requested.connect(self._on_pause_animation)
        self.timeline.stop_requested.connect(self._on_stop_animation)
        self.timeline.frame_changed.connect(self._on_frame_changed)
        self.timeline.speed_changed.connect(self._on_speed_changed)
        self.timeline.loop_changed.connect(self._on_loop_changed)

    def _on_asset_selected(self, asset_type: str, asset_id: int):
        """
        Handle asset selection from browser.

        Args:
            asset_type: Type of asset (mesh, texture, etc.)
            asset_id: Asset ID
        """
        print(f"Asset selected: {asset_type} #{asset_id}")

        # Handle mesh selection - load into viewport
        if asset_type == 'mesh':
            # Try to find a texture for this mesh (for now, just use first texture if available)
            texture_id = None
            textures = self.asset_manager.list_assets('texture')
            if textures and len(textures) > 0:
                # Use a random texture for now (in Phase 3+, we'll use proper material system)
                import random
                texture_id = random.choice(textures[:100])  # Pick from first 100 textures

            self.viewport.load_mesh(asset_id, texture_id)
            self.main_window.show_status_message(
                f"Loaded mesh {asset_id}" + (f" with texture {texture_id}" if texture_id else ""),
                3000
            )
            # Enable export action
            self.main_window.enable_export(True)

        # Handle texture selection
        elif asset_type == 'texture':
            # If a mesh is currently loaded, apply this texture to it
            if self.viewport.current_mesh_id is not None:
                self.viewport.current_texture_id = asset_id
                self.viewport.update()
                self.main_window.show_status_message(
                    f"Applied texture {asset_id} to mesh {self.viewport.current_mesh_id}",
                    3000
                )
            else:
                self.main_window.show_status_message(
                    f"Selected texture {asset_id} (load a mesh first to apply)",
                    3000
                )

        # Handle skeleton selection
        elif asset_type == 'skeleton':
            # Try to find a mesh and motion for this skeleton
            # For now, just show info
            skeleton = self.asset_manager.load_skeleton(asset_id)
            if skeleton:
                bone_count = len(skeleton.skeleton_bones) if hasattr(skeleton, 'skeleton_bones') else 0
                self.main_window.show_status_message(
                    f"Selected skeleton {asset_id} ({bone_count} bones) - Select a mesh to apply",
                    3000
                )
            else:
                self.main_window.show_status_message(
                    f"Failed to load skeleton {asset_id}",
                    3000
                )

        # Handle motion selection
        elif asset_type == 'motion':
            # If a mesh with skeleton is loaded, apply this motion
            if self.viewport.skeletal_animator is not None:
                motion = self.asset_manager.load_motion(asset_id)
                if motion:
                    from shadowbane_viewer.animation.animation_controller import AnimationController
                    self.viewport.animation_controller = AnimationController(motion)

                    # Update timeline with new animation
                    frame_count = self.viewport.animation_controller.frame_count
                    self.timeline.set_animation(frame_count)
                    self.timeline.set_playing(False)

                    self.main_window.show_status_message(
                        f"Loaded motion {asset_id} ({frame_count} frames)",
                        3000
                    )
                else:
                    self.main_window.show_status_message(
                        f"Failed to load motion {asset_id}",
                        3000
                    )
            else:
                self.main_window.show_status_message(
                    f"Selected motion {asset_id} (load a skeleton first)",
                    3000
                )

        # Other asset types
        else:
            self.main_window.show_status_message(
                f"Selected {asset_type}: {asset_id}",
                3000
            )

    def _on_play_animation(self):
        """Handle play button click."""
        if self.viewport.animation_controller:
            self.viewport.animation_controller.play()
            self.timeline.set_playing(True)
            self.main_window.show_status_message("Playing animation", 2000)

    def _on_pause_animation(self):
        """Handle pause button click."""
        if self.viewport.animation_controller:
            self.viewport.animation_controller.pause()
            self.timeline.set_playing(False)
            self.main_window.show_status_message("Paused animation", 2000)

    def _on_stop_animation(self):
        """Handle stop button click."""
        if self.viewport.animation_controller:
            self.viewport.animation_controller.stop()
            self.timeline.set_playing(False)
            self.timeline.set_frame(0.0)
            self.main_window.show_status_message("Stopped animation", 2000)

    def _on_frame_changed(self, frame: float):
        """Handle timeline scrubbing."""
        if self.viewport.animation_controller:
            self.viewport.animation_controller.set_frame(frame)
            self.viewport.update()

    def _on_speed_changed(self, speed: float):
        """Handle playback speed change."""
        if self.viewport.animation_controller:
            self.viewport.animation_controller.playback_speed = speed
            self.main_window.show_status_message(f"Playback speed: {speed * 100:.0f}%", 2000)

    def _on_loop_changed(self, loop: bool):
        """Handle loop checkbox change."""
        if self.viewport.animation_controller:
            self.viewport.animation_controller.loop = loop
            self.main_window.show_status_message(f"Loop: {'On' if loop else 'Off'}", 2000)

    def _set_dark_theme(self):
        """Set a dark color scheme for the application."""
        dark_stylesheet = """
            QMainWindow {
                background-color: #2b2b2b;
            }
            QWidget {
                background-color: #2b2b2b;
                color: #d0d0d0;
            }
            QTreeWidget {
                background-color: #1e1e1e;
                alternate-background-color: #262626;
                border: 1px solid #3a3a3a;
            }
            QTreeWidget::item:hover {
                background-color: #3a3a3a;
            }
            QTreeWidget::item:selected {
                background-color: #094771;
            }
            QLineEdit {
                background-color: #1e1e1e;
                border: 1px solid #3a3a3a;
                padding: 4px;
                border-radius: 2px;
            }
            QLineEdit:focus {
                border: 1px solid #094771;
            }
            QDockWidget {
                titlebar-close-icon: url(close.png);
                titlebar-normal-icon: url(undock.png);
            }
            QDockWidget::title {
                background-color: #3a3a3a;
                padding: 4px;
            }
            QMenuBar {
                background-color: #2b2b2b;
            }
            QMenuBar::item:selected {
                background-color: #3a3a3a;
            }
            QMenu {
                background-color: #2b2b2b;
                border: 1px solid #3a3a3a;
            }
            QMenu::item:selected {
                background-color: #094771;
            }
            QStatusBar {
                background-color: #1e1e1e;
                color: #888;
            }
        """
        self.app.setStyleSheet(dark_stylesheet)

    def run(self):
        """Start the application event loop."""
        return self.app.exec()


def main():
    """Main entry point."""
    viewer = ShadowbaneViewer()
    sys.exit(viewer.run())


if __name__ == "__main__":
    main()
