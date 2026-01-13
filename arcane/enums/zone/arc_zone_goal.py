#  • ▌ ▄ ·. ▄▄▄▄·     ▄▄▄ .·▄▄▄▄  ▪  ▄▄▄▄▄      ▄▄▄       ▄▄▄·▄▄▄       
#  ·██ ▐███▪▐█ ▀█▪    ▀▄.▀·██▪ ██ ██ •██  ▪     ▀▄ █·    ▐█ ▄█▀▄ █·▪    
#  ▐█ ▌▐▌▐█·▐█▀▀█▄    ▐▀▀▪▄▐█· ▐█▌▐█· ▐█.▪ ▄█▀▄ ▐▀▀▄      ██▀·▐▀▀▄  ▄█▀▄
#  ██ ██▌▐█▌██▄▪▐█    ▐█▄▄▌██. ██ ▐█▌ ▐█▌·▐█▌.▐▌▐█•█▌    ▐█▪·•▐█•█▌▐█▌.▐▌
#  ▀▀  █▪▀▀▀·▀▀▀▀      ▀▀▀ ▀▀▀▀▀• ▀▀▀ ▀▀▀  ▀█▄▀▪.▀  ▀    .▀   .▀  ▀ ▀█▄▀▪
#                Magicbane Emulator Project © 2013 - 2022
#                           www.magicbane.com

GOAL_TYPE_NONE = 0
GOAL_TYPE_POINTS_ORDERED = 1
GOAL_TYPE_POINTS_ORDEREDREV = 2
GOAL_TYPE_POINTS_RANDOM = 3
GOAL_TYPE_POINTS_TREENEAR = 4
GOAL_TYPE_POINTS_TREEFAR = 5
GOAL_TYPE_POINTS_WORLD_CITIES = 6

GOAL_TYPE_TO_STRING = {
    GOAL_TYPE_NONE: 'NONE',
    GOAL_TYPE_POINTS_ORDERED: 'POINTS_ORDERED',
    GOAL_TYPE_POINTS_ORDEREDREV: 'POINTS_ORDEREDREV',
    GOAL_TYPE_POINTS_RANDOM: 'POINTS_RANDOM',
    GOAL_TYPE_POINTS_TREENEAR: 'POINTS_TREENEAR',
    GOAL_TYPE_POINTS_TREEFAR: 'POINTS_TREEFAR',
    GOAL_TYPE_POINTS_WORLD_CITIES: 'POINTS_WORLD_CITIES',
}

STRING_TO_GOAL_TYPE = {
    'NONE': GOAL_TYPE_NONE,
    'POINTS_ORDERED': GOAL_TYPE_POINTS_ORDERED,
    'POINTS_ORDEREDREV': GOAL_TYPE_POINTS_ORDEREDREV,
    'POINTS_RANDOM': GOAL_TYPE_POINTS_RANDOM,
    'POINTS_TREENEAR': GOAL_TYPE_POINTS_TREENEAR,
    'POINTS_TREEFAR': GOAL_TYPE_POINTS_TREEFAR,
    'POINTS_WORLD_CITIES': GOAL_TYPE_POINTS_WORLD_CITIES,
}
