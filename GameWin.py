import pygame, sys 
from pygame.math import Vector2 as vector
from pygame.mouse import get_pressed as mouse_buttons
from pygame.mouse import get_pos as mouse_pos
from pygame.image import load

from settings import *
from support import *

from menu import Menu
from timer import Timer

from random import choice, randint
import pickle #new

class GameWin:
    def __init__(self, screen_num=2, switch=None):
        self.screen_num = screen_num
        self.display_surface = pygame.display.get_surface()
        self.canvas_data = {}
        self.imports()
        self.switch= switch
        

        # add cursor
        surf = load('graphics/cursors/mouse.png').convert_alpha()
        cursor = pygame.cursors.Cursor((0,0), surf)
        pygame.mouse.set_cursor(cursor)

        #core attributes for button
        self.pressed=False

        # add music
        self.gamewin_music = pygame.mixer.Sound('audio/gamewin.ogg')
        
    def imports(self):
        #background
        self.background_4=load('graphics/GameWin_screen.png').convert_alpha()

        #replay button
        self.replay_button=load('graphics/buttons/replay_button.png').convert_alpha()
        self.replay_button_rect=self.replay_button.get_rect(center=(282,433))
        
       

       #level menu button
        self.level_menu_button=load('graphics/buttons/level_menu_button.png').convert_alpha()
        self.level_menu_button_rect=self.level_menu_button.get_rect(center=(692,433))
        
        
    def click(self):
        # print(mouse_pos())
        #play button
        if self.replay_button_rect.collidepoint(mouse_pos()):
            if pygame.mouse.get_pressed()[0]:
                self.pressed=True
            else:
                if self.pressed==True:
                    print('click')
                    self.pressed=False
            

        #edit button
        if self.level_menu_button_rect.collidepoint(mouse_pos()):
            if pygame.mouse.get_pressed()[0]:
                self.pressed=True
            else:
                if self.pressed==True:
                    print('click')
                    self.pressed=False


        

    def run(self, dt):
        self.gamewin_music.play(loops=-1)
        while True:
            self.events(replay_button=self.replay_button,level_menu_button=self.level_menu_button)
            self.update()
            self.draw()
            self.click()
            pygame.display.update()
            #self.clock.tick(ANIMATION_SPEED)
    
    def events(self,replay_button,level_menu_button):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # if event.button == 1:
                #     if self.play_button_rect.collidepoint(self.mouse_pos):
                #         self.launcher_music.stop()
                #         self.switch()
                #     elif self.edit_button_rect.collidepoint(self.mouse_pos):
                #         self.launcher_music.stop()
                #         self.switch()
                print(self.mouse_pos)
                

           
        
    
    def update(self):
        self.mouse_pos = mouse_pos()
        

    def draw(self):
        self.display_surface.blit(self.background_4, (0,0))
        self.replay_button_rect = self.display_surface.blit(self.replay_button, (511,464))
        self.level_menu_button_rect = self.display_surface.blit(self.level_menu_button, (676,464))


if __name__ == '__main__':
    # test the launcher
    pygame.init()
    pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    GameWin().run(dt=0)
    pygame.quit()
    sys.exit()