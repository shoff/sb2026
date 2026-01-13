#  • ▌ ▄ ·. ▄▄▄▄·     ▄▄▄ .·▄▄▄▄  ▪  ▄▄▄▄▄      ▄▄▄       ▄▄▄·▄▄▄       
#  ·██ ▐███▪▐█ ▀█▪    ▀▄.▀·██▪ ██ ██ •██  ▪     ▀▄ █·    ▐█ ▄█▀▄ █·▪    
#  ▐█ ▌▐▌▐█·▐█▀▀█▄    ▐▀▀▪▄▐█· ▐█▌▐█· ▐█.▪ ▄█▀▄ ▐▀▀▄      ██▀·▐▀▀▄  ▄█▀▄
#  ██ ██▌▐█▌██▄▪▐█    ▐█▄▄▌██. ██ ▐█▌ ▐█▌·▐█▌.▐▌▐█•█▌    ▐█▪·•▐█•█▌▐█▌.▐▌
#  ▀▀  █▪▀▀▀·▀▀▀▀      ▀▀▀ ▀▀▀▀▀• ▀▀▀ ▀▀▀  ▀█▄▀▪.▀  ▀    .▀   .▀  ▀ ▀█▄▀▪
#                Magicbane Emulator Project © 2013 - 2022
#                           www.magicbane.com

from collections import OrderedDict

from arcane.util import ResStream


class RankInfo:
    def load_binary(self, stream: ResStream):
        self.rank_hirelings = stream.read_dword()
        self.rank_shrines = stream.read_dword()
        self.rank_spires = stream.read_dword()
        self.rank_barracks = stream.read_dword()
        self.rank_rank = stream.read_dword()
        self.rank_health = stream.read_dword()
        self.rank_automatic = stream.read_bool()
        self.rank_energy_k1 = stream.read_float()
        self.rank_energy_k2 = stream.read_float()
        self.rank_level_val = stream.read_float()
        num_builiding_ids = stream.read_dword()
        self.rank_building_id = [
            [
                stream.read_dword(),
                stream.read_qword(),
            ] for _ in range(num_builiding_ids)
        ]
        self.rank_formula = stream.read_dword()
        num_placement_limits = stream.read_dword()
        self.rank_placement_limit = [
            [
                stream.read_dword(),
                stream.read_dword(),
            ] for _ in range(num_placement_limits)
        ]

    def save_binary(self, stream: ResStream):
        stream.write_dword(self.rank_hirelings)
        stream.write_dword(self.rank_shrines)
        stream.write_dword(self.rank_spires)
        stream.write_dword(self.rank_barracks)
        stream.write_dword(self.rank_rank)
        stream.write_dword(self.rank_health)
        stream.write_bool(self.rank_automatic)
        stream.write_float(self.rank_energy_k1)
        stream.write_float(self.rank_energy_k2)
        stream.write_float(self.rank_level_val)
        stream.write_dword(len(self.rank_building_id))
        for building in self.rank_building_id:
            stream.write_dword(building[0])
            stream.write_qword(building[1])
        stream.write_dword(self.rank_formula)
        stream.write_dword(len(self.rank_placement_limit))
        for placement in self.rank_placement_limit:
            stream.write_dword(placement[0])
            stream.write_dword(placement[1])

    def load_json(self, data):
        self.rank_hirelings = data['rank_hirelings']
        self.rank_shrines = data['rank_shrines']
        self.rank_spires = data['rank_spires']
        self.rank_barracks = data['rank_barracks']
        self.rank_rank = data['rank_rank']
        self.rank_health = data['rank_health']
        self.rank_automatic = data['rank_automatic']
        self.rank_energy_k1 = data['rank_energy_k1']
        self.rank_energy_k2 = data['rank_energy_k2']
        self.rank_level_val = data['rank_level_val']
        self.rank_building_id = data['rank_building_id']
        self.rank_formula = data['rank_formula']
        self.rank_placement_limit = data['rank_placement_limit']

    def save_json(self):
        data = OrderedDict()
        data['rank_hirelings'] = self.rank_hirelings
        data['rank_shrines'] = self.rank_shrines
        data['rank_spires'] = self.rank_spires
        data['rank_barracks'] = self.rank_barracks
        data['rank_rank'] = self.rank_rank
        data['rank_health'] = self.rank_health
        data['rank_automatic'] = self.rank_automatic
        data['rank_energy_k1'] = self.rank_energy_k1
        data['rank_energy_k2'] = self.rank_energy_k2
        data['rank_level_val'] = self.rank_level_val
        data['rank_building_id'] = self.rank_building_id
        data['rank_formula'] = self.rank_formula
        data['rank_placement_limit'] = self.rank_placement_limit
        return data


class ArcCityAssetTemplate():
    def load_binary(self, stream: ResStream):
        self.template_max_ranks = stream.read_dword()
        self.template_start_rank = stream.read_dword()
        self.template_asset_type = stream.read_dword()
        self.template_trade_icon = stream.read_dword()
        self.template_landmark = stream.read_dword()
        self.template_is_maintenance = stream.read_bool()
        self.template_has_keys = stream.read_bool()
        self.template_use_hardpoints = stream.read_bool()
        self.template_is_fort_asset = stream.read_bool()
        self.template_is_building_of_war = stream.read_bool()
        self.template_bow_can_place_on_grid = stream.read_bool()
        self.template_requires_nation_tree_slot = stream.read_bool()
        self.template_requires_guild_tree_slot = stream.read_bool()
        self.template_use_fort_grid = stream.read_bool()
        self.template_is_fort_start = stream.read_bool()
        self.template_is_cap_asset = stream.read_bool()
        self.template_zone_no_build = [
            stream.read_float(),
            stream.read_float(),
        ]
        self.template_zone_influence = [
            stream.read_float(),
            stream.read_float(),
        ]
        self.template_eject_loc = stream.read_tuple()
        self.template_npc_load = stream.read_tuple()
        self.template_fort_grid_offset = stream.read_tuple()
        self.template_power_action_id = stream.read_dword()
        self.template_zone_flag = stream.read_dword()
        self.template_spire_event_rule = stream.read_dword()
        self.template_maintenance_set = stream.read_dword()
        self.template_damage_set = stream.read_dword()
        self.template_energy_set = stream.read_dword()
        self.template_use_trigger = stream.read_string()

        self.template_unknown_check1 = stream.read_bool()
        if self.template_unknown_check1:
            pass
        self.template_loot_trigger = stream.read_string()

        self.template_unknown_check2 = stream.read_bool()
        if self.template_unknown_check2:
            pass

        self.has_embedded_template = stream.read_bool()
        if self.has_embedded_template:
            self.template_embed_template = ArcCityAssetTemplate()
            self.template_embed_template.load_binary(stream)
        num_creators = stream.read_dword()
        self.template_creator = [
            stream.read_dword() for _ in range(num_creators)
        ]
        num_terrains = stream.read_dword()
        self.template_terrain = [
            stream.read_dword() for _ in range(num_terrains)
        ]
        num_valid_npc_types = stream.read_dword()
        self.template_valid_npc_type = [
            stream.read_dword() for _ in range(num_valid_npc_types)
        ]
        num_valid_npc_cat = stream.read_dword()
        self.template_valid_npc_cat = [
            stream.read_dword() for _ in range(num_valid_npc_cat)
        ]
        num_rank_info = stream.read_dword()
        self.template_rank_info = [RankInfo() for _ in range(num_rank_info)]
        for rank_info in self.template_rank_info:
            rank_info.load_binary(stream)
        num_cap_info = stream.read_dword()
        self.template_cap_info = [
            [
                stream.read_dword(),
                stream.read_dword(),
                stream.read_qword(),
            ] for _ in range(num_cap_info)
        ]
        num_event_rules = stream.read_dword()
        self.template_event_rules = [
            [
                stream.read_dword(),
                stream.read_dword(),
            ] for _ in range(num_event_rules)
        ]
        num_archs = stream.read_dword()
        self.template_architecture = [
            stream.read_string() for _ in range(num_archs)
        ]
        self.template_offering_type = stream.read_string()
        self.template_placement_type = stream.read_dword()
        num_offering_adjusts = stream.read_dword()
        self.template_offering_adjustment = [
            [
                stream.read_dword(),
                stream.read_float(),
            ] for _ in range(num_offering_adjusts)
        ]
        num_resource_limit = stream.read_dword()
        self.template_resource_limit = [
            [
                stream.read_dword(),
                stream.read_dword(),
                stream.read_dword(),
            ] for _ in range(num_resource_limit)
        ]
        self.template_unknown = stream.read_dword()

    def save_binary(self, stream: ResStream):
        stream.write_dword(self.template_max_ranks)
        stream.write_dword(self.template_start_rank)
        stream.write_dword(self.template_asset_type)
        stream.write_dword(self.template_trade_icon)
        stream.write_dword(self.template_landmark)
        stream.write_bool(self.template_is_maintenance)
        stream.write_bool(self.template_has_keys)
        stream.write_bool(self.template_use_hardpoints)
        stream.write_bool(self.template_is_fort_asset)
        stream.write_bool(self.template_is_building_of_war)
        stream.write_bool(self.template_bow_can_place_on_grid)
        stream.write_bool(self.template_requires_nation_tree_slot)
        stream.write_bool(self.template_requires_guild_tree_slot)
        stream.write_bool(self.template_use_fort_grid)
        stream.write_bool(self.template_is_fort_start)
        stream.write_bool(self.template_is_cap_asset)
        stream.write_float(self.template_zone_no_build[0])
        stream.write_float(self.template_zone_no_build[1])
        stream.write_float(self.template_zone_influence[0])
        stream.write_float(self.template_zone_influence[1])
        stream.write_tuple(self.template_eject_loc)
        stream.write_tuple(self.template_npc_load)
        stream.write_tuple(self.template_fort_grid_offset)
        stream.write_dword(self.template_power_action_id)
        stream.write_dword(self.template_zone_flag)
        stream.write_dword(self.template_spire_event_rule)
        stream.write_dword(self.template_maintenance_set)
        stream.write_dword(self.template_damage_set)
        stream.write_dword(self.template_energy_set)
        stream.write_string(self.template_use_trigger)
        stream.write_bool(self.template_unknown_check1)
        stream.write_string(self.template_loot_trigger)
        stream.write_bool(self.template_unknown_check2)
        stream.write_bool(self.has_embedded_template)
        if self.has_embedded_template:
            self.template_embed_template.save_binary(stream)
        stream.write_dword(len(self.template_creator))
        for creator in self.template_creator:
            stream.write_dword(creator)
        stream.write_dword(len(self.template_terrain))
        for terrain in self.template_terrain:
            stream.write_dword(terrain)
        stream.write_dword(len(self.template_valid_npc_type))
        for npc_type in self.template_valid_npc_type:
            stream.write_dword(npc_type)
        stream.write_dword(len(self.template_valid_npc_cat))
        for npc_cat in self.template_valid_npc_cat:
            stream.write_dword(npc_cat)
        stream.write_dword(len(self.template_rank_info))
        for rank_info in self.template_rank_info:
            rank_info.save_binary(stream)
        stream.write_dword(len(self.template_cap_info))
        for cap in self.template_cap_info:
            stream.write_dword(cap[0])
            stream.write_dword(cap[1])
            stream.write_qword(cap[2])
        stream.write_dword(len(self.template_event_rules))
        for event in self.template_event_rules:
            stream.write_dword(event[0])
            stream.write_dword(event[1])
        stream.write_dword(len(self.template_architecture))
        for arch in self.template_architecture:
            stream.write_string(arch)
        stream.write_string(self.template_offering_type)
        stream.write_dword(self.template_placement_type)
        stream.write_dword(len(self.template_offering_adjustment))
        for adjust in self.template_offering_adjustment:
            stream.write_dword(adjust[0])
            stream.write_float(adjust[1])
        stream.write_dword(len(self.template_resource_limit))
        for resource in self.template_resource_limit:
            stream.write_dword(resource[0])
            stream.write_dword(resource[1])
            stream.write_dword(resource[2])
        stream.write_dword(self.template_unknown)

    def load_json(self, data):
        self.template_max_ranks = data['template_max_ranks']
        self.template_start_rank = data['template_start_rank']
        self.template_asset_type = data['template_asset_type']
        self.template_trade_icon = data['template_trade_icon']
        self.template_landmark = data['template_landmark']
        self.template_is_maintenance = data['template_is_maintenance']
        self.template_has_keys = data['template_has_keys']
        self.template_use_hardpoints = data['template_use_hardpoints']
        self.template_is_fort_asset = data['template_is_fort_asset']
        self.template_is_building_of_war = data['template_is_building_of_war']
        self.template_bow_can_place_on_grid = data['template_bow_can_place_on_grid']
        self.template_requires_nation_tree_slot = data['template_requires_nation_tree_slot']
        self.template_requires_guild_tree_slot = data['template_requires_guild_tree_slot']
        self.template_use_fort_grid = data['template_use_fort_grid']
        self.template_is_fort_start = data['template_is_fort_start']
        self.template_is_cap_asset = data['template_is_cap_asset']
        self.template_zone_no_build = data['template_zone_no_build']
        self.template_zone_influence = data['template_zone_influence']
        self.template_eject_loc = data['template_eject_loc']
        self.template_npc_load = data['template_npc_load']
        self.template_fort_grid_offset = data['template_fort_grid_offset']
        self.template_power_action_id = data['template_power_action_id']
        self.template_zone_flag = data['template_zone_flag']
        self.template_spire_event_rule = data['template_spire_event_rule']
        self.template_maintenance_set = data['template_maintenance_set']
        self.template_damage_set = data['template_damage_set']
        self.template_energy_set = data['template_energy_set']
        self.template_use_trigger = data['template_use_trigger']
        self.template_unknown_check1 = data['template_unknown_check1']
        self.template_loot_trigger = data['template_loot_trigger']
        self.template_unknown_check2 = data['template_unknown_check2']
        self.has_embedded_template = data['has_embedded_template']
        if self.has_embedded_template:
            self.template_embed_template = ArcCityAssetTemplate()
            self.template_embed_template.load_json(data['template_embed_template'])
        self.template_creator = data['template_creator']
        self.template_terrain = data['template_terrain']
        self.template_valid_npc_type = data['template_valid_npc_type']
        self.template_valid_npc_cat = data['template_valid_npc_cat']
        self.template_rank_info = []
        for rank_info_data in data['template_rank_info']:
            rank_info = RankInfo()
            rank_info.load_json(rank_info_data)
            self.template_rank_info.append(rank_info)
        self.template_cap_info = data['template_cap_info']
        self.template_event_rules = data['template_event_rules']
        self.template_architecture = data['template_architecture']
        self.template_offering_type = data['template_offering_type']
        self.template_placement_type = data['template_placement_type']
        self.template_offering_adjustment = data['template_offering_adjustment']
        self.template_resource_limit = data['template_resource_limit']
        self.template_unknown = data['template_unknown']

    def save_json(self):
        data = OrderedDict()
        data['template_max_ranks'] = self.template_max_ranks
        data['template_start_rank'] = self.template_start_rank
        data['template_asset_type'] = self.template_asset_type
        data['template_trade_icon'] = self.template_trade_icon
        data['template_landmark'] = self.template_landmark
        data['template_is_maintenance'] = self.template_is_maintenance
        data['template_has_keys'] = self.template_has_keys
        data['template_use_hardpoints'] = self.template_use_hardpoints
        data['template_is_fort_asset'] = self.template_is_fort_asset
        data['template_is_building_of_war'] = self.template_is_building_of_war
        data['template_bow_can_place_on_grid'] = self.template_bow_can_place_on_grid
        data['template_requires_nation_tree_slot'] = self.template_requires_nation_tree_slot
        data['template_requires_guild_tree_slot'] = self.template_requires_guild_tree_slot
        data['template_use_fort_grid'] = self.template_use_fort_grid
        data['template_is_fort_start'] = self.template_is_fort_start
        data['template_is_cap_asset'] = self.template_is_cap_asset
        data['template_zone_no_build'] = self.template_zone_no_build
        data['template_zone_influence'] = self.template_zone_influence
        data['template_eject_loc'] = self.template_eject_loc
        data['template_npc_load'] = self.template_npc_load
        data['template_fort_grid_offset'] = self.template_fort_grid_offset
        data['template_power_action_id'] = self.template_power_action_id
        data['template_zone_flag'] = self.template_zone_flag
        data['template_spire_event_rule'] = self.template_spire_event_rule
        data['template_maintenance_set'] = self.template_maintenance_set
        data['template_damage_set'] = self.template_damage_set
        data['template_energy_set'] = self.template_energy_set
        data['template_use_trigger'] = self.template_use_trigger
        data['template_unknown_check1'] = self.template_unknown_check1
        data['template_loot_trigger'] = self.template_loot_trigger
        data['template_unknown_check2'] = self.template_unknown_check2
        data['has_embedded_template'] = self.has_embedded_template
        if self.has_embedded_template:
            data['template_embed_template'] = self.template_embed_template.save_json()
        data['template_creator'] = self.template_creator
        data['template_terrain'] = self.template_terrain
        data['template_valid_npc_type'] = self.template_valid_npc_type
        data['template_valid_npc_cat'] = self.template_valid_npc_cat
        data['template_rank_info'] = []
        for rank_info in self.template_rank_info:
            data['template_rank_info'].append(rank_info.save_json())
        data['template_cap_info'] = self.template_cap_info
        data['template_event_rules'] = self.template_event_rules
        data['template_architecture'] = self.template_architecture
        data['template_offering_type'] = self.template_offering_type
        data['template_placement_type'] = self.template_placement_type
        data['template_offering_adjustment'] = self.template_offering_adjustment
        data['template_resource_limit'] = self.template_resource_limit
        data['template_unknown'] = self.template_unknown
        return data
