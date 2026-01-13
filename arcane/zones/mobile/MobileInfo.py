#  • ▌ ▄ ·. ▄▄▄▄·     ▄▄▄ .·▄▄▄▄  ▪  ▄▄▄▄▄      ▄▄▄       ▄▄▄·▄▄▄       
#  ·██ ▐███▪▐█ ▀█▪    ▀▄.▀·██▪ ██ ██ •██  ▪     ▀▄ █·    ▐█ ▄█▀▄ █·▪    
#  ▐█ ▌▐▌▐█·▐█▀▀█▄    ▐▀▀▪▄▐█· ▐█▌▐█· ▐█.▪ ▄█▀▄ ▐▀▀▄      ██▀·▐▀▀▄  ▄█▀▄
#  ██ ██▌▐█▌██▄▪▐█    ▐█▄▄▌██. ██ ▐█▌ ▐█▌·▐█▌.▐▌▐█•█▌    ▐█▪·•▐█•█▌▐█▌.▐▌
#  ▀▀  █▪▀▀▀·▀▀▀▀      ▀▀▀ ▀▀▀▀▀• ▀▀▀ ▀▀▀  ▀█▄▀▪.▀  ▀    .▀   .▀  ▀ ▀█▄▀▪
#                Magicbane Emulator Project © 2013 - 2022
#                           www.magicbane.com

from collections import OrderedDict

from arcane.enums.arc_rune import *
from arcane.enums.hashes import hash_to_string, string_to_hash
from arcane.objects.ArcRune import Group
from arcane.objects.common.Inventory import Inventory
from arcane.util import ResStream
from .ArcBasicZoneObjectInfo import ArcBasicZoneObjectInfo


class Unknown:
    def load_binary(self, stream: ResStream):
        self.unknown_u = stream.read_dword()
        self.unknown_u = stream.read_dword()
        self.unknown_u = stream.read_dword()
        self.unknown_check = stream.read_bool()
        if self.unknown_check:
            self.unknown_u = stream.read_qword()
        else:
            self.unknown_u = stream.read_dword()
        self.unknown_u = stream.read_string()
        self.unknown_u = stream.read_float()


class InventoryContents:
    def load_binary(self, stream: ResStream):
        self.mobile_inventory_u = stream.read_qword()
        self.mobile_inventory_u = stream.read_qword()
        self.mobile_inventory_u = stream.read_tuple()
        self.mobile_inventory_u = stream.read_tuple()
        self.mobile_inventory_u = [stream.read_float() for _ in range(4)]
        self.mobile_inventory_u = stream.read_qword()
        self.mobile_inventory_u = stream.read_dword()
        self.mobile_inventory_u = stream.read_dword()
        self.mobile_inventory_u = stream.read_dword()
        self.mobile_inventory_u = stream.read_bool()
        self.mobile_inventory_u = stream.read_string()
        self.mobile_inventory_check = stream.read_bool()
        if self.mobile_inventory_check:
            self.mobile_inventory_u = stream.read_float()
            self.mobile_inventory_u = stream.read_float()
        self.mobile_inventory_check = stream.read_bool()
        if self.mobile_inventory_check:
            self.mobile_inventory_u = stream.read_qword()
            self.mobile_inventory_u = stream.read_dword()
            self.mobile_inventory_u = stream.read_dword()
            self.mobile_inventory_u = stream.read_float()
            self.mobile_inventory_u = stream.read_dword()
            self.mobile_inventory_u = stream.read_dword()
            num = stream.read_dword()
            self.mobile_inventory_u = [Unknown() for _ in range(num)]
            self.mobile_inventory_u = stream.read_dword()
        self.mobile_inventory_check = stream.read_bool()
        if self.mobile_inventory_check:
            self.mobile_inventory_u = stream.read_qword()
            self.mobile_inventory_u = stream.read_qword()
            self.mobile_inventory_u = stream.read_qword()
            self.mobile_inventory_u = stream.read_dword()
        self.mobile_inventory_check = stream.read_bool()
        if self.mobile_inventory_check:
            self.mobile_inventory_u = stream.read_qword()
            self.mobile_inventory_u = stream.read_dword()
        self.mobile_inventory_check = stream.read_bool()
        if self.mobile_inventory_check:
            self.mobile_inventory_u = stream.read_bool()
            self.mobile_inventory_u = stream.read_float()
            self.mobile_inventory_u = stream.read_dword()
            self.mobile_inventory_u = stream.read_dword()
            self.mobile_inventory_check = stream.read_bool()
            if self.mobile_inventory_check:
                self.mobile_inventory_u = [stream.read_dword() for _ in range(5)]
            self.mobile_inventory_check = stream.read_bool()
            if self.mobile_inventory_check:
                self.mobile_inventory_u = [stream.read_dword() for _ in range(5)]
            self.mobile_inventory_u = stream.read_bool()


class MobileInfo:

    def load_binary(self, stream: ResStream):
        self.mobile_base_zone = ArcBasicZoneObjectInfo()
        self.mobile_base_zone.load_binary(stream)
        self.mobile_number_in_group = stream.read_dword()
        self.mobile_change_to_find = stream.read_float()
        self.mobile_level = stream.read_dword()
        self.mobile_behavior_file = stream.read_string()
        self.mobile_dialog_override = stream.read_dword()
        self.mobile_base_exp_reward = stream.read_dword()
        self.mobile_tenacity = stream.read_float()
        self.mobile_courage = stream.read_float()
        self.mobile_has_group_tactics = stream.read_bool()
        if self.mobile_has_group_tactics:
            self.mobile_group_tactics = stream.read_dword()
        self.mobile_has_role_set = stream.read_bool()
        if self.mobile_has_role_set:
            self.mobile_role_set = stream.read_dword()
        self.mobile_has_home_goal = stream.read_bool()
        if self.mobile_has_home_goal:
            self.mobile_home_goal = stream.read_dword()
            self.mobile_spawn_home_goal = stream.read_bool()
        self.mobile_has_target_goal = stream.read_bool()
        if self.mobile_has_target_goal:
            self.mobile_target_goal = stream.read_dword()
            self.mobile_spawn_target_goal = stream.read_bool()
        num_rune_stone_ids = stream.read_dword()
        self.mobile_rune_stone_ids = [stream.read_qword() for _ in range(num_rune_stone_ids)]
        self.mobile_has_content = stream.read_bool()
        if self.mobile_has_content:
            num_contents = stream.read_dword()
            self.mobile_inventory_contents = [InventoryContents() for _ in range(num_contents)]
            for content in self.mobile_inventory_contents:
                content.load_binary(stream)
        num_equipments = stream.read_dword()
        self.mobile_equipment = [[
            stream.read_qword(),
            stream.read_float(),
        ] for _ in range(num_equipments)]
        num_lores = stream.read_dword()
        self.mobile_lores = [stream.read_dword() for _ in range(num_lores)]
        self.mobile_use_prefered_hp = stream.read_bool()
        num_spawn_hps = stream.read_dword()
        self.mobile_spawn_hps = [stream.read_dword() for _ in range(num_spawn_hps)]
        num = stream.read_dword()
        self.mobile_booties = [Inventory() for _ in range(num)]
        for booty in self.mobile_booties:
            booty.load_binary(stream)
        self.mobile_root_fs_mid = stream.read_string()
        self.mobile_group = Group()
        self.mobile_group.load_binary(stream)
        num_enemy_monster_types = stream.read_dword()
        self.mobile_enemy_monster_types = [stream.read_dword() for _ in range(num_enemy_monster_types)]
        num_not_enemy_monster_types = stream.read_dword()
        self.mobile_not_enemy_monster_types = [stream.read_dword() for _ in range(num_not_enemy_monster_types)]
        num_groupee_monster_types = stream.read_dword()
        self.mobile_groupee_monster_types = [stream.read_dword() for _ in range(num_groupee_monster_types)]
        num_helper_monster_types = stream.read_dword()
        self.mobile_helper_monster_types = [stream.read_dword() for _ in range(num_helper_monster_types)]
        num_enemy_genders = stream.read_dword()
        self.mobile_enemy_genders = [stream.read_dword() for _ in range(num_enemy_genders)]
        num_firendly_charters = stream.read_dword()
        self.mobile_firendly_charters = [stream.read_dword() for _ in range(num_firendly_charters)]
        self.mobile_parley_name = stream.read_string()

    def save_binary(self, stream: ResStream):
        self.mobile_base_zone.save_binary(stream)
        stream.write_dword(self.mobile_number_in_group)
        stream.write_float(self.mobile_change_to_find)
        stream.write_dword(self.mobile_level)
        stream.write_string(self.mobile_behavior_file)
        stream.write_dword(self.mobile_dialog_override)
        stream.write_dword(self.mobile_base_exp_reward)
        stream.write_float(self.mobile_tenacity)
        stream.write_float(self.mobile_courage)
        stream.write_bool(self.mobile_has_group_tactics)
        if self.mobile_has_group_tactics:
            stream.write_dword(self.mobile_group_tactics)
        stream.write_bool(self.mobile_has_role_set)
        if self.mobile_has_role_set:
            stream.write_dword(self.mobile_role_set)
        stream.write_bool(self.mobile_has_home_goal)
        if self.mobile_has_home_goal:
            stream.write_dword(self.mobile_home_goal)
            stream.write_bool(self.mobile_spawn_home_goal)
        stream.write_bool(self.mobile_has_target_goal)
        if self.mobile_has_target_goal:
            stream.write_dword(self.mobile_target_goal)
            stream.write_bool(self.mobile_spawn_target_goal)
        stream.write_dword(len(self.mobile_rune_stone_ids))
        for rune_stone_id in self.mobile_rune_stone_ids:
            stream.write_qword(rune_stone_id)
        stream.write_bool(self.mobile_has_content)
        if self.mobile_has_content:
            stream.write_dword(len(self.mobile_inventory_contents))
            for content in self.mobile_inventory_contents:
                content.save_binary(stream)
        stream.write_dword(len(self.mobile_equipment))
        for equipment in self.mobile_equipment:
            stream.write_qword(equipment[0])
            stream.write_float(equipment[1])
        stream.write_dword(len(self.mobile_lores))
        for lore in self.mobile_lores:
            stream.write_dword(lore)
        stream.write_bool(self.mobile_use_prefered_hp)
        stream.write_dword(len(self.mobile_spawn_hps))
        for spawn_hp in self.mobile_spawn_hps:
            stream.write_dword(spawn_hp)
        stream.write_dword(len(self.mobile_booties))
        for booty in self.mobile_booties:
            booty.save_binary(stream)
        stream.write_string(self.mobile_root_fs_mid)
        self.mobile_group.save_binary(stream)
        stream.write_dword(len(self.mobile_enemy_monster_types))
        for enemy_monster_type in self.mobile_enemy_monster_types:
            stream.write_dword(enemy_monster_type)
        stream.write_dword(len(self.mobile_not_enemy_monster_types))
        for not_enemy_monster_type in self.mobile_not_enemy_monster_types:
            stream.write_dword(not_enemy_monster_type)
        stream.write_dword(len(self.mobile_groupee_monster_types))
        for groupee_monster_type in self.mobile_groupee_monster_types:
            stream.write_dword(groupee_monster_type)
        stream.write_dword(len(self.mobile_helper_monster_types))
        for helper_monster_type in self.mobile_helper_monster_types:
            stream.write_dword(helper_monster_type)
        stream.write_dword(len(self.mobile_enemy_genders))
        for enemy_gender in self.mobile_enemy_genders:
            stream.write_dword(enemy_gender)
        stream.write_dword(len(self.mobile_firendly_charters))
        for firendly_charter in self.mobile_firendly_charters:
            stream.write_dword(firendly_charter)
        stream.write_string(self.mobile_parley_name)

    def save_json(self):
        data = OrderedDict()
        data['mobile_base_zone'] = self.mobile_base_zone.save_json()
        data['mobile_number_in_group'] = self.mobile_number_in_group
        data['mobile_change_to_find'] = self.mobile_change_to_find
        data['mobile_level'] = self.mobile_level
        data['mobile_behavior_file'] = self.mobile_behavior_file
        data['mobile_dialog_override'] = self.mobile_dialog_override
        data['mobile_base_exp_reward'] = self.mobile_base_exp_reward
        data['mobile_tenacity'] = self.mobile_tenacity
        data['mobile_courage'] = self.mobile_courage
        data['mobile_has_group_tactics'] = self.mobile_has_group_tactics
        if self.mobile_has_group_tactics:
            data['mobile_group_tactics'] = self.mobile_group_tactics
        data['mobile_has_role_set'] = self.mobile_has_role_set
        if self.mobile_has_role_set:
            data['mobile_role_set'] = self.mobile_role_set
        data['mobile_has_home_goal'] = self.mobile_has_home_goal
        if self.mobile_has_home_goal:
            data['mobile_home_goal'] = self.mobile_home_goal
            data['mobile_spawn_home_goal'] = self.mobile_spawn_home_goal
        data['mobile_has_target_goal'] = self.mobile_has_target_goal
        if self.mobile_has_target_goal:
            data['mobile_target_goal'] = self.mobile_target_goal
            data['mobile_spawn_target_goal'] = self.mobile_spawn_target_goal
        data['mobile_rune_stone_ids'] = self.mobile_rune_stone_ids
        data['mobile_has_content'] = self.mobile_has_content
        if self.mobile_has_content:
            data['mobile_inventory_contents'] = []
            for content in self.mobile_inventory_contents:
                data['mobile_inventory_contents'].append(content.save_json())
        data['mobile_equipment'] = self.mobile_equipment
        data['mobile_lores'] = self.mobile_lores
        data['mobile_use_prefered_hp'] = self.mobile_use_prefered_hp
        data['mobile_spawn_hps'] = self.mobile_spawn_hps
        data['mobile_booties'] = []
        for booty in self.mobile_booties:
            data['mobile_booties'].append(booty.save_json())
        data['mobile_root_fs_mid'] = self.mobile_root_fs_mid
        data['mobile_group'] = self.mobile_group.save_json()
        data['mobile_enemy_monster_types'] = []
        for enemy_monster_type in self.mobile_enemy_monster_types:
            data['mobile_enemy_monster_types'].append(hash_to_string(enemy_monster_type))
        data['mobile_not_enemy_monster_types'] = []
        for not_enemy_monster_type in self.mobile_not_enemy_monster_types:
            data['mobile_not_enemy_monster_types'].append(hash_to_string(not_enemy_monster_type))
        data['mobile_groupee_monster_types'] = []
        for groupee_monster_type in self.mobile_groupee_monster_types:
            data['mobile_groupee_monster_types'].append(hash_to_string(groupee_monster_type))
        data['mobile_helper_monster_types'] = []
        for helper_monster_type in self.mobile_helper_monster_types:
            data['mobile_helper_monster_types'].append(hash_to_string(helper_monster_type))
        data['mobile_enemy_genders'] = []
        for enemy_gender in self.mobile_enemy_genders:
            data['mobile_enemy_genders'].append(RUNE_SEX_TO_STRING[enemy_gender])
        data['mobile_firendly_charters'] = self.mobile_firendly_charters
        data['mobile_parley_name'] = self.mobile_parley_name
        return data

    def load_json(self, data):
        self.mobile_base_zone = ArcBasicZoneObjectInfo()
        self.mobile_base_zone.load_json(data['mobile_base_zone'])
        self.mobile_number_in_group = data['mobile_number_in_group']
        self.mobile_change_to_find = data['mobile_change_to_find']
        self.mobile_level = data['mobile_level']
        self.mobile_behavior_file = data['mobile_behavior_file']
        self.mobile_dialog_override = data['mobile_dialog_override']
        self.mobile_base_exp_reward = data['mobile_base_exp_reward']
        self.mobile_tenacity = data['mobile_tenacity']
        self.mobile_courage = data['mobile_courage']
        self.mobile_has_group_tactics = data['mobile_has_group_tactics']
        if self.mobile_has_group_tactics:
            self.mobile_group_tactics = data['mobile_group_tactics']
        self.mobile_has_role_set = data['mobile_has_role_set']
        if self.mobile_has_role_set:
            self.mobile_role_set = data['mobile_role_set']
        self.mobile_has_home_goal = data['mobile_has_home_goal']
        if self.mobile_has_home_goal:
            self.mobile_home_goal = data['mobile_home_goal']
            self.mobile_spawn_home_goal = data['mobile_spawn_home_goal']
        self.mobile_has_target_goal = data['mobile_has_target_goal']
        if self.mobile_has_target_goal:
            self.mobile_target_goal = data['mobile_target_goal']
            self.mobile_spawn_target_goal = data['mobile_spawn_target_goal']
        self.mobile_rune_stone_ids = data['mobile_rune_stone_ids']
        self.mobile_has_content = data['mobile_has_content']
        if self.mobile_has_content:
            self.mobile_inventory_contents = []
            for content_data in data['mobile_inventory_contents']:
                content = InventoryContents()
                content.load_json(content_data)
                self.mobile_inventory_contents.append(content)
        self.mobile_equipment = data['mobile_equipment']
        self.mobile_lores = data['mobile_lores']
        self.mobile_use_prefered_hp = data['mobile_use_prefered_hp']
        self.mobile_spawn_hps = data['mobile_spawn_hps']
        self.mobile_booties = []
        for booty_data in data['mobile_booties']:
            booty = Inventory()
            booty.load_json(booty_data)
            self.mobile_booties.append(booty)
        self.mobile_root_fs_mid = data['mobile_root_fs_mid']
        self.mobile_group = Group()
        self.mobile_group.load_json(data['mobile_group'])
        self.mobile_enemy_monster_types = []
        for enemy_monster_type in data['mobile_enemy_monster_types']:
            self.mobile_enemy_monster_types.append(string_to_hash(enemy_monster_type))
        self.mobile_not_enemy_monster_types = []
        for not_enemy_monster_type in data['mobile_not_enemy_monster_types']:
            self.mobile_not_enemy_monster_types.append(string_to_hash(not_enemy_monster_type))
        self.mobile_groupee_monster_types = []
        for groupee_monster_type in data['mobile_groupee_monster_types']:
            self.mobile_groupee_monster_types.append(string_to_hash(groupee_monster_type))
        self.mobile_helper_monster_types = []
        for helper_monster_type in data['mobile_helper_monster_types']:
            self.mobile_helper_monster_types.append(string_to_hash(helper_monster_type))
        self.mobile_enemy_genders = []
        for enemy_gender in data['mobile_enemy_genders']:
            self.mobile_enemy_genders.append(STRING_TO_RUNE_SEX[enemy_gender])
        self.mobile_firendly_charters = data['mobile_firendly_charters']
        self.mobile_parley_name = data['mobile_parley_name']
