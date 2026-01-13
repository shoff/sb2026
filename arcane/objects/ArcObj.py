from collections import OrderedDict

from arcane.enums.arc_object import *
from arcane.enums.hashes import hash_to_string, string_to_hash
from arcane.util import ResStream
from .common.SparseData import SparseData


class SoundEvent:
    def load_binary(self, stream: ResStream):
        self.sound_type = stream.read_dword()
        self.sound_event = stream.read_qword()

    def save_binary(self, stream: ResStream):
        stream.write_dword(self.sound_type)
        stream.write_qword(self.sound_event)

    def load_json(self, data):
        self.sound_type = STRING_TO_SOUND_TYPE[data['sound_type']]
        self.sound_event = data['sound_event']

    def save_json(self):
        data = OrderedDict()
        data['sound_type'] = SOUND_TYPE_TO_STRING[self.sound_type]
        data['sound_event'] = self.sound_event
        return data


class ArcObj:
    def load_binary(self, stream: ResStream):
        self.obj_name = stream.read_string()
        self.obj_pickable = stream.read_bool()
        self.obj_gravity = stream.read_float()
        self.obj_cull_distance = stream.read_float()
        self.obj_scale = stream.read_tuple()
        self.obj_render_object = stream.read_qword()
        self.obj_double_fusion = stream.read_bool()
        self.obj_forward_vector = stream.read_tuple()
        self.obj_tracking_name = stream.read_string()
        self.obj_max_tracking_distance = stream.read_float()
        self.obj_icon = stream.read_qword()
        self.obj_gravity_f = stream.read_float()
        num_sound_events = stream.read_dword()
        self.obj_sound_events = [SoundEvent() for _ in range(num_sound_events)]
        for sound_event in self.obj_sound_events:
            sound_event.load_binary(stream)
        num_hard_points = stream.read_dword()
        self.obj_arc_hardpoint_list = [
            [
                stream.read_dword(),
                stream.read_dword(),
                [stream.read_float() for _ in range(10)]
            ] for _ in range(num_hard_points)
        ]
        self.obj_sparse_data = SparseData()
        self.obj_sparse_data.load_binary(stream)
        self.obj_render_object_low_detail = stream.read_qword()
        self.obj_default_alignment = stream.read_tuple()
        self.obj_sound_table = stream.read_dword()

    def save_binary(self, stream: ResStream):
        stream.write_string(self.obj_name)
        stream.write_bool(self.obj_pickable)
        stream.write_float(self.obj_gravity)
        stream.write_float(self.obj_cull_distance)
        stream.write_tuple(self.obj_scale)
        stream.write_qword(self.obj_render_object)
        stream.write_bool(self.obj_double_fusion)
        stream.write_tuple(self.obj_forward_vector)
        stream.write_string(self.obj_tracking_name)
        stream.write_float(self.obj_max_tracking_distance)
        stream.write_qword(self.obj_icon)
        stream.write_float(self.obj_gravity_f)
        stream.write_dword(len(self.obj_sound_events))
        for sound_event in self.obj_sound_events:
            sound_event.save_binary(stream)
        stream.write_dword(len(self.obj_arc_hardpoint_list))
        for n, m, points in self.obj_arc_hardpoint_list:
            stream.write_dword(n)
            stream.write_dword(m)
            for i in range(10):
                stream.write_float(points[i])
        self.obj_sparse_data.save_binary(stream)
        stream.write_qword(self.obj_render_object_low_detail)
        stream.write_tuple(self.obj_default_alignment)
        stream.write_dword(self.obj_sound_table)

    def load_json(self, data):
        self.obj_name = data['obj_name']
        self.obj_pickable = data['obj_pickable']
        self.obj_gravity = data['obj_gravity']
        self.obj_cull_distance = data['obj_cull_distance']
        self.obj_scale = data['obj_scale']
        self.obj_render_object = data['obj_render_object']
        self.obj_double_fusion = data['obj_double_fusion']
        self.obj_forward_vector = data['obj_forward_vector']
        self.obj_tracking_name = data['obj_tracking_name']
        self.obj_max_tracking_distance = data['obj_max_tracking_distance']
        self.obj_icon = data['obj_icon']
        self.obj_gravity_f = data['obj_gravity_f']
        self.obj_sound_events = []
        for sound_data in data['obj_sound_events']:
            sound_event = SoundEvent()
            sound_event.load_json(sound_data)
            self.obj_sound_events.append(sound_event)
        self.obj_arc_hardpoint_list = []
        for point_list in data['obj_arc_hardpoint_list']:
            self.obj_arc_hardpoint_list.append(point_list)
        self.obj_sparse_data = SparseData()
        self.obj_sparse_data.load_json(data['obj_sparse_data'])
        self.obj_render_object_low_detail = data['obj_render_object_low_detail']
        self.obj_default_alignment = data['obj_default_alignment']
        self.obj_sound_table = string_to_hash(data['obj_sound_table'])
        return data

    def save_json(self):
        data = OrderedDict()
        data['obj_name'] = self.obj_name
        data['obj_pickable'] = self.obj_pickable
        data['obj_gravity'] = self.obj_gravity
        data['obj_cull_distance'] = self.obj_cull_distance
        data['obj_scale'] = self.obj_scale
        data['obj_render_object'] = self.obj_render_object
        data['obj_double_fusion'] = self.obj_double_fusion
        data['obj_forward_vector'] = self.obj_forward_vector
        data['obj_tracking_name'] = self.obj_tracking_name
        data['obj_max_tracking_distance'] = self.obj_max_tracking_distance
        data['obj_icon'] = self.obj_icon
        data['obj_gravity_f'] = self.obj_gravity_f
        data['obj_sound_events'] = []
        for sound_event in self.obj_sound_events:
            data['obj_sound_events'].append(sound_event.save_json())
        data['obj_arc_hardpoint_list'] = []
        for point_list in self.obj_arc_hardpoint_list:
            data['obj_arc_hardpoint_list'].append(point_list)
        data['obj_sparse_data'] = self.obj_sparse_data.save_json()
        data['obj_render_object_low_detail'] = self.obj_render_object_low_detail
        data['obj_default_alignment'] = self.obj_default_alignment
        data['obj_sound_table'] = hash_to_string(self.obj_sound_table)
        return data
