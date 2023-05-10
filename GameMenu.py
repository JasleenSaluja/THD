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

class GameMenu:
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
        self.launcher_music = pygame.mixer.Sound('audio/gamelaunch.ogg')
        
    def imports(self):
        #background
        self.background_2=load('graphics/screen_2.png').convert_alpha()

        #play button
        self.play_button=load('graphics/buttons/play_button.png').convert_alpha()
        self.play_button_rect=self.play_button.get_rect(center=(282,433))
        self.play_button_hover=load('graphics/buttons/play_button_hover.png').convert_alpha()
        self.play_button_pressed=load('graphics/buttons/play_button_pressed.png').convert_alpha()
       

       #edit button
        self.edit_button=load('graphics/buttons/edit_button.png').convert_alpha()
        self.edit_button_rect=self.edit_button.get_rect(center=(692,433))
        self.edit_button_hover=load('graphics/buttons/edit_button_hover.png').convert_alpha()
        self.edit_button_pressed=load('graphics/buttons/edit_button_pressed.png').convert_alpha()
        
    def click(self):
        # print(mouse_pos())
        #play button
        if self.play_button_rect.collidepoint(mouse_pos()):
            self.play_button_rect = self.display_surface.blit(self.play_button_hover, (282,433))
            if pygame.mouse.get_pressed()[0]:
                self.play_button_rect = self.display_surface.blit(self.play_button_pressed, (282,433))
                self.pressed=True
            else:
                if self.pressed==True:
                    print('clicked play')
                    self.pressed=False
                    self.switch()
        #edit button
        if self.edit_button_rect.collidepoint(mouse_pos()):
            self.edit_button_rect = self.display_surface.blit(self.edit_button_hover, (692,433))
            if pygame.mouse.get_pressed()[0]:
                self.edit_button_rect = self.display_surface.blit(self.edit_button_pressed, (692,433))
                self.screen_num = 3
                self.pressed=True
                self.switch()
            else:
                if self.pressed==True:
                    print('click')
                    self.pressed=False
                    

    def run(self, dt):
        self.launcher_music.play(loops=-1)
        while True:
            self.events(play_button=self.play_button,edit_button=self.edit_button)
            self.click()
            self.update()
            self.draw()
            if self.screen_num == 3:
                break
            pygame.display.update()
            #self.clock.tick(ANIMATION_SPEED)
    
    def events(self,play_button,edit_button):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if self.play_button_rect.collidepoint(self.mouse_pos):
                        self.launcher_music.stop()
                        # self.switch()
                    elif self.edit_button_rect.collidepoint(self.mouse_pos):
                        self.launcher_music.stop()
                        # self.switch()
                print(self.mouse_pos)
    
    def update(self):
        self.mouse_pos = mouse_pos()
        

    def draw(self):
        self.display_surface.blit(self.background_2, (0,0))
        #self.display_surface.blit(self.canvas_data['title'], (0,0))
        self.play_button_rect = self.display_surface.blit(self.play_button, (282,433))
        self.edit_button_rect = self.display_surface.blit(self.edit_button, (692,433))
        
        # pygame.draw.rect(self.display_surface, (255,0,0), self.play_button_rect, 1)
        # pygame.draw.rect(self.display_surface, (255,0,0), self.edit_button_rect, 1)


if __name__ == '__main__':
    # test the launcher
    pygame.init()
    pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('Launcher')
    GameMenu().run(dt=0)
    pygame.quit()
    sys.exit()