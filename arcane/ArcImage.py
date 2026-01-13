
from PIL import Image, ImageOps

from arcane.util import ResStream


class ArcTexture:
    VALUE_TO_MODE = {
        (4, 8, 2): 'RGBA',
        (3, 0, 0): 'RGB',
        (1, 0, 0): 'L',
        (1, 8, 2): 'P',
    }

    MODE_TO_VALUE = {value: key for key, value in VALUE_TO_MODE.items()}

    def load_binary(self, stream: ResStream):
        self.image_width = stream.read_dword()
        self.image_height = stream.read_dword()
        self.image_color_depth = stream.read_dword()
        self.image_alpha = stream.read_dword()
        self.image_type = stream.read_dword()
        self.image_compressed = stream.read_bool()
        self.image_linear = stream.read_bool()
        data_size = stream.read_dword()
        self.image_data = stream.read_bytes(data_size)

    def save_binary(self, stream: ResStream):
        stream.write_dword(self.image_width)
        stream.write_dword(self.image_height)
        stream.write_dword(self.image_color_depth)
        stream.write_dword(self.image_alpha)
        stream.write_dword(self.image_type)
        stream.write_bool(self.image_compressed)
        stream.write_bool(self.image_linear)
        stream.write_dword(len(self.image_data))
        stream.write_bytes(self.image_data)

    def load_img(self, filepath):
        img = Image.open(filepath)
        img = ImageOps.mirror(img).rotate(180)
        self.image_width = img.width
        self.image_height = img.height
        self.image_color_depth, self.image_alpha, self.image_type = self.MODE_TO_VALUE[img.mode]
        self.image_compressed = True
        self.image_linear = True
        self.image_data = img.tobytes()

    def save_img(self, filepath):
        mode = self.VALUE_TO_MODE[
            (self.image_color_depth, self.image_alpha, self.image_type)
        ]
        img = Image.frombytes(mode, (self.image_width, self.image_height), self.image_data)
        img = ImageOps.mirror(img.rotate(180))
        if(img.mode != 'RGB'):
            img = img.convert('RGB')
        
        img.save(filepath)


class ArcTerrain(ArcTexture):
    VALUE_TO_MODE = {
        (1, 1, 0): 'P',
    }

    MODE_TO_VALUE = {value: key for key, value in VALUE_TO_MODE.items()}
