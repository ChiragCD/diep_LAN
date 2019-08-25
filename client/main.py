"""
The main program. Run this to start the game.
If back.jpeg has not been properly created, re-download that file or run create_back.py
(Note that this uses external modules numpy and imageio)
"""

import asyncio, pygame, sprite
from input_config import action
from game_constants import *

class program(object):

    def __init__(self):

        """
        Setup the local objects, start the screen, etc.
        """

        pygame.init()
        self.tank = sprite.tank(0, 900, 900, 0)
        self.screen = pygame.display.set_mode((500, 500))
        self.map0 = pygame.Surface((1050, 1050))
        self.map1 = pygame.Surface((1050, 1050))
        self.map2 = pygame.Surface((1050, 1050))
        self.map3 = pygame.Surface((1050, 1050))
        self.map0.set_colorkey((254, 254, 254))
        self.map1.set_colorkey((254, 254, 254))
        self.map2.set_colorkey((254, 254, 254))
        self.map3.set_colorkey((254, 254, 254))
        self.back = pygame.image.load("back.jpeg").convert()

    def end(self):

        """
        End the program.
        """

        pygame.quit()
        quit()

    async def main(self):

        """
        Start and run the program.
        """

        self.own_tank = pygame.sprite.Group(self.tank.turret, self.tank)
        self.own_bullets = pygame.sprite.Group(*self.tank.bullets)
        self.groups = [pygame.sprite.Group() for i in range(TILE_NUM * TILE_NUM)]

        self.groups[0].add(self.tank.turret, self.tank)

        loop = asyncio.get_running_loop()
        reference_time = int(loop.time()) + 1                                   ##

        iteration = 1
        while(True):
            if(loop.time() < reference_time - 0.005):
                continue
            if(loop.time() - reference_time > 0.01):
                print("lag " + str(loop.time())  + "  " + str(reference_time))
            iteration += 1
            reference_time += 0.01
            if(iteration % 5 == 0):
                await self.output()
            await self.logic()
            await self.input_handler()

            ## Processing
            ## Output
            ## etc.

    async def input_handler(self):

        """
        Accept user inputs, perform actions as defined in input_config and input_to_function_chart files.
        """

        for event in pygame.event.get():
            if(event.type == pygame.MOUSEMOTION):
                action[event.type](self.tank)       ## track mouse motion
                continue
            try:                                            ## Not very clean, better if dict had a default value
                if(event.type == pygame.KEYDOWN):
                    action[event.key](self.tank, event.key, 1)     ## 1 represents key down
                    continue
                if(event.type == pygame.KEYUP):
                    action[event.key](self.tank, event.key, 0)     ## 0 represents key up
                    continue
            except KeyError:
                pass
            if(event.type == pygame.MOUSEBUTTONDOWN):
                action[event.button](self.tank, 1)  ## 1 represents button pressed
                continue
            if(event.type == pygame.MOUSEBUTTONUP):
                action[event.button](self.tank, 0)  ## 0 represents button released
                continue
            if(event.type == pygame.QUIT):
                self.end()
        return

    async def logic(self):

        """
        Run the program logic.
        """

        self.tank.move()
        for bullet in self.tank.bullets:
            bullet.move()
            if(bullet not in self.groups[bullet.tile]):
                self.groups[bullet.tile].add(bullet)
        for tile_num, group in enumerate(self.groups):
            for sprite in group:
                if(sprite.tile != tile_num):
                    group.remove(sprite)
                    if(sprite not in self.groups[sprite.tile]):
                        self.groups[sprite.tile].add(sprite)
        return

    async def output(self):

        """
        Update and display the screen.
        """

        def tile_decider():

            if(self.tank.local_pos_x > 500 and self.tank.local_pos_y > 500):
                return [self.tank.field_of_view - self.tank.local_pos_x,
            self.tank.field_of_view - self.tank.local_pos_y,
            self.tank.tile,
            self.tank.tile + 1,
            self.tank.tile + TILE_NUM,
            self.tank.tile + TILE_NUM + 1]

            if(self.tank.local_pos_x > 500 and self.tank.local_pos_y < 500):
                return [self.tank.field_of_view - self.tank.local_pos_x,
            self.tank.field_of_view - self.tank.local_pos_y - 1000,
            self.tank.tile - TILE_NUM,
            self.tank.tile - TILE_NUM + 1,
            self.tank.tile,
            self.tank.tile + 1]

            if(self.tank.local_pos_x < 500 and self.tank.local_pos_y > 500):
                return [self.tank.field_of_view - self.tank.local_pos_x - 1000,
            self.tank.field_of_view - self.tank.local_pos_y,
            self.tank.tile - 1,
            self.tank.tile,
            self.tank.tile + TILE_NUM - 1,
            self.tank.tile + TILE_NUM]

            if(self.tank.local_pos_x < 500 and self.tank.local_pos_y < 500):
                return [self.tank.field_of_view - self.tank.local_pos_x - 1000,
            self.tank.field_of_view - self.tank.local_pos_y - 1000,
            self.tank.tile - TILE_NUM - 1,
            self.tank.tile - TILE_NUM,
            self.tank.tile - 1,
            self.tank.tile]

        self.screen.fill((125, 125, 125))
        self.map0.fill((254, 254, 254))
        self.map1.fill((254, 254, 254))
        self.map2.fill((254, 254, 254))
        self.map3.fill((254, 254, 254))
        decisions = tile_decider()
        x, y = decisions.pop(0), decisions.pop(0)
        self.screen.blit(self.back, (x, y))
        self.groups[decisions.pop(0)].draw(self.map0)
        self.groups[decisions.pop(0)].draw(self.map1)
        self.groups[decisions.pop(0)].draw(self.map2)
        self.groups[decisions.pop(0)].draw(self.map3)
        self.screen.blit(self.map0, (x, y))
        self.screen.blit(self.map1, (x + 1000, y))
        self.screen.blit(self.map2, (x, y + 1000))
        self.screen.blit(self.map3, (x + 1000, y + 1000))
        pygame.display.flip()

def main():

    loop = asyncio.get_event_loop()
    tester = program()
    loop.create_task(tester.main())
    loop.run_forever()

if(__name__ == "__main__"):
    main()
