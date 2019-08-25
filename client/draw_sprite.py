import pygame
from sprite_config import data

## Type 0 - test tank
def test_tank():

    surface = pygame.Surface((2 * data[0]["radius"], 2 * data[0]["radius"]))
    surface.fill((255, 255, 255))
    surface.set_colorkey((255, 255, 255))
    pygame.draw.circle(surface, data[0]["colour"], (data[0]["radius"], data[0]["radius"]), data[0]["radius"])
    return surface

# This function is used to draw the bullet. Currently the color is hard-coded, will have to figure a way to make it available through parameters
def bullet() :
    surface = pygame.Surface((2 * data[201]["radius"], 2 * data[201]["radius"]))
    surface.fill((255, 255, 255))
    surface.set_colorkey((255, 255, 255))
    pygame.draw.circle(surface, data[0]["colour"], (data[201]["radius"], data[201]["radius"]), data[201]["radius"])
    return surface

## Type 1 - bullet turret
def bullet_turret():

    larger_dimension = max(data[1]["length"], data[1]["width"])
    surface = pygame.Surface((2 * larger_dimension, 2 * larger_dimension))
    surface.fill((255, 255, 255))
    surface.set_colorkey((255, 255, 255))
    rect = pygame.Rect((larger_dimension, larger_dimension - data[1]["width"] / 2), (data[1]["length"], data[1]["width"]))
    pygame.draw.rect(surface, data[1]["colour"], rect)
    return surface

## Type 101 - square
def square():

    surface = pygame.Surface((2 * data[101]["radius"], 2 * data[101]["radius"]))
    surface.fill((255, 255, 255))
    surface.set_colorkey((255, 255, 255))
    pygame.draw.rect(surface, data[101]["colour"], pygame.Rect((0, 0), (2 * data[101]["radius"], 2 * data[101]["radius"])))
    return surface

def get_drawing(Type):

    """
    Acts as a common interface, or index, to access the functions here.
    """

    drawings = {
        0 : test_tank,
        1 : bullet_turret,
        101 : square,
        201 : bullet,
        }

    return drawings[Type]()
