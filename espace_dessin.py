import pygame

#-------------------------------------------------------------------------------
NOIR = 0
BLANC = 1
ROUGE = 2
VERT = 3
BLEU = 4
JAUNE = 5
#-------------------------------------------------------------------------------

class Tableau(pygame.Surface):
    """docstring for Tableau."""

    def __init__(self, fenetre, x, y, width, height):
        super().__init__((width, height))
        self.fenetre = fenetre
        self.x = x
        self.y = y

        self.noir = (0, 0, 0)           # 0
        self.blanc = (255, 255, 255)    # 1
        self.rouge = (255, 0, 0)        # 2
        self.vert = (0, 255, 0)         # 3
        self.bleu = (0, 0, 255)         # 4
        self.jaune = (255, 255, 0)      # 5

        self.couleur = [
        self.noir, self.blanc, self.rouge,
        self.vert, self.bleu, self.jaune
        ]

        self.couleur_fond = self.blanc
        self.couleur_pinceau = self.noir
        self.rad_pinceau = 7  # rayon du pinceau

        self.fill(self.couleur_fond)
#-------------------------------------------------------------------------------
    def effacer(self):
        self.fill(self.couleur_fond)

    def remplir(self):
        self.fill(self.couleur_pinceau)


    def draw(self):
        self.fenetre.blit(self, (self.x, self.y))

    def peindre(self, position):
        pygame.draw.circle(self, self.couleur_pinceau, position, self.rad_pinceau)

    def gommer(self, position):
        pygame.draw.circle(self, self.couleur_fond, position, int(self.rad_pinceau * 2))

    def select_color(self, indice_couleur):
        self.couleur_pinceau = self.couleur[indice_couleur]





















# laaarge
