import pygame
import math
from sys import exit


class Player:
    def __init__(self):
        self.pos = [600 , 350]
        self.angle = 0
        self.health = 100
        self.maxHealth = 100
        self.image = pygame.transform.rotozoom(pygame.image.load("player_gun.png"), 0, 0.5)
        self.currentImage = self.image

    def look_towards(self, point):
        x = point[0]-self.pos[0]
        y = point[0]-self.pos[1]
        self.angle = math.atan2(-y, x)
        self.currentImage = pygame.transform.rotate(self.image, self.angle/math.pi*180)

    def shoot(self, projectiles):
        projectiles.append(Bullet(self.pos, self.angle))

    def move(self, x, y):
        self.pos[0] += x
        self.pos[1] += y

    def draw(self, screen):
        screen.blit(self.currentImage, self.currentImage.get_rect(center=self.pos))


class Bullet:
    def __init__(self, pos, angle):
        self.pos = pos
        self.angle = angle

pygame.init()
screen = pygame.display.set_mode((1200, 700))
clock = pygame.time.Clock()
player = Player()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.MOUSEMOTION:
            player.look_towards(pygame.mouse.get_pos())

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_z]:
        player.move(0, -5)
    if pressed[pygame.K_s]:
        player.move(0, 5)
    if pressed[pygame.K_q]:
        player.move(-5, 0)
    if pressed[pygame.K_d]:
        player.move(5, 0)



    screen.fill((150, 50, 100))
    player.draw(screen)
    pygame.display.update()
    clock.tick(120)