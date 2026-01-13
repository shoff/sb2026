#  • ▌ ▄ ·. ▄▄▄▄·     ▄▄▄ .·▄▄▄▄  ▪  ▄▄▄▄▄      ▄▄▄       ▄▄▄·▄▄▄       
#  ·██ ▐███▪▐█ ▀█▪    ▀▄.▀·██▪ ██ ██ •██  ▪     ▀▄ █·    ▐█ ▄█▀▄ █·▪    
#  ▐█ ▌▐▌▐█·▐█▀▀█▄    ▐▀▀▪▄▐█· ▐█▌▐█· ▐█.▪ ▄█▀▄ ▐▀▀▄      ██▀·▐▀▀▄  ▄█▀▄
#  ██ ██▌▐█▌██▄▪▐█    ▐█▄▄▌██. ██ ▐█▌ ▐█▌·▐█▌.▐▌▐█•█▌    ▐█▪·•▐█•█▌▐█▌.▐▌
#  ▀▀  █▪▀▀▀·▀▀▀▀      ▀▀▀ ▀▀▀▀▀• ▀▀▀ ▀▀▀  ▀█▄▀▪.▀  ▀    .▀   .▀  ▀ ▀█▄▀▪
#                Magicbane Emulator Project © 2013 - 2022
#                           www.magicbane.com

from collections import OrderedDict

from arcane.util import ResStream


class ArcSoundInfo:

    def load_binary(self, stream: ResStream):
        self.sound_playlist = stream.read_string()
        self.sound_id = stream.read_dword()
        self.sound_template = stream.read_string()
        self.sound_location = stream.read_tuple()
        self.sound_radius = stream.read_float()

    def save_binary(self, stream: ResStream):
        stream.write_string(self.sound_playlist)
        stream.write_dword(self.sound_id)
        stream.write_string(self.sound_template)
        stream.write_tuple(self.sound_location)
        stream.write_float(self.sound_radius)

    def save_json(self):
        data = OrderedDict()
        data['sound_playlist'] = self.sound_playlist
        data['sound_id'] = self.sound_id
        data['sound_template'] = self.sound_template
        data['sound_location'] = self.sound_location
        data['sound_radius'] = self.sound_radius
        return data

    def load_json(self, data):
        self.sound_playlist = data['sound_playlist']
        self.sound_id = data['sound_id']
        self.sound_template = data['sound_template']
        self.sound_location = data['sound_location']
        self.sound_radius = data['sound_radius']
