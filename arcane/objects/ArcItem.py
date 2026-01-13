
from collections import OrderedDict

from arcane.enums.arc_item import *
from arcane.enums.hashes import hash_to_string, string_to_hash
from arcane.util import ResStream
from .ArcCombatObj import ArcCombatObj
from .common.Arcane import AttributeValue, SkillLevel, PowerGrant, PowerAction, ResourceInfo
from .common.Class import ClassRequired
from .common.Discipline import DiscRequired
from .common.Race import RaceRequired

class Damage:
    def load_binary(self, stream: ResStream):
        self.damage_type = stream.read_dword()
        self.damage_min = stream.read_dword()
        self.damage_max = stream.read_dword()

    def save_binary(self, stream: ResStream):
        stream.write_dword(self.damage_type)
        stream.write_dword(self.damage_min)
        stream.write_dword(self.damage_max)

    def load_json(self, data):
        self.damage_type = STRING_TO_DAMAGE[data['damage_type']]
        self.damage_min = data['damage_min']
        self.damage_max = data['damage_max']

    def save_json(self):
        data = OrderedDict()
        data['damage_type'] = DAMAGE_TO_STRING[self.damage_type]
        data['damage_min'] = self.damage_min
        data['damage_max'] = self.damage_max
        return data

class Offerings:
    def load_binary(self, stream: ResStream):
        self.offering_type = stream.read_string()
        self.offering_value = stream.read_dword()

    def save_binary(self, stream: ResStream):
        stream.write_string(self.offering_type)
        stream.write_dword(self.offering_value)

    def load_json(self, data):
        self.offering_type = data['offering_type']
        self.offering_value = data['offering_value']

    def save_json(self):
        data = OrderedDict()
        data['offering_type'] = self.offering_type
        data['offering_value'] = self.offering_value
        return data

class Weapon:
    def load_binary(self, stream: ResStream):
        self.weapon_wepspeed = stream.read_float()
        self.weapon_max_range = stream.read_float()
        self.weapon_projectile_id = stream.read_qword()
        self.weapon_projectile_speed = stream.read_float()
        self.weapon_combat_idle_anim = stream.read_dword()
        num_damages = stream.read_dword()
        self.weapon_damage = [Damage() for _ in range(num_damages)]
        for damage in self.weapon_damage:
            damage.load_binary(stream)
        num_right_anims = stream.read_dword()
        self.weapon_attack_anim_right = [
            [
                stream.read_dword(),
                stream.read_dword(),
            ] for _ in range(num_right_anims)
        ]
        num_left_anims = stream.read_dword()
        self.weapon_attack_anim_left = [
            [
                stream.read_dword(),
                stream.read_dword(),
            ] for _ in range(num_left_anims)
        ]

    def save_binary(self, stream: ResStream):
        stream.write_float(self.weapon_wepspeed)
        stream.write_float(self.weapon_max_range)
        stream.write_qword(self.weapon_projectile_id)
        stream.write_float(self.weapon_projectile_speed)
        stream.write_dword(self.weapon_combat_idle_anim)
        stream.write_dword(len(self.weapon_damage))
        for damage in self.weapon_damage:
            damage.save_binary(stream)
        stream.write_dword(len(self.weapon_attack_anim_right))
        for anim in self.weapon_attack_anim_right:
            stream.write_dword(anim[0])
            stream.write_dword(anim[1])
        stream.write_dword(len(self.weapon_attack_anim_left))
        for anim in self.weapon_attack_anim_left:
            stream.write_dword(anim[0])
            stream.write_dword(anim[1])

    def load_json(self, data):
        self.weapon_wepspeed = data['weapon_wepspeed']
        self.weapon_max_range = data['weapon_max_range']
        self.weapon_projectile_id = data['weapon_projectile_id']
        self.weapon_projectile_speed = data['weapon_projectile_speed']
        self.weapon_combat_idle_anim = data['weapon_combat_idle_anim']
        self.weapon_damage = []
        for damage_data in data['weapon_damage']:
            damage = Damage()
            damage.load_json(damage_data)
            self.weapon_damage.append(damage)
        self.weapon_attack_anim_right = data['weapon_attack_anim_right']
        self.weapon_attack_anim_left = data['weapon_attack_anim_left']

    def save_json(self):
        data = OrderedDict()
        data['weapon_wepspeed'] = self.weapon_wepspeed
        data['weapon_max_range'] = self.weapon_max_range
        data['weapon_projectile_id'] = self.weapon_projectile_id
        data['weapon_projectile_speed'] = self.weapon_projectile_speed
        data['weapon_combat_idle_anim'] = self.weapon_combat_idle_anim
        data['weapon_damage'] = []
        for damage in self.weapon_damage:
            data['weapon_damage'].append(damage.save_json())
        data['weapon_attack_anim_right'] = self.weapon_attack_anim_right
        data['weapon_attack_anim_left'] = self.weapon_attack_anim_left
        return data

class ArcItem(ArcCombatObj):
    def load_binary(self, stream: ResStream):
        super().load_binary(stream)
        self.item_type = stream.read_dword()
        self.item_eq_slots_value = stream.read_dword()
        self.item_eq_slots_or = stream.read_dword()
        self.item_eq_slots_and = stream.read_dword()
        self.item_eq_slots_type = stream.read_bool()
        self.item_takeable = stream.read_bool()
        self.item_value = stream.read_dword()
        self.item_wt = stream.read_dword()
        self.item_passive_defense_mod = stream.read_float()
        self.item_base_name = stream.read_string()
        self.item_dsc = stream.read_string()
        self.item_render_object_female = stream.read_qword()
        self.item_health_full = stream.read_float()
        self.item_skill_used = stream.read_dword()
        self.item_skill_mastery_used = stream.read_dword()
        self.item_parry_anim_id = stream.read_dword()
        num_adjustments = stream.read_dword()
        self.item_offering_info = [Offerings() for _ in range(num_adjustments)]
        for offering in self.item_offering_info:
            offering.load_binary(stream)

        if self.item_type == ITEM_TYPE_WEAPON:
            self.item_weapon = Weapon()
            self.item_weapon.load_binary(stream)
            self.item_primary_attr = stream.read_dword()
            self.item_secondary_attr = stream.read_dword()

        if self.item_type == ITEM_TYPE_ARMOR:
            self.item_bulk_factor = stream.read_float()
            self.item_defense_rating = stream.read_dword()
        self.item_flags = stream.read_dword()
        self.item_use_flags = stream.read_dword()
        self.item_post_item_id = stream.read_qword()
        self.item_initial_charges = stream.read_dword()
        self.item_book_arcana = stream.read_dword()
        num_skills = stream.read_dword()
        self.item_skill_req = [SkillLevel() for _ in range(num_skills)]
        for skill in self.item_skill_req:
            skill.load_binary(stream)
        self.item_race_req = RaceRequired()
        self.item_race_req.load_binary(stream)
        self.item_class_req = ClassRequired()
        self.item_class_req.load_binary(stream)
        self.item_disc_req = DiscRequired()
        self.item_disc_req.load_binary(stream)
        num_attrs = stream.read_dword()
        self.item_attr_req = [AttributeValue() for _ in range(num_attrs)]
        for attr in self.item_attr_req:
            attr.load_binary(stream)
        self.item_level_req = stream.read_dword()
        self.item_rank_req = stream.read_dword()
        self.item_sex_req = stream.read_dword()
        num_user_actions = stream.read_dword()
        self.item_user_power_action = [
            [
                stream.read_dword(),
                stream.read_dword(),
                stream.read_dword(),
            ] for _ in range(num_user_actions)
        ]
        num_power_grants = stream.read_dword()
        self.item_power_grant = [PowerGrant() for _ in range(num_power_grants)]
        for action in self.item_power_grant:
            action.load_binary(stream)
        num_power_actions = stream.read_dword()
        self.item_power_action = [PowerAction() for _ in range(num_power_actions)]
        for grant in self.item_power_action:
            grant.load_binary(stream)

        self.item_sheathable = stream.read_bool()
        if self.item_sheathable:
            self.item_sheath_slot = stream.read_dword()
            self.item_sheath_offset = stream.read_tuple()
            self.item_sheath_rotation = stream.read_tuple()

        self.item_has_stub = stream.read_bool()
        if self.item_has_stub:
            self.item_stub_holder = [
                stream.read_bool(),
                stream.read_qword(),
            ]
        num_adjustments = stream.read_dword()
        self.item_offering_adjustments = [Offerings() for _ in range(num_adjustments)]
        for offering in self.item_offering_adjustments:
            offering.load_binary(stream)
        num_costs = stream.read_dword()
        self.item_resource_costs = [ResourceInfo() for _ in range(num_costs)]
        for res in self.item_resource_costs:
            res.load_binary(stream)
        self.item_bane_rank = stream.read_dword()
        self.item_ignore_saved_actions = stream.read_bool()

    def save_binary(self, stream: ResStream):
        super().save_binary(stream)
        stream.write_dword(self.item_type)
        stream.write_dword(self.item_eq_slots_value)
        stream.write_dword(self.item_eq_slots_or)
        stream.write_dword(self.item_eq_slots_and)
        stream.write_bool(self.item_eq_slots_type)
        stream.write_bool(self.item_takeable)
        stream.write_dword(self.item_value)
        stream.write_dword(self.item_wt)
        stream.write_float(self.item_passive_defense_mod)
        stream.write_string(self.item_base_name)
        stream.write_string(self.item_dsc)
        stream.write_qword(self.item_render_object_female)
        stream.write_float(self.item_health_full)
        stream.write_dword(self.item_skill_used)
        stream.write_dword(self.item_skill_mastery_used)
        stream.write_dword(self.item_parry_anim_id)
        stream.write_dword(len(self.item_offering_info))
        for offering in self.item_offering_info:
            offering.save_binary(stream)
        if self.item_type == ITEM_TYPE_WEAPON:
            self.item_weapon.save_binary(stream)
            stream.write_dword(self.item_primary_attr)
            stream.write_dword(self.item_secondary_attr)
        if self.item_type == ITEM_TYPE_ARMOR:
            stream.write_float(self.item_bulk_factor)
            stream.write_dword(self.item_defense_rating)
        stream.write_dword(self.item_flags)
        stream.write_dword(self.item_use_flags)
        stream.write_qword(self.item_post_item_id)
        stream.write_dword(self.item_initial_charges)
        stream.write_dword(self.item_book_arcana)
        stream.write_dword(len(self.item_skill_req))
        for skill in self.item_skill_req:
            skill.save_binary(stream)
        self.item_race_req.save_binary(stream)
        self.item_class_req.save_binary(stream)
        self.item_disc_req.save_binary(stream)
        stream.write_dword(len(self.item_attr_req))
        for attr in self.item_attr_req:
            attr.save_binary(stream)
        stream.write_dword(self.item_level_req)
        stream.write_dword(self.item_rank_req)
        stream.write_dword(self.item_sex_req)
        stream.write_dword(len(self.item_user_power_action))
        for power in self.item_user_power_action:
            stream.write_dword(power[0])
            stream.write_dword(power[1])
            stream.write_dword(power[2])
        stream.write_dword(len(self.item_power_grant))
        for action in self.item_power_grant:
            action.save_binary(stream)
        stream.write_dword(len(self.item_power_action))
        for grant in self.item_power_action:
            grant.save_binary(stream)
        stream.write_bool(self.item_sheathable)
        if self.item_sheathable:
            stream.write_dword(self.item_sheath_slot)
            stream.write_tuple(self.item_sheath_offset)
            stream.write_tuple(self.item_sheath_rotation)
        stream.write_bool(self.item_has_stub)
        if self.item_has_stub:
            stream.write_bool(self.item_stub_holder[0])
            stream.write_qword(self.item_stub_holder[1])
        stream.write_dword(len(self.item_offering_adjustments))
        for offering in self.item_offering_adjustments:
            offering.save_binary(stream)
        stream.write_dword(len(self.item_resource_costs))
        for res in self.item_resource_costs:
            res.save_binary(stream)
        stream.write_dword(self.item_bane_rank)
        stream.write_bool(self.item_ignore_saved_actions)

    def load_json(self, data):
        super().load_json(data)
        self.item_type = STRING_TO_ITEM_TYPE[data['item_type']]
        self.item_eq_slots_value = data['item_eq_slots_value']
        self.item_eq_slots_type = data['item_eq_slots_type']
        value = 0
        for i in range(ITEM_EQUIP_SLOT_NUM):
            eq_slot = 1 << i
            if ITEM_EQIP_SLOT_TO_STRING[eq_slot] in data['item_eq_slots_or']:
                value |= eq_slot
        self.item_eq_slots_or = value
        value = 0
        for i in range(ITEM_EQUIP_SLOT_NUM):
            eq_slot = 1 << i
            if ITEM_EQIP_SLOT_TO_STRING[eq_slot] in data['item_eq_slots_and']:
                value |= eq_slot
        self.item_eq_slots_and = value
        self.item_takeable = data['item_takeable']
        self.item_value = data['item_value']
        self.item_wt = data['item_wt']
        self.item_passive_defense_mod = data['item_passive_defense_mod']
        self.item_base_name = data['item_base_name']
        self.item_dsc = data['item_dsc']
        self.item_render_object_female = data['item_render_object_female']
        self.item_health_full = data['item_health_full']
        self.item_skill_used = string_to_hash(data['item_skill_used'])
        self.item_skill_mastery_used = string_to_hash(data['item_skill_mastery_used'])
        self.item_parry_anim_id = data['item_parry_anim_id']
        self.item_offering_info = []
        for offering_data in data['item_offering_info']:
            offering = Offerings()
            offering.load_json(offering_data)
            self.item_offering_info.append(offering)
        if self.item_type == ITEM_TYPE_WEAPON:
            self.item_weapon = Weapon()
            self.item_weapon.load_json(data['item_weapon'])
            self.item_primary_attr = string_to_hash(data['item_primary_attr'])
            self.item_secondary_attr = string_to_hash(data['item_secondary_attr'])
        if self.item_type == ITEM_TYPE_ARMOR:
            self.item_bulk_factor = data['item_bulk_factor']
            self.item_defense_rating = data['item_defense_rating']
        value = 0
        for i in range(ITEM_FLAG_NUM):
            item_flag = 1 << i
            if ITEM_FLAG_TO_STRING[item_flag] in data['item_flags']:
                value |= item_flag
        self.item_flags = value
        value = 0
        for i in range(ITEM_USE_FLAGS_NUM):
            item_use_flag = 1 << i
            if ITEM_USE_FLAGS_TO_STRING[item_use_flag] in data['item_use_flags']:
                value |= item_use_flag
        self.item_use_flags = value
        self.item_post_item_id = data['item_post_item_id']
        self.item_initial_charges = data['item_initial_charges']
        self.item_book_arcana = data['item_book_arcana']
        self.item_skill_req = []
        for skill_data in data['item_skill_req']:
            skill = SkillLevel()
            skill.load_json(skill_data)
            self.item_skill_req.append(skill)
        self.item_race_req = RaceRequired()
        self.item_race_req.load_json(data['item_race_req'])
        self.item_class_req = ClassRequired()
        self.item_class_req.load_json(data['item_class_req'])
        self.item_disc_req = DiscRequired()
        self.item_disc_req.load_json(data['item_disc_req'])
        self.item_attr_req = []
        for attr_data in data['item_attr_req']:
            attr = AttributeValue()
            attr.load_json(attr_data)
            self.item_attr_req.append(attr)
        self.item_level_req = data['item_level_req']
        self.item_rank_req = data['item_rank_req']
        self.item_sex_req = STRING_TO_ITEM_SEX_REQ[data['item_sex_req']]
        self.item_user_power_action = []
        for action in data['item_user_power_action']:
            self.item_user_power_action.append([
                string_to_hash(action['power']),
                action['arguments'][0],
                action['arguments'][1],
            ])
        self.item_power_grant = []
        for grant_data in data['item_power_grant']:
            grant = PowerGrant()
            grant.load_json(grant_data)
            self.item_power_grant.append(grant)
        self.item_power_action = []
        for action_data in data['item_power_action']:
            action = PowerAction()
            action.load_json(action_data)
            self.item_power_action.append(action)
        self.item_sheathable = data['item_sheathable']
        if self.item_sheathable:
            self.item_sheath_slot = STRING_TO_ITEM_SHEATHSLOT[data['item_sheath_slot']]
            self.item_sheath_offset = data['item_sheath_offset']
            self.item_sheath_rotation = data['item_sheath_rotation']
        self.item_has_stub = data['item_has_stub']
        if self.item_has_stub:
            self.item_stub_holder = data['item_has_stub']
        self.item_offering_adjustments = []
        for offering_data in data['item_offering_adjustments']:
            offering = Offerings()
            offering.load_json(offering_data)
            self.item_offering_adjustments.append(offering)
        self.item_resource_costs = []
        for res_data in data['item_resource_costs']:
            res = ResourceInfo()
            res.load_json(res_data)
            self.item_resource_costs.append(res)
        self.item_bane_rank = data['item_bane_rank']
        self.item_ignore_saved_actions = data['item_ignore_saved_actions']

    def save_json(self):
        data = super().save_json()
        data['item_type'] = ITEM_TYPE_TO_STRING[self.item_type]
        data['item_eq_slots_value'] = self.item_eq_slots_value
        data['item_eq_slots_type'] = self.item_eq_slots_type
        if not self.item_eq_slots_or:
            data['item_eq_slots_or'] = [ITEM_EQIP_SLOT_TO_STRING[ITEM_EQUIP_SLOT_NONE]]
        else:
            data['item_eq_slots_or'] = []
            for i in range(ITEM_EQUIP_SLOT_NUM):
                eq_slot = 1 << i
                if self.item_eq_slots_or & eq_slot:
                    data['item_eq_slots_or'].append(ITEM_EQIP_SLOT_TO_STRING[eq_slot])
        if not self.item_eq_slots_and:
            data['item_eq_slots_and'] = [ITEM_EQIP_SLOT_TO_STRING[ITEM_EQUIP_SLOT_NONE]]
        else:
            data['item_eq_slots_and'] = []
            for i in range(ITEM_EQUIP_SLOT_NUM):
                eq_slot = 1 << i
                if self.item_eq_slots_and & eq_slot:
                    data['item_eq_slots_and'].append(ITEM_EQIP_SLOT_TO_STRING[eq_slot])
        data['item_takeable'] = self.item_takeable
        data['item_value'] = self.item_value
        data['item_wt'] = self.item_wt
        data['item_passive_defense_mod'] = self.item_passive_defense_mod
        data['item_base_name'] = self.item_base_name
        data['item_dsc'] = self.item_dsc
        data['item_render_object_female'] = self.item_render_object_female
        data['item_health_full'] = self.item_health_full
        data['item_skill_used'] = hash_to_string(self.item_skill_used)
        data['item_skill_mastery_used'] = hash_to_string(self.item_skill_mastery_used)
        data['item_parry_anim_id'] = self.item_parry_anim_id
        data['item_offering_info'] = []
        for offering in self.item_offering_info:
            data['item_offering_info'].append(offering.save_json())
        if self.item_type == ITEM_TYPE_WEAPON:
            data['item_weapon'] = self.item_weapon.save_json()
            data['item_primary_attr'] = hash_to_string(self.item_primary_attr)
            data['item_secondary_attr'] = hash_to_string(self.item_secondary_attr)
        if self.item_type == ITEM_TYPE_ARMOR:
            data['item_bulk_factor'] = self.item_bulk_factor
            data['item_defense_rating'] = self.item_defense_rating
        data['item_flags'] = []
        if self.item_flags:
            for i in range(ITEM_FLAG_NUM):
                item_flag = 1 << i
                if self.item_flags & item_flag:
                    data['item_flags'].append(ITEM_FLAG_TO_STRING[item_flag])
        data['item_use_flags'] = []
        if self.item_use_flags:
            for i in range(ITEM_USE_FLAGS_NUM):
                item_use_flag = 1 << i
                if self.item_use_flags & item_use_flag:
                    data['item_use_flags'].append(ITEM_USE_FLAGS_TO_STRING[item_use_flag])
        data['item_post_item_id'] = self.item_post_item_id
        data['item_initial_charges'] = self.item_initial_charges
        data['item_book_arcana'] = self.item_book_arcana
        data['item_skill_req'] = []
        for skill in self.item_skill_req:
            data['item_skill_req'].append(skill.save_json())
        data['item_race_req'] = self.item_race_req.save_json()
        data['item_class_req'] = self.item_class_req.save_json()
        data['item_disc_req'] = self.item_disc_req.save_json()
        data['item_attr_req'] = []
        for attr in self.item_attr_req:
            data['item_attr_req'].append(attr.save_json())
        data['item_level_req'] = self.item_level_req
        data['item_rank_req'] = self.item_rank_req
        data['item_sex_req'] = ITEM_SEX_REQ_TO_STRING[self.item_sex_req]
        data['item_user_power_action'] = []
        for action in self.item_user_power_action:
            data['item_user_power_action'].append({
                'power': hash_to_string(action[0]),
                'arguments': action[1:3],
            })
        data['item_power_grant'] = []
        for grant in self.item_power_grant:
            data['item_power_grant'].append(grant.save_json())
        data['item_power_action'] = []
        for action in self.item_power_action:
            data['item_power_action'].append(action.save_json())
        data['item_sheathable'] = self.item_sheathable
        if self.item_sheathable:
            data['item_sheath_slot'] = ITEM_SHEATHSLOT_TO_STRING[self.item_sheath_slot]
            data['item_sheath_offset'] = self.item_sheath_offset
            data['item_sheath_rotation'] = self.item_sheath_rotation
        data['item_has_stub'] = self.item_has_stub
        if self.item_has_stub:
            data['item_has_stub'] = self.item_stub_holder
        data['item_offering_adjustments'] = []
        for offering in self.item_offering_adjustments:
            data['item_offering_adjustments'].append(offering.save_json())
        data['item_resource_costs'] = []
        for res in self.item_resource_costs:
            data['item_resource_costs'].append(res.save_json())
        data['item_bane_rank'] = self.item_bane_rank
        data['item_ignore_saved_actions'] = self.item_ignore_saved_actions
        return data
