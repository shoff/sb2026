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


class ClassRequired:
    def load_binary(self, stream: ResStream):
        classs = stream.read_dword()
        self.class_restrict = stream.read_bool()
        self.class_values = [
            stream.read_dword() for _ in range(classs)
        ]

    def save_binary(self, stream: ResStream):
        stream.write_dword(len(self.class_values))
        stream.write_bool(self.class_restrict)
        for cls in self.class_values:
            stream.write_dword(cls)

    def load_json(self, data):
        self.class_restrict = data['restrict']
        self.class_values = []
        for cls in data['classes']:
            self.class_values.append(string_to_hash(cls))
        return data

    def save_json(self):
        data = OrderedDict()
        data['restrict'] = self.class_restrict
        data['classes'] = []
        for cls in self.class_values:
            data['classes'].append(hash_to_string(cls))
        return data
