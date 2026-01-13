#  • ▌ ▄ ·. ▄▄▄▄·     ▄▄▄ .·▄▄▄▄  ▪  ▄▄▄▄▄      ▄▄▄       ▄▄▄·▄▄▄       
#  ·██ ▐███▪▐█ ▀█▪    ▀▄.▀·██▪ ██ ██ •██  ▪     ▀▄ █·    ▐█ ▄█▀▄ █·▪    
#  ▐█ ▌▐▌▐█·▐█▀▀█▄    ▐▀▀▪▄▐█· ▐█▌▐█· ▐█.▪ ▄█▀▄ ▐▀▀▄      ██▀·▐▀▀▄  ▄█▀▄
#  ██ ██▌▐█▌██▄▪▐█    ▐█▄▄▌██. ██ ▐█▌ ▐█▌·▐█▌.▐▌▐█•█▌    ▐█▪·•▐█•█▌▐█▌.▐▌
#  ▀▀  █▪▀▀▀·▀▀▀▀      ▀▀▀ ▀▀▀▀▀• ▀▀▀ ▀▀▀  ▀█▄▀▪.▀  ▀    .▀   .▀  ▀ ▀█▄▀▪
#                Magicbane Emulator Project © 2013 - 2022
#                           www.magicbane.com

from arcane.util import ResStream
from .ArcItem import ArcItem


class ArcKey(ArcItem):
    def load_binary(self, stream: ResStream):
        super().load_binary(stream)
        self.key_keyval = stream.read_qword()
        self.key_keyval2 = stream.read_qword()
        self.key_keyval3 = stream.read_qword()
        self.key_setting = stream.read_dword()

    def save_binary(self, stream: ResStream):
        super().save_binary(stream)
        stream.write_qword(self.key_keyval)
        stream.write_qword(self.key_keyval2)
        stream.write_qword(self.key_keyval3)
        stream.write_dword(self.key_setting)

    def load_json(self, data):
        super().load_json(data)
        self.key_keyval = data['key_keyval']
        self.key_keyval2 = data['key_keyval2']
        self.key_keyval3 = data['key_keyval3']
        self.key_setting = data['key_setting']

    def save_json(self):
        data = super().save_json()
        data['key_keyval'] = self.key_keyval
        data['key_keyval2'] = self.key_keyval2
        data['key_keyval3'] = self.key_keyval3
        data['key_setting'] = self.key_setting
        return data
