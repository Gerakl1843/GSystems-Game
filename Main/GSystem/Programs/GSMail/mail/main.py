import pygame


class Mail:

    def __init__(self):
        pygame.init()
        self.wn = pygame.display.set_mode((1280,720))
        pygame.display.set_caption('GSmail')
        self.button_number = 2

    def run(self):
        self.wn.fill('black')
        while True:
            self.DrawMenu()
            pygame.display.update()

    def DrawMenu(self):
        menu_rect = pygame.Rect()
        pygame.draw.rect(self.wn, (200, 200, 200), menu_rect)
        for num in range(1,self.button_number):
            pygame.draw.line(self.wn, 'black', (0, num*10), (320, num*10))


m = Mail()
m.run()
