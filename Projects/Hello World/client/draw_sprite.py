import pygame
from sprite_config import data

## Type 0 - test_tank
def test_tank():

    surface = pygame.Surface((30, 30))
    surface.fill((255, 255, 255))
    surface.set_colorkey((255, 255, 255))
    pygame.draw.circle(surface, data[0]["colour"], (data[0]["radius"], data[0]["radius"]), data[0]["radius"])
    return surface

def get_drawing(Type):

    drawings = {
        0 : test_tank
        }

    return drawings[Type]()
