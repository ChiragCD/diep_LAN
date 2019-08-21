import pygame
from sprite import tank

## Action to function
chart = {

    "UPDATE_SPEED" : tank.update_speed,
    "SHOOT" : tank.shoot,
    "AUTOSHOOT" : tank.autoshoot,
    "ROTATE_CLOCKWISE" : tank.rotate_clockwise,
    "ROTATE_ANTICLOCKWISE" : tank.rotate_anticlockwise,
    "REORIENT" : tank.reorient,

    }

## Input to action
action = {
    
    pygame.K_UP : chart["UPDATE_SPEED"],
    pygame.K_DOWN : chart["UPDATE_SPEED"],
    pygame.K_LEFT : chart["UPDATE_SPEED"],
    pygame.K_RIGHT : chart["UPDATE_SPEED"],

    pygame.K_SPACE : chart["SHOOT"],

    pygame.K_e : chart["AUTOSHOOT"],
    pygame.K_c : chart["ROTATE_CLOCKWISE"],
    pygame.K_a : chart["ROTATE_ANTICLOCKWISE"],

    1 : chart["SHOOT"],                          ## Left click
    3 : None,                           ## Right click

    pygame.MOUSEMOTION : chart["REORIENT"],

    }
