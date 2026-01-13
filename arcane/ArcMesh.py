from collections import OrderedDict

from arcane.util import ResStream


class ArcMesh:
    def load_binary(self, stream: ResStream):
        self.mesh_name = stream.read_string()
        self.mesh_distance = stream.read_float()
        self.mesh_start_point = stream.read_tuple()
        self.mesh_end_point = stream.read_tuple()
        self.mesh_ref_point = stream.read_tuple()
        self.mesh_use_face_normals = stream.read_bool()
        self.mesh_use_tangent_basis = stream.read_bool()
        num_vertices = stream.read_dword()
        self.mesh_vertices = [stream.read_tuple() for _ in range(num_vertices)]
        num_other_vertices = stream.read_dword()
        self.mesh_normals = [stream.read_tuple() for _ in range(num_other_vertices)]
        num = stream.read_dword()
        self.mesh_uv = [
            [
                stream.read_float(),
                stream.read_float(),
            ] for _ in range(num)
        ]
        if self.mesh_use_tangent_basis:
            num_tangent_vertices = stream.read_dword()
            self.mesh_tanget_vertices = [stream.read_tuple() for _ in range(num_tangent_vertices)]
        num_indicies = stream.read_dword()
        self.mesh_indices = [stream.read_word() for _ in range(num_indicies)]
        num = stream.read_dword()
        self.mesh_extra_indices = [
            [
                stream.read_dword(),
                stream.read_dword(),
                [stream.read_word() for _ in range(stream.read_dword())],
            ] for _ in range(num)
        ]

    def save_binary(self, stream: ResStream):
        stream.write_string(self.mesh_name)
        stream.write_float(self.mesh_distance)
        stream.write_tuple(self.mesh_start_point)
        stream.write_tuple(self.mesh_end_point)
        stream.write_tuple(self.mesh_ref_point)
        stream.write_bool(self.mesh_use_face_normals)
        stream.write_bool(self.mesh_use_tangent_basis)
        stream.write_dword(len(self.mesh_vertices))
        for i in range(len(self.mesh_vertices)):
            stream.write_tuple(self.mesh_vertices[i])
        stream.write_dword(len(self.mesh_normals))
        for i in range(len(self.mesh_normals)):
            stream.write_tuple(self.mesh_normals[i])
        stream.write_dword(len(self.mesh_uv))
        for i in range(len(self.mesh_uv)):
            stream.write_float(self.mesh_uv[i][0])
            stream.write_float(self.mesh_uv[i][1])
        if self.mesh_use_tangent_basis:
            stream.write_dword(len(self.mesh_tanget_vertices))
            for i in range(len(self.mesh_tanget_vertices)):
                stream.write_tuple(self.mesh_tanget_vertices[i])
        stream.write_dword(len(self.mesh_indices))
        for i in range(len(self.mesh_indices)):
            stream.write_word(self.mesh_indices[i])
        stream.write_dword(len(self.mesh_extra_indices))
        for i in range(len(self.mesh_extra_indices)):
            stream.write_dword(self.mesh_extra_indices[i][0])
            stream.write_dword(self.mesh_extra_indices[i][1])
            stream.write_dword(len(self.mesh_extra_indices[i][2]))
            for j in range(len(self.mesh_extra_indices[i][2])):
                stream.write_word(self.mesh_extra_indices[i][2][j])

    def load_json(self, data):
        self.mesh_name = data['mesh_name']
        self.mesh_distance = data['mesh_distance']
        self.mesh_start_point = data['mesh_start_point']
        self.mesh_end_point = data['mesh_end_point']
        self.mesh_ref_point = data['mesh_ref_point']
        self.mesh_use_face_normals = data['mesh_use_face_normals']
        self.mesh_use_tangent_basis = data['mesh_use_tangent_basis']
        self.mesh_vertices = data['mesh_vertices']
        self.mesh_normals = data['mesh_normals']
        self.mesh_uv = data['mesh_uv']
        if self.mesh_use_tangent_basis:
            self.mesh_tanget_vertices = data['mesh_tanget_vertices']
        self.mesh_indices = data['mesh_indices']
        self.mesh_extra_indices = data['mesh_extra_indices']
        # Optional skeletal skinning data (added 07-10-25)
        self.mesh_bone_indices = data.get('mesh_bone_indices', [])
        self.mesh_bone_weights = data.get('mesh_bone_weights', [])

    def save_json(self):
        data = OrderedDict()
        data['mesh_name'] = self.mesh_name
        data['mesh_distance'] = self.mesh_distance
        data['mesh_start_point'] = self.mesh_start_point
        data['mesh_end_point'] = self.mesh_end_point
        data['mesh_ref_point'] = self.mesh_ref_point
        data['mesh_use_face_normals'] = self.mesh_use_face_normals
        data['mesh_use_tangent_basis'] = self.mesh_use_tangent_basis
        data['mesh_vertices'] = self.mesh_vertices
        data['mesh_normals'] = self.mesh_normals
        data['mesh_uv'] = self.mesh_uv
        if self.mesh_use_tangent_basis:
            data['mesh_tanget_vertices'] = self.mesh_tanget_vertices
        data['mesh_indices'] = self.mesh_indices
        data['mesh_extra_indices'] = self.mesh_extra_indices
        # Preserve optional bone skinning arrays when present
        data['mesh_bone_indices'] = getattr(self, 'mesh_bone_indices', [])
        data['mesh_bone_weights'] = getattr(self, 'mesh_bone_weights', [])
        return data
