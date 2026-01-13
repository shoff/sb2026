"""
Math utilities for 3D transformations.
"""

import numpy as np
from typing import Tuple


def perspective(fov: float, aspect: float, near: float, far: float) -> np.ndarray:
    """
    Create a perspective projection matrix.

    Args:
        fov: Field of view in degrees
        aspect: Aspect ratio (width / height)
        near: Near clipping plane
        far: Far clipping plane

    Returns:
        4x4 projection matrix
    """
    f = 1.0 / np.tan(np.radians(fov) / 2.0)
    matrix = np.array([
        [f / aspect, 0, 0, 0],
        [0, f, 0, 0],
        [0, 0, (far + near) / (near - far), (2 * far * near) / (near - far)],
        [0, 0, -1, 0]
    ], dtype=np.float32)
    return matrix


def look_at(eye: np.ndarray, center: np.ndarray, up: np.ndarray) -> np.ndarray:
    """
    Create a view matrix looking at a target.

    Args:
        eye: Camera position
        center: Target position
        up: Up vector

    Returns:
        4x4 view matrix
    """
    f = (center - eye)
    f = f / np.linalg.norm(f)

    s = np.cross(f, up)
    s = s / np.linalg.norm(s)

    u = np.cross(s, f)

    matrix = np.identity(4, dtype=np.float32)
    matrix[0, 0:3] = s
    matrix[1, 0:3] = u
    matrix[2, 0:3] = -f
    matrix[0, 3] = -np.dot(s, eye)
    matrix[1, 3] = -np.dot(u, eye)
    matrix[2, 3] = np.dot(f, eye)

    return matrix


def translation_matrix(translation: Tuple[float, float, float]) -> np.ndarray:
    """
    Create a translation matrix.

    Args:
        translation: (x, y, z) translation

    Returns:
        4x4 translation matrix
    """
    matrix = np.identity(4, dtype=np.float32)
    matrix[0:3, 3] = translation
    return matrix


def rotation_matrix_x(angle: float) -> np.ndarray:
    """
    Create rotation matrix around X axis.

    Args:
        angle: Rotation angle in radians

    Returns:
        4x4 rotation matrix
    """
    c = np.cos(angle)
    s = np.sin(angle)
    return np.array([
        [1, 0, 0, 0],
        [0, c, -s, 0],
        [0, s, c, 0],
        [0, 0, 0, 1]
    ], dtype=np.float32)


def rotation_matrix_y(angle: float) -> np.ndarray:
    """
    Create rotation matrix around Y axis.

    Args:
        angle: Rotation angle in radians

    Returns:
        4x4 rotation matrix
    """
    c = np.cos(angle)
    s = np.sin(angle)
    return np.array([
        [c, 0, s, 0],
        [0, 1, 0, 0],
        [-s, 0, c, 0],
        [0, 0, 0, 1]
    ], dtype=np.float32)


def rotation_matrix_z(angle: float) -> np.ndarray:
    """
    Create rotation matrix around Z axis.

    Args:
        angle: Rotation angle in radians

    Returns:
        4x4 rotation matrix
    """
    c = np.cos(angle)
    s = np.sin(angle)
    return np.array([
        [c, -s, 0, 0],
        [s, c, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ], dtype=np.float32)


def scale_matrix(scale: Tuple[float, float, float]) -> np.ndarray:
    """
    Create a scale matrix.

    Args:
        scale: (x, y, z) scale factors

    Returns:
        4x4 scale matrix
    """
    matrix = np.identity(4, dtype=np.float32)
    matrix[0, 0] = scale[0]
    matrix[1, 1] = scale[1]
    matrix[2, 2] = scale[2]
    return matrix
