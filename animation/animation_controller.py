"""
Animation Controller - Manages animation playback and frame interpolation.
"""

import numpy as np
from enum import Enum
from typing import Dict, Optional

from animation.interpolation import lerp, slerp


class PlaybackState(Enum):
    """Animation playback state."""
    STOPPED = 0
    PLAYING = 1
    PAUSED = 2


class AnimationController:
    """
    Controls animation playback with frame interpolation.
    """

    def __init__(self, motion=None):
        """
        Initialize animation controller.

        Args:
            motion: ArcMotion object (optional)
        """
        self.motion = motion
        self.state = PlaybackState.STOPPED

        # Playback parameters
        self.current_frame = 0.0
        self.playback_speed = 1.0
        self.loop = True

        # Motion data
        self.frame_count = 0
        self.frame_rate = 30.0  # Default 30 FPS
        self.bone_frames = {}  # bone_name -> {pos: [], rot: [], scale: []}

        if motion:
            self.load_motion(motion)

    def load_motion(self, motion):
        """
        Load motion data from ArcMotion.

        Args:
            motion: ArcMotion object
        """
        self.motion = motion
        self.bone_frames = {}

        # Extract frame count
        if hasattr(motion, 'frame_count'):
            self.frame_count = motion.frame_count
        else:
            self.frame_count = 0

        # Parse motion data
        # The ArcMotion format varies, try to handle both formats
        if hasattr(motion, 'motion_name'):
            print(f"Loading animation: {motion.motion_name}")

        # Check for frame-based animation data
        if hasattr(motion, 'frames') and motion.frames:
            # Format: frames dict with bone data
            if isinstance(motion.frames, dict):
                if 'frame_count' in motion.frames:
                    self.frame_count = motion.frames['frame_count']

                if 'bones' in motion.frames:
                    for bone_name, bone_data in motion.frames['bones'].items():
                        self.bone_frames[bone_name] = {
                            'pos': bone_data.get('pos', []),
                            'rot': bone_data.get('rot', []),
                            'scale': bone_data.get('scale', [])
                        }
        # Try alternate format with direct bone access
        elif hasattr(motion, 'bone_transforms'):
            # Alternative format
            for bone_name, transforms in motion.bone_transforms.items():
                self.bone_frames[bone_name] = transforms

        # Validate data
        if self.frame_count == 0 or not self.bone_frames:
            print(f"Warning: Motion has no frame data (frame_count={self.frame_count}, bones={len(self.bone_frames)})")

        print(f"Loaded motion: {self.frame_count} frames, {len(self.bone_frames)} bones")

    def play(self):
        """Start playback."""
        self.state = PlaybackState.PLAYING

    def pause(self):
        """Pause playback."""
        self.state = PlaybackState.PAUSED

    def stop(self):
        """Stop playback and reset to start."""
        self.state = PlaybackState.STOPPED
        self.current_frame = 0.0

    def update(self, delta_time: float):
        """
        Update animation playback.

        Args:
            delta_time: Time elapsed since last update (seconds)
        """
        if self.state != PlaybackState.PLAYING:
            return

        # Advance frame
        frames_per_second = self.frame_rate * self.playback_speed
        self.current_frame += frames_per_second * delta_time

        # Handle looping
        if self.current_frame >= self.frame_count:
            if self.loop:
                self.current_frame = self.current_frame % self.frame_count
            else:
                self.current_frame = self.frame_count - 1
                self.state = PlaybackState.STOPPED

    def set_frame(self, frame: float):
        """
        Set current frame directly.

        Args:
            frame: Frame number (can be fractional)
        """
        self.current_frame = np.clip(frame, 0.0, max(0, self.frame_count - 1))

    def get_current_pose(self) -> Dict[str, tuple]:
        """
        Get interpolated pose for current frame.

        Returns:
            Dictionary mapping bone_name -> (position, rotation, scale)
        """
        if not self.bone_frames or self.frame_count == 0:
            return {}

        pose = {}

        # Get integer frame indices
        frame_idx = int(self.current_frame)
        next_idx = min(frame_idx + 1, self.frame_count - 1)
        t = self.current_frame - frame_idx  # Interpolation factor [0, 1]

        # Interpolate each bone
        for bone_name, bone_data in self.bone_frames.items():
            pos_frames = bone_data.get('pos', [])
            rot_frames = bone_data.get('rot', [])
            scale_frames = bone_data.get('scale', [])

            # Check if we have enough frames
            if frame_idx >= len(pos_frames):
                continue

            # Get keyframe data
            pos1 = np.array(pos_frames[frame_idx], dtype=np.float32)
            pos2 = np.array(pos_frames[next_idx], dtype=np.float32) if next_idx < len(pos_frames) else pos1

            rot1 = np.array(rot_frames[frame_idx], dtype=np.float32) if frame_idx < len(rot_frames) else np.array([0, 0, 0, 1], dtype=np.float32)
            rot2 = np.array(rot_frames[next_idx], dtype=np.float32) if next_idx < len(rot_frames) else rot1

            scale1 = np.array(scale_frames[frame_idx], dtype=np.float32) if frame_idx < len(scale_frames) else np.array([1, 1, 1], dtype=np.float32)
            scale2 = np.array(scale_frames[next_idx], dtype=np.float32) if next_idx < len(scale_frames) else scale1

            # Interpolate
            pos = lerp(pos1, pos2, t)
            rot = slerp(rot1, rot2, t)
            scale = lerp(scale1, scale2, t)

            pose[bone_name] = (pos, rot, scale)

        return pose

    def get_frame_percentage(self) -> float:
        """
        Get current playback position as percentage.

        Returns:
            Percentage [0, 1]
        """
        if self.frame_count == 0:
            return 0.0
        return self.current_frame / self.frame_count

    def set_frame_percentage(self, percentage: float):
        """
        Set current frame by percentage.

        Args:
            percentage: Position [0, 1]
        """
        self.current_frame = percentage * max(0, self.frame_count - 1)

    def is_playing(self) -> bool:
        """Check if animation is playing."""
        return self.state == PlaybackState.PLAYING

    def get_duration(self) -> float:
        """
        Get animation duration in seconds.

        Returns:
            Duration in seconds
        """
        if self.frame_rate == 0:
            return 0.0
        return self.frame_count / self.frame_rate
