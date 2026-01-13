#  • ▌ ▄ ·. ▄▄▄▄·     ▄▄▄ .·▄▄▄▄  ▪  ▄▄▄▄▄      ▄▄▄       ▄▄▄·▄▄▄       
#  ·██ ▐███▪▐█ ▀█▪    ▀▄.▀·██▪ ██ ██ •██  ▪     ▀▄ █·    ▐█ ▄█▀▄ █·▪    
#  ▐█ ▌▐▌▐█·▐█▀▀█▄    ▐▀▀▪▄▐█· ▐█▌▐█· ▐█.▪ ▄█▀▄ ▐▀▀▄      ██▀·▐▀▀▄  ▄█▀▄
#  ██ ██▌▐█▌██▄▪▐█    ▐█▄▄▌██. ██ ▐█▌ ▐█▌·▐█▌.▐▌▐█•█▌    ▐█▪·•▐█•█▌▐█▌.▐▌
#  ▀▀  █▪▀▀▀·▀▀▀▀      ▀▀▀ ▀▀▀▀▀• ▀▀▀ ▀▀▀  ▀█▄▀▪.▀  ▀    .▀   .▀  ▀ ▀█▄▀▪
#                Magicbane Emulator Project © 2013 - 2022
#                           www.magicbane.com

from arcane.util import ResStream
from .ArcItem import ArcItem


class ArcDeed(ArcItem):
    def load_binary(self, stream: ResStream):
        super().load_binary(stream)
        self.deed_type = stream.read_dword()
        self.deed_furniture_id = stream.read_qword()
        self.deed_target_id = stream.read_qword()
        self.deed_employment = stream.read_dword()
        self.deed_start_rank = stream.read_dword()
        self.deed_name_lookup = stream.read_dword()
        self.deed_indoors = stream.read_bool()
        self.deed_is_fortress = stream.read_bool()
        self.deed_namelookup_val = stream.read_float()
        self.deed_custom_city = stream.read_bool()
        if self.deed_custom_city:
            set_length = stream.read_dword()
            self.deed_custom_city_set = [
                stream.read_dword() for _ in range(set_length)
            ]

        self.deed_structure_id = stream.read_qword()

    def save_binary(self, stream: ResStream):
        super().save_binary(stream)
        stream.write_dword(self.deed_type)
        stream.write_qword(self.deed_furniture_id)
        stream.write_qword(self.deed_target_id)
        stream.write_dword(self.deed_employment)
        stream.write_dword(self.deed_start_rank)
        stream.write_dword(self.deed_name_lookup)
        stream.write_bool(self.deed_indoors)
        stream.write_bool(self.deed_is_fortress)
        stream.write_float(self.deed_namelookup_val)
        stream.write_bool(self.deed_custom_city)
        if self.deed_custom_city:
            stream.write_dword(len(self.deed_custom_city_set))
            for city in self.deed_custom_city_set:
                stream.write_dword(city)
        stream.write_qword(self.deed_structure_id)

    def load_json(self, data):
        super().load_json(data)
        self.deed_type = data['deed_type']
        self.deed_furniture_id = data['deed_furniture_id']
        self.deed_target_id = data['deed_target_id']
        self.deed_employment = data['deed_employment']
        self.deed_start_rank = data['deed_start_rank']
        self.deed_name_lookup = data['deed_name_lookup']
        self.deed_indoors = data['deed_indoors']
        self.deed_is_fortress = data['deed_is_fortress']
        self.deed_namelookup_val = data['deed_namelookup_val']
        self.deed_custom_city = data['deed_custom_city']
        if self.deed_custom_city:
            self.deed_custom_city_set = data['deed_custom_city_set']
        self.deed_structure_id = data['deed_structure_id']

    def save_json(self):
        data = super().save_json()
        data['deed_type'] = self.deed_type
        data['deed_furniture_id'] = self.deed_furniture_id
        data['deed_target_id'] = self.deed_target_id
        data['deed_employment'] = self.deed_employment
        data['deed_start_rank'] = self.deed_start_rank
        data['deed_name_lookup'] = self.deed_name_lookup
        data['deed_indoors'] = self.deed_indoors
        data['deed_is_fortress'] = self.deed_is_fortress
        data['deed_namelookup_val'] = self.deed_namelookup_val
        data['deed_custom_city'] = self.deed_custom_city
        if self.deed_custom_city:
            data['deed_custom_city_set'] = self.deed_custom_city_set
        data['deed_structure_id'] = self.deed_structure_id
        return data
