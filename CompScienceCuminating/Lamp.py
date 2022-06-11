import pygame

class Lamp(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((16, 120))
        self.image.fill('brown')
        self.rect = self.image.get_rect(center = pos)
        
    def update(self, x_shift):
        self.rect.x += x_shift