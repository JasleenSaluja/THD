import pygame, sys
from settings import *
from support import *

from pygame.mouse import get_pressed as mouse_buttons
from pygame.mouse import get_pos as mouse_pos
from pygame.image import load

from transition import Transition
from editor import Editor
from level import Level

from os import walk

# a simple game screen to show play and edit button to the user
class GameMenu:
    def __init__(self, toggle=False):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        #pygame.display.set_caption('pygame button')
        self.clock = pygame.time.Clock()
        self.imports()

        # cursor 
        surf = load('graphics/cursors/mouse.png').convert_alpha()
        cursor = pygame.cursors.Cursor((0,0), surf)
        pygame.mouse.set_cursor(cursor)

    def imports(self):
        # terrain
        self.land_tiles = import_folder_dict('graphics/terrain/land_1')



    def event_loop(self):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # play_button_surf=pygame.image.load('graphics/buttons/play_button.png')
            # self.display_surface.blit(play_button_surf, (282,433))
            # edit_button_surf=pygame.image.load('graphics/buttons/edit_button.png')
            # self.display_surface.blit(edit_button_surf, (692,433))


            # if event.type==pygame.MOUSEBUTTONDOWN:
            #     if self.play_button_surf.get_rect().collidepoint(event.pos):
            #         pass
            #         #Level().run()
            #     if self.edit_button_surf.get_rect().collidepoint(event.pos):
            #         pass
            #         #Editor().run()

            # a,b=pygame.mouse.mouse_pos()
            # if play_button_surf.x <=a <=play_button_surf.x+304 and play_button_surf.y <=b <=play_button_surf.y+96:
            #     play_button_surf=pygame.image.load('graphics/buttons/play_button_hover.png')
            #     self.display_surface.blit(play_button_surf, (282,433))
            
    def run(self):
        self.event_loop()
        while True:
            dt = self.clock.tick() / 1000
            surf=pygame.image.load('graphics/screen_2.png')
            self.display_surface.blit(surf, (0,0))
            #self.display_surface.fill('black')
            play_button_surf=pygame.image.load('graphics/buttons/play_button.png')
            self.display_surface.blit(play_button_surf, (282,433))
            edit_button_surf=pygame.image.load('graphics/buttons/edit_button.png')
            self.display_surface.blit(edit_button_surf, (692,433))

            
            


            pygame.display.update()


if __name__ == '__main__':
    GameMenu().run()