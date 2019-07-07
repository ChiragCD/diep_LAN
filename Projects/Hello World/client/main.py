import asyncio, pygame, sprite
from input_config import action

class program(object):

    def __init__(self):

        pygame.init()
        self.tank = sprite.tank(0, 900, 900, 0)
        self.screen = pygame.display.set_mode((500, 500))
        self.back = pygame.image.load("back.jpeg").convert()

    def end(self):
        
        pygame.quit()
        quit()

    async def main(self):

        self.own_tank = pygame.sprite.Group()
        self.own_tank.add(self.tank)
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
        # Some events such as firing a bullet generates a new object, so it is necessary to add those objects to the global list
        # TODO Find a way to initialize new_obj to null, so that there can be a common if statement to check if the action returned a new object
        for event in pygame.event.get():
            if(event.type == pygame.KEYDOWN):
                new_obj = action[event.key](self.tank, event.key, 1)     ## 1 represents key down
                if(new_obj) :
                    new_group = pygame.sprite.Group()
                    new_group.add(new_obj)
                    self.groups.append(new_group)
                    print(self.groups)
                continue
            if(event.type == pygame.KEYUP):
                new_obj = action[event.key](self.tank, event.key, 0)     ## 0 represents key up
                if (new_obj):
                    new_group = pygame.sprite.Group()
                    new_group.add(new_obj)
                    self.groups.append(new_group)
                    print(self.groups)
                continue
            if(event.type == pygame.MOUSEBUTTONDOWN):
                new_obj = action[event.button](self.tank, 1)  ## 1 represents button pressed
                if (new_obj):
                    new_group = pygame.sprite.Group()
                    new_group.add(new_obj)
                    self.groups.append(new_group)
                    print(self.groups)
                continue
            if(event.type == pygame.MOUSEBUTTONUP):
                new_obj = action[event.button](self.tank, 0)  ## 0 represents button released
                if (new_obj):
                    new_group = pygame.sprite.Group()
                    new_group.add(new_obj)
                    self.groups.append(new_group)
                    print(self.groups)
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
        self.screen.blit(self.back, (self.tank.field_of_view - self.tank.pos_x, self.tank.field_of_view - self.tank.pos_y))
        for group in self.groups:
            group.draw(self.screen)
        pygame.display.flip()

loop = asyncio.get_event_loop()
tester = program()
loop.create_task(tester.main())
loop.run_forever()
