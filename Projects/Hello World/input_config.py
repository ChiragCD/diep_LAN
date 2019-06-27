import pygame
from input_to_function_chart import chart

action = {
    
    pygame.K_UP : chart.MOVE_UP,
    pygame.K_DOWN : chart.MOVE_DOWN,
    pygame.K_LEFT : chart.MOVE_LEFT,
    pygame.K_RIGHT : chart.MOVE_RIGHT,

    pygame.K_SPACE : chart.SHOOT,

    pygame.K_e : chart.AUTOSHOOT,
    pygame.K_c : chart.ROTATE_CLOCKWISE,
    pygame.K_a : chart.ROTATE_ANTICLOCKWISE,

    1 : chart.SHOOT,                          ## Left click
    3 : None,                           ## Right click

    }
