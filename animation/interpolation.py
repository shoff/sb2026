"""
Interpolation utilities for animation.
"""

import numpy as np
from typing import Tuple


def lerp(a: np.ndarray, b: np.ndarray, t: float) -> np.ndarray:
    """
    Linear interpolation between two values.

    Args:
        a: Start value
        b: End value
        t: Interpolation factor [0, 1]

    Returns:
        Interpolated value
    """
    return a + (b - a) * t


def slerp(q1: np.ndarray, q2: np.ndarray, t: float) -> np.ndarray:
    """
    Spherical linear interpolation between two quaternions.

    Args:
        q1: Start quaternion [x, y, z, w]
        q2: End quaternion [x, y, z, w]
        t: Interpolation factor [0, 1]

    Returns:
        Interpolated quaternion
    """
    # Normalize quaternions
    q1 = q1 / np.linalg.norm(q1)
    q2 = q2 / np.linalg.norm(q2)

    # Calculate dot product
    dot = np.dot(q1, q2)

    # If dot product is negative, negate one quaternion to take shorter path
    if dot < 0.0:
        q2 = -q2
        dot = -dot

    # Clamp dot product
    dot = np.clip(dot, -1.0, 1.0)

    # Calculate angle between quaternions
    theta = np.arccos(dot)

    # If quaternions are very close, use linear interpolation
    if theta < 0.001:
        return normalize_quaternion(lerp(q1, q2, t))

    # Spherical interpolation
    sin_theta = np.sin(theta)
    w1 = np.sin((1.0 - t) * theta) / sin_theta
    w2 = np.sin(t * theta) / sin_theta

    return w1 * q1 + w2 * q2


def normalize_quaternion(q: np.ndarray) -> np.ndarray:
    """
    Normalize a quaternion.

    Args:
        q: Quaternion [x, y, z, w]

    Returns:
        Normalized quaternion
    """
    length = np.linalg.norm(q)
    if length < 0.0001:
        return np.array([0, 0, 0, 1], dtype=np.float32)
    return q / length


def quaternion_to_matrix(q: np.ndarray) -> np.ndarray:
    """
    Convert quaternion to 4x4 rotation matrix.

    Args:
        q: Quaternion [x, y, z, w]

    Returns:
        4x4 rotation matrix
    """
    # Normalize
    q = q / np.linalg.norm(q)
    x, y, z, w = q

    # Build rotation matrix
    matrix = np.array([
        [1 - 2*y*y - 2*z*z,     2*x*y - 2*w*z,     2*x*z + 2*w*y, 0],
        [    2*x*y + 2*w*z, 1 - 2*x*x - 2*z*z,     2*y*z - 2*w*x, 0],
        [    2*x*z - 2*w*y,     2*y*z + 2*w*x, 1 - 2*x*x - 2*y*y, 0],
        [                0,                 0,                 0, 1]
    ], dtype=np.float32)

    return matrix


def matrix_to_quaternion(matrix: np.ndarray) -> np.ndarray:
    """
    Convert 4x4 rotation matrix to quaternion.

    Args:
        matrix: 4x4 rotation matrix

    Returns:
        Quaternion [x, y, z, w]
    """
    trace = matrix[0, 0] + matrix[1, 1] + matrix[2, 2]

    if trace > 0:
        s = 0.5 / np.sqrt(trace + 1.0)
        w = 0.25 / s
        x = (matrix[2, 1] - matrix[1, 2]) * s
        y = (matrix[0, 2] - matrix[2, 0]) * s
        z = (matrix[1, 0] - matrix[0, 1]) * s
    elif matrix[0, 0] > matrix[1, 1] and matrix[0, 0] > matrix[2, 2]:
        s = 2.0 * np.sqrt(1.0 + matrix[0, 0] - matrix[1, 1] - matrix[2, 2])
        w = (matrix[2, 1] - matrix[1, 2]) / s
        x = 0.25 * s
        y = (matrix[0, 1] + matrix[1, 0]) / s
        z = (matrix[0, 2] + matrix[2, 0]) / s
    elif matrix[1, 1] > matrix[2, 2]:
        s = 2.0 * np.sqrt(1.0 + matrix[1, 1] - matrix[0, 0] - matrix[2, 2])
        w = (matrix[0, 2] - matrix[2, 0]) / s
        x = (matrix[0, 1] + matrix[1, 0]) / s
        y = 0.25 * s
        z = (matrix[1, 2] + matrix[2, 1]) / s
    else:
        s = 2.0 * np.sqrt(1.0 + matrix[2, 2] - matrix[0, 0] - matrix[1, 1])
        w = (matrix[1, 0] - matrix[0, 1]) / s
        x = (matrix[0, 2] + matrix[2, 0]) / s
        y = (matrix[1, 2] + matrix[2, 1]) / s
        z = 0.25 * s

    return np.array([x, y, z, w], dtype=np.float32)


def compose_transform(position: np.ndarray, rotation: np.ndarray, scale: np.ndarray) -> np.ndarray:
    """
    Compose a transformation matrix from position, rotation (quaternion), and scale.

    Args:
        position: Translation [x, y, z]
        rotation: Rotation quaternion [x, y, z, w]
        scale: Scale [x, y, z]

    Returns:
        4x4 transformation matrix
    """
    # Build rotation matrix
    R = quaternion_to_matrix(rotation)

    # Build scale matrix
    S = np.identity(4, dtype=np.float32)
    S[0, 0] = scale[0]
    S[1, 1] = scale[1]
    S[2, 2] = scale[2]

    # Build translation matrix
    T = np.identity(4, dtype=np.float32)
    T[0:3, 3] = position

    # Compose: T * R * S
    return T @ R @ S


def decompose_transform(matrix: np.ndarray) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    Decompose a transformation matrix into position, rotation, and scale.

    Args:
        matrix: 4x4 transformation matrix

    Returns:
        Tuple of (position, rotation_quaternion, scale)
    """
    # Extract translation
    position = matrix[0:3, 3]

    # Extract scale
    scale_x = np.linalg.norm(matrix[0:3, 0])
    scale_y = np.linalg.norm(matrix[0:3, 1])
    scale_z = np.linalg.norm(matrix[0:3, 2])
    scale = np.array([scale_x, scale_y, scale_z], dtype=np.float32)

    # Remove scale from matrix to get pure rotation
    rotation_matrix = matrix.copy()
    if scale_x > 0.0001:
        rotation_matrix[0:3, 0] /= scale_x
    if scale_y > 0.0001:
        rotation_matrix[0:3, 1] /= scale_y
    if scale_z > 0.0001:
        rotation_matrix[0:3, 2] /= scale_z

    # Convert to quaternion
    rotation = matrix_to_quaternion(rotation_matrix)

    return position, rotation, scale
