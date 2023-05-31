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
from editor import CanvasTile

class GameLevels:
    def __init__(self, screen_num=4, switch=None,stm=None,stg=None,):
        self.screen_num = screen_num
        self.display_surface = pygame.display.get_surface()
       
       
        # download_all_levels()
        self.canvas_objects = pygame.sprite.Group()
        self.foreground = pygame.sprite.Group()
        self.background = pygame.sprite.Group()
        
        self.switch= switch
        self.switchToMenu=stm
        self.imports()
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
            
    
        #exit button
        self.back_button=load('graphics/buttons/back_button.png').convert_alpha()
        self.back_button_rect=self.back_button.get_rect(center=(33,28))

        # terrain
        self.land_tiles = import_folder_dict('graphics/terrain/land_1')
        self.water_bottom = load('graphics/terrain/water/water_bottom.png').convert_alpha()
        self.water_top_animation = import_folder('graphics/terrain/water/animation')

        # coins
        self.gold = import_folder('graphics/items/gold')
        self.silver = import_folder('graphics/items/silver')
        self.diamond = import_folder('graphics/items/diamond')
        self.particle = import_folder('graphics/items/particle')

        # palm trees
        self.obstacles = {folder: import_folder(f'graphics/terrain/obstacles/{folder}') for folder in list(walk('graphics/terrain/obstacles'))[0][1]}

        # enemies
        self.spikes = load('graphics/enemies/spikes/spikes.png').convert_alpha()
        self.zombie = {folder: import_folder(f'graphics/enemies/zombie/{folder}') for folder in list(walk('graphics/enemies/zombie'))[0][1]}
        self.shell = {folder: import_folder(f'graphics/enemies/shell_left/{folder}') for folder in list(walk('graphics/enemies/shell_left/'))[0][1]}
        self.pearl = load('graphics/enemies/pearl/pearl.png').convert_alpha()

        # player
        self.player_graphics = {folder: import_folder(f'graphics/player_1/{folder}') for folder in list(walk('graphics/player_1/'))[0][1]}

        # clouds
        self.clouds = import_folder('graphics/clouds')

        # sounds
        self.level_sounds = {
            'coin': pygame.mixer.Sound('audio/coin.wav'),
            'hit': pygame.mixer.Sound('audio/hit.wav'),
            'jump': pygame.mixer.Sound('audio/jump.wav'),
            'music': pygame.mixer.Sound('audio/SuperHero.ogg'),
        }
        
    
    def setup_levels(self):
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
            x += 300
    
        
    def click(self):
        for levelDict in self.level_buttons:
            if levelDict['rect'].collidepoint(mouse_pos()):
                if pygame.mouse.get_pressed()[0]:
                    self.pressed=True
                    self.screen_num=5
                    level_file = f'levels/{levelDict["level"]}'
                    print(f'level => {levelDict["level"]}')
                    with open(level_file, 'rb') as f:
                        self.grid = pickle.load(f)
                        # print(self.canvas_data)
                        self.switch(self.grid)
                else:
                    if self.pressed==True:
                        print('click')
                        self.pressed=False


        #back button
        if self.back_button_rect.collidepoint(mouse_pos()):
            if pygame.mouse.get_pressed()[0]:
                self.screen_num=2
                self.pressed=True
                self.switchToMenu
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
            x += 250
        self.back_button_rect = self.display_surface.blit(self.back_button, (74,75))
        
        #pygame.draw.rect(self.display_surface, (255,0,0), self.level_button_rect, 1)


if __name__ == '__main__':
    # test the launcher
    pygame.init()
    pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    GameLevels().run(dt=0)
    pygame.quit()
    sys.exit()