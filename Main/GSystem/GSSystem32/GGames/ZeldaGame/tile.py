import pygame
from settings import *


class Tile(pygame.sprite.Sprite):

    def __init__(self,pos,groups):

        super().__init__(groups)
        self.image = pygame.image.load('../graphics/tiles/rock.bmp')
        self.rect = self.image.get_rect(topleft = pos)
