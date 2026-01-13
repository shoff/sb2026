
from collections import OrderedDict

from arcane.enums.hashes import hash_to_string, string_to_hash
from arcane.util import ResStream


class AttributeValue:
    def load_binary(self, stream: ResStream):
        self.attr_type = stream.read_dword()
        self.attr_value = stream.read_dword()

    def save_binary(self, stream: ResStream):
        stream.write_dword(self.attr_type)
        stream.write_dword(self.attr_value)

    def load_json(self, data):
        self.attr_type = string_to_hash(data['attr_type'])
        self.attr_value = data['attr_value']

    def save_json(self):
        data = OrderedDict()
        data['attr_type'] = hash_to_string(self.attr_type)
        data['attr_value'] = self.attr_value
        return data


class PowerArgument:
    def load_binary(self, stream: ResStream):
        self.power_arguments = [
            stream.read_dword(),
            stream.read_dword(),
        ]

    def save_binary(self, stream: ResStream):
        stream.write_dword(self.power_arguments[0])
        stream.write_dword(self.power_arguments[1])

    def load_json(self, data):
        self.power_arguments = data['power_arguments']

    def save_json(self):
        data = OrderedDict()
        data['power_arguments'] = self.power_arguments
        return data


class SkillLevel:
    def load_binary(self, stream: ResStream):
        self.skill_type = stream.read_dword()
        self.skill_level = stream.read_dword()

    def save_binary(self, stream: ResStream):
        stream.write_dword(self.skill_type)
        stream.write_dword(self.skill_level)

    def load_json(self, data):
        self.skill_type = string_to_hash(data['skill_type'])
        self.skill_level = data['skill_level']

    def save_json(self):
        data = OrderedDict()
        data['skill_type'] = hash_to_string(self.skill_type)
        data['skill_level'] = self.skill_level
        return data


class ResourceInfo:
    def load_binary(self, stream: ResStream):
        self.resource_type = stream.read_dword()
        self.resource_value = stream.read_dword()

    def save_binary(self, stream: ResStream):
        stream.write_dword(self.resource_type)
        stream.write_dword(self.resource_value)

    def load_json(self, data):
        self.resource_type = string_to_hash(data['resource_type'])
        self.resource_value = data['resource_value']

    def save_json(self):
        data = OrderedDict()
        data['resource_type'] = hash_to_string(self.resource_type)
        data['resource_value'] = self.resource_value
        return data


class PowerAction:
    def load_binary(self, stream: ResStream):
        self.power_type = stream.read_dword()

        num_grants = stream.read_dword()
        self.power_actions = [PowerArgument() for _ in range(num_grants)]
        for power in self.power_actions:
            power.load_binary(stream)

    def save_binary(self, stream: ResStream):
        stream.write_dword(self.power_type)
        stream.write_dword(len(self.power_actions))
        for power in self.power_actions:
            power.save_binary(stream)

    def load_json(self, data):
        self.power_type = string_to_hash(data['power_type'])
        self.power_actions = []
        for power_data in data['power_actions']:
            power = PowerArgument()
            power.load_json(power_data)
            self.power_actions.append(power)

    def save_json(self):
        data = OrderedDict()
        data['power_type'] = hash_to_string(self.power_type)
        data['power_actions'] = []
        for power in self.power_actions:
            data['power_actions'].append(power.save_json())
        return data


class PowerGrant:
    def load_binary(self, stream: ResStream):
        self.power_type = stream.read_dword()
        self.power_value = stream.read_dword()
        num_attrs = stream.read_dword()
        self.power_granted_attrs = [
            [
                stream.read_dword(),
                stream.read_dword(),
            ] for _ in range(num_attrs)
        ]
        num_skills = stream.read_dword()
        self.power_granted_skills = [
            [
                stream.read_dword(),
                stream.read_dword(),
            ] for _ in range(num_skills)
        ]
        num_powers = stream.read_dword()
        self.power_granted_powers = [
            [
                stream.read_dword(),
                stream.read_dword(),
            ] for _ in range(num_powers)
        ]
        num_monster_types = stream.read_dword()
        self.power_monster_types = [
            stream.read_dword() for _ in range(num_monster_types)
        ]

    def save_binary(self, stream: ResStream):
        stream.write_dword(self.power_type)
        stream.write_dword(self.power_value)
        stream.write_dword(len(self.power_granted_attrs))
        for attr in self.power_granted_attrs:
            stream.write_dword(attr[0])
            stream.write_dword(attr[1])
        stream.write_dword(len(self.power_granted_skills))
        for skill in self.power_granted_skills:
            stream.write_dword(skill[0])
            stream.write_dword(skill[1])
        stream.write_dword(len(self.power_granted_powers))
        for power in self.power_granted_powers:
            stream.write_dword(power[0])
            stream.write_dword(power[1])
        stream.write_dword(len(self.power_monster_types))
        for value in self.power_monster_types:
            stream.write_dword(value)

    def load_json(self, data):
        self.power_type = string_to_hash(data['power_type'])
        self.power_value = data['power_value']
        self.power_granted_attrs = data['power_granted_attrs']
        self.power_granted_skills = data['power_granted_skills']
        self.power_granted_powers = data['power_granted_powers']
        self.power_monster_types = data['power_monster_types']

    def save_json(self):
        data = OrderedDict()
        data['power_type'] = hash_to_string(self.power_type)
        data['power_value'] = self.power_value
        data['power_granted_attrs'] = self.power_granted_attrs
        data['power_granted_skills'] = self.power_granted_skills
        data['power_granted_powers'] = self.power_granted_powers
        data['power_monster_types'] = self.power_monster_types
        return data


class SkillGrant:
    def load_binary(self, stream: ResStream):
        self.skill_type = stream.read_dword()
        self.skill_value = stream.read_dword()
        num_attrs = stream.read_dword()
        self.skill_granted_attrs = [
            [
                stream.read_dword(),
                stream.read_dword(),
            ] for _ in range(num_attrs)
        ]
        num_skills = stream.read_dword()
        self.skill_granted_skills = [
            [
                stream.read_dword(),
                stream.read_dword(),
            ] for _ in range(num_skills)
        ]
        num_powers = stream.read_dword()
        self.skill_granted_powers = [
            [
                stream.read_dword(),
                stream.read_dword(),
            ] for _ in range(num_powers)
        ]
        num_monster_types = stream.read_dword()
        self.skill_monster_types = [
            stream.read_dword() for _ in range(num_monster_types)
        ]

    def save_binary(self, stream: ResStream):
        stream.write_dword(self.skill_type)
        stream.write_dword(self.skill_value)
        stream.write_dword(len(self.skill_granted_attrs))
        for attr in self.skill_granted_attrs:
            stream.write_dword(attr[0])
            stream.write_dword(attr[1])
        stream.write_dword(len(self.skill_granted_skills))
        for skill in self.skill_granted_skills:
            stream.write_dword(skill[0])
            stream.write_dword(skill[1])
        stream.write_dword(len(self.skill_granted_powers))
        for power in self.skill_granted_powers:
            stream.write_dword(power[0])
            stream.write_dword(power[1])
        stream.write_dword(len(self.skill_monster_types))
        for value in self.skill_monster_types:
            stream.write_dword(value)

    def load_json(self, data):
        self.skill_type = string_to_hash(data['skill_type'])
        self.skill_value = data['skill_value']
        self.skill_granted_attrs = data['skill_granted_attrs']
        self.skill_granted_skills = data['skill_granted_skills']
        self.skill_granted_powers = data['skill_granted_powers']
        self.skill_monster_types = data['skill_monster_types']

    def save_json(self):
        data = OrderedDict()
        data['skill_type'] = hash_to_string(self.skill_type)
        data['skill_value'] = self.skill_value
        data['skill_granted_attrs'] = self.skill_granted_attrs
        data['skill_granted_skills'] = self.skill_granted_skills
        data['skill_granted_powers'] = self.skill_granted_powers
        data['skill_monster_types'] = self.skill_monster_types
        return data
