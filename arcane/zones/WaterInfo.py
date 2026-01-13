#  • ▌ ▄ ·. ▄▄▄▄·     ▄▄▄ .·▄▄▄▄  ▪  ▄▄▄▄▄      ▄▄▄       ▄▄▄·▄▄▄       
#  ·██ ▐███▪▐█ ▀█▪    ▀▄.▀·██▪ ██ ██ •██  ▪     ▀▄ █·    ▐█ ▄█▀▄ █·▪    
#  ▐█ ▌▐▌▐█·▐█▀▀█▄    ▐▀▀▪▄▐█· ▐█▌▐█· ▐█.▪ ▄█▀▄ ▐▀▀▄      ██▀·▐▀▀▄  ▄█▀▄
#  ██ ██▌▐█▌██▄▪▐█    ▐█▄▄▌██. ██ ▐█▌ ▐█▌·▐█▌.▐▌▐█•█▌    ▐█▪·•▐█•█▌▐█▌.▐▌
#  ▀▀  █▪▀▀▀·▀▀▀▀      ▀▀▀ ▀▀▀▀▀• ▀▀▀ ▀▀▀  ▀█▄▀▪.▀  ▀    .▀   .▀  ▀ ▀█▄▀▪
#                Magicbane Emulator Project © 2013 - 2022
#                           www.magicbane.com

from collections import OrderedDict

from arcane.util import ResStream


class WaterInfo:

    def load_binary(self, stream: ResStream):
        self.water_texture = stream.read_qword()
        self.water_unknown1 = [
            stream.read_float(),
            stream.read_float(),
            stream.read_float(),
            stream.read_float(),
        ]
        self.water_x_wave_length = stream.read_float()
        self.water_z_wave_length = stream.read_float()
        self.water_x_speed = stream.read_float()
        self.water_z_speed = stream.read_float()
        self.water_unknown2 = stream.read_float()
        self.water_amplitude = stream.read_float()
        self.water_vertex_density = stream.read_float()
        self.water_texture_density = stream.read_float()
        self.water_color = [
            stream.read_float(),
            stream.read_float(),
            stream.read_float(),
            stream.read_float(),
        ]
        self.water_reflectivity = stream.read_float()
        self.water_eye_factor = stream.read_float()

    def save_binary(self, stream: ResStream):
        stream.write_qword(self.water_texture)
        stream.write_float(self.water_unknown1[0])
        stream.write_float(self.water_unknown1[1])
        stream.write_float(self.water_unknown1[2])
        stream.write_float(self.water_unknown1[3])
        stream.write_float(self.water_x_wave_length)
        stream.write_float(self.water_z_wave_length)
        stream.write_float(self.water_x_speed)
        stream.write_float(self.water_z_speed)
        stream.write_float(self.water_unknown2)
        stream.write_float(self.water_amplitude)
        stream.write_float(self.water_vertex_density)
        stream.write_float(self.water_texture_density)
        stream.write_float(self.water_color[0])
        stream.write_float(self.water_color[1])
        stream.write_float(self.water_color[2])
        stream.write_float(self.water_color[3])
        stream.write_float(self.water_reflectivity)
        stream.write_float(self.water_eye_factor)

    def save_json(self):
        data = OrderedDict()
        data['water_texture'] = self.water_texture
        data['water_unknown1'] = self.water_unknown1
        data['water_x_wave_length'] = self.water_x_wave_length
        data['water_z_wave_length'] = self.water_z_wave_length
        data['water_x_speed'] = self.water_x_speed
        data['water_z_speed'] = self.water_z_speed
        data['water_unknown2'] = self.water_unknown2
        data['water_amplitude'] = self.water_amplitude
        data['water_vertex_density'] = self.water_vertex_density
        data['water_texture_density'] = self.water_texture_density
        data['water_color'] = self.water_color
        data['water_reflectivity'] = self.water_reflectivity
        data['water_eye_factor'] = self.water_eye_factor
        return data

    def load_json(self, data):
        self.water_texture = data['water_texture']
        self.water_unknown1 = data['water_unknown1']
        self.water_x_wave_length = data['water_x_wave_length']
        self.water_z_wave_length = data['water_z_wave_length']
        self.water_x_speed = data['water_x_speed']
        self.water_z_speed = data['water_z_speed']
        self.water_unknown2 = data['water_unknown2']
        self.water_amplitude = data['water_amplitude']
        self.water_vertex_density = data['water_vertex_density']
        self.water_texture_density = data['water_texture_density']
        self.water_color = data['water_color']
        self.water_reflectivity = data['water_reflectivity']
        self.water_eye_factor = data['water_eye_factor']
