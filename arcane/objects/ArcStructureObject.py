#  • ▌ ▄ ·. ▄▄▄▄·     ▄▄▄ .·▄▄▄▄  ▪  ▄▄▄▄▄      ▄▄▄       ▄▄▄·▄▄▄       
#  ·██ ▐███▪▐█ ▀█▪    ▀▄.▀·██▪ ██ ██ •██  ▪     ▀▄ █·    ▐█ ▄█▀▄ █·▪    
#  ▐█ ▌▐▌▐█·▐█▀▀█▄    ▐▀▀▪▄▐█· ▐█▌▐█· ▐█.▪ ▄█▀▄ ▐▀▀▄      ██▀·▐▀▀▄  ▄█▀▄
#  ██ ██▌▐█▌██▄▪▐█    ▐█▄▄▌██. ██ ▐█▌ ▐█▌·▐█▌.▐▌▐█•█▌    ▐█▪·•▐█•█▌▐█▌.▐▌
#  ▀▀  █▪▀▀▀·▀▀▀▀      ▀▀▀ ▀▀▀▀▀• ▀▀▀ ▀▀▀  ▀█▄▀▪.▀  ▀    .▀   .▀  ▀ ▀█▄▀▪
#                Magicbane Emulator Project © 2013 - 2022
#                           www.magicbane.com

from collections import OrderedDict

from arcane.enums.arc_structure import *
from arcane.util import ResStream
from .ArcDoorObject import ArcDoorObject
from .ArcStaticObject import ArcStaticObject


class Region:
    def load_binary(self, stream: ResStream):
        num_points = stream.read_dword()
        self.region_points = [
            stream.read_tuple() for _ in range(num_points)
        ]
        self.region_render_scale = stream.read_tuple()
        self.region_content_behavior = stream.read_dword()
        self.region_state = stream.read_dword()
        self.region_render_flipped = stream.read_bool()
        self.region_has_stairs = stream.read_bool()
        if self.region_has_stairs:
            self.region_stairs = [
                stream.read_byte(),
                stream.read_byte()
            ]
        self.region_unknown2 = stream.read_byte()
        self.region_unknown3 = stream.read_byte()
        self.region_unknown4 = stream.read_tuple()

    def save_binary(self, stream: ResStream):
        stream.write_dword(len(self.region_points))
        for point in self.region_points:
            stream.write_tuple(point)
        stream.write_tuple(self.region_render_scale)
        stream.write_dword(self.region_content_behavior)
        stream.write_dword(self.region_state)
        stream.write_bool(self.region_render_flipped)
        stream.write_bool(self.region_has_stairs)
        if self.region_has_stairs:
            stream.write_byte(self.region_stairs[0])
            stream.write_byte(self.region_stairs[1])
        stream.write_byte(self.region_unknown2)
        stream.write_byte(self.region_unknown3)
        stream.write_tuple(self.region_unknown4)

    def load_json(self, data):
        self.region_points = data['region_points']
        self.region_render_scale = data['region_render_scale']
        self.region_content_behavior = STRING_TO_REGION_CONTENTBEHAVIOR[
            data['region_content_behavior']
        ]
        self.region_state = STRING_TO_REGION_STATE[data['region_state']]
        self.region_render_flipped = data['region_render_flipped']
        self.region_has_stairs = data['region_has_stairs']
        if self.region_has_stairs:
            self.region_stairs = data['region_stairs']
        self.region_unknown2 = data['region_unknown2']
        self.region_unknown3 = data['region_unknown3']
        self.region_unknown4 = data['region_unknown4']

    def save_json(self):
        data = OrderedDict()
        data['region_points'] = self.region_points
        data['region_render_scale'] = self.region_render_scale
        data['region_content_behavior'] = REGION_CONTENTBEHAVIOR_TO_STRING[
            self.region_content_behavior
        ]
        data['region_state'] = REGION_STATE_TO_STRING[self.region_state]
        data['region_render_flipped'] = self.region_render_flipped
        data['region_has_stairs'] = self.region_has_stairs
        if self.region_has_stairs:
            data['region_stairs'] = self.region_stairs
        data['region_unknown2'] = self.region_unknown2
        data['region_unknown3'] = self.region_unknown3
        data['region_unknown4'] = self.region_unknown4
        return data


class Room:
    def load_binary(self, stream: ResStream):
        num_regions = stream.read_dword()
        self.room_regions = [Region() for _ in range(num_regions)]
        for region in self.room_regions:
            region.load_binary(stream)

    def save_binary(self, stream: ResStream):
        stream.write_dword(len(self.room_regions))
        for region in self.room_regions:
            region.save_binary(stream)

    def load_json(self, data):
        self.room_regions = []
        for region_data in data:
            region = Region()
            region.load_json(region_data)
            self.room_regions.append(region)

    def save_json(self):
        data = []
        for region in self.room_regions:
            data.append(region.save_json())
        return data


class Floor:
    def load_binary(self, stream: ResStream):
        self.floor_level_number = stream.read_dword()
        num_exits = stream.read_dword()
        self.floor_exits = [Region() for _ in range(num_exits)]
        for exit in self.floor_exits:
            exit.load_binary(stream)
        num_regions = stream.read_dword()
        self.floor_rooms = [Room() for _ in range(num_regions)]
        for room in self.floor_rooms:
            room.load_binary(stream)

    def save_binary(self, stream: ResStream):
        stream.write_dword(self.floor_level_number)
        stream.write_dword(len(self.floor_exits))
        for exit in self.floor_exits:
            exit.save_binary(stream)
        stream.write_dword(len(self.floor_rooms))
        for room in self.floor_rooms:
            room.save_binary(stream)

    def load_json(self, data):
        self.floor_level_number = data['floor_level_number']
        self.floor_exits = []
        for exit_data in data['floor_exits']:
            exit = Region()
            exit.load_json(exit_data)
            self.floor_exits.append(exit)
        self.floor_rooms = []
        for room_data in data['floor_rooms']:
            room = Room()
            room.load_json(room_data)
            self.floor_rooms.append(room)

    def save_json(self):
        data = OrderedDict()
        data['floor_level_number'] = self.floor_level_number
        data['floor_exits'] = []
        for exit in self.floor_exits:
            data['floor_exits'].append(exit.save_json())
        data['floor_rooms'] = []
        for room in self.floor_rooms:
            data['floor_rooms'].append(room.save_json())
        return data


class Hole:
    def load_binary(self, stream: ResStream):
        num_edges = stream.read_dword()
        self.hole_edges = [
            [
                stream.read_tuple(),
                stream.read_tuple()
            ] for _ in range(num_edges)
        ]

    def save_binary(self, stream: ResStream):
        stream.write_dword(len(self.hole_edges))
        for edge in self.hole_edges:
            stream.write_tuple(edge[0])
            stream.write_tuple(edge[1])

    def load_json(self, data):
        self.hole_edges = []
        for edge in data:
            self.hole_edges.append(edge)

    def save_json(self):
        data = []
        for edge in self.hole_edges:
            data.append(edge)
        return data


class Level:
    def load_binary(self, stream: ResStream):
        self.level_number = stream.read_dword()
        self.level_type = stream.read_bool()
        self.level_value = stream.read_qword()

    def save_binary(self, stream: ResStream):
        stream.write_dword(self.level_number)
        stream.write_bool(self.level_type)
        stream.write_qword(self.level_value)

    def load_json(self, data):
        self.level_number = data['level_number']
        self.level_type = STRING_TO_LEVEL_TYPE[data['level_type']]
        self.level_value = data['level_value']

    def save_json(self):
        data = OrderedDict()
        data['level_number'] = self.level_number
        data['level_type'] = LEVEL_TYPE_TO_STRING[self.level_type]
        data['level_value'] = self.level_value
        return data


class RegionTrigger:
    def load_binary(self, stream: ResStream):
        self.trigger_class_name = stream.read_string()
        self.trigger_parameters = stream.read_string()
        self.trigger_level_number = stream.read_dword()
        self.trigger_room_number = stream.read_dword()
        self.trigger_region_number = stream.read_dword()

    def save_binary(self, stream: ResStream):
        stream.write_string(self.trigger_class_name)
        stream.write_string(self.trigger_parameters)
        stream.write_dword(self.trigger_level_number)
        stream.write_dword(self.trigger_room_number)
        stream.write_dword(self.trigger_region_number)

    def load_json(self, data):
        self.trigger_class_name = data['trigger_class_name']
        self.trigger_parameters = data['trigger_parameters']
        self.trigger_level_number = data['trigger_level_number']
        self.trigger_room_number = data['trigger_room_number']
        self.trigger_region_number = data['trigger_region_number']

    def save_json(self):
        data = OrderedDict()
        data['trigger_class_name'] = self.trigger_class_name
        data['trigger_parameters'] = self.trigger_parameters
        data['trigger_level_number'] = self.trigger_level_number
        data['trigger_room_number'] = self.trigger_room_number
        data['trigger_region_number'] = self.trigger_region_number
        return data


class ArcStructureObject(ArcStaticObject):
    def load_binary(self, stream: ResStream):
        super().load_binary(stream)
        length = stream.read_dword()
        self.structure_floors = [Floor() for _ in range(length)]
        for floor in self.structure_floors:
            floor.load_binary(stream)
        num_holes = stream.read_dword()
        self.structure_holes = [Hole() for _ in range(num_holes)]
        for hole in self.structure_holes:
            hole.load_binary(stream)
        num_levels = stream.read_dword()
        self.structure_levels = [Level() for _ in range(num_levels)]
        for level in self.structure_levels:
            level.load_binary(stream)
        num_doors = stream.read_dword()
        self.structure_doors = [ArcDoorObject() for _ in range(num_doors)]
        for door in self.structure_doors:
            door.load_binary(stream)
        num_region_triggers = stream.read_dword()
        self.structure_region_triggers = [RegionTrigger() for _ in range(num_region_triggers)]
        for trigger in self.structure_region_triggers:
            trigger.load_binary(stream)

    def save_binary(self, stream: ResStream):
        super().save_binary(stream)
        stream.write_dword(len(self.structure_floors))
        for floor in self.structure_floors:
            floor.save_binary(stream)
        stream.write_dword(len(self.structure_holes))
        for hole in self.structure_holes:
            hole.save_binary(stream)
        stream.write_dword(len(self.structure_levels))
        for level in self.structure_levels:
            level.save_binary(stream)
        stream.write_dword(len(self.structure_doors))
        for door in self.structure_doors:
            door.save_binary(stream)
        stream.write_dword(len(self.structure_region_triggers))
        for trigger in self.structure_region_triggers:
            trigger.save_binary(stream)

    def load_json(self, data):
        super().load_json(data)
        self.structure_floors = []
        for floor_data in data['structure_floors']:
            floor = Floor()
            floor.load_json(floor_data)
            self.structure_floors.append(floor)
        self.structure_holes = []
        for hole_data in data['structure_holes']:
            hole = Hole()
            hole.load_json(hole_data)
            self.structure_holes.append(hole)
        self.structure_levels = []
        for level_data in data['structure_levels']:
            level = Level()
            level.load_json(level_data)
            self.structure_levels.append(level)
        self.structure_doors = []
        for door_data in data['structure_doors']:
            door = ArcDoorObject()
            door.load_json(door_data)
            self.structure_doors.append(door)
        self.structure_region_triggers = []
        for trigger_data in data['structure_region_triggers']:
            trigger = RegionTrigger()
            trigger.load_json(trigger_data)
            self.structure_region_triggers.append(trigger)
        return data

    def save_json(self):
        data = super().save_json()
        data['structure_floors'] = []
        for floor in self.structure_floors:
            data['structure_floors'].append(floor.save_json())
        data['structure_holes'] = []
        for hole in self.structure_holes:
            data['structure_holes'].append(hole.save_json())
        data['structure_levels'] = []
        for level in self.structure_levels:
            data['structure_levels'].append(level.save_json())
        data['structure_doors'] = []
        for door in self.structure_doors:
            data['structure_doors'].append(door.save_json())
        data['structure_region_triggers'] = []
        for trigger in self.structure_region_triggers:
            data['structure_region_triggers'].append(trigger.save_json())
        return data
