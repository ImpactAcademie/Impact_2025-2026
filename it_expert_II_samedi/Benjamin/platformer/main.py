import pygame
import math
from sys import exit

from animation import Animation

pygame.init()
screen = pygame.display.set_mode((1200,700))
clock = pygame.time.Clock()

animation1 = Animation("assets/images/walk/front_walk", 10, 5)
animation1.start()
while True:
    dt = clock.tick(60)/1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        animation1.update()
    screen.fill((10,30,30))
    animation1.draw(screen,(600, 350))

    pygame.display.update()