#  • ▌ ▄ ·. ▄▄▄▄·     ▄▄▄ .·▄▄▄▄  ▪  ▄▄▄▄▄      ▄▄▄       ▄▄▄·▄▄▄       
#  ·██ ▐███▪▐█ ▀█▪    ▀▄.▀·██▪ ██ ██ •██  ▪     ▀▄ █·    ▐█ ▄█▀▄ █·▪    
#  ▐█ ▌▐▌▐█·▐█▀▀█▄    ▐▀▀▪▄▐█· ▐█▌▐█· ▐█.▪ ▄█▀▄ ▐▀▀▄      ██▀·▐▀▀▄  ▄█▀▄
#  ██ ██▌▐█▌██▄▪▐█    ▐█▄▄▌██. ██ ▐█▌ ▐█▌·▐█▌.▐▌▐█•█▌    ▐█▪·•▐█•█▌▐█▌.▐▌
#  ▀▀  █▪▀▀▀·▀▀▀▀      ▀▀▀ ▀▀▀▀▀• ▀▀▀ ▀▀▀  ▀█▄▀▪.▀  ▀    .▀   .▀  ▀ ▀█▄▀▪
#                Magicbane Emulator Project © 2013 - 2022
#                           www.magicbane.com

from arcane.util import ResStream
from .MerchantInfo import MerchantInfo


class Product:
    def load_binary(self, stream: ResStream):
        self.product_cost = stream.read_dword()
        self.product_base_time = stream.read_dword()
        self.product_min_rank = stream.read_dword()
        self.product_is_complete = stream.read_bool()
        self.product_is_pending = stream.read_bool()
        self.product_order_num = stream.read_dword()
        self.product_time_mod = stream.read_dword()
        self.product_enchantment = stream.read_dword()
        self.product_action_prefix_id = stream.read_dword()
        self.product_action_suffix_id = stream.read_dword()
        self.product_u = stream.read_dword()
        self.product_u = stream.read_bool()
        self.product_id = stream.read_qword()
        self.product_pending_id = stream.read_qword()
        self.product_item_type_id = stream.read_qword()
        self.product_next_complete = [stream.read_dword() for _ in range(6)]


class MinionElement:
    def load_binary(self, stream: ResStream):
        self.minion_element_id = stream.read_qword()
        self.minion_element_type = stream.read_qword()
        self.minion_element_lookup = stream.read_qword()
        self.minion_element_base_time = stream.read_dword()
        self.minion_element_mod_time = stream.read_dword()
        self.minion_element_u = stream.read_dword()
        self.minion_element_is_complete = stream.read_bool()
        self.minion_element_next_complete = [stream.read_dword() for _ in range(6)]
        self.minion_element_name = stream.read_string()
        self.minion_element_u = stream.read_string()
        self.minion_element_rank = stream.read_dword()
        self.minion_element_category = stream.read_dword()
        self.minion_element_u = stream.read_string()
        self.minion_element_u = stream.read_string()


class ServiceElement:
    def load_binary(self, stream: ResStream):
        self.service_element_id = stream.read_qword()
        self.service_element_keyword = stream.read_dword()
        self.service_element_key_value = stream.read_dword()
        self.service_element_description = stream.read_string()
        self.service_element_unit_description = stream.read_string()
        self.service_element_cost = stream.read_dword()
        self.service_element_unit_value = stream.read_dword()
        self.service_element_min_rank = stream.read_dword()


class HirelingMod:
    def load_binary(self, stream: ResStream):
        self.hireling_mod_type = stream.read_dword()
        self.hireling_mod_rank = stream.read_dword()
        self.hireling_mod_quantity = stream.read_dword()
        self.hireling_mod_percent = stream.read_float()


class JunkerBasics:
    def load_binary(self, stream: ResStream):
        self.junker_auto_junk = stream.read_bool()
        self.junker_auto_junk_magic = stream.read_bool()
        self.junker_auto_junk_int = stream.read_dword()
        self.junker_auto_junk_magic_int = stream.read_dword()


class HirelingInfo(MerchantInfo):
    def load_binary(self, stream: ResStream):
        super().load_binary(stream)
        self.hireling_all_items = stream.read_bool()
        self.hireling_rank = stream.read_dword()
        self.hireling_title = stream.read_string()
        self.hireling_salary = stream.read_dword()
        self.hireling_upgrade_cost = stream.read_dword()
        self.hireling_upgrade_time = stream.read_dword()
        self.hireling_can_upgrade = stream.read_bool()
        self.hireling_use_specified_location = stream.read_bool()
        self.hireling_category = stream.read_dword()
        num_npc_features = stream.read_dword()
        self.hireling_npc_features = [stream.read_dword() for _ in range(num_npc_features)]
        num_item_types = stream.read_dword()
        self.hireling_item_types = [stream.read_dword() for _ in range(num_item_types)]
        num_products = stream.read_dword()
        self.hireling_products = [Product() for _ in range(num_products)]
        num_stocks = stream.read_dword()
        self.hireling_stocks = [Product() for _ in range(num_stocks)]
        num_minions = stream.read_dword()
        self.hireling_minions = [MinionElement() for _ in range(num_minions)]
        num_servies = stream.read_dword()
        self.hireling_servies = [ServiceElement() for _ in range(num_servies)]
        num_orders = stream.read_dword()
        self.hireling_orders = [[
            stream.read_dword() for _ in range(4)
        ] for _ in range(num_orders)]
        num_starting_formulas = stream.read_dword()
        self.hireling_starting_formulas = [stream.read_qword() for _ in range(num_starting_formulas)]
        num_valid_formula_types = stream.read_dword()
        self.hireling_valid_formula_types = [stream.read_dword() for _ in range(num_valid_formula_types)]
        num_valid_formula_categories = stream.read_dword()
        self.hireling_valid_formula_category = [stream.read_dword() for _ in range(num_valid_formula_categories)]
        num_enchantment_types = stream.read_dword()
        self.hireling_enchantment_types = [stream.read_dword() for _ in range(num_enchantment_types)]
        num_valid_weapons = stream.read_dword()
        self.hireling_valid_weapons = [stream.read_dword() for _ in range(num_valid_weapons)]
        num_valid_armors = stream.read_dword()
        self.hireling_valid_armors = [stream.read_dword() for _ in range(num_valid_armors)]
        num_valid_slaves = stream.read_dword()
        self.hireling_valid_slaves = [stream.read_dword() for _ in range(num_valid_slaves)]
        num_mods = stream.read_dword()
        self.hireling_mods = [HirelingMod() for _ in range(num_mods)]
        for mod in self.hireling_mods:
            mod.load_binary(stream)
        self.hireling_max_items_stocked = stream.read_dword()
        self.hireling_has_junker = stream.read_bool()
        if self.hireling_has_junker:
            self.hireling_junker = JunkerBasics()
            self.hireling_junker.load_binary(stream)
