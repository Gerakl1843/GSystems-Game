# TODO Create Zelda-Type Game
import sys
import pygame
from settings import *
from level import *


class ZeldaGame:

    levels = []

    def __init__(self):
        # general setup
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        self.clock = pygame.time.Clock()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.screen.fill('black')
            pygame.display.update()
            self.clock.tick(FPS)

    def CreateLevel(self, file, name):
        self.levels.append(Level(name))

    def runlevel(self, name):
        for level in self.levels:
            if level.name == name:
                level.run()


if __name__ == '__main__':
    game = ZeldaGame()
    game.run()
