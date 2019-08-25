import pygame

class Group(pygame.sprite.Group):

    def draw(self, surface, offset):

        for sprite in self:
            surface.blit(sprite.image, (sprite.rect.x + offset[0], sprite.rect.y + offset[1]))
