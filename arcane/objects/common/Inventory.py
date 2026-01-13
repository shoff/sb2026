

from collections import OrderedDict

from arcane.enums.common.arc_inventory import *
from arcane.util import ResStream


class Inventory:
    def load_binary(self, stream: ResStream):
        self.inventory_type = stream.read_dword()

        if self.inventory_type == INVENTORY_TYPE_GOLD:
            self.inventory_gold = [
                stream.read_float(),
                stream.read_float(),
                stream.read_float(),
            ]
        elif self.inventory_type == INVENTORY_TYPE_ITEM:
            self.inventory_items = [
                stream.read_float(),
                stream.read_qword(),
            ]
        elif self.inventory_type == INVENTORY_TYPE_BOOTYTABLE:
            self.inventory_table = [
                stream.read_float(),
                stream.read_dword(),
            ]

    def save_binary(self, stream: ResStream):
        stream.write_dword(self.inventory_type)
        if self.inventory_type == INVENTORY_TYPE_GOLD:
            stream.write_float(self.inventory_gold[0])
            stream.write_float(self.inventory_gold[1])
            stream.write_float(self.inventory_gold[2])
        elif self.inventory_type == INVENTORY_TYPE_ITEM:
            stream.write_float(self.inventory_items[0])
            stream.write_qword(self.inventory_items[1])
        elif self.inventory_type == INVENTORY_TYPE_BOOTYTABLE:
            stream.write_float(self.inventory_table[0])
            stream.write_dword(self.inventory_table[1])

    def load_json(self, data):
        self.inventory_type = STRING_TO_INVENTORY_TYPE[data['type']]
        if self.inventory_type == INVENTORY_TYPE_GOLD:
            self.inventory_gold = data['gold']
        elif self.inventory_type == INVENTORY_TYPE_ITEM:
            self.inventory_items = data['items']
        elif self.inventory_type == INVENTORY_TYPE_BOOTYTABLE:
            self.inventory_table = data['table']

    def save_json(self):
        data = OrderedDict()
        data['type'] = INVENTORY_TYPE_TO_STRING[self.inventory_type]
        if self.inventory_type == INVENTORY_TYPE_GOLD:
            data['gold'] = self.inventory_gold
        elif self.inventory_type == INVENTORY_TYPE_ITEM:
            data['items'] = self.inventory_items
        elif self.inventory_type == INVENTORY_TYPE_BOOTYTABLE:
            data['table'] = self.inventory_table
        return data
