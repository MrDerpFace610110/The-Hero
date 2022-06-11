import pygame
#import time

from support import import_folder
#from The Hero import dt


clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.rect = self.image.get_rect(topleft = pos)
        self.import_character_assets()
        self.frame_index = 0
        self.animation_speed = 0.010
        self.image = self.animations['Idle'][self.frame_index]
        #elf.rect = self.image.get_rect(topleft = pos)
        
        #playeer move
        self.direction = pygame.math.Vector2(0,0)
        self.speed = 0.000025
        self.gravity = 0.04
        self.jump_speed = -4
        #self.grounded = True
        self.dt = clock.tick(60)
        
        #plays status
        self.status = 'Idle'
        self.crouching = False
        self.facing_right = True
        self.on_ground = False
        self.on_ceiling = False
        self.on_left = False
        self.on_right = False
        self.on_wall = False
        
        self.moving_attack = False
        self.swimming = False
        self.in_cutscene = False
        
        self.idle = True
        self.attack = False
        
    def import_character_assets(self):
        character_path = '../CompScienceCuminating/Ninja_Sprites/'
        self.animations = {'Idle':[],'Moving':[],'Jump':[],'Fall':[], 'Crouch':[], 'Idle_Attack':[], 'Idle_Climb':[], 'Climb_Up':[], 'Climb_Down':[], 'Swim':[], 'Death':[], 'Respawn':[]}
        
        for animation in self.animations.keys():
            full_path = character_path + animation
            self.animations[animation] = import_folder(full_path)
            
    def animate(self):
        animation = self.animations[self.status]
        
        #loop frames
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0
            
        image = animation[int(self.frame_index)]
        if self.facing_right:
            self.image = image
        else:
            flipped_image = pygame.transform.flip(image, True, False)
            self.image = flipped_image
            
        #destroy the collision animations <-- no longer true(mostly) 
            
            if self.on_ground and self.on_right:
                self.rect = self.image.get_rect(bottomright = self.rect.bottomright)
            elif self.on_ground and self.on_left:
                self.rect = self.image.get_rect(bottomleft = self.rect.bottomleft)
            elif self.on_ground:
                self.rect = self.image.get_rect(midbottom = self.rect.midbottom)
            elif self.on_ceiling and self.on_right:
                self.rect = self.image.get_rect(topright = self.rect.topright)
            elif self.on_ceiling and self.on_left:
                self.rect = self.image.get_rect(topleft = self.rect.topleft)
            elif self.on_ceiling:
                self.rect = self.image.get_rect(midtop = self.rect.midtop)
            #elif self.on_wall == True:
                #self.rect = self.image.get_rect(midleft = self.rect.midleft)
                #self.rect = self.image.get_rect(midright = self.rect.midleft)
            elif self.swimming and self.on_ground:
                self.rect = self.image.get_rect(midbottom = self.rect.midbottom)
            elif self.swimming and self.on_ground == False:
                self.rect = self.image.get_rect(midbottom = self.rect.midbottom)
            elif self.swimming == False:
                self.rect = self.image.get_rect(midbottom = self.rect.midbottom)
            elif self.on_wall == True:
                self.rect = self.image.get_rect(center = self.rect.center)
            elif self.on_wall == True and self.on_right == True:
                self.rect = self.image.get_rect(midright = self.rect.midright)
            elif self.on_wall == True and self.on_left == True:
                self.rect = self.image.get_rect(midleft = self.rect.midleft)
                
    def get_input(self):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_d] and self.on_wall == False:
            self.direction.x = 1
            self.Idle = False
            self.facing_right = True
            #print(clock.get_fps())
        elif keys[pygame.K_a] and self.on_wall ==  False:
            self.direction.x = -1
            self.Idle = False
            self.facing_right = False
        elif keys[pygame.K_k]:
            self.attack = True
            self.do_attack()
        else:
            self.direction.x = 0
            self.Idle = True
            
        if keys[pygame.K_SPACE] and self.on_ground and self.swimming == False:
            self.jump()
                #self.grounded = False
                #self.grounded == True
            #wall climb stuff
        elif keys[pygame.K_SPACE] and self.on_wall:
            self.gravity = 0.04
            self.jump()
            self.on_wall = False
                
        if keys[pygame.K_s] and self.on_wall == False:
            self.crouching = True
        else:
            self.crouching = False
            
        if (self.on_right == True or self.on_left == True) and self.on_ground == False and self.swimming == False:
            #self.rect = self.image.get_rect(center = self.rect.center)
            self.on_wall = True
            self.gravity = 0
            self.direction.y = 0
            
        #wall movement
        if keys[pygame.K_w] and self.on_wall == True:
                self.direction.y = -1    
        elif keys[pygame.K_s] and self.on_wall == True:
                self.direction.y = 1
        elif keys[pygame.K_w] == False and self.on_wall == True:
            self.direction.y = 0
            
        #swimming
        if keys[pygame.K_z] and self.swimming == False:
            self.swimming = True
            print(self.swimming)
            #self.rect = self.image.get_rect(midbottom = self.rect.midbottom)
            self.gravity = 0.025
            self.speed = 0.25
        elif keys[pygame.K_z] and self.swimming == True:
            self.swimming = False
            print(self.swimming)
            self.gravity = 0.04
            self.speed = 0.25
        
        if keys[pygame.K_SPACE] and self.swimming == True:
            self.direction.y = -0.5
                
    def get_status(self):
        keys = pygame.key.get_pressed()
        
        if self.direction.y  < 0 and self.on_wall == False and self.swimming == False:
            self.status = 'Jump'
        elif self.direction.y > 1 and self.on_wall == False and self.swimming ==False:
            self.status = 'Fall'
        elif self.crouching == True and self.direction.x == 0 and self.swimming == False:
            self.status = 'Crouch'
        elif self.attack == True and self.Idle == True:
            self.status = 'Idle_Attack'
            if self.Idle == False:
                self.attack = False
            elif self.frame_index >= 3.5:
                self.attack = False
                self.frame_index = 0
            else:
                self.attack = True
            
            #self.attack = False
            #broken :(
        elif self.direction.y < 0 and self.on_wall == True and self.swimming == False:
            self.status = 'Climb_Up'
            print(self.on_left)
        elif self.direction.y > 0 and self.on_wall == True and self.swimming == False:
            self.status = 'Climb_Down'
        #elif (self.on_right == True or self.on_left == True) and self.on_ground == False:
            #self.status = 'Fall'
        elif self.swimming == True:
            self.status = "Swim"
            
        #animation testing
        elif keys[pygame.K_p]:
            self.status = 'Death'
        elif keys[pygame.K_o]:
            self.status = 'Respawn'
        else:
            if self.direction.x != 0:
                self.status = 'Moving'
            elif self.direction.y == 0 and self.on_wall == True:
                self.status = 'Idle_Climb'
            elif self.on_wall == False:
                self.status = 'Idle'
            
    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y
        
    def jump(self):
         self.direction.y = self.jump_speed
         self.rect = self.image.get_rect(midbottom = self.rect.midbottom)
         
    def do_attack(self):
        print('placeholder text')
        
    def cloudstep(self):
        print('cloudstep function, create double jump if this is triggered')
        self.grounded = True
            
    def update(self):
        self.get_input()
        self.get_status()
        self.animate()