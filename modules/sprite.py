import pygame

from modules.constants import *
from modules.object import Object

class Sprite(pygame.sprite.Sprite):
    def __init__(self, object: Object):
        pygame.sprite.Sprite.__init__(self)
        self.object = object

        self.update_image()

    def update(self):
        self.update_image()
    
    def update_image(self):
        self.image = pygame.Surface((CELL_WIDTH, CELL_HEIGHT))
        self.image.set_colorkey(BLACK)
        pygame.draw.rect(self.image, self.object.color, self.image.get_rect(), 2)
        self.rect = self.image.get_rect()

        self._draw_hp()

        self.rect.topleft = (self.object.x * CELL_WIDTH, self.object.y * CELL_HEIGHT)

    def _draw_hp(self):
        font = pygame.font.SysFont('Arial', 7)
        hpSurf = font.render(str(int(self.object.hp)), False, WHITE)
        self.image.blit(hpSurf, (2, 2))

