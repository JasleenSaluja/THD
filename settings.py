# general setup
TILE_SIZE = 64
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
ANIMATION_SPEED = 8

# editor graphics 
EDITOR_DATA = {
	0: {'style': 'player', 'type': 'object', 'menu': None, 'menu_surf': None, 'preview': None, 'graphics': 'graphics/player_1/idle_right'},
	1: {'style': 'sky',    'type': 'object', 'menu': None, 'menu_surf': None, 'preview': None, 'graphics': None},
	
	2: {'style': 'terrain', 'type': 'tile', 'menu': 'terrain', 'menu_surf': 'graphics/menu/land_1.png',  'preview': 'graphics/preview/land_1.png',  'graphics': None},
	3: {'style': 'water',   'type': 'tile', 'menu': 'terrain', 'menu_surf': 'graphics/menu/water.png', 'preview': 'graphics/preview/water.png', 'graphics': 'graphics/terrain/water/animation'},
	
	4: {'style': 'coin', 'type': 'tile', 'menu': 'coin', 'menu_surf': 'graphics/menu/gold.png',    'preview': 'graphics/preview/gold.png',    'graphics': 'graphics/items/gold'},
	5: {'style': 'coin', 'type': 'tile', 'menu': 'coin', 'menu_surf': 'graphics/menu/silver.png',  'preview': 'graphics/preview/silver.png',  'graphics': 'graphics/items/silver'},
	6: {'style': 'coin', 'type': 'tile', 'menu': 'coin', 'menu_surf': 'graphics/menu/diamond.png', 'preview': 'graphics/preview/diamond.png', 'graphics': 'graphics/items/diamond'},

	7:  {'style': 'enemy', 'type': 'tile', 'menu': 'enemy', 'menu_surf': 'graphics/menu/spikes.png',      'preview': 'graphics/preview/spikes.png',      'graphics': 'graphics/enemies/spikes'},
	8:  {'style': 'enemy', 'type': 'tile', 'menu': 'enemy', 'menu_surf': 'graphics/menu/zombie.png',       'preview': 'graphics/preview/zombie.png',       'graphics': 'graphics/enemies/zombie/idle'},
	9:  {'style': 'enemy', 'type': 'tile', 'menu': 'enemy', 'menu_surf': 'graphics/menu/shell_left.png',  'preview': 'graphics/preview/shell_left.png',  'graphics': 'graphics/enemies/shell_left/idle'},
	10: {'style': 'enemy', 'type': 'tile', 'menu': 'enemy', 'menu_surf': 'graphics/menu/shell_right.png', 'preview': 'graphics/preview/shell_right.png', 'graphics': 'graphics/enemies/shell_right/idle'},
	
	11: {'style': 'palm_fg', 'type': 'object', 'menu': 'palm fg', 'menu_surf': 'graphics/menu/small_fg.png', 'preview': 'graphics/preview/small_fg.png', 'graphics': 'graphics/terrain/obstacles/small_fg'},
	12: {'style': 'palm_fg', 'type': 'object', 'menu': 'palm fg', 'menu_surf': 'graphics/menu/tree.png', 'preview': 'graphics/preview/tree.png', 'graphics': 'graphics/terrain/obstacles/tree'},
	13: {'style': 'palm_fg', 'type': 'object', 'menu': 'palm fg', 'menu_surf': 'graphics/menu/skeleton.png',  'preview': 'graphics/preview/skeleton.png',  'graphics': 'graphics/terrain/obstacles/skeleton'},
	14: {'style': 'palm_fg', 'type': 'object', 'menu': 'palm fg', 'menu_surf': 'graphics/menu/crate.png', 'preview': 'graphics/preview/crate.png', 'graphics': 'graphics/terrain/obstacles/crate'},

	15: {'style': 'obstacle', 'type': 'object', 'menu': 'obstacle', 'menu_surf': 'graphics/menu/win_board.png', 'preview': 'graphics/preview/win_board.png', 'graphics': 'graphics/terrain/obstacles/small_bg'},
	16: {'style': 'obstacle', 'type': 'object', 'menu': 'obstacle', 'menu_surf': 'graphics/menu/win_board.png', 'preview': 'graphics/preview/win_board.png', 'graphics': 'graphics/terrain/obstacles/large_bg'},
	17: {'style': 'obstacle', 'type': 'object', 'menu': 'obstacle', 'menu_surf': 'graphics/menu/win_board.png',  'preview': 'graphics/preview/win_board.png',  'graphics': 'graphics/terrain/obstacles/left_bg'},
	18: {'style': 'obstacle', 'type': 'object', 'menu': 'obstacle', 'menu_surf': 'graphics/menu/win_board.png', 'preview': 'graphics/preview/win_board.png', 'graphics': 'graphics/terrain/obstacles/right_bg'},
}

NEIGHBOR_DIRECTIONS = {
	'A': (0,-1),
	'B': (1,-1),
	'C': (1,0),
	'D': (1,1),
	'E': (0,1),
	'F': (-1,1),
	'G': (-1,0),
	'H': (-1,-1)
}

LEVEL_LAYERS = {
	'clouds': 1,
	'ocean': 2,
	'bg': 3,
	'water': 4,
	'main': 5
}

# colors 
SKY_COLOR = '#041A40'
SEA_COLOR = '#92a9ce'
HORIZON_COLOR = '#67BFC7'
HORIZON_TOP_COLOR = '#0470A7'
LINE_COLOR = 'black'
BUTTON_BG_COLOR = '#33323d'
BUTTON_LINE_COLOR = '#f5f1de'