#  • ▌ ▄ ·. ▄▄▄▄·     ▄▄▄ .·▄▄▄▄  ▪  ▄▄▄▄▄      ▄▄▄       ▄▄▄·▄▄▄       
#  ·██ ▐███▪▐█ ▀█▪    ▀▄.▀·██▪ ██ ██ •██  ▪     ▀▄ █·    ▐█ ▄█▀▄ █·▪    
#  ▐█ ▌▐▌▐█·▐█▀▀█▄    ▐▀▀▪▄▐█· ▐█▌▐█· ▐█.▪ ▄█▀▄ ▐▀▀▄      ██▀·▐▀▀▄  ▄█▀▄
#  ██ ██▌▐█▌██▄▪▐█    ▐█▄▄▌██. ██ ▐█▌ ▐█▌·▐█▌.▐▌▐█•█▌    ▐█▪·•▐█•█▌▐█▌.▐▌
#  ▀▀  █▪▀▀▀·▀▀▀▀      ▀▀▀ ▀▀▀▀▀• ▀▀▀ ▀▀▀  ▀█▄▀▪.▀  ▀    .▀   .▀  ▀ ▀█▄▀▪
#                Magicbane Emulator Project © 2013 - 2022
#                           www.magicbane.com

from collections import OrderedDict

from arcane.enums.hashes import hash_to_string, string_to_hash
from arcane.util import ResStream


class ArcZoneBiomState:

    def load_binary(self, stream: ResStream):
        self.biom_sky_state_id = stream.read_dword()
        self.biom_environment_state_id = stream.read_dword()
        self.biom_weather_state_id = stream.read_dword()

    def save_binary(self, stream: ResStream):
        stream.write_dword(self.biom_sky_state_id)
        stream.write_dword(self.biom_environment_state_id)
        stream.write_dword(self.biom_weather_state_id)

    def save_json(self):
        data = OrderedDict()
        data['biom_sky_state_id'] = hash_to_string(self.biom_sky_state_id)
        data['biom_environment_state_id'] = hash_to_string(self.biom_environment_state_id)
        data['biom_weather_state_id'] = hash_to_string(self.biom_weather_state_id)
        return data

    def load_json(self, data):
        self.biom_sky_state_id = string_to_hash(data['biom_sky_state_id'])
        self.biom_environment_state_id = string_to_hash(data['biom_environment_state_id'])
        self.biom_weather_state_id = string_to_hash(data['biom_weather_state_id'])
