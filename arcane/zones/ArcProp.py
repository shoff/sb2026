from collections import OrderedDict

from arcane.enums.hashes import hash_to_string, string_to_hash
from arcane.enums.zone.arc_prop import *
from arcane.objects.common.Inventory import Inventory
from arcane.util import ResStream
from .ArcMobile import ArcMobile
from .mobile.ArcBasicZoneObjectInfo import ArcBasicZoneObjectInfo


class ArcPropInfo:

    def load_binary(self, stream: ResStream):
        self.prop_basic_zone = ArcBasicZoneObjectInfo()
        self.prop_basic_zone.load_binary(stream)
        self.prop_has_platform = stream.read_bool()
        self.prop_platform_height = stream.read_float()
        self.prop_is_light_data = stream.read_bool()
        if self.prop_is_light_data:
            self.prop_light_color = [stream.read_dword() for _ in range(4)]
            self.prop_light_radius = stream.read_float()
            self.prop_light_flicker = stream.read_dword()
            self.prop_light_cube_map = stream.read_dword()
        num_content_props = stream.read_dword()
        self.prop_content_props = [ArcProp() for _ in range(num_content_props)]
        for prop in self.prop_content_props:
            prop.load_binary(stream)
        num_content_mobiles = stream.read_dword()
        self.prop_content_mobiles = [ArcMobile() for _ in range(num_content_mobiles)]
        for mobile in self.prop_content_mobiles:
            mobile.load_binary(stream)
        num_descriptors = stream.read_dword()
        self.prop_descriptors = [stream.read_string() for _ in range(num_descriptors)]
        self.prop_registry = stream.read_dword()
        if self.prop_registry:
            self.prop_registry_name = stream.read_string()
        self.prop_has_zone_event = stream.read_bool()
        self.prop_has_teleporter = stream.read_bool()

        if self.prop_has_zone_event:
            self.prop_zone_event = stream.read_dword()

        if self.prop_has_teleporter:
            self.prop_teleporter = stream.read_dword()

    def save_binary(self, stream: ResStream):
        self.prop_basic_zone.save_binary(stream)
        stream.write_bool(self.prop_has_platform)
        stream.write_float(self.prop_platform_height)
        stream.write_bool(self.prop_is_light_data)
        if self.prop_is_light_data:
            for i in range(4):
                stream.write_dword(self.prop_light_color[i])
            stream.write_float(self.prop_light_radius)
            stream.write_dword(self.prop_light_flicker)
            stream.write_dword(self.prop_light_cube_map)

        stream.write_dword(len(self.prop_content_props))
        for prop in self.prop_content_props:
            prop.save_binary(stream)

        stream.write_dword(len(self.prop_content_mobiles))
        for mobile in self.prop_content_mobiles:
            mobile.save_binary(stream)

        stream.write_dword(len(self.prop_descriptors))
        for descriptor in self.prop_descriptors:
            stream.write_string(descriptor)

        stream.write_dword(self.prop_registry)
        if self.prop_registry:
            stream.write_string(self.prop_registry_name)

        stream.write_bool(self.prop_has_zone_event)
        stream.write_bool(self.prop_has_teleporter)

        if self.prop_has_zone_event:
            stream.write_dword(self.prop_zone_event)
        if self.prop_has_teleporter:
            stream.write_dword(self.prop_teleporter)

    def save_json(self):
        data = OrderedDict()
        data['prop_basic_zone'] = self.prop_basic_zone.save_json()
        data['prop_has_platform'] = self.prop_has_platform
        data['prop_platform_height'] = self.prop_platform_height
        data['prop_is_light_data'] = self.prop_is_light_data
        if self.prop_is_light_data:
            data['prop_light_color'] = self.prop_light_color
            data['prop_light_radius'] = self.prop_light_radius
            data['prop_light_flicker'] = self.prop_light_flicker
            data['prop_light_cube_map'] = self.prop_light_cube_map
        data['prop_content_props'] = []
        for prop in self.prop_content_props:
            data['prop_content_props'].append(prop.save_json())
        data['prop_content_mobiles'] = []
        for mobile in self.prop_content_mobiles:
            data['prop_content_mobiles'].append(mobile.save_json())
        data['prop_descriptors'] = self.prop_descriptors
        data['prop_registry'] = self.prop_registry
        if self.prop_registry:
            data['prop_registry_name'] = self.prop_registry_name
        data['prop_has_zone_event'] = self.prop_has_zone_event
        data['prop_has_teleporter'] = self.prop_has_teleporter
        if self.prop_has_zone_event:
            data['prop_zone_event'] = hash_to_string(self.prop_zone_event)
        if self.prop_has_teleporter:
            data['prop_teleporter'] = hash_to_string(self.prop_teleporter)
        return data

    def load_json(self, data):
        self.prop_basic_zone = ArcBasicZoneObjectInfo()
        self.prop_basic_zone.load_json(data['prop_basic_zone'])
        self.prop_has_platform = data['prop_has_platform']
        self.prop_platform_height = data['prop_platform_height']
        self.prop_is_light_data = data['prop_is_light_data']
        if self.prop_is_light_data:
            self.prop_light_color = data['prop_light_color']
            self.prop_light_radius = data['prop_light_radius']
            self.prop_light_flicker = data['prop_light_flicker']
            self.prop_light_cube_map = data['prop_light_cube_map']
        self.prop_content_props = []
        for prop_data in data['prop_content_props']:
            prop = ArcProp()
            prop.load_json(prop_data)
            self.prop_content_props.append(prop)
        self.prop_content_mobiles = []
        for mobile_data in data['prop_content_mobiles']:
            mobile = ArcMobile()
            mobile.load_json(mobile_data)
            self.prop_content_mobiles.append(mobile)
        self.prop_descriptors = data['prop_descriptors']
        self.prop_registry = data['prop_registry']
        if self.prop_registry:
            self.prop_registry_name = data['prop_registry_name']
        self.prop_has_zone_event = data['prop_has_zone_event']
        self.prop_has_teleporter = data['prop_has_teleporter']
        if self.prop_has_zone_event:
            self.prop_zone_event = string_to_hash(data['prop_zone_event'])
        if self.prop_has_teleporter:
            self.prop_teleporter = string_to_hash(data['prop_teleporter'])


class ArcCityPropInfo(ArcPropInfo):
    def load_binary(self, stream: ResStream):
        super().load_binary(stream)
        self.city_prop_gm_guild = stream.read_dword()
        self.city_prop_gm_nation = stream.read_dword()
        self.city_prop_asset_rank = stream.read_dword()
        self.city_prop_asset_funds = stream.read_dword()

    def save_binary(self, stream: ResStream):
        super().save_binary(stream)
        stream.write_dword(self.city_prop_gm_guild)
        stream.write_dword(self.city_prop_gm_nation)
        stream.write_dword(self.city_prop_asset_rank)
        stream.write_dword(self.city_prop_asset_funds)

    def save_json(self):
        data = super().save_json()
        data['city_prop_gm_guild'] = self.city_prop_gm_guild
        data['city_prop_gm_nation'] = self.city_prop_gm_nation
        data['city_prop_asset_rank'] = self.city_prop_asset_rank
        data['city_prop_asset_funds'] = self.city_prop_asset_funds
        return data

    def load_json(self, data):
        super().load_json(data)
        self.city_prop_gm_guild = data['city_prop_gm_guild']
        self.city_prop_gm_nation = data['city_prop_gm_nation']
        self.city_prop_asset_rank = data['city_prop_asset_rank']
        self.city_prop_asset_funds = data['city_prop_asset_funds']


class ArcContainerInfo(ArcPropInfo):
    def load_binary(self, stream: ResStream):
        super().load_binary(stream)
        self.container_locked = stream.read_dword()
        self.container_locked_rank = stream.read_dword()
        self.container_barred = stream.read_dword()
        self.container_barred_rank = stream.read_dword()
        self.container_trapped = stream.read_dword()
        self.container_trapped_rank = stream.read_dword()
        num_booties = stream.read_dword()
        self.container_booties = [Inventory() for _ in range(num_booties)]
        for inventory in self.container_booties:
            inventory.load_binary(stream)

    def save_binary(self, stream: ResStream):
        super().save_binary(stream)
        stream.write_dword(self.container_locked)
        stream.write_dword(self.container_locked_rank)
        stream.write_dword(self.container_barred)
        stream.write_dword(self.container_barred_rank)
        stream.write_dword(self.container_trapped)
        stream.write_dword(self.container_trapped_rank)
        stream.write_dword(len(self.container_booties))
        for inventory in self.container_booties:
            inventory.save_binary(stream)

    def save_json(self):
        data = super().save_json()
        data['container_locked'] = self.container_locked
        data['container_locked_rank'] = self.container_locked_rank
        data['container_barred'] = self.container_barred
        data['container_barred_rank'] = self.container_barred_rank
        data['container_trapped'] = self.container_trapped
        data['container_trapped_rank'] = self.container_trapped_rank
        data['container_booties'] = []
        for inventory in self.container_booties:
            data['container_booties'].append(inventory.save_json())
        return data

    def load_json(self, data):
        super().load_json(data)
        self.container_locked = data['container_locked']
        self.container_locked_rank = data['container_locked_rank']
        self.container_barred = data['container_barred']
        self.container_barred_rank = data['container_barred_rank']
        self.container_trapped = data['container_trapped']
        self.container_trapped_rank = data['container_trapped_rank']
        self.container_booties = []
        for inventory_data in data['container_booties']:
            inventory = Inventory()
            inventory.load_json(inventory_data)
            self.container_booties.append(inventory)


class ArcProp:

    def load_binary(self, stream: ResStream):
        self.prop_type = stream.read_dword()

        if self.prop_type == 5:
            self.prop_data = ArcPropInfo()
            self.prop_data.load_binary(stream)
        elif self.prop_type == 6:
            self.prop_data = ArcCityPropInfo()
            self.prop_data.load_binary(stream)
        elif self.prop_type == 7:
            self.prop_data = ArcContainerInfo()
            self.prop_data.load_binary(stream)

    def save_binary(self, stream: ResStream):
        stream.write_dword(self.prop_type)
        self.prop_data.save_binary(stream)

    def save_json(self):
        data = OrderedDict()
        data['prop_type'] = PROP_TO_STRING[self.prop_type]
        data['prop_data'] = self.prop_data.save_json()
        return data

    def load_json(self, data):
        self.prop_type = STRING_TO_PROP[data['prop_type']]
        if self.prop_type == 5:
            self.prop_data = ArcPropInfo()
        elif self.prop_type == 6:
            self.prop_data = ArcCityPropInfo()
        elif self.prop_type == 7:
            self.prop_data = ArcContainerInfo()
        self.prop_data.load_json(data['prop_data'])
