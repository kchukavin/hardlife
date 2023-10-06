import pygame

import modules.constants as constants
from modules.object import Object

class Sprite(pygame.sprite.Sprite):
    def __init__(self, object: Object):
        pygame.sprite.Sprite.__init__(self)
        self.object = object

        self.image = pygame.Surface((constants.CELL_WIDTH, constants.CELL_HEIGHT))
        self.image.set_colorkey(constants.BLACK)
        pygame.draw.rect(self.image, self.object.color, self.image.get_rect(), 2)
        self.rect = self.image.get_rect()

        self.update_position()

    def update(self):
        self.update_position()
    
    def update_position(self):
        self.rect.topleft = (self.object.x * constants.CELL_WIDTH, self.object.y * constants.CELL_HEIGHT)
