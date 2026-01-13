#  • ▌ ▄ ·. ▄▄▄▄·     ▄▄▄ .·▄▄▄▄  ▪  ▄▄▄▄▄      ▄▄▄       ▄▄▄·▄▄▄       
#  ·██ ▐███▪▐█ ▀█▪    ▀▄.▀·██▪ ██ ██ •██  ▪     ▀▄ █·    ▐█ ▄█▀▄ █·▪    
#  ▐█ ▌▐▌▐█·▐█▀▀█▄    ▐▀▀▪▄▐█· ▐█▌▐█· ▐█.▪ ▄█▀▄ ▐▀▀▄      ██▀·▐▀▀▄  ▄█▀▄
#  ██ ██▌▐█▌██▄▪▐█    ▐█▄▄▌██. ██ ▐█▌ ▐█▌·▐█▌.▐▌▐█•█▌    ▐█▪·•▐█•█▌▐█▌.▐▌
#  ▀▀  █▪▀▀▀·▀▀▀▀      ▀▀▀ ▀▀▀▀▀• ▀▀▀ ▀▀▀  ▀█▄▀▪.▀  ▀    .▀   .▀  ▀ ▀█▄▀▪
#                Magicbane Emulator Project © 2013 - 2022
#                           www.magicbane.com

RUNE_UNKNOWN = 0
RUNE_RACE = 1
RUNE_CLASS = 2
RUNE_DISCIPLINE = 3
RUNE_TALENT = 4

RUNE_TYPE_TO_STRING = {
    RUNE_UNKNOWN: 'UNKNOWN',
    RUNE_RACE: 'RACE',
    RUNE_CLASS: 'CLASS',
    RUNE_DISCIPLINE: 'DISCIPLINE',
    RUNE_TALENT: 'TALENT',
}

STRING_TO_RUNE_TYPE = {
    'UNKNOWN': RUNE_UNKNOWN,
    'RACE': RUNE_RACE,
    'CLASS': RUNE_CLASS,
    'DISCIPLINE': RUNE_DISCIPLINE,
    'TALENT': RUNE_TALENT,
}

SPEED_TYPE_WALK = 0
SPEED_TYPE_RUN = 1
SPEED_TYPE_COMBATWALK = 2
SPEED_TYPE_COMBATRUN = 3
SPEED_TYPE_FLYWALK = 4
SPEED_TYPE_FLYRUN = 5
SPEED_TYPE_SWIM = 6

SPEED_TYPE_TO_STRING = {
    SPEED_TYPE_WALK: 'WALK',
    SPEED_TYPE_RUN: 'RUN',
    SPEED_TYPE_COMBATWALK: 'COMBATWALK',
    SPEED_TYPE_COMBATRUN: 'COMBATRUN',
    SPEED_TYPE_FLYWALK: 'FLYWALK',
    SPEED_TYPE_FLYRUN: 'FLYRUN',
    SPEED_TYPE_SWIM: 'SWIM',
}

STRING_TO_SPEED_TYPE = {
    SPEED_TYPE_WALK: 'WALK',
    SPEED_TYPE_RUN: 'RUN',
    SPEED_TYPE_COMBATWALK: 'COMBATWALK',
    SPEED_TYPE_COMBATRUN: 'COMBATRUN',
    SPEED_TYPE_FLYWALK: 'FLYWALK',
    SPEED_TYPE_FLYRUN: 'FLYRUN',
    SPEED_TYPE_SWIM: 'SWIM',
}

RUNE_SEX_MALE = 1
RUNE_SEX_FEMALE = 2

RUNE_SEX_TO_STRING = {
    RUNE_SEX_MALE: 'MALE',
    RUNE_SEX_FEMALE: 'FEMALE',
}
STRING_TO_RUNE_SEX = {
    'MALE': RUNE_SEX_MALE,
    'FEMALE': RUNE_SEX_FEMALE,
}
