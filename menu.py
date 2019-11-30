import pygame

class Menu(pygame.Surface):
    """docstring for Menu."""

    def __init__(self, fenetre, couleur_fond, x, y, width, height):
        super().__init__((width, height))
        self.fenetre = fenetre
        self.couleur_fond = couleur_fond
        self.x = x
        self.y = y

        """pas de couleur"""            # -1
        self.noir = (0, 0, 0)           # 0
        self.rouge = (255, 0, 0)        # 1
        self.vert = (0, 255, 0)         # 2
        self.bleu = (0, 0, 255)         # 3
        self.jaune = (255, 255, 0)      # 4

        self.couleur = [
        self.noir, self.rouge, self.vert,
        self.bleu, self.jaune
        ]

        self.pointeur_couleur = (255, 255, 255)

        self.selected = 0
        self.marge = 10

    def draw(self):
        self.fill(self.couleur_fond)
        dim_rect = [int(self.get_width() - self.get_width()/10), int(self.get_height()/len(self.couleur))]
        i = 0
        while i <= 4:
            if not i == self.selected:
                pygame.draw.rect(self, self.couleur[i], (0, i * dim_rect[1], dim_rect[0], dim_rect[1]))
            else:
                pygame.draw.rect(self, self.pointeur_couleur, (0, i * dim_rect[1], dim_rect[0], dim_rect[1]))
                pygame.draw.rect(self, self.couleur[i], (self.marge, i * dim_rect[1] + self.marge , dim_rect[0] - self.marge * 2, dim_rect[1] - self.marge * 2))
            i+=1
        self.fenetre.blit(self, (self.x, self.y))

    def which_case(self, position):
        dim_rect = [int(self.get_width() - self.get_width()/10), int(self.get_height()/len(self.couleur))]
        if position[0] <= self.get_width():
            return int(position[1] / dim_rect[1])
            # return int(self.get_height() / dim_rect[1])
        else:
            return -1

    def set_cursor(self, emplacement):
        self.selected = emplacement













#choing
