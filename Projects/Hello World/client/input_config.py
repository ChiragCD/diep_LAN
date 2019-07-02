import pygame
from input_to_function_chart import chart

action = {
    
    pygame.K_UP : chart.UPDATE_SPEED,
    pygame.K_DOWN : chart.UPDATE_SPEED,
    pygame.K_LEFT : chart.UPDATE_SPEED,
    pygame.K_RIGHT : chart.UPDATE_SPEED,

    pygame.K_SPACE : chart.SHOOT,

    pygame.K_e : chart.AUTOSHOOT,
    pygame.K_c : chart.ROTATE_CLOCKWISE,
    pygame.K_a : chart.ROTATE_ANTICLOCKWISE,

    1 : chart.SHOOT,                          ## Left click
    3 : None,                           ## Right click

    }
