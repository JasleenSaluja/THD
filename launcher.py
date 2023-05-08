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

class Launcher():
    def __init__(self, screen_num=1, delay = 100, stm=None):
        self.screen_num = screen_num 
        self.display_surface = pygame.display.get_surface()
        self.canvas_data = {}
        # initialize a five second timer
        self.time = delay
        self.imports()
        self.switch_to_menu = stm
        # add cursor
        surf = load('graphics/cursors/mouse.png').convert_alpha()
        cursor = pygame.cursors.Cursor((0,0), surf)
        pygame.mouse.set_cursor(cursor)

        # add music
        self.launcher_music = pygame.mixer.Sound('audio/gamelaunch.ogg')
        
    def imports(self):
        self.canvas_data['background'] = load('graphics/screen_1.png').convert_alpha() 
        # self.canvas_data['title'] = load('graphics/launcher/title.png').convert_alpha()
    #     self.canvas_data['play_button'] = load('graphics/buttons/play_button.png').convert_alpha()
    #     self.canvas_data['play_button_hover'] = load('graphics/buttons/play_button_hover.png').convert_alpha()
    #     # self.canvas_data['play_button_pressed'] = load('graphics/launcher/play_button_pressed.png').convert_alpha()
    #     self.canvas_data['quit_button'] = load('graphics/buttons/edit_button.png').convert_alpha()
    #     self.canvas_data['quit_button_hover'] = load('graphics/buttons/edit_button_hover.png').convert_alpha()


    def run(self, dt):
        self.launcher_music.play(loops=-1)
        while True:
            self.events()
            self.update()
            self.draw()
            pygame.display.update()
            print(self.time)
            self.time -= 1

            # if timer is done, break out of loop
            if self.time < 0:
                self.launcher_music.stop()
                self.screen_num = 2
                break
        self.switch_to_menu()
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # if event.type == pygame.MOUSEBUTTONDOWN:
            #     if event.button == 1:
            #         self.play_button_pressed = True

            # if event.type == pygame.MOUSEBUTTONUP:
            #     if event.button == 1:
            #         self.play_button_pressed = False
        
        # if self.play_button_pressed:
        #     self.launcher_music.stop()
        #     self.play_button_pressed = False
        #     self.play_button_hover = False
        #     self.play_button_pressed = False
    
    def update(self):
        self.mouse_pos = mouse_pos()
        # self.play_button_hover = self.play_button_rect.collidepoint(self.mouse_pos)
        # self.quit_button_hover = self.quit_button_rect.collidepoint(self.mouse_pos)

        # if self.play_button_hover:
        #     self.play_button = self.canvas_data['play_button_hover']
        # else:
        #     self.play_button = self.canvas_data['play_button']

        # if self.quit_button_hover:
        #     self.quit_button = self.canvas_data['quit_button_hover']
        # else:
        #     self.quit_button = self.canvas_data['quit_button']

    def draw(self):
        self.display_surface.blit(self.canvas_data['background'], (0,0))
        # self.display_surface.blit(self.canvas_data['title'], (0,0))
        # self.play_button_rect = self.display_surface.blit(self.play_button, (0,0))
        # self.quit_button_rect = self.display_surface.blit(self.quit_button, (0,0))

        # pygame.draw.rect(self.display_surface, (255,0,0), self.play_button_rect, 1)
        # pygame.draw.rect(self.display_surface, (255,0,0), self.quit_button_rect, 1)

if __name__ == '__main__':
    # test the launcher
    pygame.init()
    pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('Launcher')
    clock = pygame.time.Clock()
    dt = clock.tick() / 1000
    Launcher().run(dt)
    pygame.quit()
    sys.exit()

