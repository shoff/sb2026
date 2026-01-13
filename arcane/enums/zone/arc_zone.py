#  • ▌ ▄ ·. ▄▄▄▄·     ▄▄▄ .·▄▄▄▄  ▪  ▄▄▄▄▄      ▄▄▄       ▄▄▄·▄▄▄       
#  ·██ ▐███▪▐█ ▀█▪    ▀▄.▀·██▪ ██ ██ •██  ▪     ▀▄ █·    ▐█ ▄█▀▄ █·▪    
#  ▐█ ▌▐▌▐█·▐█▀▀█▄    ▐▀▀▪▄▐█· ▐█▌▐█· ▐█.▪ ▄█▀▄ ▐▀▀▄      ██▀·▐▀▀▄  ▄█▀▄
#  ██ ██▌▐█▌██▄▪▐█    ▐█▄▄▌██. ██ ▐█▌ ▐█▌·▐█▌.▐▌▐█•█▌    ▐█▪·•▐█•█▌▐█▌.▐▌
#  ▀▀  █▪▀▀▀·▀▀▀▀      ▀▀▀ ▀▀▀▀▀• ▀▀▀ ▀▀▀  ▀█▄▀▪.▀  ▀    .▀   .▀  ▀ ▀█▄▀▪
#                Magicbane Emulator Project © 2013 - 2022
#                           www.magicbane.com

ELLIPTICAL = 0
RECTANGULAR = 1

ZONE_TO_STRING = {
    ELLIPTICAL: 'ELLIPTICAL',
    RECTANGULAR: 'RECTANGULAR',
}

STRING_TO_ZONE = {
    'ELLIPTICAL': ELLIPTICAL,
    'RECTANGULAR': RECTANGULAR,
}

GLOBAL = 0
LOCAL = 1

TILECOORD_TO_STRING = {
    GLOBAL: 'GLOBAL',
    LOCAL: 'LOCAL',
}

STRING_TO_TILECOORD = {
    'GLOBAL': GLOBAL,
    'LOCAL': LOCAL,
}

ADJACENT = 0
RANDOM = 1

PATTERN_TO_STRING = {
    ADJACENT: 'ADJACENT',
    RANDOM: 'RANDOM',
}

STRING_TO_PATTERN = {
    'ADJACENT': ADJACENT,
    'RANDOM': RANDOM,
}

PARENT = 0
WORLD = 1
SELF = 2

SEALEVEL_TO_STRING = {
    PARENT: 'PARENT',
    WORLD: 'WORLD',
    SELF: 'SELF',
}

STRING_TO_SEALEVEL = {
    'PARENT': PARENT,
    'WORLD': WORLD,
    'SELF': SELF,
}
