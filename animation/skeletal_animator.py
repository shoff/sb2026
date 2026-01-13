"""
Skeletal Animator - Manages bone hierarchy and computes bone transforms.
"""

import numpy as np
from typing import Dict, List, Optional
from dataclasses import dataclass

from .interpolation import compose_transform


@dataclass
class Bone:
    """
    Represents a single bone in a skeleton.
    """
    index: int
    name: str
    parent_index: int  # -1 for root
    bind_pose_matrix: np.ndarray  # 4x4 matrix

    # Computed transforms
    local_matrix: np.ndarray = None  # Local transform (relative to parent)
    world_matrix: np.ndarray = None  # World transform
    skinning_matrix: np.ndarray = None  # Final skinning matrix

    def __post_init__(self):
        if self.local_matrix is None:
            self.local_matrix = np.identity(4, dtype=np.float32)
        if self.world_matrix is None:
            self.world_matrix = np.identity(4, dtype=np.float32)
        if self.skinning_matrix is None:
            self.skinning_matrix = np.identity(4, dtype=np.float32)


class SkeletalAnimator:
    """
    Manages skeletal hierarchy and computes bone transformations.
    """

    def __init__(self, skeleton):
        """
        Initialize skeletal animator.

        Args:
            skeleton: ArcSkeleton object
        """
        self.skeleton = skeleton
        self.bones: List[Bone] = []
        self.bone_map: Dict[str, int] = {}  # name -> index

        self._build_skeleton()

    def _build_skeleton(self):
        """Build bone hierarchy from ArcSkeleton."""
        # Check skeleton format
        if not hasattr(self.skeleton, 'bones') or not self.skeleton.bones:
            print("Warning: Skeleton has no bones array")
            return

        # Create bones from skeleton data
        for i, bone_data in enumerate(self.skeleton.bones):
            # Extract bone info
            if hasattr(bone_data, 'name'):
                name = bone_data.name
            elif hasattr(bone_data, 'bone_name'):
                name = bone_data.bone_name
            else:
                name = f"Bone_{i}"

            if hasattr(bone_data, 'parent_index'):
                parent_index = bone_data.parent_index
            else:
                parent_index = -1  # Assume root

            # Get bind pose matrix
            if hasattr(bone_data, 'bind_pose_matrix'):
                bind_pose = np.array(bone_data.bind_pose_matrix, dtype=np.float32).reshape(4, 4)
            else:
                bind_pose = np.identity(4, dtype=np.float32)

            # Create bone
            bone = Bone(
                index=i,
                name=name,
                parent_index=parent_index,
                bind_pose_matrix=bind_pose
            )

            self.bones.append(bone)
            self.bone_map[name] = i

        print(f"Built skeleton with {len(self.bones)} bones")

    def apply_pose(self, pose: Dict[str, tuple]):
        """
        Apply animation pose to skeleton.

        Args:
            pose: Dictionary mapping bone_name -> (position, rotation, scale)
        """
        # Update bone local transforms from pose
        for bone_name, transform in pose.items():
            if bone_name in self.bone_map:
                bone_index = self.bone_map[bone_name]
                bone = self.bones[bone_index]

                position, rotation, scale = transform

                # Compose local matrix from TRS
                bone.local_matrix = compose_transform(
                    np.array(position, dtype=np.float32),
                    np.array(rotation, dtype=np.float32),
                    np.array(scale, dtype=np.float32)
                )

        # Compute world transforms
        self._compute_world_transforms()

        # Compute skinning matrices
        self._compute_skinning_matrices()

    def _compute_world_transforms(self):
        """
        Compute world transforms for all bones (traverse hierarchy).
        """
        for bone in self.bones:
            if bone.parent_index == -1:
                # Root bone: world = local
                bone.world_matrix = bone.local_matrix.copy()
            else:
                # Child bone: world = parent_world * local
                parent = self.bones[bone.parent_index]
                bone.world_matrix = parent.world_matrix @ bone.local_matrix

    def _compute_skinning_matrices(self):
        """
        Compute final skinning matrices for rendering.
        """
        for bone in self.bones:
            # Skinning matrix = world_transform * inverse_bind_pose
            inv_bind_pose = np.linalg.inv(bone.bind_pose_matrix)
            bone.skinning_matrix = bone.world_matrix @ inv_bind_pose

    def get_skinning_matrices(self) -> np.ndarray:
        """
        Get array of skinning matrices for shader.

        Returns:
            Array of 4x4 matrices, shape (num_bones, 4, 4)
        """
        if not self.bones:
            return np.array([np.identity(4, dtype=np.float32)])

        matrices = np.array([bone.skinning_matrix for bone in self.bones], dtype=np.float32)
        return matrices

    def get_bone_world_positions(self) -> Dict[str, np.ndarray]:
        """
        Get world positions of all bones (for debug rendering).

        Returns:
            Dictionary mapping bone_name -> world_position
        """
        positions = {}
        for bone in self.bones:
            # Extract position from world matrix
            position = bone.world_matrix[0:3, 3]
            positions[bone.name] = position
        return positions

    def reset(self):
        """Reset all bones to bind pose."""
        for bone in self.bones:
            bone.local_matrix = np.identity(4, dtype=np.float32)
            bone.world_matrix = bone.bind_pose_matrix.copy()
            bone.skinning_matrix = np.identity(4, dtype=np.float32)
