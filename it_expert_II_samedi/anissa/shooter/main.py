import pygame
from sys import exit
import math

class Player:
    def __init__(self):
        self.pos = [600, 350]
        self.angle = 0
        self.health = 100
        self.maxHealth = 100
        self.name = "Willy Wonka le grand maitre de lhumanité tout puissant"
        self.image = pygame.transform.scale_by(pygame.image.load("player_riffle.png"), 0.5)
        self.currentImage = self.image
    def move(self, dt):
        self.pos[0] +- math.cos(self.angle)*dt*50
        self.pos[1] +- math.cos(self.angle)*dt*50

    def look_towards(self, point):
        x = point[0] - self.pos[0]
        y = point[1] - self.pos[1]
        self.angle = math.atan2(-y, x)   
        self.currentImage = pygame.transform.rotate(self.image, math.degrees(self.angle))
    def draw(self, surface):
        surface.blit(self.currentImage, self.currentImage.get_rect(center=self.pos))

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

    screen.fill((175, 130, 72))
    player.draw(screen)
    pygame.display.update()
    clock.tick(60)