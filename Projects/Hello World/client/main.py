import asyncio, pygame, sprite
from input_config import action

class program(object):

    def __init__(self):

        pygame.init()
        self.tank = sprite.tank(0, 900, 900, 0)
        self.screen = pygame.display.set_mode((500, 500))
        self.map = pygame.Surface((10000, 10000))
        self.back = pygame.image.load("back.jpeg").convert()

    def end(self):
        
        pygame.quit()
        quit()

    async def main(self):

        self.own_tank = pygame.sprite.Group()
        self.own_tank.add(self.tank, self.tank.turret)
        self.groups = [self.own_tank]
        
        loop = asyncio.get_running_loop()
        loop.call_soon(self.output())
        loop.call_soon(self.logic())
        loop.call_soon(self.input_handler())

            ## Processing
            ## Output
            ## etc.

    def input_handler(self):
        
        loop.call_at(loop.time() + 0.01, self.input_handler)
        for event in pygame.event.get():
            if(event.type == pygame.MOUSEMOTION):
                action[event.type](self.tank)       ## track mouse motion
                continue
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
        return

    def logic(self):

        loop.call_at(loop.time() + 0.02, self.logic)
        self.tank.move()
        return

    def output(self):

        loop.call_at(loop.time() + 0.02, self.output)
        self.map.blit(self.back, (0, 0))
        for group in self.groups:
            group.draw(self.map)
        self.screen.blit(self.map, (self.tank.field_of_view - self.tank.pos_x, self.tank.field_of_view - self.tank.pos_y))
        pygame.display.flip()

loop = asyncio.get_event_loop()
tester = program()
loop.create_task(tester.main())
loop.run_forever()
