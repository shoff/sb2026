"""
Texture Manager - Loads and manages OpenGL textures.
"""

from OpenGL.GL import *
from PIL import Image, ImageOps
import numpy as np
from typing import Dict, Optional


class TextureManager:
    """
    Manages loading and caching of OpenGL textures.
    """

    def __init__(self, asset_manager):
        """
        Initialize texture manager.

        Args:
            asset_manager: AssetManager instance for loading texture images
        """
        self.asset_manager = asset_manager
        self.textures: Dict[int, int] = {}  # asset_id -> OpenGL texture ID
        self.default_texture: Optional[int] = None

    def load_texture(self, asset_id: int) -> Optional[int]:
        """
        Load texture from asset and create OpenGL texture.

        Args:
            asset_id: Texture asset ID

        Returns:
            OpenGL texture ID or None on error
        """
        # Check cache
        if asset_id in self.textures:
            return self.textures[asset_id]

        # Load image from asset manager
        img = self.asset_manager.load_texture_image(asset_id)
        if not img:
            print(f"Failed to load texture image {asset_id}")
            return self.get_default_texture()

        # Apply Shadowbane texture transformation (mirror + rotate 180°)
        img = ImageOps.mirror(img.rotate(180))

        # Convert to RGB if needed
        if img.mode != 'RGB' and img.mode != 'RGBA':
            img = img.convert('RGB')

        # Get image data
        img_data = np.array(img, dtype=np.uint8)

        # Determine format
        if img.mode == 'RGBA':
            gl_format = GL_RGBA
        else:
            gl_format = GL_RGB

        # Create OpenGL texture
        texture_id = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, texture_id)

        # Set texture parameters
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR_MIPMAP_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)

        # Upload texture data
        glTexImage2D(
            GL_TEXTURE_2D,
            0,
            gl_format,
            img.width,
            img.height,
            0,
            gl_format,
            GL_UNSIGNED_BYTE,
            img_data
        )

        # Generate mipmaps
        glGenerateMipmap(GL_TEXTURE_2D)

        # Unbind
        glBindTexture(GL_TEXTURE_2D, 0)

        # Cache texture
        self.textures[asset_id] = texture_id

        print(f"Loaded texture {asset_id}: {img.width}x{img.height}, mode={img.mode}")
        return texture_id

    def get_default_texture(self) -> int:
        """
        Get or create default fallback texture (checkerboard pattern).

        Returns:
            OpenGL texture ID
        """
        if self.default_texture:
            return self.default_texture

        # Create 256x256 checkerboard pattern
        size = 256
        checker_size = 32
        texture_data = np.zeros((size, size, 3), dtype=np.uint8)

        for y in range(size):
            for x in range(size):
                checker_x = (x // checker_size) % 2
                checker_y = (y // checker_size) % 2
                if checker_x == checker_y:
                    texture_data[y, x] = [200, 200, 200]  # Light gray
                else:
                    texture_data[y, x] = [100, 100, 100]  # Dark gray

        # Create OpenGL texture
        texture_id = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, texture_id)

        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)

        glTexImage2D(
            GL_TEXTURE_2D,
            0,
            GL_RGB,
            size,
            size,
            0,
            GL_RGB,
            GL_UNSIGNED_BYTE,
            texture_data
        )

        glBindTexture(GL_TEXTURE_2D, 0)

        self.default_texture = texture_id
        print("Created default checkerboard texture")
        return texture_id

    def bind_texture(self, texture_id: int, texture_unit: int = 0):
        """
        Bind texture to a texture unit.

        Args:
            texture_id: OpenGL texture ID
            texture_unit: Texture unit (0-31)
        """
        glActiveTexture(GL_TEXTURE0 + texture_unit)
        glBindTexture(GL_TEXTURE_2D, texture_id)

    def cleanup(self):
        """Delete all OpenGL textures."""
        for texture_id in self.textures.values():
            glDeleteTextures(1, [texture_id])
        self.textures.clear()

        if self.default_texture:
            glDeleteTextures(1, [self.default_texture])
            self.default_texture = None
