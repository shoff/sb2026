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
from arcane.util import ResStream
from .ArcItem import ArcItem
from .common.Arcane import AttributeValue, SkillGrant
from .common.Inventory import Inventory
from .common.SparseData import SparseData


class Group:
    def load_binary(self, stream: ResStream):
        self.group_type = stream.read_dword()
        self.group_is_faction = stream.read_bool()
        self.group_is_guild = stream.read_bool()

    def save_binary(self, stream: ResStream):
        stream.write_dword(self.group_type)
        stream.write_bool(self.group_is_faction)
        stream.write_bool(self.group_is_guild)

    def load_json(self, data):
        self.group_type = data['group_type']
        self.group_is_faction = data['group_is_faction']
        self.group_is_guild = data['group_is_guild']

    def save_json(self):
        data = OrderedDict()
        data['group_type'] = self.group_type
        data['group_is_faction'] = self.group_is_faction
        data['group_is_guild'] = self.group_is_guild
        return data


class SkillAdjust:
    def load_binary(self, stream: ResStream):
        self.skill_type = stream.read_dword()

        num_adjusts = stream.read_dword()
        self.skill_adjusts = [
            [
                stream.read_dword(),
                stream.read_dword(),
            ] for _ in range(num_adjusts)
        ]

    def save_binary(self, stream: ResStream):
        stream.write_dword(self.skill_type)
        stream.write_dword(len(self.skill_adjusts))
        for skill in self.skill_adjusts:
            stream.write_dword(skill[0])
            stream.write_dword(skill[1])

    def load_json(self, data):
        self.skill_type = string_to_hash(data['skill_type'])
        self.skill_adjusts = []
        for skill in data['skill_adjusts']:
            self.skill_adjusts.append(skill)

    def save_json(self):
        data = OrderedDict()
        data['skill_type'] = hash_to_string(self.skill_type)
        data['skill_adjusts'] = []
        for skill in self.skill_adjusts:
            data['skill_adjusts'].append(skill)
        return data


class BodyPart:
    def load_binary(self, stream: ResStream):
        self.body_part_render = stream.read_qword()
        self.body_part_position = stream.read_tuple()

    def save_binary(self, stream: ResStream):
        stream.write_qword(self.body_part_render)
        stream.write_tuple(self.body_part_position)

    def load_json(self, data):
        self.body_part_render = data['body_part_render']
        self.body_part_position = data['body_part_position']

    def save_json(self):
        data = OrderedDict()
        data['body_part_render'] = self.body_part_render
        data['body_part_position'] = self.body_part_position
        return data


class ArcRune(ArcItem):
    def load_binary(self, stream: ResStream):
        super().load_binary(stream)
        self.rune_type = stream.read_dword()
        self.rune_sub_type = stream.read_dword()
        self.rune_is_standard_character_creation = stream.read_bool()
        self.rune_creation_cost = stream.read_dword()
        self.rune_rank = stream.read_dword()
        self.rune_pracs_per_level = stream.read_dword()
        self.rune_exp_req_to_level = stream.read_float()
        self.rune_sex = stream.read_dword()
        self.rune_class_icon = stream.read_qword()
        self.rune_health = stream.read_dword()
        self.rune_mana = stream.read_dword()
        self.rune_stamina = stream.read_dword()
        self.rune_min_damage = stream.read_float()
        self.rune_max_damage = stream.read_float()
        self.rune_attack = stream.read_dword()
        self.rune_defense = stream.read_dword()
        self.rune_level = stream.read_dword()
        self.rune_speed = [
            stream.read_float() for _ in range(7)
        ]
        self.rune_group = Group()
        self.rune_group.load_binary(stream)
        self.rune_dsc = stream.read_string()
        self.rune_fx_txt = stream.read_string()
        self.rune_group_tactics = stream.read_dword()
        self.rune_group_role_set = stream.read_dword()
        num_enemies = stream.read_dword()
        self.rune_enemy_monster_types = [
            stream.read_dword() for _ in range(num_enemies)
        ]
        num_groupees = stream.read_dword()
        self.rune_groupee_monster_types = [
            stream.read_dword() for _ in range(num_groupees)
        ]
        num_helpers = stream.read_dword()
        self.rune_helper_monster_types = [
            stream.read_dword() for _ in range(num_helpers)
        ]
        num_not_enemies = stream.read_dword()
        self.rune_not_enemy_monster_types = [
            stream.read_dword() for _ in range(num_not_enemies)
        ]
        num_genders = stream.read_dword()
        self.rune_enemy_gender = [
            stream.read_dword() for _ in range(num_genders)
        ]
        num_skill_grants = stream.read_dword()
        self.rune_skill_grant = [SkillGrant() for _ in range(num_skill_grants)]
        for grant in self.rune_skill_grant:
            grant.load_binary(stream)
        num_skill_adjusts = stream.read_dword()
        self.rune_skill_adj = [SkillAdjust() for _ in range(num_skill_adjusts)]
        for adjust in self.rune_skill_adj:
            adjust.load_binary(stream)
        num_attr_adjusts = stream.read_dword()
        self.rune_attr_adj = [AttributeValue() for _ in range(num_attr_adjusts)]
        for attr in self.rune_attr_adj:
            attr.load_binary(stream)
        num_max_attr_adjusts = stream.read_dword()
        self.rune_max_attr_adj = [AttributeValue() for _ in range(num_max_attr_adjusts)]
        for attr in self.rune_max_attr_adj:
            attr.load_binary(stream)
        num_natural_attacks = stream.read_dword()
        self.rune_naturalattacks = [
            [
                stream.read_float(),
                stream.read_float(),
                stream.read_dword(),
                stream.read_dword(),
                stream.read_qword(),
                stream.read_float(),
                stream.read_dword(),
                stream.read_dword(),
                stream.read_dword(),
                stream.read_dword(),
            ] for _ in range(num_natural_attacks)
        ]
        num_enchants = stream.read_dword()
        self.rune_enchantment_type = [
            stream.read_dword() for _ in range(num_enchants)
        ]
        num_contents = stream.read_dword()
        self.rune_inventory_contents = [Inventory() for _ in range(num_contents)]
        for content in self.rune_inventory_contents:
            content.load_binary(stream)

        self.rune_renderable = stream.read_bool()
        if self.rune_renderable:
            self.rune_scale_factor = stream.read_tuple()
            self.rune_skeleton = stream.read_qword()
            self.rune_slope_hugger = stream.read_bool()
            self.rune_can_fly = stream.read_bool()
            self.rune_death_effect = stream.read_qword()
            self.rune_tombstone_id = stream.read_qword()
            num_body_parts = stream.read_dword()
            self.rune_body_parts = [BodyPart() for _ in range(num_body_parts)]
            for part in self.rune_body_parts:
                part.load_binary(stream)
            num_hair = stream.read_dword()
            self.rune_hair = [
                stream.read_qword() for _ in range(num_hair)
            ]
            num_beard = stream.read_dword()
            self.rune_beard = [
                stream.read_qword() for _ in range(num_beard)
            ]
        self.rune_natural_power_attack = stream.read_dword()
        self.rune_sparse_data = SparseData()
        self.rune_sparse_data.load_binary(stream)

    def save_binary(self, stream: ResStream):
        super().save_binary(stream)
        stream.write_dword(self.rune_type)
        stream.write_dword(self.rune_sub_type)
        stream.write_bool(self.rune_is_standard_character_creation)
        stream.write_dword(self.rune_creation_cost)
        stream.write_dword(self.rune_rank)
        stream.write_dword(self.rune_pracs_per_level)
        stream.write_float(self.rune_exp_req_to_level)
        stream.write_dword(self.rune_sex)
        stream.write_qword(self.rune_class_icon)
        stream.write_dword(self.rune_health)
        stream.write_dword(self.rune_mana)
        stream.write_dword(self.rune_stamina)
        stream.write_float(self.rune_min_damage)
        stream.write_float(self.rune_max_damage)
        stream.write_dword(self.rune_attack)
        stream.write_dword(self.rune_defense)
        stream.write_dword(self.rune_level)
        for i in range(7):
            stream.write_float(self.rune_speed[i])
        self.rune_group.save_binary(stream)
        stream.write_string(self.rune_dsc)
        stream.write_string(self.rune_fx_txt)
        stream.write_dword(self.rune_group_tactics)
        stream.write_dword(self.rune_group_role_set)
        stream.write_dword(len(self.rune_enemy_monster_types))
        for monster in self.rune_enemy_monster_types:
            stream.write_dword(monster)
        stream.write_dword(len(self.rune_groupee_monster_types))
        for monster in self.rune_groupee_monster_types:
            stream.write_dword(monster)
        stream.write_dword(len(self.rune_helper_monster_types))
        for monster in self.rune_helper_monster_types:
            stream.write_dword(monster)
        stream.write_dword(len(self.rune_not_enemy_monster_types))
        for monster in self.rune_not_enemy_monster_types:
            stream.write_dword(monster)
        stream.write_dword(len(self.rune_enemy_gender))
        for gender in self.rune_enemy_gender:
            stream.write_dword(gender)
        stream.write_dword(len(self.rune_skill_grant))
        for grant in self.rune_skill_grant:
            grant.save_binary(stream)
        stream.write_dword(len(self.rune_skill_adj))
        for adjust in self.rune_skill_adj:
            adjust.save_binary(stream)
        stream.write_dword(len(self.rune_attr_adj))
        for attr in self.rune_attr_adj:
            attr.save_binary(stream)
        stream.write_dword(len(self.rune_max_attr_adj))
        for attr in self.rune_max_attr_adj:
            attr.save_binary(stream)
        stream.write_dword(len(self.rune_naturalattacks))
        for attack in self.rune_naturalattacks:
            stream.write_float(attack[0])
            stream.write_float(attack[1])
            stream.write_dword(attack[2])
            stream.write_dword(attack[3])
            stream.write_qword(attack[4])
            stream.write_float(attack[5])
            stream.write_dword(attack[6])
            stream.write_dword(attack[7])
            stream.write_dword(attack[8])
            stream.write_dword(attack[9])
        stream.write_dword(len(self.rune_enchantment_type))
        for enchantment in self.rune_enchantment_type:
            stream.write_dword(enchantment)
        stream.write_dword(len(self.rune_inventory_contents))
        for content in self.rune_inventory_contents:
            content.save_binary(stream)
        stream.write_bool(self.rune_renderable)
        if self.rune_renderable:
            stream.write_tuple(self.rune_scale_factor)
            stream.write_qword(self.rune_skeleton)
            stream.write_bool(self.rune_slope_hugger)
            stream.write_bool(self.rune_can_fly)
            stream.write_qword(self.rune_death_effect)
            stream.write_qword(self.rune_tombstone_id)
            stream.write_dword(len(self.rune_body_parts))
            for part in self.rune_body_parts:
                part.save_binary(stream)
            stream.write_dword(len(self.rune_hair))
            for hair in self.rune_hair:
                stream.write_qword(hair)
            stream.write_dword(len(self.rune_beard))
            for beard in self.rune_beard:
                stream.write_qword(beard)
        stream.write_dword(self.rune_natural_power_attack)
        self.rune_sparse_data.save_binary(stream)

    def load_json(self, data):
        super().load_json(data)
        self.rune_type = STRING_TO_RUNE_TYPE[data['rune_type']]
        self.rune_sub_type = string_to_hash(data['rune_sub_type'])
        self.rune_is_standard_character_creation = data['rune_is_standard_character_creation']
        self.rune_creation_cost = data['rune_creation_cost']
        self.rune_rank = data['rune_rank']
        self.rune_pracs_per_level = data['rune_pracs_per_level']
        self.rune_exp_req_to_level = data['rune_exp_req_to_level']
        self.rune_sex = STRING_TO_RUNE_SEX[data['rune_sex']]
        self.rune_class_icon = data['rune_class_icon']
        self.rune_health = data['rune_health']
        self.rune_mana = data['rune_mana']
        self.rune_stamina = data['rune_stamina']
        self.rune_min_damage = data['rune_min_damage']
        self.rune_max_damage = data['rune_max_damage']
        self.rune_attack = data['rune_attack']
        self.rune_defense = data['rune_defense']
        self.rune_level = data['rune_level']
        self.rune_speed = []
        for i in range(7):
            self.rune_speed.append(data['rune_speed'][SPEED_TYPE_TO_STRING[i]])
        self.rune_group = Group()
        self.rune_group.load_json(data['rune_group'])
        self.rune_dsc = data['rune_dsc']
        self.rune_fx_txt = data['rune_fx_txt']
        self.rune_group_tactics = data['rune_group_tactics']
        self.rune_group_role_set = data['rune_group_role_set']
        self.rune_enemy_monster_types = []
        for monster in data['rune_enemy_monster_types']:
            self.rune_enemy_monster_types.append(string_to_hash(monster))
        self.rune_groupee_monster_types = []
        for monster in data['rune_groupee_monster_types']:
            self.rune_groupee_monster_types.append(string_to_hash(monster))
        self.rune_helper_monster_types = []
        for monster in data['rune_helper_monster_types']:
            self.rune_helper_monster_types.append(string_to_hash(monster))
        self.rune_not_enemy_monster_types = []
        for monster in data['rune_not_enemy_monster_types']:
            self.rune_not_enemy_monster_types.append(string_to_hash(monster))
        self.rune_enemy_gender = []
        for gender in data['rune_enemy_gender']:
            self.rune_enemy_gender.append(gender)
        self.rune_skill_grant = []
        for grant_data in data['rune_skill_grant']:
            grant = SkillGrant()
            grant.load_json(grant_data)
            self.rune_skill_grant.append(grant)
        self.rune_skill_adj = []
        for adjust_data in data['rune_skill_adj']:
            adjust = SkillAdjust()
            adjust.load_json(adjust_data)
            self.rune_skill_adj.append(adjust)
        self.rune_attr_adj = []
        for attr_data in data['rune_attr_adj']:
            attr = AttributeValue()
            attr.load_json(attr_data)
            self.rune_attr_adj.append(attr)
        self.rune_max_attr_adj = []
        for attr_data in data['rune_max_attr_adj']:
            attr = AttributeValue()
            attr.load_json(attr_data)
            self.rune_max_attr_adj.append(attr)
        self.rune_naturalattacks = data['rune_naturalattacks']
        self.rune_enchantment_type = []
        for enchantment in data['rune_enchantment_type']:
            self.rune_enchantment_type.append(enchantment)
        self.rune_inventory_contents = []
        for content_data in data['rune_inventory_contents']:
            content = Inventory()
            content.load_json(content_data)
            self.rune_inventory_contents.append(content)
        self.rune_renderable = data['rune_renderable']
        if self.rune_renderable:
            self.rune_scale_factor = data['rune_scale_factor']
            self.rune_skeleton = data['rune_skeleton']
            self.rune_slope_hugger = data['rune_slope_hugger']
            self.rune_can_fly = data['rune_can_fly']
            self.rune_death_effect = data['rune_death_effect']
            self.rune_tombstone_id = data['rune_tombstone_id']
            self.rune_body_parts = []
            for part_data in data['rune_body_parts']:
                part = BodyPart()
                part.load_json(part_data)
                self.rune_body_parts.append(part)
            self.rune_hair = data['rune_hair']
            self.rune_beard = data['rune_beard']
        self.rune_natural_power_attack = data['rune_natural_power_attack']
        self.rune_sparse_data = SparseData()
        self.rune_sparse_data.load_json(data['rune_sparse_data'])

    def save_json(self):
        data = super().save_json()
        data['rune_type'] = RUNE_TYPE_TO_STRING[self.rune_type]
        data['rune_sub_type'] = hash_to_string(self.rune_sub_type)
        data['rune_is_standard_character_creation'] = self.rune_is_standard_character_creation
        data['rune_creation_cost'] = self.rune_creation_cost
        data['rune_rank'] = self.rune_rank
        data['rune_pracs_per_level'] = self.rune_pracs_per_level
        data['rune_exp_req_to_level'] = self.rune_exp_req_to_level
        data['rune_sex'] = RUNE_SEX_TO_STRING[self.rune_sex]
        data['rune_class_icon'] = self.rune_class_icon
        data['rune_health'] = self.rune_health
        data['rune_mana'] = self.rune_mana
        data['rune_stamina'] = self.rune_stamina
        data['rune_min_damage'] = self.rune_min_damage
        data['rune_max_damage'] = self.rune_max_damage
        data['rune_attack'] = self.rune_attack
        data['rune_defense'] = self.rune_defense
        data['rune_level'] = self.rune_level
        data['rune_speed'] = OrderedDict()
        for i in range(7):
            data['rune_speed'][SPEED_TYPE_TO_STRING[i]] = self.rune_speed[i]
        data['rune_group'] = self.rune_group.save_json()
        data['rune_dsc'] = self.rune_dsc
        data['rune_fx_txt'] = self.rune_fx_txt
        data['rune_group_tactics'] = self.rune_group_tactics
        data['rune_group_role_set'] = self.rune_group_role_set
        data['rune_enemy_monster_types'] = []
        for monster in self.rune_enemy_monster_types:
            data['rune_enemy_monster_types'].append(hash_to_string(monster))
        data['rune_groupee_monster_types'] = []
        for monster in self.rune_groupee_monster_types:
            data['rune_groupee_monster_types'].append(hash_to_string(monster))
        data['rune_helper_monster_types'] = []
        for monster in self.rune_helper_monster_types:
            data['rune_helper_monster_types'].append(hash_to_string(monster))
        data['rune_not_enemy_monster_types'] = []
        for monster in self.rune_not_enemy_monster_types:
            data['rune_not_enemy_monster_types'].append(hash_to_string(monster))
        data['rune_enemy_gender'] = []
        for gender in self.rune_enemy_gender:
            data['rune_enemy_gender'].append(gender)
        data['rune_skill_grant'] = []
        for grant in self.rune_skill_grant:
            data['rune_skill_grant'].append(grant.save_json())
        data['rune_skill_adj'] = []
        for adjust in self.rune_skill_adj:
            data['rune_skill_adj'].append(adjust.save_json())
        data['rune_attr_adj'] = []
        for attr in self.rune_attr_adj:
            data['rune_attr_adj'].append(attr.save_json())
        data['rune_max_attr_adj'] = []
        for attr in self.rune_max_attr_adj:
            data['rune_max_attr_adj'].append(attr.save_json())
        data['rune_naturalattacks'] = self.rune_naturalattacks
        data['rune_enchantment_type'] = []
        for enchantment in self.rune_enchantment_type:
            data['rune_enchantment_type'].append(enchantment)
        data['rune_inventory_contents'] = []
        for content in self.rune_inventory_contents:
            data['rune_inventory_contents'].append(content.save_json())
        data['rune_renderable'] = self.rune_renderable
        if self.rune_renderable:
            data['rune_scale_factor'] = self.rune_scale_factor
            data['rune_skeleton'] = self.rune_skeleton
            data['rune_slope_hugger'] = self.rune_slope_hugger
            data['rune_can_fly'] = self.rune_can_fly
            data['rune_death_effect'] = self.rune_death_effect
            data['rune_tombstone_id'] = self.rune_tombstone_id
            data['rune_body_parts'] = []
            for part in self.rune_body_parts:
                data['rune_body_parts'].append(part.save_json())
            data['rune_hair'] = self.rune_hair
            data['rune_beard'] = self.rune_beard
        data['rune_natural_power_attack'] = self.rune_natural_power_attack
        data['rune_sparse_data'] = self.rune_sparse_data.save_json()
        return data
