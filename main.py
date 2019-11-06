import pygame
from pygame.locals import *
from espace_dessin import *
from menu import *

#initialisation des variables
""""dimentions"""
dim_fenetre = [800, 650]  #0 --> x / 1 --> y
"""couleurs"""
gris = (161, 161, 161)
"""timers"""
DESSIN = 1
"""marge"""
marge = 100  # marge qu' il y a a gauche du tableau

# initialisation de pygame
pygame.init()

# initialisation de la fenetre
fenetre = pygame.display.set_mode((dim_fenetre[0], dim_fenetre[1]))
pygame.display.set_caption("dessin")  # nom de la fenetre

#fond bleu
fenetre.fill(gris)

# initialisation du Tableau
tableau = Tableau(fenetre, marge, 0, dim_fenetre[0] - marge, dim_fenetre[1])

# initialisation du Menu
selec = Menu(fenetre, (0, 0, 0), 0, 0, marge, dim_fenetre[1])

# initialisation des timers
pygame.time.set_timer(DESSIN, 3)

# rafraichissement de la fenetre
pygame.display.flip()
b = 0
# boucle infinie
continuer = True  # si continuer vaut False, alors la boucle (et le programme) s'arrete(nt)
while continuer:

    # parcourir les evenements
    for event in pygame.event.get():

        # quitte l'app si on appuie sur la croix
        if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
            continuer = False

        if event.type == KEYDOWN:
            if event.key == K_e:
                tableau.effacer()
            if event.key == K_SPACE:
                tableau.remplir()
            if event.key == K_1:
                tableau.select_color(NOIR)
            if event.key == K_2:
                tableau.select_color(ROUGE)
            if event.key == K_3:
                tableau.select_color(VERT)
            if event.key == K_4:
                tableau.select_color(BLEU)
            if event.key == K_5:
                tableau.select_color(JAUNE)


        if event.type == DESSIN:
            if pygame.mouse.get_pressed()[0]:
                tableau.peindre((pygame.mouse.get_pos()[0] - marge, pygame.mouse.get_pos()[1]))
            elif pygame.mouse.get_pressed()[2]:
                tableau.gommer((pygame.mouse.get_pos()[0] - marge, pygame.mouse.get_pos()[1]))






    tableau.draw()
    selec.draw()


    #rafraichissement de la fenetre
    pygame.display.flip()
