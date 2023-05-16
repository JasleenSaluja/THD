import pygame, sys 
from pygame.math import Vector2 as vector
from pygame.mouse import get_pressed as mouse_buttons
from pygame.mouse import get_pos as mouse_pos
from pygame.image import load

from settings import *
from support import *
import os
from menu import Menu
from timer import Timer

from random import choice, randint
import pickle #new
from firbase import download_all_levels

class GameLevels:
    def __init__(self, screen_num=4, switch=None,stm=None,stg=None):
        self.screen_num = screen_num
        self.display_surface = pygame.display.get_surface()
        self.canvas_data = {}
        download_all_levels()
        self.imports()
        self.switch= switch
        self.switchToMenu=stm
        self.switchToGame=stg
        self.download_all_levels=download_all_levels()

        # add cursor
        surf = load('graphics/cursors/mouse.png').convert_alpha()
        cursor = pygame.cursors.Cursor((0,0), surf)
        pygame.mouse.set_cursor(cursor)

        #core attributes for button
        self.pressed=False

        # add music
        self.launcher_music = pygame.mixer.Sound('audio/gamelaunch.ogg')

        # sounds
        self.level_sounds = {
            'coin': pygame.mixer.Sound('audio/coin.wav'),
            'hit': pygame.mixer.Sound('audio/hit.wav'),
            'jump': pygame.mixer.Sound('audio/jump.wav'),
            'music': pygame.mixer.Sound('audio/SuperHero.ogg'),
        }

        


        
    def imports(self):
        #background
        self.background_2=load('graphics/screen_3.png').convert_alpha()

        #level button
        self.level_buttons = []
        for level in os.listdir('levels'):
            x= 282
            y= 433
            level_button=load('graphics/buttons/level_button.png').convert_alpha()
            level_button_rect=level_button.get_rect(center=(x,y))
            self.level_buttons.append({
                'button': level_button,
                'rect': level_button_rect,
                'level': level
            })
            x += 100
            
    
        #exit button
        self.back_button=load('graphics/buttons/back_button.png').convert_alpha()
        self.back_button_rect=self.back_button.get_rect(center=(33,28))

       
        
    def click(self):
        # print(mouse_pos())
        #play button
        for levelDict in self.level_buttons:
            if levelDict['rect'].collidepoint(mouse_pos()):
                if pygame.mouse.get_pressed()[0]:
                    self.pressed=True
                    self.screen_num=5
                    #self.switchToGame(levelDict['level'])
                else:
                    if self.pressed==True:
                        print('click')
                        self.pressed=False


        #back button
        if self.back_button_rect.collidepoint(mouse_pos()):
            if pygame.mouse.get_pressed()[0]:
                self.screen_num=2
                self.pressed=True
                self.switch()
            else:
                if self.pressed==True:
                    print('click')
                    self.pressed=False
        

    def run(self, dt):
        self.launcher_music.play(loops=-1)
        while True:
            self.events(level_buttons=self.level_buttons,back_button=self.back_button)
            self.click()
            self.update()
            self.draw()
            if self.screen_num==5:
                break
            if self.screen_num==2:
                break
            pygame.display.update()
            #self.clock.tick(ANIMATION_SPEED)
    
    def events(self,level_buttons,back_button):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    for levelDict in self.level_buttons:
                        print(levelDict)
                        if levelDict['rect'].collidepoint(self.mouse_pos):
                            self.launcher_music.stop()
                        
                    if self.back_button_rect.collidepoint(self.mouse_pos):
                        self.launcher_music.stop()
                        # self.switch()
                print(self.mouse_pos)
                

           
        
    
    def update(self):
        self.mouse_pos = mouse_pos()
        

    def draw(self):
        self.display_surface.blit(self.background_2, (0,0))
        x, y = 107, 204
        for levelDict in self.level_buttons:
            levelDict['rect'] = self.display_surface.blit(levelDict['button'], (x,y))
            x += 100
        self.back_button_rect = self.display_surface.blit(self.back_button, (74,75))
        
        #pygame.draw.rect(self.display_surface, (255,0,0), self.level_button_rect, 1)


if __name__ == '__main__':
    # test the launcher
    pygame.init()
    pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    GameLevels().run(dt=0)
    pygame.quit()
    sys.exit()