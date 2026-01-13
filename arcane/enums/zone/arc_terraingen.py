#  • ▌ ▄ ·. ▄▄▄▄·     ▄▄▄ .·▄▄▄▄  ▪  ▄▄▄▄▄      ▄▄▄       ▄▄▄·▄▄▄       
#  ·██ ▐███▪▐█ ▀█▪    ▀▄.▀·██▪ ██ ██ •██  ▪     ▀▄ █·    ▐█ ▄█▀▄ █·▪    
#  ▐█ ▌▐▌▐█·▐█▀▀█▄    ▐▀▀▪▄▐█· ▐█▌▐█· ▐█.▪ ▄█▀▄ ▐▀▀▄      ██▀·▐▀▀▄  ▄█▀▄
#  ██ ██▌▐█▌██▄▪▐█    ▐█▄▄▌██. ██ ▐█▌ ▐█▌·▐█▌.▐▌▐█•█▌    ▐█▪·•▐█•█▌▐█▌.▐▌
#  ▀▀  █▪▀▀▀·▀▀▀▀      ▀▀▀ ▀▀▀▀▀• ▀▀▀ ▀▀▀  ▀█▄▀▪.▀  ▀    .▀   .▀  ▀ ▀█▄▀▪
#                Magicbane Emulator Project © 2013 - 2022
#                           www.magicbane.com

PEAKED = 1
RIDGED = 2
ROLLING = 3
MESA = 5
PLANAR = 4
MESH = 6
TARGA = 7

TERRAIN_TYPE_TO_STRING = {
    PEAKED: 'PEAKED',
    RIDGED: 'RIDGED',
    ROLLING: 'ROLLING',
    MESA: 'MESA',
    PLANAR: 'PLANAR',
    MESH: 'MESH',
    TARGA: 'TARGA',
}

STRING_TO_TERRAIN_TYPE = {
    'PEAKED': PEAKED,
    'RIDGED': RIDGED,
    'ROLLING': ROLLING,
    'MESA': MESA,
    'PLANAR': PLANAR,
    'MESH': MESH,
    'TARGA': TARGA,
}
