import pygame, sys 
from pygame.math import Vector2 as vector

from settings import *
from support import *

from sprites import Generic, Block, Animated, Particle, Coin, Player, Spikes, Zombie, Shell, Cloud

from random import choice, randint
from GameOver import GameOver
from GameWin import GameWin
from editor import CanvasTile

class Level:
    def __init__(self, grid, switch, asset_dict, audio,change_coins):
        self.display_surface = pygame.display.get_surface()
        self.switch = switch

        # groups 
        self.all_sprites = CameraGroup()
        self.coin_sprites = pygame.sprite.Group()
        self.damage_sprites = pygame.sprite.Group()
        self.collision_sprites = pygame.sprite.Group()
        self.shell_sprites = pygame.sprite.Group()
        self.killable_sprites = pygame.sprite.Group() #change
        self.win_sprites = pygame.sprite.Group() #change

        #gameover and gamewin screen
        self.gameover=GameOver() #change
        self.gamewin=GameWin() #change

        self.build_level(grid, asset_dict, audio['jump'])

        # level limits
        self.level_limits = {
        'left': -WINDOW_WIDTH,
        'right': sorted(list(grid['terrain'].keys()), key = lambda pos: pos[0])[-1][0] + 500
        }

        # coins collected- user interface
        self.change_coins=change_coins #change

        # additional stuff
        self.particle_surfs = asset_dict['particle']
        self.cloud_surfs = asset_dict['clouds']
        self.cloud_timer = pygame.USEREVENT + 2
        pygame.time.set_timer(self.cloud_timer, 2000)
        self.startup_clouds()

        # sounds 
        self.bg_music = audio['music']
        self.bg_music.set_volume(1.0)
        self.bg_music.play(loops = -1)

        self.coin_sound = audio['coin']
        self.coin_sound.set_volume(0.3)

        self.hit_sound = audio['hit']
        self.hit_sound.set_volume(0.3)

    def build_level(self, grid, asset_dict, jump_sound):
        for layer_name, layer in grid.items():
            # print(layer_name, layer, "=<")
            for pos, data in layer.items():
                if layer_name == 'terrain':
                    Generic(pos, asset_dict['land'][data], [self.all_sprites, self.collision_sprites])
                if layer_name == 'water':
                    if data == 'top':
                        Animated(asset_dict['water top'], pos, self.all_sprites, LEVEL_LAYERS['water'])
                    else:
                        Generic(pos, asset_dict['water bottom'], self.all_sprites, LEVEL_LAYERS['water'])
                print(data)
                match data:
                    case 0: self.player = Player(pos, asset_dict['player'], self.all_sprites, self.collision_sprites, jump_sound)
                    case 1: 
                        try:
                            self.horizon_y = pos[1]
                        except Exception as e:
                            print(e)
                            self.horizon_y = 20
                        self.all_sprites.horizon_y = pos[1]
                    # coins
                    case 4: Coin('gold', asset_dict['gold'], pos, [self.all_sprites, self.coin_sprites],50) #change
                    case 5: Coin('silver', asset_dict['silver'], pos, [self.all_sprites, self.coin_sprites],25) #change
                    case 6: Coin('diamond', asset_dict['diamond'], pos, [self.all_sprites, self.coin_sprites],15) #change

                    # enemies
                    case 7: Spikes(asset_dict['spikes'], pos, [self.all_sprites, self.damage_sprites])
                    case 8: 
                        Zombie(asset_dict['zombie'], pos, [self.all_sprites, self.damage_sprites,self.killable_sprites], self.collision_sprites) #change
                    case 9: 
                        Shell(
                            orientation = 'left', 
                            assets = asset_dict['shell'], 
                            pos =  pos, 
                            group =  [self.all_sprites, self.collision_sprites, self.shell_sprites],
                            pearl_surf = asset_dict['pearl'],
                            damage_sprites = self.damage_sprites)
                    case 10: 
                        Shell(
                            orientation = 'right', 
                            assets = asset_dict['shell'], 
                            pos =  pos, 
                            group =  [self.all_sprites, self.collision_sprites, self.shell_sprites],
                            pearl_surf = asset_dict['pearl'],
                            damage_sprites = self.damage_sprites)

                    # palm trees
                    case 11: 
                        Animated(asset_dict['obstacles']['small_fg'], pos, self.all_sprites)
                        Block(pos, (76,50), self.collision_sprites)
                    case 12: 
                        Animated(asset_dict['obstacles']['tree'], pos, self.all_sprites)
                        #Block(pos, (76,50), self.collision_sprites)
                    case 13: 

                        Animated(asset_dict['obstacles']['skeleton'], pos, self.all_sprites)
                        Block(pos, (42,32), self.collision_sprites)
                    case 14: 
                        Animated(asset_dict['obstacles']['crate'], pos, self.all_sprites)
                        Block(pos, (64,64), self.collision_sprites)
                        #Block(pos + vector(50,0), (76,50), self.collision_sprites)
                    
                    case 15: Animated(asset_dict['obstacles']['small_bg'], pos,[ self.all_sprites,self.win_sprites], LEVEL_LAYERS['bg']) #change
                    case 16: Animated(asset_dict['obstacles']['large_bg'], pos, [self.all_sprites,self.win_sprites], LEVEL_LAYERS['bg']) #change
                    case 17: Animated(asset_dict['obstacles']['left_bg'], pos, [self.all_sprites,self.win_sprites], LEVEL_LAYERS['bg']) #change
                    case 18: Animated(asset_dict['obstacles']['right_bg'], pos, [self.all_sprites,self.win_sprites], LEVEL_LAYERS['bg']) #change

        for sprite in self.shell_sprites:
            sprite.player = self.player

    def get_coins(self):
        collided_coins = pygame.sprite.spritecollide(self.player, self.coin_sprites, True)
        for sprite in collided_coins:
            self.coin_sound.play()
            self.change_coins(sprite.value)   # coins collected  #change
            Particle(self.particle_surfs, sprite.rect.center, self.all_sprites)

    def get_damage(self):
        collision_sprites = pygame.sprite.spritecollide(self.player, self.damage_sprites, False, pygame.sprite.collide_mask)
        if collision_sprites:
            self.hit_sound.play()
            self.player.damage()
            self.bg_music.stop()
            self.switch()
            self.bg_music.stop()
            # self.gameover.run(dt=0)  #change
            #self.player.kill()
            # pygame.quit()
            # exit()

    #if player falls off ground
    def check_death(self):
        if self.player.rect.top > WINDOW_HEIGHT:
            self.bg_music.stop()
            #self.gameover.run(dt=0)
            self.switch()
            self.bg_music.stop()


    #player wins- if the player collides with the win board
    # def check_win(self):#change
    # 	if pygame.sprite.spritecollide(self.player, self.win_sprites,True):
    # 		self.bg_music.stop()
    # 		self.gamewin.run(dt=0)
            # pygame.quit()
            # exit()

    def create_grid(self):
        
        # add objects to the tiles

        for tile in self.canvas_data.values():
            tile.objects = []

        for obj in self.canvas_objects:
            current_cell = self.get_current_cell(obj)
            offset = vector(obj.distance_to_origin) - (vector(current_cell) * TILE_SIZE)

            if current_cell in self.canvas_data: # tile exists already
                self.canvas_data[current_cell].add_id(obj.tile_id, offset)
            else: # no tile exists yet 
                self.canvas_data[current_cell] = CanvasTile(obj.tile_id, offset)

        # create an empty grid
        layers = {
            'water': {},
            'obstacle': {},
            'terrain': {}, 
            'enemies': {},
            'coins': {}, 
            'fg objects': {},
        }

        # grid offset 
        left = sorted(self.canvas_data.keys(), key = lambda tile: tile[0])[0][0]
        top = sorted(self.canvas_data.keys(), key = lambda tile: tile[1])[0][1]

        # fill the grid
        for tile_pos, tile in self.canvas_data.items():
            row_adjusted = tile_pos[1] - top
            col_adjusted = tile_pos[0] - left
            x = col_adjusted * TILE_SIZE
            y = row_adjusted * TILE_SIZE

            if tile.has_water:
                layers['water'][(x,y)] = tile.get_water()

            if tile.has_terrain:
                layers['terrain'][(x,y)] = tile.get_terrain() if tile.get_terrain() in self.land_tiles else 'X'

            if tile.coin:
                layers['coins'][(x + TILE_SIZE // 2,y + TILE_SIZE // 2)] = tile.coin

            if tile.enemy:
                layers['enemies'][x,y] = tile.enemy

            if tile.objects: # (obj, offset)
                for obj, offset in tile.objects:
                    if obj in [key for key, value in EDITOR_DATA.items() if value['style'] == 'obstacle']: # bg palm
                        layers['obstacle'][(int(x + offset.x), int(y + offset.y))] = obj
                    else: # fg objects
                        layers['fg objects'][(int(x + offset.x), int(y + offset.y))] = obj
        return layers
     
    def event_loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.switch()
                self.bg_music.stop()

            if event.type == self.cloud_timer:
                surf = choice(self.cloud_surfs)
                surf = pygame.transform.scale2x(surf) if randint(0,5) > 3 else surf
                x = self.level_limits['right'] + randint(100,300)
                y = self.horizon_y - randint(-50,600)
                Cloud((x,y), surf, self.all_sprites, self.level_limits['left'])

    def startup_clouds(self):
        for i in range(40):
            surf = choice(self.cloud_surfs)
            surf = pygame.transform.scale2x(surf) if randint(0,5) > 3 else surf
            x = randint(self.level_limits['left'], self.level_limits['right'])
            try:
                y = self.horizon_y - randint(-50,600)
            except:
                self.horizon_y = 20
                y = self.horizon_y - randint(-50,600)
            Cloud((x,y), surf, self.all_sprites, self.level_limits['left'])

    def run(self, dt):
        # update
        self.event_loop()
        self.all_sprites.update(dt)
        self.get_coins()
        # self.zombie_kill() #change
        self.get_damage()
        self.check_death()
        # self.check_win()

        # drawing
        self.display_surface.fill(SKY_COLOR)
        self.all_sprites.custom_draw(self.player)

class CameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.offset = vector()

    def draw_horizon(self):
        horizon_pos = self.horizon_y - self.offset.y	

        if horizon_pos < WINDOW_HEIGHT:
            sea_rect = pygame.Rect(0,horizon_pos,WINDOW_WIDTH,WINDOW_HEIGHT - horizon_pos)
            pygame.draw.rect(self.display_surface, SEA_COLOR, sea_rect)

            # horizon line 
            # 3 extra rectangles 
            horizon_rect1 = pygame.Rect(0,horizon_pos - 10,WINDOW_WIDTH,10)
            horizon_rect2 = pygame.Rect(0,horizon_pos - 16,WINDOW_WIDTH,4)
            horizon_rect3 = pygame.Rect(0,horizon_pos - 20,WINDOW_WIDTH,2)
            pygame.draw.rect(self.display_surface, HORIZON_TOP_COLOR, horizon_rect1)
            pygame.draw.rect(self.display_surface, HORIZON_TOP_COLOR, horizon_rect2)
            pygame.draw.rect(self.display_surface, HORIZON_TOP_COLOR, horizon_rect3)
            pygame.draw.line(self.display_surface, HORIZON_COLOR, (0,horizon_pos), (WINDOW_WIDTH,horizon_pos), 3)

        if horizon_pos < 0:
            self.display_surface.fill(SEA_COLOR)

    def custom_draw(self, player):
        self.offset.x = player.rect.centerx - WINDOW_WIDTH / 2
        self.offset.y = player.rect.centery - WINDOW_HEIGHT / 2

        for sprite in self:
            if sprite.z == LEVEL_LAYERS['clouds']:
                offset_rect = sprite.rect.copy()
                offset_rect.center -= self.offset
                self.display_surface.blit(sprite.image, offset_rect)

        self.draw_horizon()
        for sprite in self:
            for layer in LEVEL_LAYERS.values():
                if sprite.z == layer and sprite.z != LEVEL_LAYERS['clouds']:
                    offset_rect = sprite.rect.copy()
                    offset_rect.center -= self.offset
                    self.display_surface.blit(sprite.image, offset_rect)