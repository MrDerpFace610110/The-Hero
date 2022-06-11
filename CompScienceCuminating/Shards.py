import pygame

from Player import Player

class Shard(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((16, 16))
        self.image.fill('yellow')
        self.rect = self.image.get_rect(center = pos)
        
    def update(self, x_shift):
        self.rect.x += x_shift