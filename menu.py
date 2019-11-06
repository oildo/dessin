import pygame

class Menu(pygame.Surface):
    """docstring for Menu."""

    def __init__(self, fenetre, color, x, y, width, height):
        super().__init__((width, height))
        self.fenetre = fenetre
        self.color = color
        self.x = x
        self.y = y

    def draw(self):
        self.fill((50, 94, 192))
        self.fenetre.blit(self, (self.x, self.y))
