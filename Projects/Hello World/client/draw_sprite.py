import pygame
from sprite_config import data

## Type 0 - test_tank
def test_tank():

    surface = pygame.Surface((30, 30))
    surface.fill((255, 255, 255))
    surface.set_colorkey((255, 255, 255))
    pygame.draw.circle(surface, data[0]["colour"], (data[0]["radius"], data[0]["radius"]), data[0]["radius"])
    return surface

# This function is used to draw the bullet. Currently the color is hard-coded, will have to figure a way to make it available through parameters
def bullet() :
    surface = pygame.Surface((35, 35))
    surface.fill((255, 255, 255))
    surface.set_colorkey((255, 255, 255))
    pygame.draw.circle(surface, ((0, 0, 255)), (data[201]["radius"], data[201]["radius"]), data[201]["radius"])
    return surface

def get_drawing(Type):

    drawings = {
        0 : test_tank,
        201 : bullet,
        }

    return drawings[Type]()
