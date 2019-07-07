import pygame
import draw_sprite
import numpy as np
from sprite_config import data

class sprite(pygame.sprite.Sprite):

    def __init__(self, Type, pos_x, pos_y, orientation):

        pygame.sprite.Sprite.__init__(self)
        self.type = Type
        self.health = data[Type]["health"]
        self.max_speed = data[Type]["max_speed"]
        self.speed_x = 0
        self.speed_y = 0
        self.orientation = orientation
        self.image = draw_sprite.get_drawing(Type)
        self.rect = self.image.get_rect()
        self.radius = data[Type]["radius"]
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.update_rect()

class bullet(sprite):

    def __init__(self,  Type, pos_x, pos_y, orientation):

        sprite.__init__(self,  Type, pos_x, pos_y, orientation)

    # Function to update the properties of the sprite and bullet when a collision occurs
    def collision(self , sprite):

        pass

    def update_rect(self):

        pass

class tank(sprite):

    def __init__(self, Type, pos_x, pos_y, orientation):

        sprite.__init__(self, Type, pos_x, pos_y, orientation)
        self.field_of_view = data[Type]["field_of_view"]

    def move(self):

        self.pos_x += self.speed_x
        self.pos_y += self.speed_y
        self.update_rect()

    # This function generates a new bullet, sets the properties for it according to the tank-type, and then returns it
    def shoot(self, *args):

        new_bullet = bullet(data[self.type]["bullet_type"], self.pos_x, self.pos_y, self.orientation)
        # Currently I have ignored the effects of recoil and tank speed
        new_bullet.speed_x = data[new_bullet.type]["speed"] * np.math.cos(new_bullet.orientation)
        new_bullet.speed_y = data[new_bullet.type]["speed"] * np.math.sin(new_bullet.orientation)
        return new_bullet

    def autoshoot(self, *args):

        pass

    def rotate_clockwise(self, *args):

        self.orientation -= 5
        # Will have to redraw the sprite
        self.update_rect()

    def rotate_anticlockwise(self, *args):

        self.orientation += 5
        # Will have to redraw the sprite
        self.update_rect()

    def update_rect(self):

        self.rect.x = 250 - self.radius
        self.rect.y = 250 - self.radius

        ##self.rect.x = int(self.pos_x) - self.radius          ## the image is pasted on screen using its top left corner, rather than centre (pos_x, pos_y)
        ##self.rect.y = int(self.pos_y) - self.radius

    def update_speed(self, key, pressed):

        if(pressed):
            if(key == pygame.K_UP):
                if(self.speed_x):
                    self.speed_y -= 0.707 * self.max_speed
                    self.speed_x *= 0.707
                else:
                    self.speed_y -= 1 * self.max_speed
            if(key == pygame.K_DOWN):
                if(self.speed_x):
                    self.speed_y += 0.707 * self.max_speed
                    self.speed_x *= 0.707
                else:
                    self.speed_y += 1 * self.max_speed
            if(key == pygame.K_LEFT):
                if(self.speed_y):
                    self.speed_x -= 0.707 * self.max_speed
                    self.speed_y *= 0.707
                else:
                    self.speed_x -= 1 * self.max_speed
            if(key == pygame.K_RIGHT):
                if(self.speed_y):
                    self.speed_x += 0.707 * self.max_speed
                    self.speed_y *= 0.707
                else:
                    self.speed_x += 1 * self.max_speed
        else:
            if(key == pygame.K_UP):
                if(self.speed_x):
                    self.speed_y += 0.707 * self.max_speed
                    self.speed_x /= 0.707
                else:
                    self.speed_y += 1 * self.max_speed
            if(key == pygame.K_DOWN):
                if(self.speed_x):
                    self.speed_y -= 0.707 * self.max_speed
                    self.speed_x /= 0.707
                else:
                    self.speed_y -= 1 * self.max_speed
            if(key == pygame.K_LEFT):
                if(self.speed_y):
                    self.speed_x += 0.707 * self.max_speed
                    self.speed_y /= 0.707
                else:
                    self.speed_x += 1 * self.max_speed
            if(key == pygame.K_RIGHT):
                if(self.speed_y):
                    self.speed_x -= 0.707 * self.max_speed
                    self.speed_y /= 0.707
                else:
                    self.speed_x -= 1 * self.max_speed