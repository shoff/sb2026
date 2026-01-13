#  • ▌ ▄ ·. ▄▄▄▄·     ▄▄▄ .·▄▄▄▄  ▪  ▄▄▄▄▄      ▄▄▄       ▄▄▄·▄▄▄       
#  ·██ ▐███▪▐█ ▀█▪    ▀▄.▀·██▪ ██ ██ •██  ▪     ▀▄ █·    ▐█ ▄█▀▄ █·▪    
#  ▐█ ▌▐▌▐█·▐█▀▀█▄    ▐▀▀▪▄▐█· ▐█▌▐█· ▐█.▪ ▄█▀▄ ▐▀▀▄      ██▀·▐▀▀▄  ▄█▀▄
#  ██ ██▌▐█▌██▄▪▐█    ▐█▄▄▌██. ██ ▐█▌ ▐█▌·▐█▌.▐▌▐█•█▌    ▐█▪·•▐█•█▌▐█▌.▐▌
#  ▀▀  █▪▀▀▀·▀▀▀▀      ▀▀▀ ▀▀▀▀▀• ▀▀▀ ▀▀▀  ▀█▄▀▪.▀  ▀    .▀   .▀  ▀ ▀█▄▀▪
#                Magicbane Emulator Project © 2013 - 2022
#                           www.magicbane.com

DOOR_TYPE_ROTATE = 0
DOOR_TYPE_SLIDE = 1

DOOR_TYPE_TO_STRING = {
    DOOR_TYPE_ROTATE: 'ROTATE',
    DOOR_TYPE_SLIDE: 'SLIDE',
}

STRING_TO_DOOR_TYPE = {
    'ROTATE': DOOR_TYPE_ROTATE,
    'SLIDE': DOOR_TYPE_SLIDE,
}

DOOR_MOVEMENT_AXIS_XAXIS = 0
DOOR_MOVEMENT_AXIS_YAXIS = 1
DOOR_MOVEMENT_AXIS_ZAXIS = 2

DOOR_MOVEMENT_AXIS_TO_STRING = {
    DOOR_MOVEMENT_AXIS_XAXIS: 'XAXIS',
    DOOR_MOVEMENT_AXIS_YAXIS: 'YAXIS',
    DOOR_MOVEMENT_AXIS_ZAXIS: 'ZAXIS',
}

STRING_TO_DOOR_MOVEMENT_AXIS = {
    'XAXIS': DOOR_MOVEMENT_AXIS_XAXIS,
    'YAXIS': DOOR_MOVEMENT_AXIS_YAXIS,
    'ZAXIS': DOOR_MOVEMENT_AXIS_ZAXIS,
}

DOOR_SWING_DIRECTION_CLOCKWISE = 0
DOOR_SWING_DIRECTION_COUNTERCLOCKWISE = 1

DOOR_SWING_DIRECTION_TO_STRING = {
    DOOR_SWING_DIRECTION_CLOCKWISE: 'CLOCKWISE',
    DOOR_SWING_DIRECTION_COUNTERCLOCKWISE: 'COUNTERCLOCKWISE',
}

STRING_TO_DOOR_SWING_DIRECTION = {
    'CLOCKWISE': DOOR_SWING_DIRECTION_CLOCKWISE,
    'COUNTERCLOCKWISE': DOOR_SWING_DIRECTION_COUNTERCLOCKWISE,
}
