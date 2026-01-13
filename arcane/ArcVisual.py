
from base64 import b64decode, b64encode
from collections import OrderedDict

from arcane.util import ResStream

EFFETCT_TO_STRING = {
    0: 'PARTICLE',
    1: 'LIGHTNING',
    2: 'GEOMETRY',
}

STRING_TO_EFFECT = {value: key for key, value in EFFETCT_TO_STRING.items()}


class ArcParticle:
    def load_binary(self, stream: ResStream):
        self.particle_attached_bone = stream.read_dword()
        self.particle_count = stream.read_dword()
        self.particle_size = stream.read_float()
        self.particle_life = stream.read_float()
        self.particle_life_rand = stream.read_float()
        self.particle_shape_and_pos = stream.read_dword()
        self.particle_emitter_scale = stream.read_float()
        self.particle_pos_offset = stream.read_tuple()
        self.particle_ppos_reference = stream.read_tuple()
        self.particle_initial_velocities = stream.read_dword()
        self.particle_velocity_scale = stream.read_float()
        self.particle_vel_reference = stream.read_tuple()
        self.particle_dir_random = stream.read_float()
        self.particle_spd_random = stream.read_float()
        self.particle_initial_rot = stream.read_float()
        self.particle_initial_rot_random = stream.read_float()
        self.particle_incremental_rot = stream.read_float()
        self.particle_incremental_rot_random = stream.read_float()
        self.particle_color_keys = [
            [
                stream.read_float(),
                stream.read_float(),
                stream.read_float(),
                stream.read_float(),
            ] for _ in range(5)
        ]
        self.particle_color_keytimes = [stream.read_float() for _ in range(5)]
        self.particle_size_keys = [stream.read_float() for _ in range(5)]
        self.particle_targettype = stream.read_dword()
        self.particle_lifetime = stream.read_float()
        self.particle_texture = stream.read_dword()
        self.particle_blend_type = stream.read_dword()
        self.particle_attractor_bone = stream.read_dword()
        self.particle_directional_grav = stream.read_tuple()
        self.particle_field_function = stream.read_dword()
        self.particle_gravity_strength = stream.read_float()

    def save_binary(self, stream: ResStream):
        stream.write_dword(self.particle_attached_bone)
        stream.write_dword(self.particle_count)
        stream.write_float(self.particle_size)
        stream.write_float(self.particle_life)
        stream.write_float(self.particle_life_rand)
        stream.write_dword(self.particle_shape_and_pos)
        stream.write_float(self.particle_emitter_scale)
        stream.write_tuple(self.particle_pos_offset)
        stream.write_tuple(self.particle_ppos_reference)
        stream.write_dword(self.particle_initial_velocities)
        stream.write_float(self.particle_velocity_scale)
        stream.write_tuple(self.particle_vel_reference)
        stream.write_float(self.particle_dir_random)
        stream.write_float(self.particle_spd_random)
        stream.write_float(self.particle_initial_rot)
        stream.write_float(self.particle_initial_rot_random)
        stream.write_float(self.particle_incremental_rot)
        stream.write_float(self.particle_incremental_rot_random)
        for i in range(5):
            stream.write_float(self.particle_color_keys[i][0])
            stream.write_float(self.particle_color_keys[i][1])
            stream.write_float(self.particle_color_keys[i][2])
            stream.write_float(self.particle_color_keys[i][3])
        for i in range(5):
            stream.write_float(self.particle_color_keytimes[i])
        for i in range(5):
            stream.write_float(self.particle_size_keys[i])
        stream.write_dword(self.particle_targettype)
        stream.write_float(self.particle_lifetime)
        stream.write_dword(self.particle_texture)
        stream.write_dword(self.particle_blend_type)
        stream.write_dword(self.particle_attractor_bone)
        stream.write_tuple(self.particle_directional_grav)
        stream.write_dword(self.particle_field_function)
        stream.write_float(self.particle_gravity_strength)

    def load_json(self, data):
        self.particle_attached_bone = data['particle_attached_bone']
        self.particle_count = data['particle_count']
        self.particle_size = data['particle_size']
        self.particle_life = data['particle_life']
        self.particle_life_rand = data['particle_life_rand']
        self.particle_shape_and_pos = data['particle_shape_and_pos']
        self.particle_emitter_scale = data['particle_emitter_scale']
        self.particle_pos_offset = data['particle_pos_offset']
        self.particle_ppos_reference = data['particle_ppos_reference']
        self.particle_initial_velocities = data['particle_initial_velocities']
        self.particle_velocity_scale = data['particle_velocity_scale']
        self.particle_vel_reference = data['particle_vel_reference']
        self.particle_dir_random = data['particle_dir_random']
        self.particle_spd_random = data['particle_spd_random']
        self.particle_initial_rot = data['particle_initial_rot']
        self.particle_initial_rot_random = data['particle_initial_rot_random']
        self.particle_incremental_rot = data['particle_incremental_rot']
        self.particle_incremental_rot_random = data['particle_incremental_rot_random']
        self.particle_color_keys = data['particle_color_keys']
        self.particle_color_keytimes = data['particle_color_keytimes']
        self.particle_size_keys = data['particle_size_keys']
        self.particle_targettype = data['particle_targettype']
        self.particle_lifetime = data['particle_lifetime']
        self.particle_texture = data['particle_texture']
        self.particle_blend_type = data['particle_blend_type']
        self.particle_attractor_bone = data['particle_attractor_bone']
        self.particle_directional_grav = data['particle_directional_grav']
        self.particle_field_function = data['particle_field_function']
        self.particle_gravity_strength = data['particle_gravity_strength']

    def save_json(self):
        data = OrderedDict()
        data['particle_attached_bone'] = self.particle_attached_bone
        data['particle_count'] = self.particle_count
        data['particle_size'] = self.particle_size
        data['particle_life'] = self.particle_life
        data['particle_life_rand'] = self.particle_life_rand
        data['particle_shape_and_pos'] = self.particle_shape_and_pos
        data['particle_emitter_scale'] = self.particle_emitter_scale
        data['particle_pos_offset'] = self.particle_pos_offset
        data['particle_ppos_reference'] = self.particle_ppos_reference
        data['particle_initial_velocities'] = self.particle_initial_velocities
        data['particle_velocity_scale'] = self.particle_velocity_scale
        data['particle_vel_reference'] = self.particle_vel_reference
        data['particle_dir_random'] = self.particle_dir_random
        data['particle_spd_random'] = self.particle_spd_random
        data['particle_initial_rot'] = self.particle_initial_rot
        data['particle_initial_rot_random'] = self.particle_initial_rot_random
        data['particle_incremental_rot'] = self.particle_incremental_rot
        data['particle_incremental_rot_random'] = self.particle_incremental_rot_random
        data['particle_color_keys'] = self.particle_color_keys
        data['particle_color_keytimes'] = self.particle_color_keytimes
        data['particle_size_keys'] = self.particle_size_keys
        data['particle_targettype'] = self.particle_targettype
        data['particle_lifetime'] = self.particle_lifetime
        data['particle_texture'] = self.particle_texture
        data['particle_blend_type'] = self.particle_blend_type
        data['particle_attractor_bone'] = self.particle_attractor_bone
        data['particle_directional_grav'] = self.particle_directional_grav
        data['particle_field_function'] = self.particle_field_function
        data['particle_gravity_strength'] = self.particle_gravity_strength
        return data


class ArcLightning:
    def load_binary(self, stream: ResStream):
        self.lightning_texture = stream.read_dword()
        self.lightning_src_bone = stream.read_dword()
        self.lightning_dst_bone = stream.read_dword()
        self.lightning_width = stream.read_float()
        self.lightning_random_factor = stream.read_float()
        self.lightning_sine_factor = stream.read_float()
        self.lightning_sine_phase = stream.read_float()
        self.lightning_sine_phase_rep = stream.read_float()
        self.lightning_length = stream.read_float()
        self.lightning_random_move_speed = stream.read_float()
        self.lightning_color = stream.read_tuple()
        self.lightning_lifetime = stream.read_float()

    def save_binary(self, stream: ResStream):
        stream.write_dword(self.lightning_texture)
        stream.write_dword(self.lightning_src_bone)
        stream.write_dword(self.lightning_dst_bone)
        stream.write_float(self.lightning_width)
        stream.write_float(self.lightning_random_factor)
        stream.write_float(self.lightning_sine_factor)
        stream.write_float(self.lightning_sine_phase)
        stream.write_float(self.lightning_sine_phase_rep)
        stream.write_float(self.lightning_length)
        stream.write_float(self.lightning_random_move_speed)
        stream.write_tuple(self.lightning_color)
        stream.write_float(self.lightning_lifetime)

    def load_json(self, data):
        self.lightning_texture = data['lightning_texture']
        self.lightning_src_bone = data['lightning_src_bone']
        self.lightning_dst_bone = data['lightning_dst_bone']
        self.lightning_width = data['lightning_width']
        self.lightning_random_factor = data['lightning_random_factor']
        self.lightning_sine_factor = data['lightning_sine_factor']
        self.lightning_sine_phase = data['lightning_sine_phase']
        self.lightning_sine_phase_rep = data['lightning_sine_phase_rep']
        self.lightning_length = data['lightning_length']
        self.lightning_random_move_speed = data['lightning_random_move_speed']
        self.lightning_color = data['lightning_color']
        self.lightning_lifetime = data['lightning_lifetime']

    def save_json(self):
        data = OrderedDict()
        data['lightning_texture'] = self.lightning_texture
        data['lightning_src_bone'] = self.lightning_src_bone
        data['lightning_dst_bone'] = self.lightning_dst_bone
        data['lightning_width'] = self.lightning_width
        data['lightning_random_factor'] = self.lightning_random_factor
        data['lightning_sine_factor'] = self.lightning_sine_factor
        data['lightning_sine_phase'] = self.lightning_sine_phase
        data['lightning_sine_phase_rep'] = self.lightning_sine_phase_rep
        data['lightning_length'] = self.lightning_length
        data['lightning_random_move_speed'] = self.lightning_random_move_speed
        data['lightning_color'] = self.lightning_color
        data['lightning_lifetime'] = self.lightning_lifetime
        return data


class ArcGeometry:
    def load_binary(self, stream: ResStream):
        self.geometry_texture = stream.read_dword()
        self.geometry_src_bone = stream.read_dword()
        self.geometry_lifetime = stream.read_float()
        self.geometry_tex_trans_x = stream.read_float()
        self.geometry_tex_trans_y = stream.read_float()
        self.geometry_tex_rot = stream.read_float()
        self.geometry_grow = stream.read_tuple()
        self.geometry_tesselation = stream.read_float()
        self.geometry_size = stream.read_tuple()
        self.geometry_geo_rot_x = stream.read_float()
        self.geometry_fade_falloff = stream.read_float()
        self.geometry_fadein = stream.read_float()
        self.geometry_fadeout = stream.read_float()
        self.geometry_color = [stream.read_float() for _ in range(4)]
        self.geometry_type = stream.read_dword()
        self.geometry_texture_proj = stream.read_dword()
        self.geometry_fade_dir = stream.read_dword()
        self.geometry_offset = stream.read_tuple()

    def save_binary(self, stream: ResStream):
        stream.write_dword(self.geometry_texture)
        stream.write_dword(self.geometry_src_bone)
        stream.write_float(self.geometry_lifetime)
        stream.write_float(self.geometry_tex_trans_x)
        stream.write_float(self.geometry_tex_trans_y)
        stream.write_float(self.geometry_tex_rot)
        stream.write_tuple(self.geometry_grow)
        stream.write_float(self.geometry_tesselation)
        stream.write_tuple(self.geometry_size)
        stream.write_float(self.geometry_geo_rot_x)
        stream.write_float(self.geometry_fade_falloff)
        stream.write_float(self.geometry_fadein)
        stream.write_float(self.geometry_fadeout)
        for i in range(4):
            stream.write_float(self.geometry_color[i])
        stream.write_dword(self.geometry_type)
        stream.write_dword(self.geometry_texture_proj)
        stream.write_dword(self.geometry_fade_dir)
        stream.write_tuple(self.geometry_offset)

    def load_json(self, data):
        self.geometry_texture = data['geometry_texture']
        self.geometry_src_bone = data['geometry_src_bone']
        self.geometry_lifetime = data['geometry_lifetime']
        self.geometry_tex_trans_x = data['geometry_tex_trans_x']
        self.geometry_tex_trans_y = data['geometry_tex_trans_y']
        self.geometry_tex_rot = data['geometry_tex_rot']
        self.geometry_grow = data['geometry_grow']
        self.geometry_tesselation = data['geometry_tesselation']
        self.geometry_size = data['geometry_size']
        self.geometry_geo_rot_x = data['geometry_geo_rot_x']
        self.geometry_fade_falloff = data['geometry_fade_falloff']
        self.geometry_fadein = data['geometry_fadein']
        self.geometry_fadeout = data['geometry_fadeout']
        self.geometry_color = data['geometry_color']
        self.geometry_type = data['geometry_type']
        self.geometry_texture_proj = data['geometry_texture_proj']
        self.geometry_fade_dir = data['geometry_fade_dir']
        self.geometry_offset = data['geometry_offset']

    def save_json(self):
        data = OrderedDict()
        data['geometry_texture'] = self.geometry_texture
        data['geometry_src_bone'] = self.geometry_src_bone
        data['geometry_lifetime'] = self.geometry_lifetime
        data['geometry_tex_trans_x'] = self.geometry_tex_trans_x
        data['geometry_tex_trans_y'] = self.geometry_tex_trans_y
        data['geometry_tex_rot'] = self.geometry_tex_rot
        data['geometry_grow'] = self.geometry_grow
        data['geometry_tesselation'] = self.geometry_tesselation
        data['geometry_size'] = self.geometry_size
        data['geometry_geo_rot_x'] = self.geometry_geo_rot_x
        data['geometry_fade_falloff'] = self.geometry_fade_falloff
        data['geometry_fadein'] = self.geometry_fadein
        data['geometry_fadeout'] = self.geometry_fadeout
        data['geometry_color'] = self.geometry_color
        data['geometry_type'] = self.geometry_type
        data['geometry_texture_proj'] = self.geometry_texture_proj
        data['geometry_fade_dir'] = self.geometry_fade_dir
        data['geometry_offset'] = self.geometry_offset
        return data


class ArcVisualEffect:
    def load_binary(self, stream: ResStream):
        self.effect_type = stream.read_dword()
        self.effect_time = stream.read_float()

        if self.effect_type == 0:
            self.effect = ArcParticle()
        elif self.effect_type == 1:
            self.effect = ArcLightning()
        elif self.effect_type == 2:
            self.effect = ArcGeometry()
        self.effect.load_binary(stream)

    def save_binary(self, stream: ResStream):
        stream.write_dword(self.effect_type)
        stream.write_float(self.effect_time)
        self.effect.save_binary(stream)

    def load_json(self, data):
        self.effect_type = STRING_TO_EFFECT[data['effect_type']]
        self.effect_time = data['effect_time']
        if self.effect_type == 0:
            self.effect = ArcParticle()
        elif self.effect_type == 1:
            self.effect = ArcLightning()
        elif self.effect_type == 2:
            self.effect = ArcGeometry()
        self.effect.load_json(data['effect'])

    def save_json(self):
        data = OrderedDict()
        data['effect_type'] = EFFETCT_TO_STRING[self.effect_type]
        data['effect_time'] = self.effect_time
        data['effect'] = self.effect.save_json()
        return data


class ArcVisual:
    def load_binary(self, stream: ResStream):
        num_effects = stream.read_dword()

        self.vfx_fail = None
        if num_effects == 1617156728:
            stream.buffer.seek(0, 0)
            self.vfx_fail = stream.buffer.read()
            return

        self.vfx_duration = stream.read_float()
        self.vfx_effects = [ArcVisualEffect() for _ in range(num_effects)]
        for effect in self.vfx_effects:
            effect.load_binary(stream)

    def save_binary(self, stream: ResStream):
        if self.vfx_fail:
            stream.buffer.write(self.vfx_fail)
            return

        stream.write_dword(len(self.vfx_effects))
        stream.write_float(self.vfx_duration)
        for effect in self.vfx_effects:
            effect.save_binary(stream)

    def load_json(self, data):
        self.vfx_fail = data.get('vfx_fail')
        if self.vfx_fail:
            self.vfx_fail = b64decode(self.vfx_fail)
            return

        self.vfx_duration = data['vfx_duration']
        self.vfx_effects = []
        for effect_data in data['vfx_effects']:
            effect = ArcVisualEffect()
            effect.load_json(effect_data)
            self.vfx_effects.append(effect)

    def save_json(self):
        data = OrderedDict()
        if self.vfx_fail:
            data['vfx_fail'] = b64encode(self.vfx_fail).decode()
            return data

        data['vfx_duration'] = self.vfx_duration
        data['vfx_effects'] = []
        for effect in self.vfx_effects:
            data['vfx_effects'].append(effect.save_json())
        return data
