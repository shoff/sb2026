"""
Camera - Orbit camera with rotate, pan, and zoom controls.
"""

import numpy as np
from utils.math_utils import perspective, look_at


class Camera:
    """
    Orbit camera for 3D viewing.
    """

    def __init__(self, width: int = 800, height: int = 600):
        """
        Initialize camera.

        Args:
            width: Viewport width
            height: Viewport height
        """
        # Camera parameters
        self.distance = 10.0  # Distance from target
        self.azimuth = 45.0   # Horizontal rotation (degrees)
        self.elevation = 30.0  # Vertical rotation (degrees)
        self.target = np.array([0.0, 0.0, 0.0], dtype=np.float32)  # Look-at target

        # Projection parameters
        self.fov = 45.0  # Field of view (degrees)
        self.near = 0.1
        self.far = 1000.0
        self.aspect = width / height if height > 0 else 1.0

        # Pan offset
        self.pan_offset = np.array([0.0, 0.0], dtype=np.float32)

    def resize(self, width: int, height: int):
        """
        Update aspect ratio on window resize.

        Args:
            width: New viewport width
            height: New viewport height
        """
        self.aspect = width / height if height > 0 else 1.0

    def get_view_matrix(self) -> np.ndarray:
        """
        Calculate view matrix from camera parameters.

        Returns:
            4x4 view matrix
        """
        # Calculate camera position from spherical coordinates
        azimuth_rad = np.radians(self.azimuth)
        elevation_rad = np.radians(self.elevation)

        # Spherical to Cartesian
        x = self.distance * np.cos(elevation_rad) * np.cos(azimuth_rad)
        z = self.distance * np.cos(elevation_rad) * np.sin(azimuth_rad)
        y = self.distance * np.sin(elevation_rad)

        eye = np.array([x, y, z], dtype=np.float32)

        # Apply pan offset (in camera space)
        # Calculate right and up vectors
        forward = -eye / np.linalg.norm(eye)
        right = np.cross(forward, np.array([0, 1, 0]))
        right = right / np.linalg.norm(right)
        up = np.cross(right, forward)

        # Apply pan
        target = self.target + right * self.pan_offset[0] + up * self.pan_offset[1]
        eye = eye + right * self.pan_offset[0] + up * self.pan_offset[1]

        # Create view matrix
        return look_at(eye, target, np.array([0, 1, 0]))

    def get_projection_matrix(self) -> np.ndarray:
        """
        Calculate projection matrix.

        Returns:
            4x4 projection matrix
        """
        return perspective(self.fov, self.aspect, self.near, self.far)

    def get_position(self) -> np.ndarray:
        """
        Get camera position in world space.

        Returns:
            Camera position (x, y, z)
        """
        azimuth_rad = np.radians(self.azimuth)
        elevation_rad = np.radians(self.elevation)

        x = self.distance * np.cos(elevation_rad) * np.cos(azimuth_rad)
        z = self.distance * np.cos(elevation_rad) * np.sin(azimuth_rad)
        y = self.distance * np.sin(elevation_rad)

        # Apply pan offset
        forward = -np.array([x, y, z]) / self.distance
        right = np.cross(forward, np.array([0, 1, 0]))
        right = right / np.linalg.norm(right)
        up = np.cross(right, forward)

        position = np.array([x, y, z]) + right * self.pan_offset[0] + up * self.pan_offset[1]

        return position

    def rotate(self, delta_azimuth: float, delta_elevation: float):
        """
        Rotate camera (orbit around target).

        Args:
            delta_azimuth: Change in azimuth (degrees)
            delta_elevation: Change in elevation (degrees)
        """
        self.azimuth += delta_azimuth
        self.elevation += delta_elevation

        # Clamp elevation to prevent gimbal lock
        self.elevation = np.clip(self.elevation, -89.0, 89.0)

        # Wrap azimuth
        self.azimuth = self.azimuth % 360.0

    def pan(self, delta_x: float, delta_y: float):
        """
        Pan camera (move target).

        Args:
            delta_x: Horizontal pan
            delta_y: Vertical pan
        """
        # Scale pan by distance for consistent feel
        scale = self.distance * 0.001

        self.pan_offset[0] += delta_x * scale
        self.pan_offset[1] += delta_y * scale

    def zoom(self, delta: float):
        """
        Zoom camera (change distance from target).

        Args:
            delta: Zoom amount (negative = zoom in, positive = zoom out)
        """
        self.distance += delta * self.distance * 0.1

        # Clamp distance
        self.distance = np.clip(self.distance, 0.1, 1000.0)

    def reset(self):
        """Reset camera to default position."""
        self.distance = 10.0
        self.azimuth = 45.0
        self.elevation = 30.0
        self.target = np.array([0.0, 0.0, 0.0], dtype=np.float32)
        self.pan_offset = np.array([0.0, 0.0], dtype=np.float32)

    def frame_object(self, bounds_min: np.ndarray, bounds_max: np.ndarray):
        """
        Frame camera to view an object's bounding box.

        Args:
            bounds_min: Minimum point of bounding box
            bounds_max: Maximum point of bounding box
        """
        # Calculate bounding box center
        center = (bounds_min + bounds_max) / 2.0
        self.target = center
        self.pan_offset = np.array([0.0, 0.0], dtype=np.float32)

        # Calculate bounding box size
        size = bounds_max - bounds_min
        max_dim = np.max(size)

        # Set distance to frame object
        self.distance = max_dim * 2.0
