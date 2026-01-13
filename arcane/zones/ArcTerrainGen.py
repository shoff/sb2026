#  • ▌ ▄ ·. ▄▄▄▄·     ▄▄▄ .·▄▄▄▄  ▪  ▄▄▄▄▄      ▄▄▄       ▄▄▄·▄▄▄       
#  ·██ ▐███▪▐█ ▀█▪    ▀▄.▀·██▪ ██ ██ •██  ▪     ▀▄ █·    ▐█ ▄█▀▄ █·▪    
#  ▐█ ▌▐▌▐█·▐█▀▀█▄    ▐▀▀▪▄▐█· ▐█▌▐█· ▐█.▪ ▄█▀▄ ▐▀▀▄      ██▀·▐▀▀▄  ▄█▀▄
#  ██ ██▌▐█▌██▄▪▐█    ▐█▄▄▌██. ██ ▐█▌ ▐█▌·▐█▌.▐▌▐█•█▌    ▐█▪·•▐█•█▌▐█▌.▐▌
#  ▀▀  █▪▀▀▀·▀▀▀▀      ▀▀▀ ▀▀▀▀▀• ▀▀▀ ▀▀▀  ▀█▄▀▪.▀  ▀    .▀   .▀  ▀ ▀█▄▀▪
#                Magicbane Emulator Project © 2013 - 2022
#                           www.magicbane.com

from collections import OrderedDict

from arcane.enums.zone.arc_terraingen import *
from arcane.util import ResStream


class ArcTerrainGen:

    def load_binary(self, stream: ResStream):
        self.terrain_type = stream.read_dword()
        if self.terrain_type in [1, 2, 3, 5]:
            self.terrain_max_x = stream.read_float()
            self.terrain_max_z = stream.read_float()
            self.terrain_h = stream.read_float()
            self.terrain_lacunarity = stream.read_float()
            self.terrain_octaves = stream.read_dword()
            self.terrain_offset = stream.read_float()
            self.terrain_gain = stream.read_float()
            self.terrain_seeds = [
                stream.read_dword(),
                stream.read_dword(),
            ]
        if self.terrain_type == 4:
            self.terrain_max_x = stream.read_float()
            self.terrain_max_z = stream.read_float()
            self.terrain_height = stream.read_float()
        if self.terrain_type == 6:
            self.terrain_max_x = stream.read_float()
            self.terrain_max_z = stream.read_float()
            self.terrain_x_size = stream.read_float()
            self.terrain_z_size = stream.read_float()
            self.terrain_mesh = stream.read_qword()
        if self.terrain_type == 7:
            self.terrain_max_x = stream.read_float()
            self.terrain_max_z = stream.read_float()
            self.terrain_x_size = stream.read_float()
            self.terrain_z_size = stream.read_float()
            self.terrain_min_y = stream.read_float()
            self.terrain_max_y = stream.read_float()
            self.terrain_image = stream.read_qword()

    def save_binary(self, stream: ResStream):
        stream.write_dword(self.terrain_type)
        if self.terrain_type in [1, 2, 3, 5]:
            stream.write_float(self.terrain_max_x)
            stream.write_float(self.terrain_max_z)
            stream.write_float(self.terrain_h)
            stream.write_float(self.terrain_lacunarity)
            stream.write_dword(self.terrain_octaves)
            stream.write_float(self.terrain_offset)
            stream.write_float(self.terrain_gain)
            stream.read_dword(self.terrain_seeds[0])
            stream.read_dword(self.terrain_seeds[1])
        if self.terrain_type == 4:
            stream.write_float(self.terrain_max_x)
            stream.write_float(self.terrain_max_z)
            stream.write_float(self.terrain_height)
        if self.terrain_type == 6:
            stream.write_float(self.terrain_max_x)
            stream.write_float(self.terrain_max_z)
            stream.write_float(self.terrain_x_size)
            stream.write_float(self.terrain_z_size)
            stream.write_qword(self.terrain_mesh)
        if self.terrain_type == 7:
            stream.write_float(self.terrain_max_x)
            stream.write_float(self.terrain_max_z)
            stream.write_float(self.terrain_x_size)
            stream.write_float(self.terrain_z_size)
            stream.write_float(self.terrain_min_y)
            stream.write_float(self.terrain_max_y)
            stream.write_qword(self.terrain_image)

    def save_json(self):
        data = OrderedDict()
        data['terrain_type'] = TERRAIN_TYPE_TO_STRING[self.terrain_type]
        if self.terrain_type in [1, 2, 3, 5]:
            data['terrain_max_x'] = self.terrain_max_x
            data['terrain_max_z'] = self.terrain_max_z
            data['terrain_h'] = self.terrain_h
            data['terrain_lacunarity'] = self.terrain_lacunarity
            data['terrain_octaves'] = self.terrain_octaves
            data['terrain_offset'] = self.terrain_offset
            data['terrain_gain'] = self.terrain_gain
            data['terrain_seeds'] = self.terrain_seeds
        if self.terrain_type == 4:
            data['terrain_max_x'] = self.terrain_max_x
            data['terrain_max_z'] = self.terrain_max_z
            data['terrain_height'] = self.terrain_height
        if self.terrain_type == 6:
            data['terrain_max_x'] = self.terrain_max_x
            data['terrain_max_z'] = self.terrain_max_z
            data['terrain_x_size'] = self.terrain_x_size
            data['terrain_z_size'] = self.terrain_z_size
            data['terrain_mesh'] = self.terrain_mesh
        if self.terrain_type == 7:
            data['terrain_max_x'] = self.terrain_max_x
            data['terrain_max_z'] = self.terrain_max_z
            data['terrain_x_size'] = self.terrain_x_size
            data['terrain_z_size'] = self.terrain_z_size
            data['terrain_min_y'] = self.terrain_min_y
            data['terrain_max_y'] = self.terrain_max_y
            data['terrain_image'] = self.terrain_image
        return data

    def load_json(self, data):
        self.terrain_type = STRING_TO_TERRAIN_TYPE[data['terrain_type']]
        if self.terrain_type in [1, 2, 3, 5]:
            self.terrain_max_x = data['terrain_max_x']
            self.terrain_max_z = data['terrain_max_z']
            self.terrain_h = data['terrain_h']
            self.terrain_lacunarity = data['terrain_lacunarity']
            self.terrain_octaves = data['terrain_octaves']
            self.terrain_offset = data['terrain_offset']
            self.terrain_gain = data['terrain_gain']
            self.terrain_seeds = data['terrain_seeds']
        if self.terrain_type == 4:
            self.terrain_max_x = data['terrain_max_x']
            self.terrain_max_z = data['terrain_max_z']
            self.terrain_height = data['terrain_height']
        if self.terrain_type == 6:
            self.terrain_max_x = data['terrain_max_x']
            self.terrain_max_z = data['terrain_max_z']
            self.terrain_x_size = data['terrain_x_size']
            self.terrain_z_size = data['terrain_z_size']
            self.terrain_mesh = data['terrain_mesh']
        if self.terrain_type == 7:
            self.terrain_max_x = data['terrain_max_x']
            self.terrain_max_z = data['terrain_max_z']
            self.terrain_x_size = data['terrain_x_size']
            self.terrain_z_size = data['terrain_z_size']
            self.terrain_min_y = data['terrain_min_y']
            self.terrain_max_y = data['terrain_max_y']
            self.terrain_image = data['terrain_image']
