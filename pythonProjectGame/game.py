import pygame
from player import Player
from  monster import Monster

#crer une classe représente le jeu
class Game:
    def __init__(self):
        #definir si le jeu est commencer
        self.is_playing = False
        #generer notre joueur
        self.all_player =pygame.sprite.Group()
        self.player = Player(self)
        self.all_player.add(self.player)
        #groupe de monster
        self.all_monsters = pygame.sprite.Group()
        self.pressed = {}

    def start(self):
        self.is_playing =True
        self.spawn_monster()
        self.spawn_monster()

    def game_over(self):
        # remettre le jeu à neuf, retirer le monstre, remettre le joueur à 100
        self.all_monsters = pygame.sprite.Group()
        self.player.health = 100
        self.player.health = self.player.max_health
        self.is_playing = False

    def update(self, screen):
        # appliquer l'image de mon j;oueur
        screen.blit(self.player.image, self.player.rect)

        # actualiser la barre de vie de joueur
        self.player.update_health_bar(screen)

        # recuperer les projectiles du joueur
        for projectile in self.player.all_projectiles:
            projectile.move()

        # recuperer les monstres de jeu
        for monster in self.all_monsters:
            monster.forward()
            monster.update_health_bar(screen)

        # appliquer l'ensemble des images de mon groupe de projectile
        self.player.all_projectiles.draw(screen)

        # appliquer l'ensemble des images de mon groupe de monstre
        self.all_monsters.draw((screen))

        # appliquer l'ensemble des images de groupe projectile
        self.player.all_projectiles.draw(screen)
        # Verifier si le joueur souhaite aller à gauche ou a dt
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width():
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()
        print(self.player.rect.x)

    def check_collision(self, sprite, group):
        return  pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_monster(self):
        monster = Monster(self)
        self.all_monsters.add(monster)


