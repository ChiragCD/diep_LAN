import pygame, asyncio, sprite
from input_config import action

class program(object):

    def __init__(self):

        pygame.init()
        self.tank = sprite.tank(0, 900, 900, 0)

    def end(self):

        pygame.quit()

    @asyncio.coroutine
    def main(self):

        self.own_tank = pygame.sprite.Group()
        self.own_tank.add(self.tank)
        self.groups = [self.own_tank]
        asyncio.ensure_future(self.output(), loop = loop)
        asyncio.ensure_future(self.logic())
        asyncio.ensure_future(self.input_handler(), loop = loop)
            ## Processing
            ## Output
            ## etc.

    @asyncio.coroutine
    def input_handler(self):

        clock = pygame.time.Clock()

        while(True):
            clock.tick(100)
            for event in pygame.event.get():
                if(event.type == pygame.KEYDOWN):
                    action[event.key](self.tank, event.key, 1)     ## 1 represents key down
                    continue
                if(event.type == pygame.KEYUP):
                    action[event.key](self.tank, event.key, 0)     ## 0 represents key up
                    continue
                if(event.type == pygame.MOUSEBUTTONDOWN):
                    action[event.button](self.tank, 1)  ## 1 represents button pressed
                    continue
                if(event.type == pygame.MOUSEBUTTONUP):
                    action[event.button](self.tank, 0)  ## 0 represents button released
                    continue
                if(event.type == pygame.QUIT):
                    self.end()
            yield

    @asyncio.coroutine
    def logic(self):

        while(True):
            self.tank.move()
            yield
        
    @asyncio.coroutine
    def output(self):

        self.screen = pygame.display.set_mode((500, 500))
        back = pygame.image.load("back.jpeg").convert()

        clock = pygame.time.Clock()

        while(True):
            clock.tick(60)
            self.screen.blit(back, (self.tank.field_of_view - self.tank.pos_x, self.tank.field_of_view - self.tank.pos_y))
            for group in self.groups:
                group.draw(self.screen)
            pygame.display.flip()
            yield

tester = program()
loop = asyncio.get_event_loop()
asyncio.ensure_future(tester.main(), loop = loop)
loop.run_forever()
