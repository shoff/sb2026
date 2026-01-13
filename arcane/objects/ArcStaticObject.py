#  • ▌ ▄ ·. ▄▄▄▄·     ▄▄▄ .·▄▄▄▄  ▪  ▄▄▄▄▄      ▄▄▄       ▄▄▄·▄▄▄       
#  ·██ ▐███▪▐█ ▀█▪    ▀▄.▀·██▪ ██ ██ •██  ▪     ▀▄ █·    ▐█ ▄█▀▄ █·▪    
#  ▐█ ▌▐▌▐█·▐█▀▀█▄    ▐▀▀▪▄▐█· ▐█▌▐█· ▐█.▪ ▄█▀▄ ▐▀▀▄      ██▀·▐▀▀▄  ▄█▀▄
#  ██ ██▌▐█▌██▄▪▐█    ▐█▄▄▌██. ██ ▐█▌ ▐█▌·▐█▌.▐▌▐█•█▌    ▐█▪·•▐█•█▌▐█▌.▐▌
#  ▀▀  █▪▀▀▀·▀▀▀▀      ▀▀▀ ▀▀▀▀▀• ▀▀▀ ▀▀▀  ▀█▄▀▪.▀  ▀    .▀   .▀  ▀ ▀█▄▀▪
#                Magicbane Emulator Project © 2013 - 2022
#                           www.magicbane.com

from collections import OrderedDict

from arcane.util import ResStream
from .ArcCombatObj import ArcCombatObj


class Sound:
    def load_binary(self, stream: ResStream):
        self.sound_0 = stream.read_qword()
        self.sound_1 = stream.read_qword()
        self.sound_min_dist = stream.read_float()
        self.sound_max_dist = stream.read_float()
        self.sound_dist = stream.read_bool()
        self.sound_loop = stream.read_bool()
        self.sound_chance = stream.read_dword()
        self.sound_interval = stream.read_float()
        self.sound_reserved = stream.read_dword()

    def save_binary(self, stream: ResStream):
        stream.write_qword(self.sound_0)
        stream.write_qword(self.sound_1)
        stream.write_float(self.sound_min_dist)
        stream.write_float(self.sound_max_dist)
        stream.write_bool(self.sound_dist)
        stream.write_bool(self.sound_loop)
        stream.write_dword(self.sound_chance)
        stream.write_float(self.sound_interval)
        stream.write_dword(self.sound_reserved)

    def load_json(self, data):
        self.sound_0 = data['sound_0']
        self.sound_1 = data['sound_1']
        self.sound_min_dist = data['sound_min_dist']
        self.sound_max_dist = data['sound_max_dist']
        self.sound_dist = data['sound_dist']
        self.sound_loop = data['sound_loop']
        self.sound_chance = data['sound_chance']
        self.sound_interval = data['sound_interval']
        self.sound_reserved = data['sound_reserved']

    def save_json(self):
        data = OrderedDict()
        data['sound_0'] = self.sound_0
        data['sound_1'] = self.sound_1
        data['sound_min_dist'] = self.sound_min_dist
        data['sound_max_dist'] = self.sound_max_dist
        data['sound_dist'] = self.sound_dist
        data['sound_loop'] = self.sound_loop
        data['sound_chance'] = self.sound_chance
        data['sound_interval'] = self.sound_interval
        data['sound_reserved'] = self.sound_reserved
        return data


class ArcStaticObject(ArcCombatObj):
    def load_binary(self, stream: ResStream):
        super().load_binary(stream)
        self.static_platform_height = stream.read_float()
        self.static_has_platform = stream.read_bool()
        self.static_collision_detect = stream.read_bool()
        self.static_has_sound = stream.read_bool()
        if self.static_has_sound:
            self.static_sound = Sound()
            self.static_sound.load_binary(stream)

    def save_binary(self, stream: ResStream):
        super().save_binary(stream)
        stream.write_float(self.static_platform_height)
        stream.write_bool(self.static_has_platform)
        stream.write_bool(self.static_collision_detect)
        stream.write_bool(self.static_has_sound)
        if self.static_has_sound:
            self.static_sound.save_binary(stream)

    def load_json(self, data):
        super().load_json(data)
        self.static_platform_height = data['static_platform_height']
        self.static_has_platform = data['static_has_platform']
        self.static_collision_detect = data['static_collision_detect']
        self.static_has_sound = data['static_has_sound']
        if self.static_has_sound:
            self.static_sound = Sound()
            self.static_sound.load_json(data['static_sound'])

    def save_json(self):
        data = super().save_json()
        data['static_platform_height'] = self.static_platform_height
        data['static_has_platform'] = self.static_has_platform
        data['static_collision_detect'] = self.static_collision_detect
        data['static_has_sound'] = self.static_has_sound
        if self.static_has_sound:
            data['static_sound'] = self.static_sound.save_json()
        return data
