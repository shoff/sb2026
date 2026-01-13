#  • ▌ ▄ ·. ▄▄▄▄·     ▄▄▄ .·▄▄▄▄  ▪  ▄▄▄▄▄      ▄▄▄       ▄▄▄·▄▄▄       
#  ·██ ▐███▪▐█ ▀█▪    ▀▄.▀·██▪ ██ ██ •██  ▪     ▀▄ █·    ▐█ ▄█▀▄ █·▪    
#  ▐█ ▌▐▌▐█·▐█▀▀█▄    ▐▀▀▪▄▐█· ▐█▌▐█· ▐█.▪ ▄█▀▄ ▐▀▀▄      ██▀·▐▀▀▄  ▄█▀▄
#  ██ ██▌▐█▌██▄▪▐█    ▐█▄▄▌██. ██ ▐█▌ ▐█▌·▐█▌.▐▌▐█•█▌    ▐█▪·•▐█•█▌▐█▌.▐▌
#  ▀▀  █▪▀▀▀·▀▀▀▀      ▀▀▀ ▀▀▀▀▀• ▀▀▀ ▀▀▀  ▀█▄▀▪.▀  ▀    .▀   .▀  ▀ ▀█▄▀▪
#                Magicbane Emulator Project © 2013 - 2022
#                           www.magicbane.com

from collections import OrderedDict

from arcane.enums.arc_door import *
from arcane.util import ResStream


class ArcDoorObject():
    def load_binary(self, stream: ResStream):
        self.door_id = stream.read_qword()
        self.door_type = stream.read_dword()
        self.door_movement_axis = stream.read_dword()
        self.door_swing_direction = stream.read_dword()
        self.door_min_time_to_stay_open = stream.read_float()
        self.door_max_time_to_stay_open = stream.read_float()
        self.door_swing_time = stream.read_float()
        self.door_swing = stream.read_float()
        self.door_slide_distance = stream.read_float()
        self.door_slide_direction = stream.read_tuple()
        self.door_slide_start = stream.read_tuple()
        self.door_slide_end = stream.read_tuple()
        self.door_locked = stream.read_dword()
        self.door_linked_to = stream.read_qword()
        self.door_key = stream.read_qword()
        self.door_sound_event = stream.read_qword()

    def save_binary(self, stream: ResStream):
        stream.write_qword(self.door_id)
        stream.write_dword(self.door_type)
        stream.write_dword(self.door_movement_axis)
        stream.write_dword(self.door_swing_direction)
        stream.write_float(self.door_min_time_to_stay_open)
        stream.write_float(self.door_max_time_to_stay_open)
        stream.write_float(self.door_swing_time)
        stream.write_float(self.door_swing)
        stream.write_float(self.door_slide_distance)
        stream.write_tuple(self.door_slide_direction)
        stream.write_tuple(self.door_slide_start)
        stream.write_tuple(self.door_slide_end)
        stream.write_dword(self.door_locked)
        stream.write_qword(self.door_linked_to)
        stream.write_qword(self.door_key)
        stream.write_qword(self.door_sound_event)

    def load_json(self, data):
        self.door_id = data['door_id']
        self.door_type = STRING_TO_DOOR_TYPE[data['door_type']]
        self.door_movement_axis = STRING_TO_DOOR_MOVEMENT_AXIS[data['door_movement_axis']]
        self.door_swing_direction = STRING_TO_DOOR_SWING_DIRECTION[data['door_swing_direction']]
        self.door_min_time_to_stay_open = data['door_min_time_to_stay_open']
        self.door_max_time_to_stay_open = data['door_max_time_to_stay_open']
        self.door_swing_time = data['door_swing_time']
        self.door_swing = data['door_swing']
        self.door_slide_distance = data['door_slide_distance']
        self.door_slide_direction = data['door_slide_direction']
        self.door_slide_start = data['door_slide_start']
        self.door_slide_end = data['door_slide_end']
        self.door_locked = data['door_locked']
        self.door_linked_to = data['door_linked_to']
        self.door_key = data['door_key']
        self.door_sound_event = data['door_sound_event']

    def save_json(self):
        data = OrderedDict()
        data['door_id'] = self.door_id
        data['door_type'] = DOOR_TYPE_TO_STRING[self.door_type]
        data['door_movement_axis'] = DOOR_MOVEMENT_AXIS_TO_STRING[self.door_movement_axis]
        data['door_swing_direction'] = DOOR_SWING_DIRECTION_TO_STRING[self.door_swing_direction]
        data['door_min_time_to_stay_open'] = self.door_min_time_to_stay_open
        data['door_max_time_to_stay_open'] = self.door_max_time_to_stay_open
        data['door_swing_time'] = self.door_swing_time
        data['door_swing'] = self.door_swing
        data['door_slide_distance'] = self.door_slide_distance
        data['door_slide_direction'] = self.door_slide_direction
        data['door_slide_start'] = self.door_slide_start
        data['door_slide_end'] = self.door_slide_end
        data['door_locked'] = self.door_locked
        data['door_linked_to'] = self.door_linked_to
        data['door_key'] = self.door_key
        data['door_sound_event'] = self.door_sound_event
        return data
