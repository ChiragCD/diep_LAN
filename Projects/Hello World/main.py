import pygame, asyncio, sprite
from input_config import action

class program(object):

    def __init__(self):

        self.tank = None

    def end(self):

        pass

    def main(self):

        while(True):
            asyncio.run(self.input_handler())
            ## Processing
            ## Output
            ## etc.
            await ## main_loop_frequency_based_thing

    async def input_handler(self):

        for event in pygame.event.get():
            if(event.type == pygame.KEYDOWN):
                action[event.key](self.tank, 0)     ## 0 represents key down
                continue
            if(event.type == pygame.KEYUP):
                action[event.key](self.tank, 1)     ## 1 represents key up
                continue
            if(event.type == pygame.MOUSEBUTTONDOWN):
                action[event.button](self.tank, 0)  ## 0 represents button pressed
                continue
            if(event.type == pygame.MOUSEBUTTONUP):
                action[event.button](self.tank, 1)  ## 0 represents button released
                continue
            if(event.type == pygame.QUIT):
                self.end()
