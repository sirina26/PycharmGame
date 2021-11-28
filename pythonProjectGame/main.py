import pygame
import math
from game import Game

pygame.init()

#generer fenetre
pygame.display.set_caption("Commet fall Game")
screen = pygame.display.set_mode((1080, 620))

#background
background = pygame.image.load('assets/bg.png')

#importer la bannière
banner = pygame.image.load("assets/banner.png")
banner = pygame.transform.scale(banner, (500, 500))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width() / 4)

#play bouton
play_button = pygame.image.load("assets/button.png")
play_button = pygame.transform.scale(play_button, (400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 4 + 60)
play_button_rect.y = math.ceil(screen.get_height() / 2 + 50)
#charger le jeu
game =Game()

running = True

# boucle tant que cette condition est vrai
while running:

    #appliquer l'arriére plan
    #screen.blit(background, (0, -300))
    screen.blit(background, (0, -400))

    #verifier si le jeu a commencer ou non
    if game.is_playing:
        #declancher les instructions de la partie
        game.update(screen)
    #verifier si le jeu n'est pas commencer
    else:
        #ajouter l'ecran bienvenue
        screen.blit(play_button, play_button_rect) # position(0,0)
        screen.blit(banner, banner_rect)

    #mettre a jour l'écran
    pygame.display.flip()

    #si le jouer ferme cette fenetre
    for event in pygame.event.get():
        # QUE L evenement est fermeture de fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture de jeu")
        #detecter si un joueur lache une touche de clavier
        elif event.type == pygame.KEYDOWN:
           game.pressed[event.key] = True
           # detecter si la touche espace est enclenchée pour lancer notre projectile
           if event.key == pygame.K_SPACE:
               game.player.launch_projectile()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            #verification pour savoir si la souris est en collision avec le bouton joueur
            if play_button_rect.collidepoint(event.pos):
                #mettre le jeu en mode  "lancée"
                game.start()