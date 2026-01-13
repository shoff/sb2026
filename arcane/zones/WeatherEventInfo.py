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


class WeatherEventInfo:
    def load_binary(self, stream: ResStream):
        self.weather_event_effect_id = stream.read_dword()
        self.weather_event_spawn_location = stream.read_tuple()
        self.weather_event_min_duration = stream.read_float()
        self.weather_event_duration_variant = stream.read_float()
        self.weather_event_time_to_respawn = stream.read_float()
        self.weather_event_init_height_off_ground = stream.read_float()
        self.weather_event_local_top = stream.read_bool()

    def save_binary(self, stream: ResStream):
        stream.write_dword(self.weather_event_effect_id)
        stream.write_tuple(self.weather_event_spawn_location)
        stream.write_float(self.weather_event_min_duration)
        stream.write_float(self.weather_event_duration_variant)
        stream.write_float(self.weather_event_time_to_respawn)
        stream.write_float(self.weather_event_init_height_off_ground)
        stream.write_bool(self.weather_event_local_top)

    def save_json(self):
        data = OrderedDict()
        data['weather_event_effect_id'] = hash_to_string(self.weather_event_effect_id)
        data['weather_event_spawn_location'] = self.weather_event_spawn_location
        data['weather_event_min_duration'] = self.weather_event_min_duration
        data['weather_event_duration_variant'] = self.weather_event_duration_variant
        data['weather_event_time_to_respawn'] = self.weather_event_time_to_respawn
        data['weather_event_init_height_off_ground'] = self.weather_event_init_height_off_ground
        data['weather_event_local_top'] = self.weather_event_local_top
        return data

    def load_json(self, data):
        self.weather_event_effect_id = string_to_hash(data['weather_event_effect_id'])
        self.weather_event_spawn_location = data['weather_event_spawn_location']
        self.weather_event_min_duration = data['weather_event_min_duration']
        self.weather_event_duration_variant = data['weather_event_duration_variant']
        self.weather_event_time_to_respawn = data['weather_event_time_to_respawn']
        self.weather_event_init_height_off_ground = data['weather_event_init_height_off_ground']
        self.weather_event_local_top = data['weather_event_local_top']
