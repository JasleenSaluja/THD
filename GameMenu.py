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
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.canvas_data = {}
        self.imports()

        self.play_button_pressed = False

        # add cursor
        surf = load('graphics/cursors/mouse.png').convert_alpha()
        cursor = pygame.cursors.Cursor((0,0), surf)
        pygame.mouse.set_cursor(cursor)

        # add music
        self.launcher_music = pygame.mixer.Sound('audio/gamelaunch.ogg')
        
    def imports(self):
        # self.canvas_data['background'] = load('graphics/screen_2.png').convert_alpha() 
        # #self.canvas_data['title'] = load('graphics/launcher/title.png').convert_alpha()
        # self.canvas_data['play_button'] = load('graphics/buttons/play_button.png').convert_alpha()
        # self.canvas_data['play_button_hover'] = load('graphics/buttons/play_button_hover.png').convert_alpha()
        # # self.canvas_data['play_button_pressed'] = load('graphics/launcher/play_button_pressed.png').convert_alpha()
        # self.canvas_data['edit_button'] = load('graphics/buttons/edit_button.png').convert_alpha()
        # self.canvas_data['edit_button_hover'] = load('graphics/buttons/edit_button_hover.png').convert_alpha()
        self.background_2=load('graphics/screen_2.png').convert_alpha()
        self.play_button=load('graphics/buttons/play_button.png').convert_alpha()
        #self.play_button_rect=self.play_button.get_rect(center=(282,433))
        self.play_button_hover=load('graphics/buttons/play_button_hover.png').convert_alpha()
        self.edit_button=load('graphics/buttons/edit_button.png').convert_alpha()
        self.edit_button_hover=load('graphics/buttons/edit_button_hover.png').convert_alpha()
        #self.edit_button_rect=self.edit_button.get_rect(center=(692,433))


    def run(self):
        self.launcher_music.play(loops=-1)
        while True:
            self.events()
            self.update()
            self.draw()
            pygame.display.update()
            #self.clock.tick(ANIMATION_SPEED)
    
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
        # self.edit_button_hover = self.edit_button_rect.collidepoint(self.mouse_pos)
        

        if self.play_button_hover:
            self.play_button = self.play_button_hover
        else:
            self.play_button = self.play_button

        if self.edit_button_hover:
            self.edit_button = self.edit_button_hover
        else:
            self.edit_button = self.edit_button

    def draw(self):
        self.display_surface.blit(self.background_2, (0,0))
        #self.display_surface.blit(self.canvas_data['title'], (0,0))
        self.play_button_rect = self.display_surface.blit(self.play_button, (282,433))
        self.edit_button_rect = self.display_surface.blit(self.edit_button, (692,433))
        
        pygame.draw.rect(self.display_surface, (255,0,0), self.play_button_rect, 1)
        pygame.draw.rect(self.display_surface, (255,0,0), self.edit_button_rect, 1)

if __name__ == '__main__':
    # test the launcher
    pygame.init()
    pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('Launcher')
    Launcher().run()
    pygame.quit()
    sys.exit()

