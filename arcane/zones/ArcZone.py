#  • ▌ ▄ ·. ▄▄▄▄·     ▄▄▄ .·▄▄▄▄  ▪  ▄▄▄▄▄      ▄▄▄       ▄▄▄·▄▄▄       
#  ·██ ▐███▪▐█ ▀█▪    ▀▄.▀·██▪ ██ ██ •██  ▪     ▀▄ █·    ▐█ ▄█▀▄ █·▪    
#  ▐█ ▌▐▌▐█·▐█▀▀█▄    ▐▀▀▪▄▐█· ▐█▌▐█· ▐█.▪ ▄█▀▄ ▐▀▀▄      ██▀·▐▀▀▄  ▄█▀▄
#  ██ ██▌▐█▌██▄▪▐█    ▐█▄▄▌██. ██ ▐█▌ ▐█▌·▐█▌.▐▌▐█•█▌    ▐█▪·•▐█•█▌▐█▌.▐▌
#  ▀▀  █▪▀▀▀·▀▀▀▀      ▀▀▀ ▀▀▀▀▀• ▀▀▀ ▀▀▀  ▀█▄▀▪.▀  ▀    .▀   .▀  ▀ ▀█▄▀▪
#                Magicbane Emulator Project © 2013 - 2022
#                           www.magicbane.com

from collections import OrderedDict

from arcane.enums.zone.arc_zone import *
from arcane.util import ResStream
from .ArcDungeonInfo import ArcDungeonInfo
from .ArcMobile import ArcMobile
from .ArcProp import ArcProp
from .ArcSoundInfo import ArcSoundInfo
from .ArcTerrainGen import ArcTerrainGen
from .ArcZoneBiomState import ArcZoneBiomState
from .ArcZoneEvent import ArcZoneEvent
from .ArcZoneGoal import ArcZoneGoal
from .TerrainObjectInfo import TerrainObjectInfo
from .WaterInfo import WaterInfo
from .WeatherEventInfo import WeatherEventInfo


class ArcZone:

    def load_binary(self, stream: ResStream):
        self.zone_type = stream.read_dword()
        self.zone_name = stream.read_string()
        self.zone_custom_texture = stream.read_qword()
        self.zone_width_threshold = stream.read_dword()
        self.zone_material_threshold = stream.read_dword()
        self.zone_max_width_index = stream.read_dword()
        self.zone_max_material_index = stream.read_dword()
        self.zone_custom_texture_wrap = stream.read_bool()
        self.zone_peace_zone = stream.read_bool()
        self.zone_guild_zone = stream.read_bool()
        self.zone_minor_radius = stream.read_float()
        self.zone_major_radius = stream.read_float()
        self.zone_min_blend = stream.read_float()
        self.zone_max_blend = stream.read_float()
        self.zone_influence = stream.read_float()
        self.zone_unknown1 = stream.read_float()
        self.zone_y_offset = stream.read_float()
        self.zone_global_height = stream.read_float()
        self.zone_transition_height = stream.read_float()
        self.zone_upper_transition_height = stream.read_float()
        self.zone_tile_cord_type = stream.read_dword()
        self.zone_tile_pattern_prob = stream.read_float()
        self.zone_pattern_type = stream.read_dword()
        self.zone_sea_level_index = stream.read_dword()
        self.zone_sea_level = stream.read_float()
        self.zone_sea_level_type = stream.read_dword()
        self.zone_grad = stream.read_float()
        self.zone_tile_set = stream.read_qword()
        self.zone_song = stream.read_qword()
        self.zone_is_biom = stream.read_bool()
        if self.zone_is_biom:
            self.zone_biom = ArcZoneBiomState()
            self.zone_biom.load_binary(stream)
        num_weather_events = stream.read_dword()
        self.zone_weather_events = [WeatherEventInfo() for _ in range(num_weather_events)]
        for event in self.zone_weather_events:
            event.load_binary(stream)
        self.zone_has_water = stream.read_bool()
        if self.zone_has_water:
            self.zone_water = WaterInfo()
            self.zone_water.load_binary(stream)
        self.zone_has_terrain_gen = stream.read_bool()
        if self.zone_has_terrain_gen:
            self.zone_terrain_gen = ArcTerrainGen()
            self.zone_terrain_gen.load_binary(stream)
        num_patterns = stream.read_dword()
        self.zone_patterns = [
            [
                stream.read_dword(),
                stream.read_float(),
            ] for _ in range(num_patterns)
        ]
        num_alts = stream.read_dword()
        self.zone_alts = [stream.read_float() for _ in range(num_alts)]
        num_terrain_objects = stream.read_dword()
        self.zone_terrain_objects = [TerrainObjectInfo() for _ in range(num_terrain_objects)]
        for obj in self.zone_terrain_objects:
            obj.load_binary(stream)
        num_mobiles = stream.read_dword()
        self.zone_mobile_info = [ArcMobile() for _ in range(num_mobiles)]
        for mobile in self.zone_mobile_info:
            mobile.load_binary(stream)
        num_sounds = stream.read_dword()
        self.zone_sound_info = [ArcSoundInfo() for _ in range(num_sounds)]
        for sound in self.zone_sound_info:
            sound.load_binary(stream)
        num_dungeons = stream.read_dword()
        self.zone_dungeon_info = [ArcDungeonInfo() for _ in range(num_dungeons)]
        for dungeon in self.zone_dungeon_info:
            dungeon.load_binary(stream)
        num_props = stream.read_dword()
        self.zone_prop_info = [ArcProp() for _ in range(num_props)]
        for prop in self.zone_prop_info:
            prop.load_binary(stream)
        num_architectures = stream.read_dword()
        self.zone_architecture = [stream.read_string() for _ in range(num_architectures)]
        num_events = stream.read_dword()
        self.zone_events = [ArcZoneEvent() for _ in range(num_events)]
        for event in self.zone_events:
            event.load_binary(stream)
        num_point_sets = stream.read_dword()
        self.zone_point_sets = [ArcZoneGoal() for _ in range(num_point_sets)]
        for point_set in self.zone_point_sets:
            point_set.load_binary(stream)
        self.zone_has_layers = stream.read_bool()
        if self.zone_has_layers:
            self.zone_base_texture = stream.read_qword()
            num_layer_texture_ids = stream.read_dword()
            self.zone_layer_texture_ids = [stream.read_qword() for _ in range(num_layer_texture_ids)]
            num_layer_mappings = stream.read_dword()
            self.zone_layer_mappings = []
            for _ in range(num_layer_mappings):
                layer = stream.read_qword()
                num = stream.read_dword()
                textures = [stream.read_qword() for _ in range(num)]
                self.zone_layer_mappings.append([layer, textures])
        else:
            num_textures = stream.read_dword()
            self.zone_textures = [
                [
                    stream.read_qword(),
                    stream.read_float(),
                    stream.read_float(),
                    stream.read_float(),
                    stream.read_float(),
                    stream.read_float(),
                    stream.read_dword(),
                    stream.read_dword(),
                    stream.read_dword(),
                ] for _ in range(num_textures)
            ]

    def save_binary(self, stream: ResStream):
        stream.write_dword(self.zone_type)
        stream.write_string(self.zone_name)
        stream.write_qword(self.zone_custom_texture)
        stream.write_dword(self.zone_width_threshold)
        stream.write_dword(self.zone_material_threshold)
        stream.write_dword(self.zone_max_width_index)
        stream.write_dword(self.zone_max_material_index)
        stream.write_bool(self.zone_custom_texture_wrap)
        stream.write_bool(self.zone_peace_zone)
        stream.write_bool(self.zone_guild_zone)
        stream.write_float(self.zone_minor_radius)
        stream.write_float(self.zone_major_radius)
        stream.write_float(self.zone_min_blend)
        stream.write_float(self.zone_max_blend)
        stream.write_float(self.zone_influence)
        stream.write_float(self.zone_unknown1)
        stream.write_float(self.zone_y_offset)
        stream.write_float(self.zone_global_height)
        stream.write_float(self.zone_transition_height)
        stream.write_float(self.zone_upper_transition_height)
        stream.write_dword(self.zone_tile_cord_type)
        stream.write_float(self.zone_tile_pattern_prob)
        stream.write_dword(self.zone_pattern_type)
        stream.write_dword(self.zone_sea_level_index)
        stream.write_float(self.zone_sea_level)
        stream.write_dword(self.zone_sea_level_type)
        stream.write_float(self.zone_grad)
        stream.write_qword(self.zone_tile_set)
        stream.write_qword(self.zone_song)
        stream.write_bool(self.zone_is_biom)
        if self.zone_is_biom:
            self.zone_biom.save_binary(stream)
        stream.write_dword(len(self.zone_weather_events))
        for event in self.zone_weather_events:
            event.save_binary(stream)
        stream.write_bool(self.zone_has_water)
        if self.zone_has_water:
            self.zone_water.save_binary(stream)
        stream.write_bool(self.zone_has_terrain_gen)
        if self.zone_has_terrain_gen:
            self.zone_terrain_gen.save_binary(stream)
        stream.write_dword(len(self.zone_patterns))
        for pattern in self.zone_patterns:
            stream.write_dword(pattern[0])
            stream.write_float(pattern[1])
        stream.write_dword(len(self.zone_alts))
        for alt in self.zone_alts:
            stream.write_float(alt)
        stream.write_dword(len(self.zone_terrain_objects))
        for obj in self.zone_terrain_objects:
            obj.save_binary(stream)
        stream.write_dword(len(self.zone_mobile_info))
        for mobile in self.zone_mobile_info:
            mobile.save_binary(stream)
        stream.write_dword(len(self.zone_sound_info))
        for sound in self.zone_sound_info:
            sound.save_binary(stream)
        stream.write_dword(len(self.zone_dungeon_info))
        for dungeon in self.zone_dungeon_info:
            dungeon.save_binary(stream)
        stream.write_dword(len(self.zone_prop_info))
        for prop in self.zone_prop_info:
            prop.save_binary(stream)
        stream.write_dword(len(self.zone_architecture))
        for arch in self.zone_architecture:
            stream.write_string(arch)
        stream.write_dword(len(self.zone_events))
        for event in self.zone_events:
            event.save_binary(stream)
        stream.write_dword(len(self.zone_point_sets))
        for point_set in self.zone_point_sets:
            point_set.save_binary(stream)

        stream.write_bool(self.zone_has_layers)
        if self.zone_has_layers:
            stream.write_qword(self.zone_base_texture)
            stream.write_dword(len(self.zone_layer_texture_ids))
            for texture_id in self.zone_layer_texture_ids:
                stream.write_qword(texture_id)

            stream.write_dword(len(self.zone_layer_mappings))
            for layer, textures in self.zone_layer_mappings:
                stream.write_qword(layer)
                stream.write_dword(len(textures))
                for texture in textures:
                    stream.write_qword(texture)
        else:
            stream.write_dword(len(self.zone_textures))
            for texture in self.zone_textures:
                stream.write_qword(texture[0])
                stream.write_float(texture[1])
                stream.write_float(texture[2])
                stream.write_float(texture[3])
                stream.write_float(texture[4])
                stream.write_float(texture[5])
                stream.write_dword(texture[6])
                stream.write_dword(texture[7])
                stream.write_dword(texture[8])

    def save_json(self):
        data = OrderedDict()
        data['zone_type'] = ZONE_TO_STRING[self.zone_type]
        data['zone_name'] = self.zone_name
        data['zone_custom_texture'] = self.zone_custom_texture
        data['zone_width_threshold'] = self.zone_width_threshold
        data['zone_material_threshold'] = self.zone_material_threshold
        data['zone_max_width_index'] = self.zone_max_width_index
        data['zone_max_material_index'] = self.zone_max_material_index
        data['zone_custom_texture_wrap'] = self.zone_custom_texture_wrap
        data['zone_peace_zone'] = self.zone_peace_zone
        data['zone_guild_zone'] = self.zone_guild_zone
        data['zone_minor_radius'] = self.zone_minor_radius
        data['zone_major_radius'] = self.zone_major_radius
        data['zone_min_blend'] = self.zone_min_blend
        data['zone_max_blend'] = self.zone_max_blend
        data['zone_influence'] = self.zone_influence
        data['zone_unknown1'] = self.zone_unknown1
        data['zone_y_offset'] = self.zone_y_offset
        data['zone_global_height'] = self.zone_global_height
        data['zone_transition_height'] = self.zone_transition_height
        data['zone_upper_transition_height'] = self.zone_upper_transition_height
        data['zone_tile_cord_type'] = TILECOORD_TO_STRING[self.zone_tile_cord_type]
        data['zone_tile_pattern_prob'] = self.zone_tile_pattern_prob
        data['zone_pattern_type'] = PATTERN_TO_STRING[self.zone_pattern_type]
        data['zone_sea_level_index'] = self.zone_sea_level_index
        data['zone_sea_level'] = self.zone_sea_level
        data['zone_sea_level_type'] = SEALEVEL_TO_STRING[self.zone_sea_level_type]
        data['zone_grad'] = self.zone_grad
        data['zone_tile_set'] = self.zone_tile_set
        data['zone_song'] = self.zone_song
        data['zone_is_biom'] = self.zone_is_biom
        if self.zone_is_biom:
            data['zone_biom'] = self.zone_biom.save_json()
        data['zone_weather_events'] = []
        for event in self.zone_weather_events:
            data['zone_weather_events'].append(event.save_json())
        data['zone_has_water'] = self.zone_has_water
        if self.zone_has_water:
            data['zone_water'] = self.zone_water.save_json()
        data['zone_has_terrain_gen'] = self.zone_has_terrain_gen
        if self.zone_has_terrain_gen:
            data['zone_terrain_gen'] = self.zone_terrain_gen.save_json()
        data['zone_patterns'] = self.zone_patterns
        data['zone_alts'] = self.zone_alts
        data['zone_terrain_objects'] = []
        for obj in self.zone_terrain_objects:
            data['zone_terrain_objects'].append(obj.save_json())
        data['zone_mobile_info'] = []
        for mobile in self.zone_mobile_info:
            data['zone_mobile_info'].append(mobile.save_json())
        data['zone_sound_info'] = []
        for sound in self.zone_sound_info:
            data['zone_sound_info'].append(sound.save_json())
        data['zone_dungeon_info'] = []
        for dungeon in self.zone_dungeon_info:
            data['zone_dungeon_info'].append(dungeon.save_json())
        data['zone_prop_info'] = []
        for prop in self.zone_prop_info:
            data['zone_prop_info'].append(prop.save_json())
        data['zone_architecture'] = self.zone_architecture
        data['zone_events'] = []
        for event in self.zone_events:
            data['zone_events'].append(event.save_json())
        data['zone_point_sets'] = []
        for point_set in self.zone_point_sets:
            data['zone_point_sets'].append(point_set.save_json())
        data['zone_has_layers'] = self.zone_has_layers
        if self.zone_has_layers:
            data['zone_base_texture'] = self.zone_base_texture
            data['zone_layer_texture_ids'] = self.zone_layer_texture_ids
            data['zone_layer_mappings'] = self.zone_layer_mappings
        else:
            data['zone_textures'] = self.zone_textures
        return data

    def load_json(self, data):
        self.zone_type = STRING_TO_ZONE[data['zone_type']]
        self.zone_name = data['zone_name']
        self.zone_custom_texture = data['zone_custom_texture']
        self.zone_width_threshold = data['zone_width_threshold']
        self.zone_material_threshold = data['zone_material_threshold']
        self.zone_max_width_index = data['zone_max_width_index']
        self.zone_max_material_index = data['zone_max_material_index']
        self.zone_custom_texture_wrap = data['zone_custom_texture_wrap']
        self.zone_peace_zone = data['zone_peace_zone']
        self.zone_guild_zone = data['zone_guild_zone']
        self.zone_minor_radius = data['zone_minor_radius']
        self.zone_major_radius = data['zone_major_radius']
        self.zone_min_blend = data['zone_min_blend']
        self.zone_max_blend = data['zone_max_blend']
        self.zone_influence = data['zone_influence']
        self.zone_unknown1 = data['zone_unknown1']
        self.zone_y_offset = data['zone_y_offset']
        self.zone_global_height = data['zone_global_height']
        self.zone_transition_height = data['zone_transition_height']
        self.zone_upper_transition_height = data['zone_upper_transition_height']
        self.zone_tile_cord_type = STRING_TO_TILECOORD[data['zone_tile_cord_type']]
        self.zone_tile_pattern_prob = data['zone_tile_pattern_prob']
        self.zone_pattern_type = STRING_TO_PATTERN[data['zone_pattern_type']]
        self.zone_sea_level_index = data['zone_sea_level_index']
        self.zone_sea_level = data['zone_sea_level']
        self.zone_sea_level_type = STRING_TO_SEALEVEL[data['zone_sea_level_type']]
        self.zone_grad = data['zone_grad']
        self.zone_tile_set = data['zone_tile_set']
        self.zone_song = data['zone_song']
        self.zone_is_biom = data['zone_is_biom']
        if self.zone_is_biom:
            self.zone_biom = ArcZoneBiomState()
            self.zone_biom.load_json(data['zone_biom'])
        self.zone_weather_events = []
        for event_data in data['zone_weather_events']:
            event = WeatherEventInfo()
            event.load_json(event_data)
            self.zone_weather_events.append(event)
        self.zone_has_water = data['zone_has_water']
        if self.zone_has_water:
            self.zone_water = WaterInfo()
            self.zone_water.load_json(data['zone_water'])
        self.zone_has_terrain_gen = data['zone_has_terrain_gen']
        if self.zone_has_terrain_gen:
            self.zone_terrain_gen = ArcTerrainGen()
            self.zone_terrain_gen.load_json(data['zone_terrain_gen'])
        self.zone_patterns = data['zone_patterns']
        self.zone_alts = data['zone_alts']
        self.zone_terrain_objects = []
        for obj_data in data['zone_terrain_objects']:
            obj = TerrainObjectInfo()
            obj.load_json(obj_data)
            self.zone_terrain_objects.append(obj)
        self.zone_mobile_info = []
        for mobile_data in data['zone_mobile_info']:
            mobile = ArcMobile()
            mobile.load_json(mobile_data)
            self.zone_mobile_info.append(mobile)
        self.zone_sound_info = []
        for sound_data in data['zone_sound_info']:
            sound = ArcSoundInfo()
            sound.load_json(sound_data)
            self.zone_sound_info.append(sound)
        self.zone_dungeon_info = []
        for dungeon_data in data['zone_dungeon_info']:
            dungeon = ArcDungeonInfo()
            dungeon.load_json(dungeon_data)
            self.zone_dungeon_info.append(dungeon)
        self.zone_prop_info = []
        for prop_data in data['zone_prop_info']:
            prop = ArcProp()
            prop.load_json(prop_data)
            self.zone_prop_info.append(prop)
        self.zone_architecture = data['zone_architecture']
        self.zone_events = []
        for event_data in data['zone_events']:
            event = ArcZoneEvent()
            event.load_json(event_data)
            self.zone_events.append(event)
        self.zone_point_sets = []
        for point_set_data in data['zone_point_sets']:
            point_set = ArcZoneGoal()
            point_set.load_json(point_set_data)
            self.zone_point_sets.append(point_set)
        self.zone_has_layers = data['zone_has_layers']
        if self.zone_has_layers:
            self.zone_base_texture = data['zone_base_texture']
            self.zone_layer_texture_ids = data['zone_layer_texture_ids']
            self.zone_layer_mappings = data['zone_layer_mappings']
        else:
            self.zone_textures = data['zone_textures']
