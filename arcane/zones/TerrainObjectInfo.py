#  • ▌ ▄ ·. ▄▄▄▄·     ▄▄▄ .·▄▄▄▄  ▪  ▄▄▄▄▄      ▄▄▄       ▄▄▄·▄▄▄       
#  ·██ ▐███▪▐█ ▀█▪    ▀▄.▀·██▪ ██ ██ •██  ▪     ▀▄ █·    ▐█ ▄█▀▄ █·▪    
#  ▐█ ▌▐▌▐█·▐█▀▀█▄    ▐▀▀▪▄▐█· ▐█▌▐█· ▐█.▪ ▄█▀▄ ▐▀▀▄      ██▀·▐▀▀▄  ▄█▀▄
#  ██ ██▌▐█▌██▄▪▐█    ▐█▄▄▌██. ██ ▐█▌ ▐█▌·▐█▌.▐▌▐█•█▌    ▐█▪·•▐█•█▌▐█▌.▐▌
#  ▀▀  █▪▀▀▀·▀▀▀▀      ▀▀▀ ▀▀▀▀▀• ▀▀▀ ▀▀▀  ▀█▄▀▪.▀  ▀    .▀   .▀  ▀ ▀█▄▀▪
#                Magicbane Emulator Project © 2013 - 2022
#                           www.magicbane.com

from collections import OrderedDict

from arcane.util import ResStream


class TerrainObjectInfo:

    def load_binary(self, stream: ResStream):
        self.terrain_object_id = stream.read_qword()
        self.terrain_object_h = stream.read_float()
        self.terrain_object_lacunarity = stream.read_float()
        self.terrain_object_octaves = stream.read_dword()
        self.terrain_object_offset = stream.read_float()
        self.terrain_object_gain = stream.read_float()
        self.terrain_object_min_alt = stream.read_float()
        self.terrain_object_max_alt = stream.read_float()
        self.terrain_object_min_slope = stream.read_float()
        self.terrain_object_max_slope = stream.read_float()
        self.terrain_object_max_pop = stream.read_dword()
        self.terrain_object_is_fractal_pop = stream.read_bool()
        self.terrain_object_unknown1 = stream.read_dword()
        self.terrain_object_y_offset = stream.read_float()
        self.terrain_object_pop_image_id = stream.read_qword()
        self.terrain_object_image_min_y = stream.read_float()
        self.terrain_object_image_max_y = stream.read_float()

    def save_binary(self, stream: ResStream):
        stream.write_qword(self.terrain_object_id)
        stream.write_float(self.terrain_object_h)
        stream.write_float(self.terrain_object_lacunarity)
        stream.write_dword(self.terrain_object_octaves)
        stream.write_float(self.terrain_object_offset)
        stream.write_float(self.terrain_object_gain)
        stream.write_float(self.terrain_object_min_alt)
        stream.write_float(self.terrain_object_max_alt)
        stream.write_float(self.terrain_object_min_slope)
        stream.write_float(self.terrain_object_max_slope)
        stream.write_dword(self.terrain_object_max_pop)
        stream.write_bool(self.terrain_object_is_fractal_pop)
        stream.write_dword(self.terrain_object_unknown1)
        stream.write_float(self.terrain_object_y_offset)
        stream.write_qword(self.terrain_object_pop_image_id)
        stream.write_float(self.terrain_object_image_min_y)
        stream.write_float(self.terrain_object_image_max_y)

    def save_json(self):
        data = OrderedDict()
        data['terrain_object_id'] = self.terrain_object_id
        data['terrain_object_h'] = self.terrain_object_h
        data['terrain_object_lacunarity'] = self.terrain_object_lacunarity
        data['terrain_object_octaves'] = self.terrain_object_octaves
        data['terrain_object_offset'] = self.terrain_object_offset
        data['terrain_object_gain'] = self.terrain_object_gain
        data['terrain_object_min_alt'] = self.terrain_object_min_alt
        data['terrain_object_max_alt'] = self.terrain_object_max_alt
        data['terrain_object_min_slope'] = self.terrain_object_min_slope
        data['terrain_object_max_slope'] = self.terrain_object_max_slope
        data['terrain_object_max_pop'] = self.terrain_object_max_pop
        data['terrain_object_is_fractal_pop'] = self.terrain_object_is_fractal_pop
        data['terrain_object_unknown1'] = self.terrain_object_unknown1
        data['terrain_object_y_offset'] = self.terrain_object_y_offset
        data['terrain_object_pop_image_id'] = self.terrain_object_pop_image_id
        data['terrain_object_image_min_y'] = self.terrain_object_image_min_y
        data['terrain_object_image_max_y'] = self.terrain_object_image_max_y
        return data

    def load_json(self, data):
        self.terrain_object_id = data['terrain_object_id']
        self.terrain_object_h = data['terrain_object_h']
        self.terrain_object_lacunarity = data['terrain_object_lacunarity']
        self.terrain_object_octaves = data['terrain_object_octaves']
        self.terrain_object_offset = data['terrain_object_offset']
        self.terrain_object_gain = data['terrain_object_gain']
        self.terrain_object_min_alt = data['terrain_object_min_alt']
        self.terrain_object_max_alt = data['terrain_object_max_alt']
        self.terrain_object_min_slope = data['terrain_object_min_slope']
        self.terrain_object_max_slope = data['terrain_object_max_slope']
        self.terrain_object_max_pop = data['terrain_object_max_pop']
        self.terrain_object_is_fractal_pop = data['terrain_object_is_fractal_pop']
        self.terrain_object_unknown1 = data['terrain_object_unknown1']
        self.terrain_object_y_offset = data['terrain_object_y_offset']
        self.terrain_object_pop_image_id = data['terrain_object_pop_image_id']
        self.terrain_object_image_min_y = data['terrain_object_image_min_y']
        self.terrain_object_image_max_y = data['terrain_object_image_max_y']
