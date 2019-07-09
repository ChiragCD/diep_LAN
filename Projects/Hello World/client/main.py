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
        loop.call_soon(self.output())
        loop.call_soon(self.logic())
        loop.call_soon(self.input_handler())

            ## Processing
            ## Output
            ## etc.

    def input_handler(self):

        """
        Accept user inputs, perform actions as defined in input_config and input_to_function_chart files.
        """

        loop = asyncio.get_running_loop()
        loop.call_at(loop.time() + 0.04, self.input_handler)
        # Some events such as firing a bullet generates a new object, so it is necessary to add those objects to the global list
        # TODO Find a way to initialize new_obj to null, so that there can be a common if statement to check if the action returned a new object
        for event in pygame.event.get():
            if(event.type == pygame.MOUSEMOTION):
                new_obj = action[event.type](self.tank)       ## track mouse motion
                continue
            try:                                            ## Not very clean, better if Enum had a default value
                if(event.type == pygame.KEYDOWN):
                    new_obj = action[event.key](self.tank, event.key, 1)     ## 1 represents key down
                    continue
                if(event.type == pygame.KEYUP):
                    new_obj = action[event.key](self.tank, event.key, 0)     ## 0 represents key up
                    continue
            except KeyError:
                pass
            if(event.type == pygame.MOUSEBUTTONDOWN):
                new_obj = action[event.button](self.tank, 1)  ## 1 represents button pressed
                continue
            if(event.type == pygame.MOUSEBUTTONUP):
                new_obj = action[event.button](self.tank, 0)  ## 0 represents button released
                continue
            if(event.type == pygame.QUIT):
                self.end()
        return

    def logic(self):

        """
        Run the program logic.
        """

        loop = asyncio.get_running_loop()
        loop.call_at(loop.time() + 0.02, self.logic)
        self.tank.move()
        self.tank.turret.reorient(self.tank.orientation)
        for bullet in self.tank.bullets:
            bullet.move()
        if(self.own_bullets.sprites() != self.tank.bullets):
            ## Update own_bullet group if bullets are added or deleted
            [self.own_bullets.add(bullet) for bullet in self.tank.bullets if
                    bullet not in self.own_bullets]
            [self.own_bullets.remove(bullet) for bullet in self.own_bullets if
                    bullet not in self.tank.bullets]
        return

    def output(self):

        """
        Update and display the screen.
        """

        loop = asyncio.get_running_loop()
        loop.call_at(loop.time() + 0.02, self.output)
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
