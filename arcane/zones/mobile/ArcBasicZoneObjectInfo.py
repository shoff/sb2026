#  • ▌ ▄ ·. ▄▄▄▄·     ▄▄▄ .·▄▄▄▄  ▪  ▄▄▄▄▄      ▄▄▄       ▄▄▄·▄▄▄       
#  ·██ ▐███▪▐█ ▀█▪    ▀▄.▀·██▪ ██ ██ •██  ▪     ▀▄ █·    ▐█ ▄█▀▄ █·▪    
#  ▐█ ▌▐▌▐█·▐█▀▀█▄    ▐▀▀▪▄▐█· ▐█▌▐█· ▐█.▪ ▄█▀▄ ▐▀▀▄      ██▀·▐▀▀▄  ▄█▀▄
#  ██ ██▌▐█▌██▄▪▐█    ▐█▄▄▌██. ██ ▐█▌ ▐█▌·▐█▌.▐▌▐█•█▌    ▐█▪·•▐█•█▌▐█▌.▐▌
#  ▀▀  █▪▀▀▀·▀▀▀▀      ▀▀▀ ▀▀▀▀▀• ▀▀▀ ▀▀▀  ▀█▄▀▪.▀  ▀    .▀   .▀  ▀ ▀█▄▀▪
#                Magicbane Emulator Project © 2013 - 2022
#                           www.magicbane.com

from collections import OrderedDict

from arcane.objects.common.SparseData import SparseData
from arcane.util import ResStream


class ArcBasicZoneObjectInfo:

    def load_binary(self, stream: ResStream):
        self.basic_zone_spawn_location = stream.read_tuple()
        self.basic_zone_name_override = stream.read_string()
        self.basic_zone_time_to_respawn = stream.read_float()
        self.basic_zone_spawn_radius = stream.read_float()
        self.basic_zone_y_rot = stream.read_float()
        self.basic_zone_template_id = stream.read_qword()
        self.basic_zone_unknown1 = stream.read_qword()
        self.basic_zone_level_number = stream.read_dword()
        self.basic_zone_room_number = stream.read_dword()
        self.basic_zone_unknown2 = stream.read_qword()
        self.basic_zone_dungeon_level = stream.read_dword()
        self.basic_zone_dungeon_row = stream.read_dword()
        self.basic_zone_dungeon_column = stream.read_dword()
        self.basic_zone_sparse_data = SparseData()
        self.basic_zone_sparse_data.load_binary(stream)

    def save_binary(self, stream: ResStream):
        stream.write_tuple(self.basic_zone_spawn_location)
        stream.write_string(self.basic_zone_name_override)
        stream.write_float(self.basic_zone_time_to_respawn)
        stream.write_float(self.basic_zone_spawn_radius)
        stream.write_float(self.basic_zone_y_rot)
        stream.write_qword(self.basic_zone_template_id)
        stream.write_qword(self.basic_zone_unknown1)
        stream.write_dword(self.basic_zone_level_number)
        stream.write_dword(self.basic_zone_room_number)
        stream.write_qword(self.basic_zone_unknown2)
        stream.write_dword(self.basic_zone_dungeon_level)
        stream.write_dword(self.basic_zone_dungeon_row)
        stream.write_dword(self.basic_zone_dungeon_column)
        self.basic_zone_sparse_data.save_binary(stream)

    def save_json(self):
        data = OrderedDict()
        data['basic_zone_spawn_location'] = self.basic_zone_spawn_location
        data['basic_zone_name_override'] = self.basic_zone_name_override
        data['basic_zone_time_to_respawn'] = self.basic_zone_time_to_respawn
        data['basic_zone_spawn_radius'] = self.basic_zone_spawn_radius
        data['basic_zone_y_rot'] = self.basic_zone_y_rot
        data['basic_zone_template_id'] = self.basic_zone_template_id
        data['basic_zone_unknown1'] = self.basic_zone_unknown1
        data['basic_zone_level_number'] = self.basic_zone_level_number
        data['basic_zone_room_number'] = self.basic_zone_room_number
        data['basic_zone_unknown2'] = self.basic_zone_unknown2
        data['basic_zone_dungeon_level'] = self.basic_zone_dungeon_level
        data['basic_zone_dungeon_row'] = self.basic_zone_dungeon_row
        data['basic_zone_dungeon_column'] = self.basic_zone_dungeon_column
        data['basic_zone_sparse_data'] = self.basic_zone_sparse_data.save_json()
        return data

    def load_json(self, data):
        self.basic_zone_spawn_location = data['basic_zone_spawn_location']
        self.basic_zone_name_override = data['basic_zone_name_override']
        self.basic_zone_time_to_respawn = data['basic_zone_time_to_respawn']
        self.basic_zone_spawn_radius = data['basic_zone_spawn_radius']
        self.basic_zone_y_rot = data['basic_zone_y_rot']
        self.basic_zone_template_id = data['basic_zone_template_id']
        self.basic_zone_unknown1 = data['basic_zone_unknown1']
        self.basic_zone_level_number = data['basic_zone_level_number']
        self.basic_zone_room_number = data['basic_zone_room_number']
        self.basic_zone_unknown2 = data['basic_zone_unknown2']
        self.basic_zone_dungeon_level = data['basic_zone_dungeon_level']
        self.basic_zone_dungeon_row = data['basic_zone_dungeon_row']
        self.basic_zone_dungeon_column = data['basic_zone_dungeon_column']
        self.basic_zone_sparse_data = SparseData()
        self.basic_zone_sparse_data.load_json(data['basic_zone_sparse_data'])
