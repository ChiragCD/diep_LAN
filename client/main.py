"""
The main program. Run this to start the game.
If back.jpeg has not been properly created, re-download that file or run create_back.py
(Note that this uses external modules numpy and imageio)
"""

import asyncio, pygame, sprite
from input_config import action

class program(object):

    def __init__(self):

        """
        Setup the local objects, start the screen, etc.
        """

        pygame.init()
        self.tank = sprite.tank(0, 900, 900, 0)
        self.screen = pygame.display.set_mode((500, 500))
        self.map = pygame.Surface((10000, 10000))
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
        self.groups = [self.own_bullets, self.own_tank]

        loop = asyncio.get_running_loop()
        reference_time = int(loop.time()) + 1                                   ##

        iteration = 1
        while(True):
            if(loop.time() < reference_time):
                continue
            if(loop.time() - reference_time > 0.1):
                print("lag " + str(loop.time())  + "  " + str(reference_time))
            iteration += 1
            reference_time += 0.01
            if(iteration % 10 == 0):
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
        if(self.own_bullets.sprites() != self.tank.bullets):
            ## Update own_bullet group if bullets are added or deleted
            [self.own_bullets.add(bullet) for bullet in self.tank.bullets if
                    bullet not in self.own_bullets]
            [self.own_bullets.remove(bullet) for bullet in self.own_bullets if
                    bullet not in self.tank.bullets]
        return

    async def output(self):

        """
        Update and display the screen.
        """

        self.screen.fill((125, 125, 125))
        self.map.blit(self.back, (0, 0))
        for group in self.groups:
            group.draw(self.map)
        self.screen.blit(self.map, (self.tank.field_of_view - self.tank.pos_x, self.tank.field_of_view - self.tank.pos_y))
        pygame.display.flip()

def main():

    loop = asyncio.get_event_loop()
    tester = program()
    loop.create_task(tester.main())
    loop.run_forever()

if(__name__ == "__main__"):
    main()
