

from collections import OrderedDict

from arcane.enums.hashes import hash_to_string, string_to_hash
from arcane.util import ResStream


class RaceRequired:
    def load_binary(self, stream: ResStream):
        races = stream.read_dword()
        self.race_restrict = stream.read_bool()
        self.race_values = [
            stream.read_dword() for _ in range(races)
        ]

    def save_binary(self, stream: ResStream):
        stream.write_dword(len(self.race_values))
        stream.write_bool(self.race_restrict)
        for race in self.race_values:
            stream.write_dword(race)

    def load_json(self, data):
        self.race_restrict = data['restrict']
        self.race_values = []
        for race in data['races']:
            self.race_values.append(string_to_hash(race))

    def save_json(self):
        data = OrderedDict()
        data['restrict'] = self.race_restrict
        data['races'] = []
        for race in self.race_values:
            data['races'].append(hash_to_string(race))
        return data
