import pygame


class Level:

    name = None

    def __init__(self, name):

        self.name = name
        self.visible_sprites = pygame.sprite.Group()
        self.obstacles_sprites = pygame.sprite.Group()

    def run(self):
        pass
