import pygame
import random

#sprite pour affichage
class Monster(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 20
        self.max_health = 20
        self.attack = 0.3
        self.image = pygame.image.load('assets/mummy.png')
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0, 300)
        self.rect.y = 440
        self.velocity = random.randint(1, 2)
        self.clock = pygame.time.Clock()

    def damage(self, amount):
        #infliger les dégats
        self.health -= amount

        #verifier si son nouveau nombre de points de vie est inférieur ou égal à 0
        if self.health <= 0:
            #reapparaitre comme un nouveau monstre
            self.clock.tick(60)
            self.rect.x = 1000 + random.randint(0, 300)
            self.velocity = random.randint(1, 2)
            self.health = self.max_health

    def update_health_bar(self, surface):

        #DESSIner barre de vie
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 10, self.rect.y - 20, self.max_health, 5])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 10, self.rect.y - 20, self.health, 5])

    def forward(self):
        #le deplacement ne se fait que s'il y a pas de collision avec un groupe de joueur
        if not self.game.check_collision(self, self.game.all_player):
            self.rect.x -= self.velocity
        #si le monstre est en collision en collision avec le joueur
        else:
            #infliger des degat
            self.game.player.damage(self.attack)

