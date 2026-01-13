
from collections import OrderedDict

from arcane.util import ResStream

TRACKER_TO_STRING = {
    0: 'NONE',
    1: 'XY',
    2: 'Y',
}
STRING_TO_TRACKER = {value: key for key, value in TRACKER_TO_STRING.items()}

TRANSPARENT_TO_STRING = {
    0: 'NONE',
    1: 'PINK',
    2: 'BLACK',
    3: 'WHITE',
    4: 'SEMI',
    6: 'ALPHA',
}
STRING_TO_TRANSPARENT = {value: key for key, value in TRANSPARENT_TO_STRING.items()}

TEXTURE_TO_STRING = {
    0: 'SINGLE_TEXTURE',
    1: 'COLOR_TEXTURE',
    3: 'ANIMATED_TEXTURE',
}
STRING_TO_TEXTURE = {value: key for key, value in TEXTURE_TO_STRING.items()}

LIGHT_TYPE_TO_STRING = {
    0xb6787258: 'ArcLightPoint',
    0x54e8ff1d: 'ArcLightAffectorAttach',
    0xa73bd9d4: 'ArcLightAffectorFlicker',
}
STRING_TO_LIGHT_TYPE = {value: key for key, value in LIGHT_TYPE_TO_STRING.items()}


class ArcSinglePolyMesh:
    def load_binary(self, stream: ResStream):
        self.polymesh_id = stream.read_qword()
        self.polymesh_decal = stream.read_bool()
        self.polymesh_double_sided = stream.read_bool()

    def save_binary(self, stream: ResStream):
        stream.write_qword(self.polymesh_id)
        stream.write_bool(self.polymesh_decal)
        stream.write_bool(self.polymesh_double_sided)

    def load_json(self, data):
        self.polymesh_id = data['polymesh_id']
        self.polymesh_decal = data['polymesh_decal']
        self.polymesh_double_sided = data['polymesh_double_sided']

    def save_json(self):
        data = OrderedDict()
        data['polymesh_id'] = self.polymesh_id
        data['polymesh_decal'] = self.polymesh_decal
        data['polymesh_double_sided'] = self.polymesh_double_sided
        return data


class ArcMeshSet:
    def load_binary(self, stream: ResStream):
        num = stream.read_dword()
        self.mesh_set = [ArcSinglePolyMesh() for _ in range(num)]
        for mesh in self.mesh_set:
            mesh.load_binary(stream)

    def save_binary(self, stream: ResStream):
        stream.write_dword(len(self.mesh_set))
        for mesh in self.mesh_set:
            mesh.save_binary(stream)

    def load_json(self, data):
        self.mesh_set = []
        for mesh_data in data['mesh_set']:
            mesh = ArcSinglePolyMesh()
            mesh.load_json(mesh_data)
            self.mesh_set.append(mesh)

    def save_json(self):
        data = OrderedDict()
        data['mesh_set'] = []
        for mesh in self.mesh_set:
            data['mesh_set'].append(mesh.save_json())
        return data


class ArcRenderTemplate:
    def load_binary(self, stream: ResStream):
        self.template_object_can_fade = stream.read_bool()
        self.template_tracker = stream.read_dword()
        self.template_illuminated = stream.read_bool()
        self.template_bone_length = stream.read_float()
        self.template_clip_map = stream.read_dword()
        self.template_light_two_side = stream.read_dword()
        self.template_cull_face = stream.read_dword()
        self.template_specular_map = stream.read_qword()
        self.template_shininess = stream.read_float()
        self.template_has_mesh = stream.read_bool()
        if self.template_has_mesh:
            self.template_mesh = ArcMeshSet()
            self.template_mesh.load_binary(stream)

    def save_binary(self, stream: ResStream):
        stream.write_bool(self.template_object_can_fade)
        stream.write_dword(self.template_tracker)
        stream.write_bool(self.template_illuminated)
        stream.write_float(self.template_bone_length)
        stream.write_dword(self.template_clip_map)
        stream.write_dword(self.template_light_two_side)
        stream.write_dword(self.template_cull_face)
        stream.write_qword(self.template_specular_map)
        stream.write_float(self.template_shininess)
        stream.write_bool(self.template_has_mesh)
        if self.template_has_mesh:
            self.template_mesh.save_binary(stream)

    def load_json(self, data):
        self.template_object_can_fade = data['template_object_can_fade']
        self.template_tracker = STRING_TO_TRACKER[data['template_tracker']]
        self.template_illuminated = data['template_illuminated']
        self.template_bone_length = data['template_bone_length']
        self.template_clip_map = data['template_clip_map']
        self.template_light_two_side = data['template_light_two_side']
        self.template_cull_face = data['template_cull_face']
        self.template_specular_map = data['template_specular_map']
        self.template_shininess = data['template_shininess']
        self.template_has_mesh = data['template_has_mesh']
        if self.template_has_mesh:
            self.template_mesh = ArcMeshSet()
            self.template_mesh.load_json(data['template_mesh'])

    def save_json(self):
        data = OrderedDict()
        data['template_object_can_fade'] = self.template_object_can_fade
        data['template_tracker'] = TRACKER_TO_STRING[self.template_tracker]
        data['template_illuminated'] = self.template_illuminated
        data['template_bone_length'] = self.template_bone_length
        data['template_clip_map'] = self.template_clip_map
        data['template_light_two_side'] = self.template_light_two_side
        data['template_cull_face'] = self.template_cull_face
        data['template_specular_map'] = self.template_specular_map
        data['template_shininess'] = self.template_shininess
        data['template_has_mesh'] = self.template_has_mesh
        if self.template_has_mesh:
            data['template_mesh'] = self.template_mesh.save_json()
        return data


class ArcSingleTexture:
    def load_binary(self, stream: ResStream):
        self.texture_id = stream.read_qword()
        self.texture_transparent = stream.read_dword()
        self.texture_compress = stream.read_bool()
        self.texture_normal_map = stream.read_bool()
        self.texture_detail_normal_map = stream.read_bool()
        self.texture_create_mip_maps = stream.read_bool()
        self.texture_x0 = stream.read_string()
        self.texture_x1 = stream.read_string()
        self.texture_x2 = stream.read_dword()
        self.texture_x3 = stream.read_dword()
        self.texture_x4 = stream.read_bool()
        self.texture_wrap = stream.read_bool()

    def save_binary(self, stream: ResStream):
        stream.write_qword(self.texture_id)
        stream.write_dword(self.texture_transparent)
        stream.write_bool(self.texture_compress)
        stream.write_bool(self.texture_normal_map)
        stream.write_bool(self.texture_detail_normal_map)
        stream.write_bool(self.texture_create_mip_maps)
        stream.write_string(self.texture_x0)
        stream.write_string(self.texture_x1)
        stream.write_dword(self.texture_x2)
        stream.write_dword(self.texture_x3)
        stream.write_bool(self.texture_x4)
        stream.write_bool(self.texture_wrap)

    def load_json(self, data):
        self.texture_id = data['texture_id']
        self.texture_transparent = STRING_TO_TRANSPARENT[data['texture_transparent']]
        self.texture_compress = data['texture_compress']
        self.texture_normal_map = data['texture_normal_map']
        self.texture_detail_normal_map = data['texture_detail_normal_map']
        self.texture_create_mip_maps = data['texture_create_mip_maps']
        self.texture_x0 = ''
        self.texture_x1 = ''
        self.texture_x2 = 255
        self.texture_x3 = 0
        self.texture_x4 = False
        self.texture_wrap = data['texture_wrap']

    def save_json(self):
        data = OrderedDict()
        data['texture_id'] = self.texture_id
        data['texture_transparent'] = TRANSPARENT_TO_STRING[self.texture_transparent]
        data['texture_compress'] = self.texture_compress
        data['texture_normal_map'] = self.texture_normal_map
        data['texture_detail_normal_map'] = self.texture_detail_normal_map
        data['texture_create_mip_maps'] = self.texture_create_mip_maps
        data['texture_wrap'] = self.texture_wrap
        return data


class ArcColorTexture(ArcSingleTexture):
    pass


class ArcAnimatedTexture:
    def load_binary(self, stream: ResStream):
        self.animated_texture_id = stream.read_qword()
        self.animated_texture_transparent = stream.read_dword()
        self.animated_texture_compress = stream.read_bool()
        self.animated_texture_normal_map = stream.read_bool()
        self.animated_texture_detail_normal_map = stream.read_bool()
        self.animated_texture_create_mip_maps = stream.read_bool()
        self.animated_texture_frame_timer = stream.read_float()
        self.animated_texture_x0 = stream.read_float()
        self.animated_texture_frame_rand = stream.read_dword()

        num = stream.read_dword()
        self.animated_texture_sets = [ArcTextureSet() for _ in range(num)]
        for texture in self.animated_texture_sets:
            texture.load_binary(stream)

    def save_binary(self, stream: ResStream):
        stream.write_qword(self.animated_texture_id)
        stream.write_dword(self.animated_texture_transparent)
        stream.write_bool(self.animated_texture_compress)
        stream.write_bool(self.animated_texture_normal_map)
        stream.write_bool(self.animated_texture_detail_normal_map)
        stream.write_bool(self.animated_texture_create_mip_maps)
        stream.write_float(self.animated_texture_frame_timer)
        stream.write_float(self.animated_texture_x0)
        stream.write_dword(self.animated_texture_frame_rand)

        stream.write_dword(len(self.animated_texture_sets))
        for texture in self.animated_texture_sets:
            texture.save_binary(stream)

    def load_json(self, data):
        self.animated_texture_id = data['animated_texture_id']
        self.animated_texture_transparent = STRING_TO_TRANSPARENT[data['animated_texture_transparent']]
        self.animated_texture_compress = data['animated_texture_compress']
        self.animated_texture_normal_map = data['animated_texture_normal_map']
        self.animated_texture_detail_normal_map = data['animated_texture_detail_normal_map']
        self.animated_texture_create_mip_maps = data['animated_texture_create_mip_maps']
        self.animated_texture_frame_timer = data['animated_texture_frame_timer']
        self.animated_texture_x0 = 0.0
        self.animated_texture_frame_rand = data['animated_texture_frame_rand']
        self.animated_texture_sets = []
        for texture_data in data['animated_texture_sets']:
            texture = ArcTextureSet()
            texture.load_json(texture_data)
            self.animated_texture_sets.append(texture)

    def save_json(self):
        data = OrderedDict()
        data['animated_texture_id'] = self.animated_texture_id
        data['animated_texture_transparent'] = TRANSPARENT_TO_STRING[self.animated_texture_transparent]
        data['animated_texture_compress'] = self.animated_texture_compress
        data['animated_texture_normal_map'] = self.animated_texture_normal_map
        data['animated_texture_detail_normal_map'] = self.animated_texture_detail_normal_map
        data['animated_texture_create_mip_maps'] = self.animated_texture_create_mip_maps
        data['animated_texture_frame_timer'] = self.animated_texture_frame_timer
        data['animated_texture_frame_rand'] = self.animated_texture_frame_rand
        data['animated_texture_sets'] = []
        for texture in self.animated_texture_sets:
            data['animated_texture_sets'].append(texture.save_json())
        return data


class ArcTextureSet:
    def load_binary(self, stream: ResStream):
        self.texture_type = stream.read_dword()
        if self.texture_type == 0:
            self.texture_data = ArcSingleTexture()
        elif self.texture_type == 1:
            self.texture_data = ArcColorTexture()
        elif self.texture_type == 3:
            self.texture_data = ArcAnimatedTexture()
        self.texture_data.load_binary(stream)

    def save_binary(self, stream: ResStream):
        stream.write_dword(self.texture_type)
        self.texture_data.save_binary(stream)

    def load_json(self, data):
        self.texture_type = STRING_TO_TEXTURE[data['texture_type']]
        if self.texture_type == 0:
            self.texture_data = ArcSingleTexture()
        elif self.texture_type == 1:
            self.texture_data = ArcColorTexture()
        elif self.texture_type == 3:
            self.texture_data = ArcAnimatedTexture()
        self.texture_data.load_json(data['texture_data'])

    def save_json(self):
        data = OrderedDict()
        data['texture_type'] = TEXTURE_TO_STRING[self.texture_type]
        data['texture_data'] = self.texture_data.save_json()
        return data


class ArcLightPoint:
    def load_binary(self, stream: ResStream):
        self.lightpoint_x0 = stream.read_dword()
        self.lightpoint_x1 = stream.read_bool()
        self.lightpoint_shader = stream.read_bool()
        self.lightpoint_update_offscreen = stream.read_bool()
        self.lightpoint_radius = stream.read_float()
        self.lightpoint_position = stream.read_tuple()
        self.lightpoint_diffuse_color = [stream.read_float() for _ in range(4)]
        self.lightpoint_x2 = stream.read_dword()
        self.lightpoint_orientation = [stream.read_float() for _ in range(4)]
        self.lightpoint_cubemap = stream.read_dword()
        self.lightpoint_x3 = stream.read_bool()

    def save_binary(self, stream: ResStream):
        stream.write_dword(self.lightpoint_x0)
        stream.write_bool(self.lightpoint_x1)
        stream.write_bool(self.lightpoint_shader)
        stream.write_bool(self.lightpoint_update_offscreen)
        stream.write_float(self.lightpoint_radius)
        stream.write_tuple(self.lightpoint_position)
        for i in range(4):
            stream.write_float(self.lightpoint_diffuse_color[i])
        stream.write_dword(self.lightpoint_x2)
        for i in range(4):
            stream.write_float(self.lightpoint_orientation[i])
        stream.write_dword(self.lightpoint_cubemap)
        stream.write_bool(self.lightpoint_x3)

    def load_json(self, data):
        self.lightpoint_x0 = 1
        self.lightpoint_x1 = True
        self.lightpoint_shader = data['lightpoint_shader']
        self.lightpoint_update_offscreen = data['lightpoint_update_offscreen']
        self.lightpoint_radius = data['lightpoint_radius']
        self.lightpoint_position = data['lightpoint_position']
        self.lightpoint_diffuse_color = data['lightpoint_diffuse_color']
        self.lightpoint_x2 = 1
        self.lightpoint_orientation = data['lightpoint_orientation']
        self.lightpoint_cubemap = data['lightpoint_cubemap']
        self.lightpoint_x3 = False

    def save_json(self):
        data = OrderedDict()
        data['lightpoint_shader'] = self.lightpoint_shader
        data['lightpoint_update_offscreen'] = self.lightpoint_update_offscreen
        data['lightpoint_radius'] = self.lightpoint_radius
        data['lightpoint_position'] = self.lightpoint_position
        data['lightpoint_diffuse_color'] = self.lightpoint_diffuse_color
        data['lightpoint_orientation'] = self.lightpoint_orientation
        data['lightpoint_cubemap'] = self.lightpoint_cubemap
        return data


class ArcLightAffectorAttach:
    def load_binary(self, stream: ResStream):
        self.attach_x0 = stream.read_dword()
        self.attach_offset = stream.read_tuple()

    def save_binary(self, stream: ResStream):
        stream.write_dword(self.attach_x0)
        stream.write_tuple(self.attach_offset)

    def load_json(self, data):
        self.attach_x0 = 1
        self.attach_offset = data['attach_offset']

    def save_json(self):
        data = OrderedDict()
        data['attach_offset'] = self.attach_offset
        return data


class ArcLightAffectorFlicker:
    def load_binary(self, stream: ResStream):
        self.flicker_x0 = stream.read_dword()
        self.flicker_avg_period = stream.read_float()
        self.flicker_std_dev_radius = stream.read_float()
        self.flicker_std_dev_period = stream.read_float()
        self.flicker_falloff = stream.read_float()

    def save_binary(self, stream: ResStream):
        stream.write_dword(self.flicker_x0)
        stream.write_float(self.flicker_avg_period)
        stream.write_float(self.flicker_std_dev_radius)
        stream.write_float(self.flicker_std_dev_period)
        stream.write_float(self.flicker_falloff)

    def load_json(self, data):
        self.flicker_x0 = 1
        self.flicker_avg_period = data['flicker_avg_period']
        self.flicker_std_dev_radius = data['flicker_std_dev_radius']
        self.flicker_std_dev_period = data['flicker_std_dev_period']
        self.flicker_falloff = data['flicker_falloff']

    def save_json(self):
        data = OrderedDict()
        data['flicker_avg_period'] = self.flicker_avg_period
        data['flicker_std_dev_radius'] = self.flicker_std_dev_radius
        data['flicker_std_dev_period'] = self.flicker_std_dev_period
        data['flicker_falloff'] = self.flicker_falloff
        return data


class ArcLightAffectors:
    def load_binary(self, stream: ResStream):
        self.light_affector_type = stream.read_dword()

        if self.light_affector_type == 0x54e8ff1d:
            self.light_affector_data = ArcLightAffectorAttach()
        elif self.light_affector_type == 0xa73bd9d4:
            self.light_affector_data = ArcLightAffectorFlicker()
        self.light_affector_data.load_binary(stream)

        self.light_affector_0xdaed = stream.read_dword()

    def save_binary(self, stream: ResStream):
        stream.write_dword(self.light_affector_type)
        self.light_affector_data.save_binary(stream)
        stream.write_dword(self.light_affector_0xdaed)

    def load_json(self, data):
        self.light_affector_type = STRING_TO_LIGHT_TYPE[data['light_affector_type']]
        if self.light_affector_type == 0x54e8ff1d:
            self.light_affector_data = ArcLightAffectorAttach()
        elif self.light_affector_type == 0xa73bd9d4:
            self.light_affector_data = ArcLightAffectorFlicker()
        self.light_affector_data.load_json(data['light_affector_data'])
        self.light_affector_0xdaed = 0xddaaeedd

    def save_json(self):
        data = OrderedDict()
        data['light_affector_type'] = LIGHT_TYPE_TO_STRING[self.light_affector_type]
        data['light_affector_data'] = self.light_affector_data.save_json()
        return data


class ArcLight:
    def load_binary(self, stream: ResStream):
        self.light_x0 = stream.read_dword()
        self.light_x1 = stream.read_bool()
        self.light_type = stream.read_dword()

        if self.light_type == 0xb6787258:
            self.light_data = ArcLightPoint()
        self.light_data.load_binary(stream)

        self.light_0xdaed = stream.read_dword()

        num = stream.read_dword()
        self.light_affectors = [ArcLightAffectors() for _ in range(num)]
        for extra in self.light_affectors:
            extra.load_binary(stream)

    def save_binary(self, stream: ResStream):
        stream.write_dword(self.light_x0)
        stream.write_bool(self.light_x1)
        stream.write_dword(self.light_type)
        self.light_data.save_binary(stream)
        stream.write_dword(self.light_0xdaed)

        stream.write_dword(len(self.light_affectors))
        for extra in self.light_affectors:
            extra.save_binary(stream)

    def load_json(self, data):
        self.light_x0 = 1
        self.light_x1 = True
        self.light_type = STRING_TO_LIGHT_TYPE[data['light_type']]
        if self.light_type == 0xb6787258:
            self.light_data = ArcLightPoint()
        self.light_data.load_json(data['light_data'])
        self.light_0xdaed = 0xddaaeedd

        self.light_affectors = []
        for extra_data in data['light_affectors']:
            extra = ArcLightAffectors()
            extra.load_json(extra_data)
            self.light_affectors.append(extra)

    def save_json(self):
        data = OrderedDict()
        data['light_type'] = LIGHT_TYPE_TO_STRING[self.light_type]
        data['light_data'] = self.light_data.save_json()

        data['light_affectors'] = []
        for extra in self.light_affectors:
            data['light_affectors'].append(extra.save_json())
        return data


class ArcRender:
    def load_binary(self, stream: ResStream):
        self.render_template = ArcRenderTemplate()
        self.render_template.load_binary(stream)
        self.render_target_bone = stream.read_string()
        self.render_scale = stream.read_tuple()
        self.render_has_loc = stream.read_dword()
        if self.render_has_loc:
            self.render_loc = stream.read_tuple()
            num_children = stream.read_dword()
            self.render_children = [stream.read_qword() for _ in range(num_children)]
        self.render_has_texture_set = stream.read_bool()
        if self.render_has_texture_set:
            num = stream.read_dword()
            self.render_texture_set = [ArcTextureSet() for _ in range(num)]
            for texture in self.render_texture_set:
                texture.load_binary(stream)
        self.render_collides = stream.read_bool()
        self.render_calculate_bounding_box = stream.read_bool()
        self.render_nation_crest = stream.read_bool()
        self.render_guild_crest = stream.read_bool()
        self.render_bumped = stream.read_bool()
        self.render_vp_active = stream.read_bool()
        if self.render_vp_active:
            self.render_vp_name = stream.read_string()
            num_params = stream.read_dword()
            self.render_vp_params = [
                [
                    stream.read_dword(),
                    stream.read_float(),
                    stream.read_float(),
                    stream.read_float(),
                    stream.read_float(),
                ] for _ in range(num_params)
            ]
        self.render_has_light_effects = stream.read_bool()
        if self.render_has_light_effects:
            num_effects = stream.read_dword()
            self.render_light_effects = [ArcLight() for _ in range(num_effects)]
            for effect in self.render_light_effects:
                effect.load_binary(stream)

    def save_binary(self, stream: ResStream):
        self.render_template.save_binary(stream)
        stream.write_string(self.render_target_bone)
        stream.write_tuple(self.render_scale)
        stream.write_dword(self.render_has_loc)
        if self.render_has_loc:
            stream.write_tuple(self.render_loc)
            stream.write_dword(len(self.render_children))
            for child in self.render_children:
                stream.write_qword(child)
        stream.write_bool(self.render_has_texture_set)
        if self.render_has_texture_set:
            stream.write_dword(len(self.render_texture_set))
            for texture in self.render_texture_set:
                texture.save_binary(stream)
        stream.write_bool(self.render_collides)
        stream.write_bool(self.render_calculate_bounding_box)
        stream.write_bool(self.render_nation_crest)
        stream.write_bool(self.render_guild_crest)
        stream.write_bool(self.render_bumped)
        stream.write_bool(self.render_vp_active)
        if self.render_vp_active:
            stream.write_string(self.render_vp_name)

            stream.write_dword(len(self.render_vp_params))
            for param in self.render_vp_params:
                stream.write_dword(param[0])
                stream.write_float(param[1])
                stream.write_float(param[2])
                stream.write_float(param[3])
                stream.write_float(param[4])
        stream.write_bool(self.render_has_light_effects)
        if self.render_has_light_effects:
            stream.write_dword(len(self.render_light_effects))
            for effect in self.render_light_effects:
                effect.save_binary(stream)

    def load_json(self, data):
        self.render_template = ArcRenderTemplate()
        self.render_template.load_json(data['render_template'])
        self.render_target_bone = data['render_target_bone']
        self.render_scale = data['render_scale']
        self.render_has_loc = data['render_has_loc']
        if self.render_has_loc:
            self.render_loc = data['render_loc']
            self.render_children = data['render_children']
        self.render_has_texture_set = data['render_has_texture_set']
        if self.render_has_texture_set:
            self.render_texture_set = []
            for texture_data in data['render_texture_set']:
                texture = ArcTextureSet()
                texture.load_json(texture_data)
                self.render_texture_set.append(texture)
        self.render_collides = data['render_collides']
        self.render_calculate_bounding_box = data['render_calculate_bounding_box']
        self.render_nation_crest = data['render_nation_crest']
        self.render_guild_crest = data['render_guild_crest']
        self.render_bumped = data['render_bumped']
        self.render_vp_active = data['render_vp_active']
        if self.render_vp_active:
            self.render_vp_name = data['render_vp_name']
            self.render_vp_params = data['render_vp_params']
        self.render_has_light_effects = data['render_has_light_effects']
        if self.render_has_light_effects:
            self.render_light_effects = []
            for effect_data in data['render_light_effects']:
                effect = ArcLight()
                effect.load_json(effect_data)
                self.render_light_effects.append(effect)

    def save_json(self):
        data = OrderedDict()
        data['render_template'] = self.render_template.save_json()
        data['render_target_bone'] = self.render_target_bone
        data['render_scale'] = self.render_scale
        data['render_has_loc'] = self.render_has_loc
        if self.render_has_loc:
            data['render_loc'] = self.render_loc
            data['render_children'] = self.render_children
        data['render_has_texture_set'] = self.render_has_texture_set
        if self.render_has_texture_set:
            data['render_texture_set'] = []
            for texture in self.render_texture_set:
                data['render_texture_set'].append(texture.save_json())
        data['render_collides'] = self.render_collides
        data['render_calculate_bounding_box'] = self.render_calculate_bounding_box
        data['render_nation_crest'] = self.render_nation_crest
        data['render_guild_crest'] = self.render_guild_crest
        data['render_bumped'] = self.render_bumped
        data['render_vp_active'] = self.render_vp_active
        if self.render_vp_active:
            data['render_vp_name'] = self.render_vp_name
            data['render_vp_params'] = self.render_vp_params
        data['render_has_light_effects'] = self.render_has_light_effects
        if self.render_has_light_effects:
            data['render_light_effects'] = []
            for effect in self.render_light_effects:
                data['render_light_effects'].append(effect.save_json())
        return data
