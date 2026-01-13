

from collections import OrderedDict

from arcane.enums.hashes import hash_to_string, string_to_hash
from arcane.util import ResStream


class DiscRequired:
    def load_binary(self, stream: ResStream):
        discs = stream.read_dword()
        self.disc_restrict = stream.read_bool()
        self.disc_values = [
            stream.read_dword() for _ in range(discs)
        ]

    def save_binary(self, stream: ResStream):
        stream.write_dword(len(self.disc_values))
        stream.write_bool(self.disc_restrict)
        for disc in self.disc_values:
            stream.write_dword(disc)

    def load_json(self, data):
        self.disc_restrict = data['restrict']
        self.disc_values = []
        for disc in data['discs']:
            self.disc_values.append(string_to_hash(disc))

    def save_json(self):
        data = OrderedDict()
        data['restrict'] = self.disc_restrict
        data['discs'] = []
        for disc in self.disc_values:
            data['discs'].append(hash_to_string(disc))
        return data
