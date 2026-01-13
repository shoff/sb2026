"""
Asset Manager - Central registry for loading and caching Shadowbane assets.
"""

import json
import os
from pathlib import Path
from typing import Dict, Optional, List
from PIL import Image

# Import arcane asset classes
import sys
from pathlib import Path as PathLib

# Add parent directory to path for arcane imports
parent_dir = PathLib(__file__).parent.parent.parent
if str(parent_dir) not in sys.path:
    sys.path.insert(0, str(parent_dir))

try:
    from arcane.ArcMesh import ArcMesh
    from arcane.ArcImage import ArcTexture
    from arcane.ArcSkeleton import ArcSkeleton
    from arcane.ArcMotion import ArcMotion
    from arcane.ArcRender import ArcRender
    from arcane.ArcCObject import ArcCObject
except ImportError as e:
    raise ImportError(
        f"Failed to import arcane package. Make sure the 'arcane' package is available in the parent directory ({parent_dir}). "
        f"Original error: {e}"
    )


class AssetManager:
    """
    Manages loading and caching of game assets from arcane_dump/ folders.
    """

    def __init__(self, arcane_dump_path: str):
        """
        Initialize asset manager.

        Args:
            arcane_dump_path: Path to arcane_dump/ directory
        """
        self.arcane_dump_path = Path(arcane_dump_path)

        # Asset caches
        self.meshes: Dict[int, ArcMesh] = {}
        self.textures: Dict[int, ArcTexture] = {}
        self.skeletons: Dict[int, ArcSkeleton] = {}
        self.motions: Dict[int, ArcMotion] = {}
        self.renders: Dict[int, ArcRender] = {}
        self.cobjects: Dict[int, ArcCObject] = {}

        # Image cache for texture files
        self.texture_images: Dict[int, Image.Image] = {}

        # Asset type paths
        self.asset_paths = {
            'mesh': self.arcane_dump_path / 'MESH',
            'texture': self.arcane_dump_path / 'TEXTURE',
            'skeleton': self.arcane_dump_path / 'SKELETON',
            'motion': self.arcane_dump_path / 'MOTION',
            'render': self.arcane_dump_path / 'RENDER',
            'cobject': self.arcane_dump_path / 'COBJECTS',
        }

    def load_mesh(self, asset_id: int) -> Optional[ArcMesh]:
        """
        Load mesh from JSON file.

        Args:
            asset_id: Mesh ID

        Returns:
            ArcMesh object or None if not found
        """
        if asset_id in self.meshes:
            return self.meshes[asset_id]

        json_path = self.asset_paths['mesh'] / f"{asset_id}.json"
        if not json_path.exists():
            print(f"Mesh {asset_id} not found at {json_path}")
            return None

        try:
            with open(json_path, 'r') as f:
                data = json.load(f)

            mesh = ArcMesh()
            mesh.load_json(data)
            self.meshes[asset_id] = mesh
            return mesh
        except Exception as e:
            print(f"Error loading mesh {asset_id}: {e}")
            return None

    def load_texture(self, asset_id: int) -> Optional[ArcTexture]:
        """
        Load texture metadata (not the actual image).

        Args:
            asset_id: Texture ID

        Returns:
            ArcTexture object or None if not found
        """
        if asset_id in self.textures:
            return self.textures[asset_id]

        # Try JSON file first
        json_path = self.asset_paths['texture'] / f"{asset_id}.json"
        if json_path.exists():
            try:
                with open(json_path, 'r') as f:
                    data = json.load(f)

                texture = ArcTexture()
                texture.load_json(data)
                self.textures[asset_id] = texture
                return texture
            except Exception as e:
                print(f"Error loading texture metadata {asset_id}: {e}")

        # If no JSON, return None (we'll just use the JPG directly)
        return None

    def load_texture_image(self, asset_id: int) -> Optional[Image.Image]:
        """
        Load texture image file (JPG).

        Args:
            asset_id: Texture ID

        Returns:
            PIL Image object or None if not found
        """
        if asset_id in self.texture_images:
            return self.texture_images[asset_id]

        jpg_path = self.asset_paths['texture'] / f"{asset_id}.jpg"
        if not jpg_path.exists():
            print(f"Texture image {asset_id} not found at {jpg_path}")
            return None

        try:
            img = Image.open(jpg_path)
            # Note: Transformation (mirror/rotate) will be applied in TextureManager
            self.texture_images[asset_id] = img
            return img
        except Exception as e:
            print(f"Error loading texture image {asset_id}: {e}")
            return None

    def load_skeleton(self, asset_id: int) -> Optional[ArcSkeleton]:
        """
        Load skeleton from JSON file.

        Args:
            asset_id: Skeleton ID

        Returns:
            ArcSkeleton object or None if not found
        """
        if asset_id in self.skeletons:
            return self.skeletons[asset_id]

        json_path = self.asset_paths['skeleton'] / f"{asset_id}.json"
        if not json_path.exists():
            print(f"Skeleton {asset_id} not found at {json_path}")
            return None

        try:
            with open(json_path, 'r') as f:
                data = json.load(f)

            skeleton = ArcSkeleton()
            skeleton.load_json(data)
            self.skeletons[asset_id] = skeleton
            return skeleton
        except Exception as e:
            print(f"Error loading skeleton {asset_id}: {e}")
            return None

    def load_motion(self, asset_id: int) -> Optional[ArcMotion]:
        """
        Load motion/animation from JSON file.

        Args:
            asset_id: Motion ID

        Returns:
            ArcMotion object or None if not found
        """
        if asset_id in self.motions:
            return self.motions[asset_id]

        json_path = self.asset_paths['motion'] / f"{asset_id}.json"
        if not json_path.exists():
            print(f"Motion {asset_id} not found at {json_path}")
            return None

        try:
            with open(json_path, 'r') as f:
                data = json.load(f)

            motion = ArcMotion()
            motion.load_json(data)
            self.motions[asset_id] = motion
            return motion
        except Exception as e:
            print(f"Error loading motion {asset_id}: {e}")
            return None

    def load_render(self, asset_id: int) -> Optional[ArcRender]:
        """
        Load render template from JSON file.

        Args:
            asset_id: Render ID

        Returns:
            ArcRender object or None if not found
        """
        if asset_id in self.renders:
            return self.renders[asset_id]

        json_path = self.asset_paths['render'] / f"{asset_id}.json"
        if not json_path.exists():
            print(f"Render {asset_id} not found at {json_path}")
            return None

        try:
            with open(json_path, 'r') as f:
                data = json.load(f)

            render = ArcRender()
            render.load_json(data)
            self.renders[asset_id] = render
            return render
        except Exception as e:
            print(f"Error loading render {asset_id}: {e}")
            return None

    def load_cobject(self, asset_id: int) -> Optional[ArcCObject]:
        """
        Load CObject from JSON file.

        Args:
            asset_id: CObject ID

        Returns:
            ArcCObject or None if not found
        """
        if asset_id in self.cobjects:
            return self.cobjects[asset_id]

        json_path = self.asset_paths['cobject'] / f"{asset_id}.json"
        if not json_path.exists():
            print(f"CObject {asset_id} not found at {json_path}")
            return None

        try:
            with open(json_path, 'r') as f:
                data = json.load(f)

            cobject = ArcCObject()
            cobject.load_json(data)
            self.cobjects[asset_id] = cobject
            return cobject
        except Exception as e:
            print(f"Error loading CObject {asset_id}: {e}")
            return None

    def list_assets(self, asset_type: str) -> List[int]:
        """
        List all available asset IDs of a given type.

        Args:
            asset_type: Type of asset ('mesh', 'texture', 'skeleton', etc.)

        Returns:
            List of asset IDs
        """
        if asset_type not in self.asset_paths:
            return []

        asset_dir = self.asset_paths[asset_type]
        if not asset_dir.exists():
            return []

        asset_ids = []
        for json_file in asset_dir.glob('*.json'):
            try:
                asset_id = int(json_file.stem)
                asset_ids.append(asset_id)
            except ValueError:
                continue

        return sorted(asset_ids)

    def get_texture_image_path(self, asset_id: int) -> Optional[str]:
        """
        Get the file path to a texture image (JPG).

        Args:
            asset_id: Texture ID

        Returns:
            Path to JPG file as string, or None if not found
        """
        jpg_path = self.asset_paths['texture'] / f"{asset_id}.jpg"
        if jpg_path.exists():
            return str(jpg_path)
        return None

    def clear_cache(self):
        """Clear all cached assets."""
        self.meshes.clear()
        self.textures.clear()
        self.skeletons.clear()
        self.motions.clear()
        self.renders.clear()
        self.cobjects.clear()
        self.texture_images.clear()
