#  • ▌ ▄ ·. ▄▄▄▄·     ▄▄▄ .·▄▄▄▄  ▪  ▄▄▄▄▄      ▄▄▄       ▄▄▄·▄▄▄       
#  ·██ ▐███▪▐█ ▀█▪    ▀▄.▀·██▪ ██ ██ •██  ▪     ▀▄ █·    ▐█ ▄█▀▄ █·▪    
#  ▐█ ▌▐▌▐█·▐█▀▀█▄    ▐▀▀▪▄▐█· ▐█▌▐█· ▐█.▪ ▄█▀▄ ▐▀▀▄      ██▀·▐▀▀▄  ▄█▀▄
#  ██ ██▌▐█▌██▄▪▐█    ▐█▄▄▌██. ██ ▐█▌ ▐█▌·▐█▌.▐▌▐█•█▌    ▐█▪·•▐█•█▌▐█▌.▐▌
#  ▀▀  █▪▀▀▀·▀▀▀▀      ▀▀▀ ▀▀▀▀▀• ▀▀▀ ▀▀▀  ▀█▄▀▪.▀  ▀    .▀   .▀  ▀ ▀█▄▀▪
#                Magicbane Emulator Project © 2013 - 2022
#                           www.magicbane.com

from arcane.util.ResStream import ResStream
from .ArcStructureObject import ArcStructureObject


class ArcDungeonUnitObject(ArcStructureObject):
    def load_binary(self, stream: ResStream):
        super().load_binary(stream)
        num_connectables = stream.read_dword()
        self.dungeon_connectable_edges = [
            stream.read_dword() for _ in range(num_connectables)
        ]

    def save_binary(self, stream: ResStream):
        super().save_binary(stream)
        stream.write_dword(len(self.dungeon_connectable_edges))
        for edge in self.dungeon_connectable_edges:
            stream.write_dword(edge)

    def load_json(self, data):
        super().load_json(data)
        self.dungeon_connectable_edges = data['dungeon_connectable_edges']
        return data

    def save_json(self):
        data = super().save_json()
        data['dungeon_connectable_edges'] = self.dungeon_connectable_edges
        return data


class ArcDungeonExitObject(ArcDungeonUnitObject):
    pass


class ArcDungeonStairObject(ArcDungeonUnitObject):
    pass
