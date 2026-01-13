#  • ▌ ▄ ·. ▄▄▄▄·     ▄▄▄ .·▄▄▄▄  ▪  ▄▄▄▄▄      ▄▄▄       ▄▄▄·▄▄▄       
#  ·██ ▐███▪▐█ ▀█▪    ▀▄.▀·██▪ ██ ██ •██  ▪     ▀▄ █·    ▐█ ▄█▀▄ █·▪    
#  ▐█ ▌▐▌▐█·▐█▀▀█▄    ▐▀▀▪▄▐█· ▐█▌▐█· ▐█.▪ ▄█▀▄ ▐▀▀▄      ██▀·▐▀▀▄  ▄█▀▄
#  ██ ██▌▐█▌██▄▪▐█    ▐█▄▄▌██. ██ ▐█▌ ▐█▌·▐█▌.▐▌▐█•█▌    ▐█▪·•▐█•█▌▐█▌.▐▌
#  ▀▀  █▪▀▀▀·▀▀▀▀      ▀▀▀ ▀▀▀▀▀• ▀▀▀ ▀▀▀  ▀█▄▀▪.▀  ▀    .▀   .▀  ▀ ▀█▄▀▪
#                Magicbane Emulator Project © 2013 - 2022
#                           www.magicbane.com

import glob
import os

from arcane.util.hasher import hash_string

_STRING_TO_HASH = {}
_HASH_TO_STRING = {}


def load_files():
    directory = os.path.dirname(__file__)

    for filepath in glob.glob(os.path.join(directory, '*.txt')):
        lines = list(map(lambda s: s.strip(), open(filepath).readlines()))

        _STRING_TO_HASH.update({
            s: hash_string(s) for s in lines
        })

        _HASH_TO_STRING.update({
            hash_string(s): s for s in lines
        })


def string_to_hash(s):
    return _STRING_TO_HASH.get(s, s)


def hash_to_string(h):
    return _HASH_TO_STRING.get(h, h)


load_files()
