#  • ▌ ▄ ·. ▄▄▄▄·     ▄▄▄ .·▄▄▄▄  ▪  ▄▄▄▄▄      ▄▄▄       ▄▄▄·▄▄▄       
#  ·██ ▐███▪▐█ ▀█▪    ▀▄.▀·██▪ ██ ██ •██  ▪     ▀▄ █·    ▐█ ▄█▀▄ █·▪    
#  ▐█ ▌▐▌▐█·▐█▀▀█▄    ▐▀▀▪▄▐█· ▐█▌▐█· ▐█.▪ ▄█▀▄ ▐▀▀▄      ██▀·▐▀▀▄  ▄█▀▄
#  ██ ██▌▐█▌██▄▪▐█    ▐█▄▄▌██. ██ ▐█▌ ▐█▌·▐█▌.▐▌▐█•█▌    ▐█▪·•▐█•█▌▐█▌.▐▌
#  ▀▀  █▪▀▀▀·▀▀▀▀      ▀▀▀ ▀▀▀▀▀• ▀▀▀ ▀▀▀  ▀█▄▀▪.▀  ▀    .▀   .▀  ▀ ▀█▄▀▪
#                Magicbane Emulator Project © 2013 - 2022
#                           www.magicbane.com

from arcane.util import ResStream
from .ArcItem import ArcItem
from .common.Inventory import Inventory


class ArcContainerObject(ArcItem):
    def load_binary(self, stream: ResStream):
        super().load_binary(stream)
        self.container_open = stream.read_dword()
        self.container_locked = stream.read_dword()
        self.container_locked_rank = stream.read_dword()
        self.container_barred = stream.read_dword()
        self.container_barred_rank = stream.read_dword()
        self.container_trapped = stream.read_dword()
        self.container_trappe_rank = stream.read_dword()
        num_contents = stream.read_dword()
        self.container_inventory_contents = [Inventory() for _ in range(num_contents)]
        for content in self.container_inventory_contents:
            content.load_binary(stream)

    def save_binary(self, stream: ResStream):
        super().save_binary(stream)
        stream.read_dword(self.container_open)
        stream.read_dword(self.container_locked)
        stream.read_dword(self.container_locked_rank)
        stream.read_dword(self.container_barred)
        stream.read_dword(self.container_barred_rank)
        stream.read_dword(self.container_trapped)
        stream.read_dword(self.container_trappe_rank)
        stream.read_dword(len(self.container_inventory_contents))
        for content in self.container_inventory_contents:
            content.save_binary(stream)

    def load_json(self, data):
        super().load_json()
        self.container_open = data['container_open']
        self.container_locked = data['container_locked']
        self.container_locked_rank = data['container_locked_rank']
        self.container_barred = data['container_barred']
        self.container_barred_rank = data['container_barred_rank']
        self.container_trapped = data['container_trapped']
        self.container_trappe_rank = data['container_trappe_rank']
        self.container_inventory_contents = []
        for content_data in data['container_inventory_contents']:
            content = Inventory()
            content.load_json(content_data)
            self.container_inventory_contents.append(content)

    def save_json(self):
        data = super().save_json()
        data['container_open'] = self.container_open
        data['container_locked'] = self.container_locked
        data['container_locked_rank'] = self.container_locked_rank
        data['container_barred'] = self.container_barred
        data['container_barred_rank'] = self.container_barred_rank
        data['container_trapped'] = self.container_trapped
        data['container_trappe_rank'] = self.container_trappe_rank
        data['container_inventory_contents'] = []
        for content in self.container_inventory_contents:
            data['container_inventory_contents'].append(content.save_json())
        return data
