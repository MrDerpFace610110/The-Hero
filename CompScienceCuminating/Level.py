import pygame
from support import import_csv_layout, import_cut_graphics
from settings import tile_size
from tiles import Tile, StaticTile, Coin
from GreenKappa import GKappa
from Player import Player

class Level1:
    def __init__(self, level_data, surface):
        #setup
        self.display_surface = surface
        self.world_shift = 0
        
        #player
        player_layout = import_csv_layout(level_data['Player'])
        self.player = pygame.sprite.GroupSingle()
        self.goal = pygame.sprite.GroupSingle()
        self.player_setup(player_layout)
        
        #terrain setup
        terrain_layout = import_csv_layout(level_data['Ground'])
        self.terrain_sprites = self.create_tile_group(terrain_layout, 'Ground')
        
        #grass setup
        grass_layout = import_csv_layout(level_data['Grass'])
        self.grass_sprites = self.create_tile_group(grass_layout, 'Grass')
        
        #shards
        coin_layout = import_csv_layout(level_data['Shards'])
        self.coin_sprites = self.create_tile_group(coin_layout, 'Shards')
        
        #enemy
        gkappa_layout = import_csv_layout(level_data['GreenKappa'])
        self.gkappa_sprites = self.create_tile_group(gkappa_layout, 'GreenKappa')
        
        #enemys stop
        constraint_layout = import_csv_layout(level_data['GreenKappaConstraint'])
        self.constraint_sprites = self.create_tile_group(constraint_layout, 'GreenKappaConstraint')
        
    def create_tile_group(self, layout, type):
        sprite_group = pygame.sprite.Group()
        
        for row_index, row in enumerate(layout):
            for col_index, val in enumerate(row):
                if val != '-1':
                    x = col_index * tile_size
                    y = row_index * tile_size
                    
                    if type == 'Ground':
                        terrain_tile_list = import_cut_graphics('../CompScienceCuminating/Tile_sets/AutumnHillsTileset_8.png')
                        tile_surface = terrain_tile_list[int(val)]
                        sprite = StaticTile(tile_size, x, y, tile_surface)
                        
                    if type == 'Grass':
                        grass_tile_list = import_cut_graphics('../CompScienceCuminating/Tile_sets/AutumnHillsTileset_8.png')
                        tile_surface = grass_tile_list[int(val)]
                        sprite = StaticTile(tile_size, x, y, tile_surface)
                        
                    if type == 'Shards':
                        sprite = Coin(tile_size, x, y, '../CompScienceCuminating/Shards')
                        
                    if type == 'GreenKappa':
                        sprite =  GKappa(tile_size, x, y)
                        
                    if type == 'GreenKappaConstraint':
                        sprite = Tile(tile_size , x ,y - 20)
                        
                    sprite_group.add(sprite)
        
        return sprite_group
    
    def player_setup(self, layout):
        for row_index, row in enumerate(layout):
            for col_index, val in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size
                
                if val == '0':
                    sprite = Player((x,y))
                    self.player.add(sprite)
                if val == '1':
                    print('goal')
                    goal_surface = pygame.image.load('../CompScienceCuminating/TestTile.png')
                    sprite = StaticTile(tile_size, x, y, goal_surface)
                    self.goal.add(sprite)
    
    def enemy_coll_rev(self):
        for greenKap in self.gkappa_sprites.sprites():
            if pygame.sprite.spritecollide(greenKap, self.constraint_sprites, False):
                greenKap.reverse()
                
    def hori_move_collision(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed
        
        for sprite in self.terrain_sprites.sprites():
            #do + for more layers
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                    player.on_left = True
                    self.current_x = player.rect.left
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left
                    player.on_right = True
                    self.current_x = player.rect.right
                    
        if player.on_left and (player.rect.left < self.current_x or player.direction.x >= 0):
            player.on_left = False
            
        if player.on_right and (player.rect.right > self.current_x or player.direction.x <= 0):
            player.on_right = False
                    
    def vert_move_collision(self):
        player = self.player.sprite
        player.apply_gravity()
        
        for sprite in self.terrain_sprites.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    #player.grounded = True
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                    player.on_ground = True
                elif player.direction.y < 0:
                    # player.grounded = False
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0
                    player.on_ceiling = True
                   
        if player.on_ground and player.direction.y < 0 or player.direction.y > 1:
            player.on_ground = False
            
        if player.on_ceiling and player.direction. y > 0:
            player.on_ceiling = False
        
    def run(self):
        #rungame
        self.terrain_sprites.draw(self.display_surface)
        self.terrain_sprites.update(self.world_shift)
        #self.display_surface.fill('purple')
        
        self.grass_sprites.draw(self.display_surface)
        self.grass_sprites.update(self.world_shift)
        
        #coins
        self.coin_sprites.draw(self.display_surface)
        self.coin_sprites.update(self.world_shift)
        
        #Green Kappa
        self.gkappa_sprites.update(self.world_shift)
        self.constraint_sprites.update(self.world_shift)
        #self.constraint_sprites.draw(self.display_surface)
        self.enemy_coll_rev()
        self.gkappa_sprites.draw(self.display_surface)
        
        #player 
        self.player.update()
        self.hori_move_collision()
        self.vert_move_collision()
        self.player.draw(self.display_surface)
        self.goal.update(self.world_shift)
        self.goal.draw(self.display_surface)
        