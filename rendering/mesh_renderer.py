"""
Mesh Renderer - Converts ArcMesh to OpenGL buffers and renders meshes.
"""

from OpenGL.GL import *
import numpy as np
from typing import Optional, Tuple
import os
from dataclasses import dataclass

from rendering.runtime_render_payload import RuntimeImmediateSubmission


@dataclass
class GPUMesh:
    """
    GPU representation of a mesh.
    """
    vao: int  # Vertex Array Object
    vbo_positions: int  # Vertex Buffer Object for positions
    vbo_normals: int  # Vertex Buffer Object for normals
    vbo_uvs: int  # Vertex Buffer Object for UVs
    vbo_bone_indices: int  # Vertex Buffer Object for bone indices
    vbo_bone_weights: int  # Vertex Buffer Object for bone weights
    ebo: int  # Element Buffer Object (indices)
    vertex_count: int
    index_count: int
    bounds_min: np.ndarray
    bounds_max: np.ndarray
    has_uvs: bool
    has_skinning: bool  # Whether mesh has bone skinning data


@dataclass(frozen=True)
class ImmediateRenderRequest:
    submission: RuntimeImmediateSubmission
    shader_program: object
    texture_id: Optional[int] = None


class MeshRenderer:
    """
    Renders meshes using OpenGL.
    """

    def __init__(self):
        self.meshes = {}  # asset_id -> GPUMesh

    def upload_mesh(self, mesh, asset_id: int) -> Optional[GPUMesh]:
        """
        Upload ArcMesh to GPU.

        Args:
            mesh: ArcMesh object
            asset_id: Mesh asset ID

        Returns:
            GPUMesh or None on error
        """
        # Check cache
        if asset_id in self.meshes:
            return self.meshes[asset_id]

        # Convert mesh data to numpy arrays
        vertices = np.array(mesh.mesh_vertices, dtype=np.float32)
        normals = np.array(mesh.mesh_normals, dtype=np.float32) if mesh.mesh_normals else np.zeros((len(vertices), 3), dtype=np.float32)
        uvs = np.array(mesh.mesh_uv, dtype=np.float32) if mesh.mesh_uv else np.zeros((len(vertices), 2), dtype=np.float32)
        indices = np.array(mesh.mesh_indices, dtype=np.uint32)

        # Check for valid data
        if len(vertices) == 0 or len(indices) == 0:
            print(f"Invalid mesh data for {asset_id}: vertices={len(vertices)}, indices={len(indices)}")
            return None

        # Calculate bounding box
        bounds_min = np.min(vertices, axis=0)
        bounds_max = np.max(vertices, axis=0)

        # Create VAO
        vao = glGenVertexArrays(1)
        glBindVertexArray(vao)

        # Upload positions
        vbo_positions = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, vbo_positions)
        glBufferData(GL_ARRAY_BUFFER, vertices.nbytes, vertices, GL_STATIC_DRAW)
        glEnableVertexAttribArray(0)
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, None)

        # Upload normals
        vbo_normals = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, vbo_normals)
        glBufferData(GL_ARRAY_BUFFER, normals.nbytes, normals, GL_STATIC_DRAW)
        glEnableVertexAttribArray(1)
        glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 0, None)

        # Upload UVs
        vbo_uvs = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, vbo_uvs)
        glBufferData(GL_ARRAY_BUFFER, uvs.nbytes, uvs, GL_STATIC_DRAW)
        glEnableVertexAttribArray(2)
        glVertexAttribPointer(2, 2, GL_FLOAT, GL_FALSE, 0, None)

        # Upload bone indices and weights (if available)
        has_skinning = hasattr(mesh, 'mesh_bone_indices') and mesh.mesh_bone_indices
        vbo_bone_indices = 0
        vbo_bone_weights = 0

        if has_skinning:
            bone_indices = np.array(mesh.mesh_bone_indices, dtype=np.float32)
            bone_weights = np.array(mesh.mesh_bone_weights, dtype=np.float32)

            # Bone indices
            vbo_bone_indices = glGenBuffers(1)
            glBindBuffer(GL_ARRAY_BUFFER, vbo_bone_indices)
            glBufferData(GL_ARRAY_BUFFER, bone_indices.nbytes, bone_indices, GL_STATIC_DRAW)
            glEnableVertexAttribArray(3)
            glVertexAttribPointer(3, 4, GL_FLOAT, GL_FALSE, 0, None)

            # Bone weights
            vbo_bone_weights = glGenBuffers(1)
            glBindBuffer(GL_ARRAY_BUFFER, vbo_bone_weights)
            glBufferData(GL_ARRAY_BUFFER, bone_weights.nbytes, bone_weights, GL_STATIC_DRAW)
            glEnableVertexAttribArray(4)
            glVertexAttribPointer(4, 4, GL_FLOAT, GL_FALSE, 0, None)
        else:
            # Default bone data (for static meshes) - bind to bone 0 with weight 1.0
            default_indices = np.zeros((len(vertices), 4), dtype=np.float32)
            default_weights = np.zeros((len(vertices), 4), dtype=np.float32)
            default_weights[:, 0] = 1.0  # Full weight on bone 0

            vbo_bone_indices = glGenBuffers(1)
            glBindBuffer(GL_ARRAY_BUFFER, vbo_bone_indices)
            glBufferData(GL_ARRAY_BUFFER, default_indices.nbytes, default_indices, GL_STATIC_DRAW)
            glEnableVertexAttribArray(3)
            glVertexAttribPointer(3, 4, GL_FLOAT, GL_FALSE, 0, None)

            vbo_bone_weights = glGenBuffers(1)
            glBindBuffer(GL_ARRAY_BUFFER, vbo_bone_weights)
            glBufferData(GL_ARRAY_BUFFER, default_weights.nbytes, default_weights, GL_STATIC_DRAW)
            glEnableVertexAttribArray(4)
            glVertexAttribPointer(4, 4, GL_FLOAT, GL_FALSE, 0, None)

        # Upload indices
        ebo = glGenBuffers(1)
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, ebo)
        glBufferData(GL_ELEMENT_ARRAY_BUFFER, indices.nbytes, indices, GL_STATIC_DRAW)

        # Unbind
        glBindVertexArray(0)
        glBindBuffer(GL_ARRAY_BUFFER, 0)
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, 0)

        # Create GPU mesh
        gpu_mesh = GPUMesh(
            vao=vao,
            vbo_positions=vbo_positions,
            vbo_normals=vbo_normals,
            vbo_uvs=vbo_uvs,
            vbo_bone_indices=vbo_bone_indices,
            vbo_bone_weights=vbo_bone_weights,
            ebo=ebo,
            vertex_count=len(vertices),
            index_count=len(indices),
            bounds_min=bounds_min,
            bounds_max=bounds_max,
            has_uvs=(len(uvs) > 0 and np.any(uvs != 0)),
            has_skinning=has_skinning
        )

        # Cache
        self.meshes[asset_id] = gpu_mesh

        print(f"Uploaded mesh {asset_id}: {gpu_mesh.vertex_count} vertices, {gpu_mesh.index_count} indices")
        return gpu_mesh

    def render_mesh(self, gpu_mesh: GPUMesh, shader_program, texture_id: Optional[int] = None, bone_matrices: Optional[np.ndarray] = None):
        """
        Render a mesh.

        Args:
            gpu_mesh: GPUMesh to render
            shader_program: ShaderProgram to use
            texture_id: Optional texture ID to bind
            bone_matrices: Optional array of bone matrices for skinning
        """
        if not gpu_mesh:
            return

        # Bind shader
        shader_program.use()

        # Bind texture if provided
        has_texture = texture_id is not None
        shader_program.set_bool("uHasTexture", has_texture)

        if has_texture:
            glActiveTexture(GL_TEXTURE0)
            glBindTexture(GL_TEXTURE_2D, texture_id)
            shader_program.set_int("uTexture", 0)

        # Set skinning uniforms
        use_skinning = bone_matrices is not None and gpu_mesh.has_skinning
        shader_program.set_bool("uUseSkinning", use_skinning)

        if use_skinning and bone_matrices is not None:
            # Upload bone matrices
            for i, matrix in enumerate(bone_matrices):
                if i >= 128:  # Shader limit
                    break
                shader_program.set_mat4(f"uBoneMatrices[{i}]", matrix)

        # Bind VAO and draw
        glBindVertexArray(gpu_mesh.vao)
        glDrawElements(GL_TRIANGLES, gpu_mesh.index_count, GL_UNSIGNED_INT, None)
        glBindVertexArray(0)

        # Unbind texture
        if has_texture:
            glBindTexture(GL_TEXTURE_2D, 0)

    def render_immediate_payload(self, request: ImmediateRenderRequest) -> None:
        if request.submission is None:
            return

        trace_enabled = os.getenv("RUNTIME_RENDER_TRACE", "0") == "1"
        no_draw = os.getenv("RUNTIME_RENDER_NO_DRAW", "0") == "1"

        positions = request.submission.positions.astype(np.float32, copy=False)
        normals = request.submission.normals.astype(np.float32, copy=False)
        uvs = request.submission.uvs.astype(np.float32, copy=False)

        if trace_enabled:
            sample_count = min(3, request.submission.vertex_count)
            sample_positions = positions[:sample_count].tolist()
            print(
                "runtime_submit|verts=%d|prim=GL_TRIANGLE_STRIP|stride_pos=12|stride_norm=12|stride_uv=8|pos_ptr=0x%08x|norm_ptr=0x%08x|uv_ptr=0x%08x"
                % (
                    request.submission.vertex_count,
                    request.submission.payload.positions_ptr,
                    request.submission.payload.normals_ptr,
                    request.submission.payload.uvs_ptr,
                )
            )
            print("runtime_submit_positions|count=%d|values=%s" % (sample_count, sample_positions))

        if no_draw:
            return

        vao = glGenVertexArrays(1)
        glBindVertexArray(vao)

        vbo_positions = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, vbo_positions)
        glBufferData(GL_ARRAY_BUFFER, positions.nbytes, positions, GL_STATIC_DRAW)
        glEnableVertexAttribArray(0)
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, None)

        vbo_normals = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, vbo_normals)
        glBufferData(GL_ARRAY_BUFFER, normals.nbytes, normals, GL_STATIC_DRAW)
        glEnableVertexAttribArray(1)
        glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 0, None)

        vbo_uvs = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, vbo_uvs)
        glBufferData(GL_ARRAY_BUFFER, uvs.nbytes, uvs, GL_STATIC_DRAW)
        glEnableVertexAttribArray(2)
        glVertexAttribPointer(2, 2, GL_FLOAT, GL_FALSE, 0, None)

        request.shader_program.use()
        has_texture = request.texture_id is not None
        request.shader_program.set_bool("uHasTexture", has_texture)
        request.shader_program.set_bool("uUseSkinning", False)
        if has_texture:
            glActiveTexture(GL_TEXTURE0)
            glBindTexture(GL_TEXTURE_2D, request.texture_id)
            request.shader_program.set_int("uTexture", 0)

        glDrawArrays(GL_TRIANGLE_STRIP, 0, request.submission.vertex_count)

        glBindVertexArray(0)
        glBindBuffer(GL_ARRAY_BUFFER, 0)
        if has_texture:
            glBindTexture(GL_TEXTURE_2D, 0)

        glDeleteBuffers(1, [vbo_positions])
        glDeleteBuffers(1, [vbo_normals])
        glDeleteBuffers(1, [vbo_uvs])
        glDeleteVertexArrays(1, [vao])

    def get_mesh_bounds(self, asset_id: int) -> Optional[Tuple[np.ndarray, np.ndarray]]:
        """
        Get mesh bounding box.

        Args:
            asset_id: Mesh asset ID

        Returns:
            Tuple of (bounds_min, bounds_max) or None
        """
        gpu_mesh = self.meshes.get(asset_id)
        if gpu_mesh:
            return (gpu_mesh.bounds_min, gpu_mesh.bounds_max)
        return None

    def cleanup(self):
        """Delete all GPU meshes."""
        for gpu_mesh in self.meshes.values():
            glDeleteVertexArrays(1, [gpu_mesh.vao])
            glDeleteBuffers(1, [gpu_mesh.vbo_positions])
            glDeleteBuffers(1, [gpu_mesh.vbo_normals])
            glDeleteBuffers(1, [gpu_mesh.vbo_uvs])
            glDeleteBuffers(1, [gpu_mesh.vbo_bone_indices])
            glDeleteBuffers(1, [gpu_mesh.vbo_bone_weights])
            glDeleteBuffers(1, [gpu_mesh.ebo])
        self.meshes.clear()
