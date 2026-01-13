from collections import OrderedDict

from arcane.util import ResStream

TILE_TO_STRING = {
    0: "UNKNOWN",
    1: "Regular",
    2: "Slope",
    3: "Road",
}
STRING_TO_TILE = {value: key for key, value in TILE_TO_STRING.items()}

MASK_TO_STRING = {
    0: "UNKNOWN",
    1: "Transition",
    2: "Road",
}
STRING_TO_MASK = {value: key for key, value in MASK_TO_STRING.items()}


class ArcTile:
    def load_binary(self, stream: ResStream):
        self.tile_row_0 = stream.read_dword()
        self.tile_row_1 = stream.read_dword()
        self.tile_row_2 = stream.read_dword()
        self.tile_row_3 = stream.read_dword()
        self.tile_prob = stream.read_float()
        self.tile_type = stream.read_dword()

        num_alts = stream.read_dword()
        self.tile_alts = [stream.read_dword() for _ in range(num_alts)]

    def save_binary(self, stream: ResStream):
        stream.write_dword(self.tile_row_0)
        stream.write_dword(self.tile_row_1)
        stream.write_dword(self.tile_row_2)
        stream.write_dword(self.tile_row_3)
        stream.write_float(self.tile_prob)
        stream.write_dword(self.tile_type)
        stream.write_dword(len(self.tile_alts))
        for i in range(len(self.tile_alts)):
            stream.write_dword(self.tile_alts[i])

    def load_json(self, data):
        self.tile_row_0 = data['tile_row_0']
        self.tile_row_1 = data['tile_row_1']
        self.tile_row_2 = data['tile_row_2']
        self.tile_row_3 = data['tile_row_3']
        self.tile_prob = data['tile_prob']
        self.tile_type = STRING_TO_TILE[data['tile_type']]
        self.tile_alts = data['tile_alts']

    def save_json(self):
        data = OrderedDict()
        data['tile_row_0'] = self.tile_row_0
        data['tile_row_1'] = self.tile_row_1
        data['tile_row_2'] = self.tile_row_2
        data['tile_row_3'] = self.tile_row_3
        data['tile_prob'] = self.tile_prob
        data['tile_type'] = TILE_TO_STRING[self.tile_type]
        data['tile_alts'] = self.tile_alts
        return data


class ArcTileMask:
    def load_binary(self, stream: ResStream):
        self.mask_row_0 = stream.read_dword()
        self.mask_row_1 = stream.read_dword()
        self.mask_row_2 = stream.read_dword()
        self.mask_row_3 = stream.read_dword()
        self.mask_prob = stream.read_float()
        self.mask_start = stream.read_dword()
        self.mask_end = stream.read_dword()
        self.mask_end1 = stream.read_dword()
        self.mask_end2 = stream.read_dword()
        self.mask_type = stream.read_dword()
        self.mask_width = stream.read_dword()

    def save_binary(self, stream: ResStream):
        stream.write_dword(self.mask_row_0)
        stream.write_dword(self.mask_row_1)
        stream.write_dword(self.mask_row_2)
        stream.write_dword(self.mask_row_3)
        stream.write_float(self.mask_prob)
        stream.write_dword(self.mask_start)
        stream.write_dword(self.mask_end)
        stream.write_dword(self.mask_end1)
        stream.write_dword(self.mask_end2)
        stream.write_dword(self.mask_type)
        stream.write_dword(self.mask_width)

    def load_json(self, data):
        self.mask_row_0 = data['mask_row_0']
        self.mask_row_1 = data['mask_row_1']
        self.mask_row_2 = data['mask_row_2']
        self.mask_row_3 = data['mask_row_3']
        self.mask_prob = data['mask_prob']
        self.mask_start = data['mask_start']
        self.mask_end = data['mask_end']
        self.mask_end1 = data['mask_end1']
        self.mask_end2 = data['mask_end2']
        self.mask_type = STRING_TO_MASK[data['mask_type']]
        self.mask_width = data['mask_width']

    def save_json(self):
        data = OrderedDict()
        data['mask_row_0'] = self.mask_row_0
        data['mask_row_1'] = self.mask_row_1
        data['mask_row_2'] = self.mask_row_2
        data['mask_row_3'] = self.mask_row_3
        data['mask_prob'] = self.mask_prob
        data['mask_start'] = self.mask_start
        data['mask_end'] = self.mask_end
        data['mask_end1'] = self.mask_end1
        data['mask_end2'] = self.mask_end2
        data['mask_type'] = MASK_TO_STRING[self.mask_type]
        data['mask_width'] = self.mask_width
        return data


class ArcTilePattern:
    def load_binary(self, stream: ResStream):
        self.pattern_row_0 = stream.read_dword()
        self.pattern_row_1 = stream.read_dword()
        self.pattern_row_2 = stream.read_dword()
        self.pattern_row_3 = stream.read_dword()
        self.pattern_prob = stream.read_float()
        self.pattern_patx = stream.read_dword()
        self.pattern_patz = stream.read_dword()
        num_tiles = stream.read_dword()
        self.pattern_tiles = [stream.read_dword() for _ in range(num_tiles)]

    def save_binary(self, stream: ResStream):
        stream.write_dword(self.pattern_row_0)
        stream.write_dword(self.pattern_row_1)
        stream.write_dword(self.pattern_row_2)
        stream.write_dword(self.pattern_row_3)
        stream.write_float(self.pattern_prob)
        stream.write_dword(self.pattern_patx)
        stream.write_dword(self.pattern_patz)
        stream.write_dword(len(self.pattern_tiles))
        for i in range(len(self.pattern_tiles)):
            stream.write_dword(self.pattern_tiles[i])

    def load_json(self, data):
        self.pattern_row_0 = data['pattern_row_0']
        self.pattern_row_1 = data['pattern_row_1']
        self.pattern_row_2 = data['pattern_row_2']
        self.pattern_row_3 = data['pattern_row_3']
        self.pattern_prob = data['pattern_prob']
        self.pattern_patx = data['pattern_patx']
        self.pattern_patz = data['pattern_patz']
        self.pattern_tiles = data['pattern_tiles']

    def save_json(self):
        data = OrderedDict()
        data['pattern_row_0'] = self.pattern_row_0
        data['pattern_row_1'] = self.pattern_row_1
        data['pattern_row_2'] = self.pattern_row_2
        data['pattern_row_3'] = self.pattern_row_3
        data['pattern_prob'] = self.pattern_prob
        data['pattern_patx'] = self.pattern_patx
        data['pattern_patz'] = self.pattern_patz
        data['pattern_tiles'] = self.pattern_tiles
        return data


class ArcTileManager:
    def load_binary(self, stream: ResStream):
        self.manager_texture_width = stream.read_dword()
        self.manager_tile_width = stream.read_dword()
        self.manager_tile_texture = stream.read_qword()
        num_tiles = stream.read_dword()
        self.manager_tiles = [ArcTile() for _ in range(num_tiles)]
        for tile in self.manager_tiles:
            tile.load_binary(stream)
        num_masks = stream.read_dword()
        self.manager_masks = [ArcTileMask() for _ in range(num_masks)]
        for mask in self.manager_masks:
            mask.load_binary(stream)
        num_patterns = stream.read_dword()
        self.manager_patterns = [ArcTilePattern() for _ in range(num_patterns)]
        for pattern in self.manager_patterns:
            pattern.load_binary(stream)

    def save_binary(self, stream: ResStream):
        stream.write_dword(self.manager_texture_width)
        stream.write_dword(self.manager_tile_width)
        stream.write_qword(self.manager_tile_texture)
        stream.write_dword(len(self.manager_tiles))
        for tile in self.manager_tiles:
            tile.save_binary(stream)
        stream.write_dword(len(self.manager_masks))
        for mask in self.manager_masks:
            mask.save_binary(stream)
        stream.write_dword(len(self.manager_patterns))
        for pattern in self.manager_patterns:
            pattern.save_binary(stream)

    def load_json(self, data):
        self.manager_texture_width = data['manager_texture_width']
        self.manager_tile_width = data['manager_tile_width']
        self.manager_tile_texture = data['manager_tile_texture']
        self.manager_tiles = []
        for tile_data in data['manager_tiles']:
            tile = ArcTile()
            tile.load_json(tile_data)
            self.manager_tiles.append(tile)
        self.manager_masks = []
        for mask_data in data['manager_masks']:
            mask = ArcTileMask()
            mask.load_json(mask_data)
            self.manager_masks.append(mask)
        self.manager_patterns = []
        for pattern_data in data['manager_patterns']:
            pattern = ArcTilePattern()
            pattern.load_json(pattern_data)
            self.manager_patterns.append(pattern)

    def save_json(self):
        data = OrderedDict()
        data['manager_texture_width'] = self.manager_texture_width
        data['manager_tile_width'] = self.manager_tile_width
        data['manager_tile_texture'] = self.manager_tile_texture
        data['manager_tiles'] = []
        for tile in self.manager_tiles:
            data['manager_tiles'].append(tile.save_json())
        data['manager_masks'] = []
        for mask in self.manager_masks:
            data['manager_masks'].append(mask.save_json())
        data['manager_patterns'] = []
        for pattern in self.manager_patterns:
            data['manager_patterns'].append(pattern.save_json())
        return data
