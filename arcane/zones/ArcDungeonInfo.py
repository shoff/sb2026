#  • ▌ ▄ ·. ▄▄▄▄·     ▄▄▄ .·▄▄▄▄  ▪  ▄▄▄▄▄      ▄▄▄       ▄▄▄·▄▄▄       
#  ·██ ▐███▪▐█ ▀█▪    ▀▄.▀·██▪ ██ ██ •██  ▪     ▀▄ █·    ▐█ ▄█▀▄ █·▪    
#  ▐█ ▌▐▌▐█·▐█▀▀█▄    ▐▀▀▪▄▐█· ▐█▌▐█· ▐█.▪ ▄█▀▄ ▐▀▀▄      ██▀·▐▀▀▄  ▄█▀▄
#  ██ ██▌▐█▌██▄▪▐█    ▐█▄▄▌██. ██ ▐█▌ ▐█▌·▐█▌.▐▌▐█•█▌    ▐█▪·•▐█•█▌▐█▌.▐▌
#  ▀▀  █▪▀▀▀·▀▀▀▀      ▀▀▀ ▀▀▀▀▀• ▀▀▀ ▀▀▀  ▀█▄▀▪.▀  ▀    .▀   .▀  ▀ ▀█▄▀▪
#                Magicbane Emulator Project © 2013 - 2022
#                           www.magicbane.com

from collections import OrderedDict

from arcane.util import ResStream


class ArcDungeonInfo:
    def load_binary(self, stream: ResStream):
        self.dungeon_template_id = stream.read_qword()
        self.dungeon_unknown = stream.read_qword()
        self.dungeon_spawn_location = stream.read_tuple()
        self.dungeon_y_offset = stream.read_float()

    def save_binary(self, stream: ResStream):
        stream.write_qword(self.dungeon_template_id)
        stream.write_qword(self.dungeon_unknown)
        stream.write_tuple(self.dungeon_spawn_location)
        stream.write_float(self.dungeon_y_offset)

    def save_json(self):
        data = OrderedDict()
        data['dungeon_template_id'] = self.dungeon_template_id
        data['dungeon_unknown'] = self.dungeon_unknown
        data['dungeon_spawn_location'] = self.dungeon_spawn_location
        data['dungeon_y_offset'] = self.dungeon_y_offset
        return data

    def load_json(self, data):
        self.dungeon_template_id = data['dungeon_template_id']
        self.dungeon_unknown = data['dungeon_unknown']
        self.dungeon_spawn_location = data['dungeon_spawn_location']
        self.dungeon_y_offset = data['dungeon_y_offset']
