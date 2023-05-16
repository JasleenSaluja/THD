import pygame
from pygame.math import Vector2 as vector
from settings import *
from support import *

from pygame.image import load

from editor import Editor
from level import Level
from launcher import  Launcher
from GameMenu import GameMenu 
from GameLevels import GameLevels	

from os import walk

class Main:

	screen_num = 1

	def __init__(self):
		pygame.init()
		self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
		pygame.display.set_caption('The Hungry Dead')
		self.clock = pygame.time.Clock()
		self.imports()
		self.editor_active = False
		self.transition = Transition(self.toggle)
		self.launcher = Launcher(self.screen_num, 10, self.switchToMenu)
		self.gamemenu = GameMenu(self.screen_num, self.switch_to_editor, self.switch_to_level)
		self.editor = Editor(self.land_tiles, self.switch)
		self.gamelevels=GameLevels(self.screen_num,self.switchToMenu,self.switchtoGame)
		#self.level = Level(self.screen_num, self.switch,self.level_sounds,self.switch)
		surf = load('graphics/cursors/mouse.png').convert_alpha()
		cursor = pygame.cursors.Cursor((0,0), surf)
		pygame.mouse.set_cursor(cursor)

	def imports(self):
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

	def toggle(self):
		# 4 state switch
		if self.screen_num == 1:
			pass
		elif self.screen_num == 2:
			pass
		elif self.screen_num == 3:
			if self.editor_active:
				self.editor.editor_music.play()		
		elif self.screen_num == 4:
			pass
		elif self.screen_num == 5:
			self.level.bg_music.play()
		

	def switchToMenu(self):
		print("switching to menu")
		self.screen_num = 2

	def switch_to_editor(self):
		#print("switching to editor")
		self.screen_num = 3
		self.editor_active = True
	
	def switch_to_level(self):  #for the levels page
		print("switching to level")
		self.screen_num = 4

	def switchtoGame(self): # for the actual level
		self.screen_num = 5

		
		
	

	def switch(self, grid = None):
		self.screen_num = 5
		self.transition.active = True
		if grid:
			self.level = Level(
				grid, 
				self.switch,{
					'land': self.land_tiles,
					'water bottom': self.water_bottom,
					'water top': self.water_top_animation,
					'gold': self.gold,
					'silver': self.silver,
					'diamond': self.diamond,
					'particle': self.particle,
					'obstacles': self.obstacles,
					'spikes': self.spikes,
					'zombie': self.zombie,
					'shell': self.shell,
					'player': self.player_graphics,
					'pearl': self.pearl,
					'clouds': self.clouds},
				self.level_sounds)
		else:
			pass
			
	def run(self):
		while True:
			dt = self.clock.tick() / 1000
			print(f'dt: {dt}, screen = {self.screen_num}')
			if self.screen_num == 1:
				self.launcher.run(dt)
			elif self.screen_num == 2:
				self.gamemenu.run(dt)
			elif self.screen_num == 3:
				self.editor.run(dt)
			elif self.screen_num == 4 :
				self.gamelevels.run(dt)	
			elif self.screen_num == 5:
				self.level.run(dt)
			self.transition.display(dt)
			pygame.display.update()



class Transition:
	def __init__(self, toggle):
		self.display_surface = pygame.display.get_surface()
		self.toggle = toggle
		self.active = False

		self.border_width = 0
		self.direction = 1
		self.center = (WINDOW_WIDTH /2, WINDOW_HEIGHT / 2)
		self.radius = vector(self.center).magnitude()
		self.threshold = self.radius + 100

	def display(self, dt):
		if self.active:
			self.border_width += 1000 * dt * self.direction
			if self.border_width >= self.threshold:
				self.direction = -1
				self.toggle()
			
			if self.border_width < 0:
				self.active = False
				self.border_width = 0
				self.direction = 1
			pygame.draw.circle(self.display_surface, 'black',self.center, self.radius, int(self.border_width))

if __name__ == '__main__':
	main = Main()
	main.run() 