"""
OBJ Exporter - Export meshes to Wavefront OBJ format.
"""

import numpy as np
from pathlib import Path
from typing import Optional


class OBJExporter:
    """
    Exports meshes to Wavefront OBJ format with optional MTL material file.
    """

    @staticmethod
    def export_mesh(mesh, output_path: str, texture_path: Optional[str] = None, mesh_name: str = "mesh"):
        """
        Export ArcMesh to OBJ format.

        Args:
            mesh: ArcMesh object
            output_path: Path to output .obj file
            texture_path: Optional path to texture image file
            mesh_name: Name for the mesh (used in OBJ file)

        Returns:
            True if export succeeded, False otherwise
        """
        try:
            output_path = Path(output_path)
            obj_path = output_path.with_suffix('.obj')
            mtl_path = output_path.with_suffix('.mtl')

            # Get mesh data
            vertices = np.array(mesh.mesh_vertices, dtype=np.float32)
            normals = np.array(mesh.mesh_normals, dtype=np.float32) if mesh.mesh_normals else None
            uvs = np.array(mesh.mesh_uv, dtype=np.float32) if mesh.mesh_uv else None
            indices = np.array(mesh.mesh_indices, dtype=np.uint32)

            # Validate data
            if len(vertices) == 0 or len(indices) == 0:
                print(f"Error: Empty mesh data (vertices={len(vertices)}, indices={len(indices)})")
                return False

            # Write OBJ file
            with open(obj_path, 'w') as f:
                # Header
                f.write("# Exported from Shadowbane Asset Viewer\n")
                f.write(f"# Mesh: {mesh_name}\n")
                f.write(f"# Vertices: {len(vertices)}\n")
                f.write(f"# Faces: {len(indices) // 3}\n")
                f.write("\n")

                # Reference MTL file if texture is provided
                if texture_path:
                    f.write(f"mtllib {mtl_path.name}\n")
                    f.write(f"usemtl {mesh_name}_material\n")
                    f.write("\n")

                # Write vertices
                f.write("# Vertices\n")
                for v in vertices:
                    f.write(f"v {v[0]:.6f} {v[1]:.6f} {v[2]:.6f}\n")
                f.write("\n")

                # Write normals
                if normals is not None and len(normals) > 0:
                    f.write("# Normals\n")
                    for n in normals:
                        f.write(f"vn {n[0]:.6f} {n[1]:.6f} {n[2]:.6f}\n")
                    f.write("\n")

                # Write texture coordinates
                if uvs is not None and len(uvs) > 0:
                    f.write("# Texture Coordinates\n")
                    for uv in uvs:
                        f.write(f"vt {uv[0]:.6f} {uv[1]:.6f}\n")
                    f.write("\n")

                # Write faces
                f.write("# Faces\n")
                has_normals = normals is not None and len(normals) > 0
                has_uvs = uvs is not None and len(uvs) > 0

                for i in range(0, len(indices), 3):
                    # OBJ indices are 1-based
                    v1 = indices[i] + 1
                    v2 = indices[i + 1] + 1
                    v3 = indices[i + 2] + 1

                    if has_uvs and has_normals:
                        # Format: f v1/vt1/vn1 v2/vt2/vn2 v3/vt3/vn3
                        f.write(f"f {v1}/{v1}/{v1} {v2}/{v2}/{v2} {v3}/{v3}/{v3}\n")
                    elif has_uvs:
                        # Format: f v1/vt1 v2/vt2 v3/vt3
                        f.write(f"f {v1}/{v1} {v2}/{v2} {v3}/{v3}\n")
                    elif has_normals:
                        # Format: f v1//vn1 v2//vn2 v3//vn3
                        f.write(f"f {v1}//{v1} {v2}//{v2} {v3}//{v3}\n")
                    else:
                        # Format: f v1 v2 v3
                        f.write(f"f {v1} {v2} {v3}\n")

            # Write MTL file if texture is provided
            if texture_path:
                texture_path = Path(texture_path)
                with open(mtl_path, 'w') as f:
                    f.write("# Exported from Shadowbane Asset Viewer\n")
                    f.write(f"newmtl {mesh_name}_material\n")
                    f.write("Ka 1.0 1.0 1.0\n")  # Ambient color
                    f.write("Kd 1.0 1.0 1.0\n")  # Diffuse color
                    f.write("Ks 0.3 0.3 0.3\n")  # Specular color
                    f.write("Ns 32.0\n")         # Specular exponent
                    f.write("d 1.0\n")           # Transparency (opaque)
                    f.write("illum 2\n")         # Illumination model (specular)

                    # Texture map (use relative path if in same directory)
                    if texture_path.parent == mtl_path.parent:
                        f.write(f"map_Kd {texture_path.name}\n")
                    else:
                        f.write(f"map_Kd {texture_path}\n")

            print(f"✓ Exported OBJ to {obj_path}")
            if texture_path:
                print(f"✓ Created MTL file at {mtl_path}")

            return True

        except Exception as e:
            print(f"✗ OBJ export failed: {e}")
            import traceback
            traceback.print_exc()
            return False

    @staticmethod
    def export_current_pose(mesh, skeletal_animator, output_path: str,
                           texture_path: Optional[str] = None, mesh_name: str = "mesh"):
        """
        Export mesh with current animation pose applied (baked skinning).

        Args:
            mesh: ArcMesh object
            skeletal_animator: SkeletalAnimator with current pose applied
            output_path: Path to output .obj file
            texture_path: Optional path to texture image file
            mesh_name: Name for the mesh

        Returns:
            True if export succeeded, False otherwise
        """
        try:
            # Get original mesh data
            vertices = np.array(mesh.mesh_vertices, dtype=np.float32)
            normals = np.array(mesh.mesh_normals, dtype=np.float32) if mesh.mesh_normals else None
            uvs = np.array(mesh.mesh_uv, dtype=np.float32) if mesh.mesh_uv else None
            indices = np.array(mesh.mesh_indices, dtype=np.uint32)

            # Get bone data
            has_skinning = hasattr(mesh, 'mesh_bone_indices') and mesh.mesh_bone_indices

            if has_skinning and skeletal_animator:
                bone_indices = np.array(mesh.mesh_bone_indices, dtype=np.int32)
                bone_weights = np.array(mesh.mesh_bone_weights, dtype=np.float32)
                bone_matrices = skeletal_animator.get_skinning_matrices()

                # Apply skinning to vertices
                skinned_vertices = np.zeros_like(vertices)
                skinned_normals = np.zeros_like(normals) if normals is not None else None

                for i in range(len(vertices)):
                    # Transform vertex
                    skinned_pos = np.zeros(4, dtype=np.float32)
                    skinned_pos[3] = 1.0

                    for j in range(4):  # Up to 4 bones per vertex
                        bone_idx = bone_indices[i][j]
                        weight = bone_weights[i][j]

                        if weight > 0.0 and 0 <= bone_idx < len(bone_matrices):
                            bone_matrix = bone_matrices[bone_idx]
                            vertex_homo = np.append(vertices[i], 1.0)  # Homogeneous coordinates
                            skinned_pos += bone_matrix @ vertex_homo * weight

                    skinned_vertices[i] = skinned_pos[:3]

                    # Transform normal (if available)
                    if normals is not None:
                        skinned_norm = np.zeros(3, dtype=np.float32)
                        for j in range(4):
                            bone_idx = bone_indices[i][j]
                            weight = bone_weights[i][j]

                            if weight > 0.0 and 0 <= bone_idx < len(bone_matrices):
                                bone_matrix = bone_matrices[bone_idx]
                                # Normals use 3x3 rotation part only
                                skinned_norm += (bone_matrix[:3, :3] @ normals[i]) * weight

                        # Normalize
                        norm_length = np.linalg.norm(skinned_norm)
                        if norm_length > 0:
                            skinned_normals[i] = skinned_norm / norm_length

                # Replace vertices and normals with skinned versions
                vertices = skinned_vertices
                normals = skinned_normals

            # Create a temporary mesh-like object with skinned data
            class SkinnedMesh:
                def __init__(self, verts, norms, uvs, inds):
                    self.mesh_vertices = verts.tolist()
                    self.mesh_normals = norms.tolist() if norms is not None else []
                    self.mesh_uv = uvs.tolist() if uvs is not None else []
                    self.mesh_indices = inds.tolist()

            skinned_mesh = SkinnedMesh(vertices, normals, uvs, indices)

            # Export using standard OBJ export
            return OBJExporter.export_mesh(skinned_mesh, output_path, texture_path, mesh_name)

        except Exception as e:
            print(f"✗ Skinned OBJ export failed: {e}")
            import traceback
            traceback.print_exc()
            return False
