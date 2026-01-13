"""
GLTF Exporter - Export meshes with animations to GLTF 2.0 format.
"""

import numpy as np
from pathlib import Path
from typing import Optional, List, Tuple
import struct
import json


class GLTFExporter:
    """
    Exports meshes with skeletons and animations to GLTF 2.0 format.

    Note: This is a simplified exporter. For production use, consider using
    libraries like pygltflib or trimesh for full GLTF spec compliance.
    """

    @staticmethod
    def export_static_mesh(mesh, output_path: str, texture_path: Optional[str] = None, mesh_name: str = "mesh"):
        """
        Export static mesh to GLTF format.

        Args:
            mesh: ArcMesh object
            output_path: Path to output .gltf file
            texture_path: Optional path to texture image file
            mesh_name: Name for the mesh

        Returns:
            True if export succeeded, False otherwise
        """
        try:
            output_path = Path(output_path)
            gltf_path = output_path.with_suffix('.gltf')
            bin_path = output_path.with_suffix('.bin')

            # Get mesh data
            vertices = np.array(mesh.mesh_vertices, dtype=np.float32)
            normals = np.array(mesh.mesh_normals, dtype=np.float32) if mesh.mesh_normals else np.zeros((len(vertices), 3), dtype=np.float32)
            uvs = np.array(mesh.mesh_uv, dtype=np.float32) if mesh.mesh_uv else np.zeros((len(vertices), 2), dtype=np.float32)
            indices = np.array(mesh.mesh_indices, dtype=np.uint32)

            if len(vertices) == 0 or len(indices) == 0:
                print(f"Error: Empty mesh data")
                return False

            # Calculate bounding box
            min_pos = vertices.min(axis=0).tolist()
            max_pos = vertices.max(axis=0).tolist()

            # Build binary buffer
            buffer_data = bytearray()

            # Helper to add data to buffer and return offset
            def add_to_buffer(data: np.ndarray) -> Tuple[int, int]:
                """Add numpy array to buffer, return (byte_offset, byte_length)"""
                offset = len(buffer_data)
                buffer_data.extend(data.tobytes())
                # Align to 4-byte boundary
                while len(buffer_data) % 4 != 0:
                    buffer_data.append(0)
                return offset, len(data.tobytes())

            # Add mesh data to buffer
            vertices_offset, vertices_length = add_to_buffer(vertices)
            normals_offset, normals_length = add_to_buffer(normals)
            uvs_offset, uvs_length = add_to_buffer(uvs)
            indices_offset, indices_length = add_to_buffer(indices)

            # Write binary buffer
            with open(bin_path, 'wb') as f:
                f.write(buffer_data)

            # Build GLTF JSON structure
            gltf = {
                "asset": {
                    "version": "2.0",
                    "generator": "Shadowbane Asset Viewer"
                },
                "scene": 0,
                "scenes": [
                    {
                        "name": "Scene",
                        "nodes": [0]
                    }
                ],
                "nodes": [
                    {
                        "name": mesh_name,
                        "mesh": 0
                    }
                ],
                "meshes": [
                    {
                        "name": mesh_name,
                        "primitives": [
                            {
                                "attributes": {
                                    "POSITION": 0,
                                    "NORMAL": 1,
                                    "TEXCOORD_0": 2
                                },
                                "indices": 3,
                                "mode": 4  # TRIANGLES
                            }
                        ]
                    }
                ],
                "accessors": [
                    # 0: POSITION
                    {
                        "bufferView": 0,
                        "componentType": 5126,  # FLOAT
                        "count": len(vertices),
                        "type": "VEC3",
                        "min": min_pos,
                        "max": max_pos
                    },
                    # 1: NORMAL
                    {
                        "bufferView": 1,
                        "componentType": 5126,  # FLOAT
                        "count": len(normals),
                        "type": "VEC3"
                    },
                    # 2: TEXCOORD_0
                    {
                        "bufferView": 2,
                        "componentType": 5126,  # FLOAT
                        "count": len(uvs),
                        "type": "VEC2"
                    },
                    # 3: INDICES
                    {
                        "bufferView": 3,
                        "componentType": 5125,  # UNSIGNED_INT
                        "count": len(indices),
                        "type": "SCALAR"
                    }
                ],
                "bufferViews": [
                    # 0: Vertices
                    {
                        "buffer": 0,
                        "byteOffset": vertices_offset,
                        "byteLength": vertices_length,
                        "target": 34962  # ARRAY_BUFFER
                    },
                    # 1: Normals
                    {
                        "buffer": 0,
                        "byteOffset": normals_offset,
                        "byteLength": normals_length,
                        "target": 34962  # ARRAY_BUFFER
                    },
                    # 2: UVs
                    {
                        "buffer": 0,
                        "byteOffset": uvs_offset,
                        "byteLength": uvs_length,
                        "target": 34962  # ARRAY_BUFFER
                    },
                    # 3: Indices
                    {
                        "buffer": 0,
                        "byteOffset": indices_offset,
                        "byteLength": indices_length,
                        "target": 34963  # ELEMENT_ARRAY_BUFFER
                    }
                ],
                "buffers": [
                    {
                        "uri": bin_path.name,
                        "byteLength": len(buffer_data)
                    }
                ]
            }

            # Add material/texture if provided
            if texture_path:
                texture_path = Path(texture_path)
                gltf["images"] = [
                    {
                        "uri": texture_path.name if texture_path.parent == gltf_path.parent else str(texture_path)
                    }
                ]
                gltf["textures"] = [
                    {
                        "source": 0
                    }
                ]
                gltf["materials"] = [
                    {
                        "name": f"{mesh_name}_material",
                        "pbrMetallicRoughness": {
                            "baseColorTexture": {
                                "index": 0
                            },
                            "metallicFactor": 0.0,
                            "roughnessFactor": 0.8
                        }
                    }
                ]
                # Reference material in mesh primitive
                gltf["meshes"][0]["primitives"][0]["material"] = 0

            # Write GLTF JSON
            with open(gltf_path, 'w') as f:
                json.dump(gltf, f, indent=2)

            print(f"✓ Exported GLTF to {gltf_path}")
            print(f"✓ Created binary buffer at {bin_path}")

            return True

        except Exception as e:
            print(f"✗ GLTF export failed: {e}")
            import traceback
            traceback.print_exc()
            return False

    @staticmethod
    def export_animated_mesh(mesh, skeleton, motion, output_path: str,
                           texture_path: Optional[str] = None, mesh_name: str = "mesh"):
        """
        Export mesh with skeleton and animation to GLTF format.

        Args:
            mesh: ArcMesh object
            skeleton: ArcSkeleton object
            motion: ArcMotion object (optional)
            output_path: Path to output .gltf file
            texture_path: Optional path to texture image file
            mesh_name: Name for the mesh

        Returns:
            True if export succeeded, False otherwise
        """
        try:
            print(f"✓ GLTF animated export is a complex feature.")
            print(f"✓ For now, exporting as static mesh.")
            print(f"✓ Full skeletal animation export coming soon!")

            # For now, export as static mesh
            # Full implementation would require:
            # 1. Exporting skeleton hierarchy as GLTF nodes
            # 2. Creating skin with inverse bind matrices
            # 3. Adding bone indices/weights to mesh
            # 4. Creating animation samplers and channels for each bone
            # 5. Handling quaternion rotations and translations

            return GLTFExporter.export_static_mesh(mesh, output_path, texture_path, mesh_name)

        except Exception as e:
            print(f"✗ GLTF animated export failed: {e}")
            import traceback
            traceback.print_exc()
            return False
