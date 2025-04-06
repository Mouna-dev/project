import pygame
import time
import random

# Initialisation de pygame
pygame.init()

# Couleurs
blanc = (255, 255, 255)
noir = (0, 0, 0)
rouge = (213, 50, 80)
vert = (0, 255, 0)
bleu = (50, 153, 213)

# Dimensions de la fenêtre
largeur = 600
hauteur = 400

# Taille de chaque bloc du snake
taille_bloc = 10

# Vitesse du jeu
vitesse = 15

# Création de la fenêtre
ecran = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Snake Game")

# Horloge pour contrôler la vitesse
clock = pygame.time.Clock()

# Police
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

# Fonction pour afficher le score
def ton_score(score):
    value = score_font.render(f"Score: {score}", True, bleu)
    ecran.blit(value, [0, 0])

# Fonction pour dessiner le snake
def snake(taille_bloc, liste_snake):
    for bloc in liste_snake:
        pygame.draw.rect(ecran, noir, [bloc[0], bloc[1], taille_bloc, taille_bloc])

# Message de fin
def message(msg, color):
    msg_surface = font_style.render(msg, True, color)
    ecran.blit(msg_surface, [largeur / 6, hauteur / 3])

# Jeu Snake
def jeu():
    game_over = False
    game_close = False

    x1 = largeur / 2
    y1 = hauteur / 2

    x1_changement = 0
    y1_changement = 0

    liste_snake = []
    longueur_snake = 1

    # Position initiale de la pomme
    pomme_x = round(random.randrange(0, largeur - taille_bloc) / 10.0) * 10.0
    pomme_y = round(random.randrange(0, hauteur - taille_bloc) / 10.0) * 10.0

    while not game_over:

        while game_close:
            ecran.fill(blanc)
            message("Game Over! Appuyez sur C pour rejouer ou Q pour quitter", rouge)
            ton_score(longueur_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        jeu()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_changement = -taille_bloc
                    y1_changement = 0
                elif event.key == pygame.K_RIGHT:
                    x1_changement = taille_bloc
                    y1_changement = 0
                elif event.key == pygame.K_UP:
                    y1_changement = -taille_bloc
                    x1_changement = 0
                elif event.key == pygame.K_DOWN:
                    y1_changement = taille_bloc
                    x1_changement = 0

        # Collision avec les bords
        if x1 >= largeur or x1 < 0 or y1 >= hauteur or y1 < 0:
            game_close = True

        x1 += x1_changement
        y1 += y1_changement
        ecran.fill(blanc)

        # Dessiner la pomme
        pygame.draw.rect(ecran, vert, [pomme_x, pomme_y, taille_bloc, taille_bloc])

        # Ajouter les blocs du snake
        tete = [x1, y1]
        liste_snake.append(tete)
        if len(liste_snake) > longueur_snake:
            del liste_snake[0]

        # Collision avec le corps
        for bloc in liste_snake[:-1]:
            if bloc == tete:
                game_close = True

        # Dessiner le snake
        snake(taille_bloc, liste_snake)
        ton_score(longueur_snake - 1)

        pygame.display.update()

        # Manger la pomme
        if x1 == pomme_x and y1 == pomme_y:
            pomme_x = round(random.randrange(0, largeur - taille_bloc) / 10.0) * 10.0
            pomme_y = round(random.randrange(0, hauteur - taille_bloc) / 10.0) * 10.0
            longueur_snake += 1

        clock.tick(vitesse)

    pygame.quit()
    quit()

# Lancer le jeu
jeu()