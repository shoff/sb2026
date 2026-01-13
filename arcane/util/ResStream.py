#  • ▌ ▄ ·. ▄▄▄▄·     ▄▄▄ .·▄▄▄▄  ▪  ▄▄▄▄▄      ▄▄▄       ▄▄▄·▄▄▄       
#  ·██ ▐███▪▐█ ▀█▪    ▀▄.▀·██▪ ██ ██ •██  ▪     ▀▄ █·    ▐█ ▄█▀▄ █·▪    
#  ▐█ ▌▐▌▐█·▐█▀▀█▄    ▐▀▀▪▄▐█· ▐█▌▐█· ▐█.▪ ▄█▀▄ ▐▀▀▄      ██▀·▐▀▀▄  ▄█▀▄
#  ██ ██▌▐█▌██▄▪▐█    ▐█▄▄▌██. ██ ▐█▌ ▐█▌·▐█▌.▐▌▐█•█▌    ▐█▪·•▐█•█▌▐█▌.▐▌
#  ▀▀  █▪▀▀▀·▀▀▀▀      ▀▀▀ ▀▀▀▀▀• ▀▀▀ ▀▀▀  ▀█▄▀▪.▀  ▀    .▀   .▀  ▀ ▀█▄▀▪
#                Magicbane Emulator Project © 2013 - 2022
#                           www.magicbane.com

import struct
from io import BytesIO


class ResStream:
    def __init__(self, initial_bytes=b''):
        self.buffer = BytesIO(initial_bytes)

    def read_byte(self):
        data = self.buffer.read(1)
        return struct.unpack('<B', data)[0]

    def read_bytes(self, n):
        data = self.buffer.read(n)
        return data

    def read_word(self):
        data = self.buffer.read(2)
        return struct.unpack('<H', data)[0]

    def read_dword(self):
        data = self.buffer.read(4)
        return struct.unpack('<I', data)[0]

    def read_qword(self):
        dwords = struct.unpack('<II', self.buffer.read(8))
        buffer = struct.pack('<II', dwords[1], dwords[0])
        return struct.unpack('<Q', buffer)[0]

    def read_float(self):
        data = self.buffer.read(4)
        return struct.unpack('<f', data)[0]

    def read_tuple(self):
        data = self.buffer.read(12)
        return struct.unpack('<fff', data)

    def read_bool(self):
        data = self.buffer.read(1)
        return True if struct.unpack('<B', data)[0] else False

    def read_wchar(self):
        data = self.buffer.read(2)
        return chr(struct.unpack('<H', data)[0])

    def read_string(self):
        length = self.read_dword()
        data = [self.read_wchar() for _ in range(length)]
        return ''.join(data)

    def write_byte(self, value):
        data = struct.pack('<B', value)
        self.buffer.write(data)

    def write_bytes(self, value):
        data = value
        self.buffer.write(data)

    def write_word(self, value):
        data = struct.pack('<H', value)
        self.buffer.write(data)

    def write_dword(self, value):
        data = struct.pack('<I', value)
        self.buffer.write(data)

    def write_qword(self, value):
        qword = struct.pack('<Q', value)
        dwords = [
            struct.unpack('<I', qword[:4])[0],
            struct.unpack('<I', qword[4:])[0],
        ]
        data = struct.pack('<II', dwords[1], dwords[0])
        self.buffer.write(data)

    def write_float(self, value):
        data = struct.pack('<f', value)
        self.buffer.write(data)

    def write_tuple(self, value):
        data = struct.pack('<fff', *value)
        self.buffer.write(data)

    def write_bool(self, value):
        data = struct.pack('<B', 1 if value else 0)
        self.buffer.write(data)

    def write_wchar(self, value):
        data = struct.pack('<H', value)
        self.buffer.write(data)

    def write_string(self, value):
        length = len(value)
        self.write_dword(length)
        for char in value.encode('utf-16-le'):
            self.write_byte(char)

    def get_bytes(self):
        self.buffer.seek(0)
        return self.buffer.read()
