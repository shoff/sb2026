#  • ▌ ▄ ·. ▄▄▄▄·     ▄▄▄ .·▄▄▄▄  ▪  ▄▄▄▄▄      ▄▄▄       ▄▄▄·▄▄▄       
#  ·██ ▐███▪▐█ ▀█▪    ▀▄.▀·██▪ ██ ██ •██  ▪     ▀▄ █·    ▐█ ▄█▀▄ █·▪    
#  ▐█ ▌▐▌▐█·▐█▀▀█▄    ▐▀▀▪▄▐█· ▐█▌▐█· ▐█.▪ ▄█▀▄ ▐▀▀▄      ██▀·▐▀▀▄  ▄█▀▄
#  ██ ██▌▐█▌██▄▪▐█    ▐█▄▄▌██. ██ ▐█▌ ▐█▌·▐█▌.▐▌▐█•█▌    ▐█▪·•▐█•█▌▐█▌.▐▌
#  ▀▀  █▪▀▀▀·▀▀▀▀      ▀▀▀ ▀▀▀▀▀• ▀▀▀ ▀▀▀  ▀█▄▀▪.▀  ▀    .▀   .▀  ▀ ▀█▄▀▪
#                Magicbane Emulator Project © 2013 - 2022
#                           www.magicbane.com

from collections import OrderedDict

from arcane.enums.arc_combat import *
from arcane.util import ResStream
from .ArcObj import ArcObj


class ArcCombatObj(ArcObj):
    def load_binary(self, stream: ResStream):
        super().load_binary(stream)
        self.combat_health_current = stream.read_float()
        self.combat_health_full = stream.read_float()
        self.combat_attack_resist = [
            stream.read_float() for _ in range(0x10)
        ]
        num_powers = stream.read_dword()
        self.combat_powers = [
            [
                stream.read_dword(),
                stream.read_dword(),
            ] for _ in range(num_powers)
        ]

    def save_binary(self, stream: ResStream):
        super().save_binary(stream)
        stream.write_float(self.combat_health_current)
        stream.write_float(self.combat_health_full)
        for i in range(0x10):
            stream.write_float(self.combat_attack_resist[i])
        stream.write_dword(len(self.combat_powers))
        for power in self.combat_powers:
            stream.write_dword(power[0])
            stream.write_dword(power[1])

    def load_json(self, data):
        super().load_json(data)
        self.combat_health_current = data['combat_health_current']
        self.combat_health_full = data['combat_health_full']
        self.combat_attack_resist = []
        for i in range(0x10):
            self.combat_attack_resist.append(data['combat_attack_resist'][
                                                 ATTACK_RESIST_TO_STRING[i]
                                             ])
        self.combat_powers = data['combat_powers']

    def save_json(self):
        data = super().save_json()
        data['combat_health_current'] = self.combat_health_current
        data['combat_health_full'] = self.combat_health_full
        data['combat_attack_resist'] = OrderedDict()
        for i in range(0x10):
            data['combat_attack_resist'][
                ATTACK_RESIST_TO_STRING[i]
            ] = self.combat_attack_resist[i]
        data['combat_powers'] = self.combat_powers
        return data


class ArcCharacter(ArcCombatObj):
    pass
