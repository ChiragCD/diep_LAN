import pygame, math
import draw_sprite
from sprite_config import data
from math_constants import *

class sprite(pygame.sprite.Sprite):

    def __init__(self, Type, pos_x, pos_y, orientation):

        """
        Setup the sprite, use data from sprite_config.
        Type is the key to be used.
        """

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

    def __init__(self, Type, pos_x, pos_y, orientation):

        sprite.__init__(self, Type, pos_x, pos_y, orientation)
        self.speed_x = self.max_speed * math.cos(self.orientation)
        self.speed_y = self.max_speed * -1 * math.sin(self.orientation)

    def move(self):

        self.pos_x += self.speed_x
        self.pos_y += self.speed_y
        self.update_rect()

    def update_rect(self):

        self.rect.x = int(self.pos_x) - self.radius          ## the image is pasted on screen using its top left corner, rather than centre (pos_x, pos_y)
        self.rect.y = int(self.pos_y) - self.radius

    # Function to update the properties of the sprite and bullet when a collision occurs
    def collision(self , sprite):

        pass


class tank(sprite):

    def __init__(self, Type, pos_x, pos_y, orientation):

        """
        Setup the sprite and some tank specific attributes.
        """

        sprite.__init__(self, Type, pos_x, pos_y, orientation)
        self.field_of_view = data[Type]["field_of_view"]
        self.turret = turret(data[Type]["linked_turret"], self)
        self.movement_state = set()
        self.bullets = []

    def move(self):

        """
        Update position using speed.
        """

        self.pos_x += self.speed_x
        self.pos_y += self.speed_y
        self.update_rect()
        self.turret.move()

    # This function generates a new bullet, sets the properties for it according to the tank-type, and then returns it
    def shoot(self, *args):

        self.bullets.append(bullet(data[self.type]["bullet_type"], self.pos_x, self.pos_y, self.orientation))
        # Currently I have ignored the effects of recoil and tank speed

    def autoshoot(self, *args):

        pass

    def reorient(self):

        """
        Using mouse position, update the orientation attribute.
        """

        x, y = pygame.mouse.get_pos()
        x -= self.field_of_view               ## relative to centre
        y -= self.field_of_view
        try:
            self.orientation = math.atan2(-1 * y, x)    ## -1 handles pygame's inverted y-axis
                                                        ## atan2 returns between -pi and pi
        except ZeroDivisionError:
            if(y > 0): self.orientation = -1 * PIBY2
            else: self.orientation = PIBY2

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

        """
        A display function - update the drawing's position in accordance with the sprite's position.
        """

        self.rect.x = int(self.pos_x) - self.radius          ## the image is pasted on screen using its top left corner, rather than centre (pos_x, pos_y)
        self.rect.y = int(self.pos_y) - self.radius

    def update_speed(self, key, pressed):

        """
        Using keyboard keys, decide the tank's speed.
        """

        speeds = {() : (0, 0), ("U",) : (0, -1), ("D",) : (0, 1), ("L",) : (-1, 0), ("R",) : (1, 0), ("L", "U") : (-1 * ROOT2BY2, -1 * ROOT2BY2), ("R", "U") : (ROOT2BY2, -1 * ROOT2BY2), ("D", "L") : (-1 * ROOT2BY2, ROOT2BY2), ("D", "R") : (ROOT2BY2, ROOT2BY2)}

        if(not(pressed)):
            if(key == pygame.K_UP or key == pygame.K_w): key = pygame.K_DOWN
            elif(key == pygame.K_DOWN or key == pygame.K_s): key = pygame.K_UP
            elif(key == pygame.K_LEFT or key == pygame.K_a): key = pygame.K_RIGHT
            elif(key == pygame.K_RIGHT or key == pygame.K_d): key = pygame.K_LEFT

        if(key == pygame.K_UP or key == pygame.K_w): self.movement_state.add("U")
        if(key == pygame.K_DOWN or key == pygame.K_s): self.movement_state.add("D")
        if(key == pygame.K_LEFT or key == pygame.K_a): self.movement_state.add("L")
        if(key == pygame.K_RIGHT or key == pygame.K_d): self.movement_state.add("R")

        if("U" in self.movement_state and "D" in self.movement_state):
            self.movement_state.discard("U")
            self.movement_state.discard("D")
        if("L" in self.movement_state and "R" in self.movement_state):
            self.movement_state.discard("L")
            self.movement_state.discard("R")

        speed_x, speed_y = speeds[tuple(sorted(self.movement_state))]
        self.speed_x = self.max_speed * speed_x
        self.speed_y = self.max_speed * speed_y

class turret(sprite):

    def __init__(self, Type, owner_tank):

        """
        Setup the turret, and its unique attributes.
        """

        self.tank = owner_tank
        self.dimension = 2 * max(data[Type]["length"], data[Type]["width"])         ## The image of the turret will be in a square of endge length dimension.
        sprite.__init__(self, Type, owner_tank.pos_x, owner_tank.pos_y, owner_tank.orientation)
        self.type = Type
        self.basic_image = self.image

    def update_rect(self):

        """
        Display function - Set the image position in accordance with the parent tank's position.
        """

        self.rect.x = self.tank.pos_x - self.dimension / 2  ## self.pos_x, pos_y are not used or maintained, these are always expected to be same as that of tank
        self.rect.y = self.tank.pos_y - self.dimension / 2

    def move(self):

        """
        Update the turret's position. Since pos_x and pos_y are not used, this function has no direct purpose.
        """

        self.update_rect()

    def reorient(self, angle):

        """
        Update the drawing to make the turret point at a direction.
        """

        self.image = pygame.transform.rotate(self.basic_image, math.degrees(angle))
        self.orientation = angle
        self.rect = self.image.get_rect()
        self.dimension = max(self.rect.height, self.rect.width)
        self.update_rect()

