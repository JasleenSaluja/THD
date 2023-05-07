import pygame
from settings import *
from support import *
from pygame.image import load
from transition import Transition
from editor import Editor
from level import Level

from os import walk


# a screen to display all the levels
class GameLevels:
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
            surf=pygame.image.load('graphics/screen_3.png')
            self.display_surface.blit(surf, (0,0)) 
            play_button_surf=pygame.image.load('graphics/buttons/level_button.png')
            self.display_surface.blit(play_button_surf, (107,204))

            #self.display_surface.fill('black')
            pygame.display.update()


if __name__ == '__main__':
    GameLevels().run()