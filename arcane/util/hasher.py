#  • ▌ ▄ ·. ▄▄▄▄·     ▄▄▄ .·▄▄▄▄  ▪  ▄▄▄▄▄      ▄▄▄       ▄▄▄·▄▄▄       
#  ·██ ▐███▪▐█ ▀█▪    ▀▄.▀·██▪ ██ ██ •██  ▪     ▀▄ █·    ▐█ ▄█▀▄ █·▪    
#  ▐█ ▌▐▌▐█·▐█▀▀█▄    ▐▀▀▪▄▐█· ▐█▌▐█· ▐█.▪ ▄█▀▄ ▐▀▀▄      ██▀·▐▀▀▄  ▄█▀▄
#  ██ ██▌▐█▌██▄▪▐█    ▐█▄▄▌██. ██ ▐█▌ ▐█▌·▐█▌.▐▌▐█•█▌    ▐█▪·•▐█•█▌▐█▌.▐▌
#  ▀▀  █▪▀▀▀·▀▀▀▀      ▀▀▀ ▀▀▀▀▀• ▀▀▀ ▀▀▀  ▀█▄▀▪.▀  ▀    .▀   .▀  ▀ ▀█▄▀▪
#                Magicbane Emulator Project © 2013 - 2022
#                           www.magicbane.com

def _hash_string_short(array):
    v04 = (8 * array[7]) & 0xffffffff
    v05 = v04 ^ array[4]
    v06 = (16 * v05) & 0xffffffff
    v07 = array[5] ^ v06
    v08 = (16 * v07) & 0xffffffff
    v09 = array[6] ^ v08
    v10 = (32 * v09) & 0xffffffff
    v11 = array[2] ^ v10
    v12 = (32 * v11) & 0xffffffff
    v13 = (array[1] ^ v12)
    v14 = (32 * v13) & 0xffffffff
    v15 = (array[7] ^ 0x5A0) >> 2
    return array[0] ^ (v15) ^ (v14)


def _hash_string_long(array):
    i = 0
    result = 0
    for c in array:
        v = c - 32
        result ^= (v << (i)) & 0xffffffff
        if i > 0x18:
            result ^= v >> (32 - i)
            if i >= 0x1b:
                i -= 32
        i += 5
    return result & 0xffffffff


def hash_string(string):
    array = bytearray(string.encode())
    length = len(string)

    if (length == 7 or length == 8) and string[3] == '-':
        array += bytearray(b'\x00')
        return _hash_string_short(array)
    else:
        return _hash_string_long(array)
