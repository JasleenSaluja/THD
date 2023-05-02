import pygame
from settings import *
from support import *
from pygame.image import load
from transition import Transition
from editor import Editor
from level import Level

from os import walk

# first game screen showing the name of the game
class GameLaunch:
    def __init__(self, toggle=False):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.clock = pygame.time.Clock()
        self.imports()

        # cursor 
        surf = load('graphics/cursors/mouse.png').convert_alpha()
        cursor = pygame.cursors.Cursor((0,0), surf)
        pygame.mouse.set_cursor(cursor)

    def imports(self):
        # terrain
        self.land_tiles = import_folder_dict('graphics/terrain/land_1')
               
     

    def run(self):
        while True:
            dt = self.clock.tick() / 1000
            surf=pygame.image.load('graphics/screen_1.png')
            self.display_surface.blit(surf, (0,0)) #blit screen for 5 secs
            #pygame.time.set_timer(pygame.USEREVENT, 5000)
            pygame.time.wait(5000)

            #self.display_surface.fill('black')
            pygame.display.update()


if __name__ == '__main__':
    GameLaunch().run()