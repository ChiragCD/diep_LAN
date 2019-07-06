import pygame, math
import draw_sprite
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

class tank(sprite):

    def __init__(self, Type, pos_x, pos_y, orientation):

        sprite.__init__(self, Type, pos_x, pos_y, orientation)
        self.field_of_view = data[Type]["field_of_view"]
        self.turret = turret(data[Type]["linked_turret"], self)

    def move(self):

        self.pos_x += self.speed_x
        self.pos_y += self.speed_y
        self.update_rect()
        self.turret.move()

    def shoot(self, *args):

        pass

    def autoshoot(self, *args):

        pass

    def reorient(self):
        
        x, y = pygame.mouse.get_pos()
        x -= self.field_of_view               ## relative to centre
        y -= self.field_of_view
        self.orientation = -1 * math.degrees(math.atan(y / x))  ## -1 handles pygame's inverted y-axis
        self.turret.reorient(self.orientation)

    def rotate_clockwise(self, *args):

        self.orientation -= 5
        # Will have to redraw the sprite
        self.update_rect()

    def rotate_anticlockwise(self, *args):

        self.orientation += 5
        # Will have to redraw the sprite
        self.update_rect()

    def update_rect(self):

        self.rect.x = self.pos_x - self.radius
        self.rect.y = self.pos_y - self.radius

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

class bullet(sprite):

    def __init__(self,  Type, pos_x, pos_y, orientation):

        sprite.__init__(self,  Type, pos_x, pos_y, orientation)

    # Function to update the properties of the sprite and bullet when a collision occurs
    def collision(self , sprite):

        pass

class turret(sprite):

    def __init__(self, Type, owner_tank):

        self.tank = owner_tank
        self.dimension = 2 * max(data[Type]["length"], data[Type]["width"])
        sprite.__init__(self, Type, owner_tank.pos_x, owner_tank.pos_y, owner_tank.orientation)
        self.type = Type

    def update_rect(self):

        self.rect.x = self.tank.pos_x - self.dimension / 2  ## self.pos_x, pos_y are not used or maintained, these are always expected to be same as that of tank
        self.rect.y = self.tank.pos_y - self.dimension / 2

    def move(self):

        self.update_rect()

    def reorient(self, angle):
        
        if(abs(self.orientation - angle) > 2):              ## Don't worry about small variations.
            self.image = pygame.transform.rotate(self.image, angle - self.orientation)
            self.orientation = angle
            self.rect = self.image.get_rect()
            self.dimension = max(self.rect.height, self.rect.width)
            self.update_rect()

