from random import randint
from time import time
import pygame

# Initialisation de Pygame
pygame.init()

# Constantes
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400
GRAVITY = 0.8
JUMP_STRENGTH = -13
OBSTACLE_SPEED = 5

# Couleurs
WHITE = (255, 255, 255)

# Écran
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Mini Geometry Dash")

# Charger les images (remplace les chemins par tes images)
player_image = pygame.transform.scale(pygame.image.load("player.png"), (50, 50)).convert_alpha()
obstacle_image = pygame.transform.scale(pygame.image.load("obstacle.png"), (35, 35)).convert_alpha()
background_image = pygame.image.load("background.png").convert_alpha()
background_image = pygame.transform.scale_by(background_image, SCREEN_WIDTH/background_image.get_width()).convert_alpha()

# Classe joueur
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.base_image = player_image
        self.image = player_image
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = SCREEN_HEIGHT - self.rect.height - 50
        self.vel_y = 0
        self.angle = 0

    def update(self):
        # Appliquer la gravité
        self.vel_y += GRAVITY
        self.rect.y += self.vel_y

        if self.angle%90 != 0:
            self.angle -= 5 if self.angle%90 > 5 else self.angle%90
            self.image = pygame.transform.rotate(self.base_image, self.angle)

        # Collision avec le sol
        if self.rect.bottom >= SCREEN_HEIGHT - 50:
            self.rect.bottom = SCREEN_HEIGHT - 50
            self.vel_y = 0

    def jump(self):
        if self.vel_y == 0:
            self.vel_y = JUMP_STRENGTH
            self.angle -= 1

# Classe obstacle
class Obstacle(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = obstacle_image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.rect.x -= OBSTACLE_SPEED
        if self.rect.right < 0:
            self.kill()

# Groupes de sprites
player = Player()
player_group = pygame.sprite.Group()
player_group.add(player)

obstacles = pygame.sprite.Group()

# Horloge
clock = pygame.time.Clock()

# Timer pour générer des obstacles
obstacle_spawn_time = 0.75
start_time = time()

# Boucle principale
running = True
while running:
    screen.blit(background_image, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.jump()
    if time()-start_time >= obstacle_spawn_time:
        if randint(0, 50) == 0:
            obstacle = Obstacle(SCREEN_WIDTH, SCREEN_HEIGHT - 83)
            obstacles.add(obstacle)
            start_time = time()

    # Mettre à jour les sprites
    player_group.update()
    obstacles.update()

    # Vérifier les collisions
    if pygame.sprite.spritecollide(player, obstacles, False):
        print("Game Over!")
        running = False

    # Dessiner les sprites
    player_group.draw(screen)
    obstacles.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
