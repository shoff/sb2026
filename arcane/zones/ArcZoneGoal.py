#  • ▌ ▄ ·. ▄▄▄▄·     ▄▄▄ .·▄▄▄▄  ▪  ▄▄▄▄▄      ▄▄▄       ▄▄▄·▄▄▄       
#  ·██ ▐███▪▐█ ▀█▪    ▀▄.▀·██▪ ██ ██ •██  ▪     ▀▄ █·    ▐█ ▄█▀▄ █·▪    
#  ▐█ ▌▐▌▐█·▐█▀▀█▄    ▐▀▀▪▄▐█· ▐█▌▐█· ▐█.▪ ▄█▀▄ ▐▀▀▄      ██▀·▐▀▀▄  ▄█▀▄
#  ██ ██▌▐█▌██▄▪▐█    ▐█▄▄▌██. ██ ▐█▌ ▐█▌·▐█▌.▐▌▐█•█▌    ▐█▪·•▐█•█▌▐█▌.▐▌
#  ▀▀  █▪▀▀▀·▀▀▀▀      ▀▀▀ ▀▀▀▀▀• ▀▀▀ ▀▀▀  ▀█▄▀▪.▀  ▀    .▀   .▀  ▀ ▀█▄▀▪
#                Magicbane Emulator Project © 2013 - 2022
#                           www.magicbane.com

from collections import OrderedDict

from arcane.enums.hashes import hash_to_string, string_to_hash
from arcane.enums.zone.arc_zone_goal import *
from arcane.util import ResStream


class ArcZoneGoalPoint:
    def load_binary(self, stream: ResStream):
        self.zone_goal_point_vectors = [stream.read_dword() for _ in range(6)]
        self.zone_goal_point_location = stream.read_tuple()

    def save_binary(self, stream: ResStream):
        for i in range(6):
            stream.write_dword(self.zone_goal_point_vectors[i])
        stream.write_tuple(self.zone_goal_point_location)

    def save_json(self):
        data = OrderedDict()
        data['zone_goal_point_vectors'] = self.zone_goal_point_vectors
        data['zone_goal_point_location'] = self.zone_goal_point_location
        return data

    def load_json(self, data):
        self.zone_goal_point_vectors = data['zone_goal_point_vectors']
        self.zone_goal_point_location = data['zone_goal_point_location']


class ArcZoneGoal:
    def load_binary(self, stream: ResStream):
        self.zone_goal_type = stream.read_dword()
        self.zone_goal_value = stream.read_dword()
        self.zone_goal_name = stream.read_string()
        self.zone_goal_delay = stream.read_dword()
        self.zone_goal_has_teleport_registry = stream.read_bool()
        if self.zone_goal_has_teleport_registry:
            self.zone_goal_teleport_registry = stream.read_dword()
        self.zone_goal_dungeon = stream.read_qword()
        num_points = stream.read_dword()
        self.zone_goal_points = [ArcZoneGoalPoint() for _ in range(num_points)]
        for point in self.zone_goal_points:
            point.load_binary(stream)

    def save_binary(self, stream: ResStream):
        stream.write_dword(self.zone_goal_type)
        stream.write_dword(self.zone_goal_value)
        stream.write_string(self.zone_goal_name)
        stream.write_dword(self.zone_goal_delay)
        stream.write_bool(self.zone_goal_has_teleport_registry)
        if self.zone_goal_has_teleport_registry:
            stream.write_dword(self.zone_goal_teleport_registry)
        stream.write_qword(self.zone_goal_dungeon)
        stream.write_dword(len(self.zone_goal_points))
        for point in self.zone_goal_points:
            point.save_binary(stream)

    def save_json(self):
        data = OrderedDict()
        data['zone_goal_type'] = GOAL_TYPE_TO_STRING[self.zone_goal_type]
        data['zone_goal_value'] = hash_to_string(self.zone_goal_value)
        data['zone_goal_name'] = self.zone_goal_name
        data['zone_goal_delay'] = self.zone_goal_delay
        data['zone_goal_has_teleport_registry'] = self.zone_goal_has_teleport_registry
        if self.zone_goal_has_teleport_registry:
            data['zone_goal_teleport_registry'] = hash_to_string(self.zone_goal_teleport_registry)
        data['zone_goal_dungeon'] = self.zone_goal_dungeon
        data['zone_goal_points'] = []
        for point in self.zone_goal_points:
            data['zone_goal_points'].append(point.save_json())
        return data

    def load_json(self, data):
        self.zone_goal_type = STRING_TO_GOAL_TYPE[data['zone_goal_type']]
        self.zone_goal_value = string_to_hash(data['zone_goal_value'])
        self.zone_goal_name = data['zone_goal_name']
        self.zone_goal_delay = data['zone_goal_delay']
        self.zone_goal_has_teleport_registry = data['zone_goal_has_teleport_registry']
        if self.zone_goal_has_teleport_registry:
            self.zone_goal_teleport_registry = string_to_hash(data['zone_goal_teleport_registry'])
        self.zone_goal_dungeon = data['zone_goal_dungeon']
        self.zone_goal_points = []
        for point_data in data['zone_goal_points']:
            point = ArcZoneGoalPoint()
            point.load_json(point_data)
            self.zone_goal_points.append(point)
