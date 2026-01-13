"""
Animation Timeline Widget - Controls for animation playback.
"""

from PyQt6.QtWidgets import (
    QWidget, QHBoxLayout, QVBoxLayout, QSlider, QPushButton,
    QLabel, QSpinBox, QCheckBox
)
from PyQt6.QtCore import Qt, pyqtSignal, QTimer
from PyQt6.QtGui import QIcon


class AnimationTimelineWidget(QWidget):
    """
    Widget for controlling animation playback.
    """

    # Signals
    play_requested = pyqtSignal()
    pause_requested = pyqtSignal()
    stop_requested = pyqtSignal()
    frame_changed = pyqtSignal(float)  # frame number
    speed_changed = pyqtSignal(float)  # playback speed
    loop_changed = pyqtSignal(bool)  # loop enabled

    def __init__(self, parent=None):
        super().__init__(parent)

        self.frame_count = 0
        self.current_frame = 0.0
        self.is_playing = False

        self._create_ui()

    def _create_ui(self):
        """Create timeline UI."""
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(5, 5, 5, 5)

        # Top row: Playback controls
        controls_layout = QHBoxLayout()

        # Play/Pause button
        self.play_button = QPushButton("▶")  # Play symbol
        self.play_button.setFixedSize(40, 30)
        self.play_button.setToolTip("Play animation (Spacebar)")
        self.play_button.clicked.connect(self._on_play_pause)
        controls_layout.addWidget(self.play_button)

        # Stop button
        self.stop_button = QPushButton("■")  # Stop symbol
        self.stop_button.setFixedSize(40, 30)
        self.stop_button.setToolTip("Stop and reset to start")
        self.stop_button.clicked.connect(self._on_stop)
        controls_layout.addWidget(self.stop_button)

        # Frame display
        self.frame_label = QLabel("Frame: 0 / 0")
        self.frame_label.setMinimumWidth(120)
        controls_layout.addWidget(self.frame_label)

        controls_layout.addStretch()

        # Speed control
        speed_label = QLabel("Speed:")
        controls_layout.addWidget(speed_label)

        self.speed_spinbox = QSpinBox()
        self.speed_spinbox.setRange(10, 400)
        self.speed_spinbox.setValue(100)
        self.speed_spinbox.setSuffix("%")
        self.speed_spinbox.setToolTip("Playback speed")
        self.speed_spinbox.valueChanged.connect(self._on_speed_changed)
        controls_layout.addWidget(self.speed_spinbox)

        # Loop checkbox
        self.loop_checkbox = QCheckBox("Loop")
        self.loop_checkbox.setChecked(True)
        self.loop_checkbox.setToolTip("Loop animation")
        self.loop_checkbox.stateChanged.connect(self._on_loop_changed)
        controls_layout.addWidget(self.loop_checkbox)

        main_layout.addLayout(controls_layout)

        # Bottom row: Timeline slider
        slider_layout = QHBoxLayout()

        # Start label
        start_label = QLabel("0")
        slider_layout.addWidget(start_label)

        # Timeline slider
        self.timeline_slider = QSlider(Qt.Orientation.Horizontal)
        self.timeline_slider.setMinimum(0)
        self.timeline_slider.setMaximum(100)
        self.timeline_slider.setValue(0)
        self.timeline_slider.setToolTip("Scrub timeline")
        self.timeline_slider.valueChanged.connect(self._on_slider_changed)
        slider_layout.addWidget(self.timeline_slider)

        # End label
        self.end_label = QLabel("0")
        slider_layout.addWidget(self.end_label)

        main_layout.addLayout(slider_layout)

        self.setLayout(main_layout)

        # Disable controls until animation is loaded
        self.set_enabled(False)

    def set_animation(self, frame_count: int):
        """
        Set animation parameters.

        Args:
            frame_count: Total number of frames
        """
        self.frame_count = frame_count
        self.current_frame = 0.0

        # Update slider range
        self.timeline_slider.setMaximum(max(0, frame_count - 1))
        self.timeline_slider.setValue(0)

        # Update labels
        self.end_label.setText(str(frame_count - 1))
        self._update_frame_label()

        # Enable controls
        self.set_enabled(frame_count > 0)

    def set_enabled(self, enabled: bool):
        """
        Enable/disable timeline controls.

        Args:
            enabled: Whether to enable controls
        """
        self.play_button.setEnabled(enabled)
        self.stop_button.setEnabled(enabled)
        self.timeline_slider.setEnabled(enabled)
        self.speed_spinbox.setEnabled(enabled)
        self.loop_checkbox.setEnabled(enabled)

    def set_frame(self, frame: float):
        """
        Update current frame.

        Args:
            frame: Current frame number
        """
        self.current_frame = frame

        # Update slider (block signals to prevent recursion)
        self.timeline_slider.blockSignals(True)
        self.timeline_slider.setValue(int(frame))
        self.timeline_slider.blockSignals(False)

        # Update label
        self._update_frame_label()

    def set_playing(self, playing: bool):
        """
        Update playing state.

        Args:
            playing: Whether animation is playing
        """
        self.is_playing = playing

        # Update button text
        if playing:
            self.play_button.setText("⏸")  # Pause symbol
            self.play_button.setToolTip("Pause animation (Spacebar)")
        else:
            self.play_button.setText("▶")  # Play symbol
            self.play_button.setToolTip("Play animation (Spacebar)")

    def _on_play_pause(self):
        """Handle play/pause button click."""
        if self.is_playing:
            self.pause_requested.emit()
        else:
            self.play_requested.emit()

    def _on_stop(self):
        """Handle stop button click."""
        self.stop_requested.emit()

    def _on_slider_changed(self, value: int):
        """Handle timeline slider change."""
        self.current_frame = float(value)
        self._update_frame_label()
        self.frame_changed.emit(self.current_frame)

    def _on_speed_changed(self, value: int):
        """Handle speed spinbox change."""
        speed = value / 100.0
        self.speed_changed.emit(speed)

    def _on_loop_changed(self, state: int):
        """Handle loop checkbox change."""
        loop = (state == Qt.CheckState.Checked.value)
        self.loop_changed.emit(loop)

    def _update_frame_label(self):
        """Update frame display label."""
        self.frame_label.setText(f"Frame: {int(self.current_frame)} / {self.frame_count - 1}")

    def keyPressEvent(self, event):
        """Handle key press events."""
        if event.key() == Qt.Key.Key_Space:
            # Spacebar = play/pause
            self._on_play_pause()
            event.accept()
        else:
            super().keyPressEvent(event)
