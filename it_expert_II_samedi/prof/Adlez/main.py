import math
import pygame
from sys import exit
from animation import Animation



class Entity:
    def __init__(self, pos, angle, speed):
        self.pos = list(pos)
        self.angle = angle
        self.speed = speed

    def move(self, dt, angle=None):
        self.pos[0] += math.cos(angle if angle else self.angle)*dt*self.speed
        self.pos[1] -= math.sin(angle if angle else self.angle)*dt*self.speed 

class Player(Entity):
    def __init__(self):
        super().__init__([600, 350], 0, 200)
        self.animations = [
            Animation("walk/walk_right", 10, 12),
            Animation("walk/walk_back", 10, 12),
            Animation("walk/walk_left", 10, 12),
            Animation("walk/front_walk", 10, 12),
            Animation("idle/idle_right", 3, 3),
            Animation("idle/idle_back", 1, 3),
            Animation("idle/idle_left", 3, 3),
            Animation("idle/idle_front", 3, 3),
        ]
        self.currentAnim = -1
        self.animations[self.currentAnim].start()
    def move(self, dt, angle):
        anim = round(angle/math.pi*2)%4
        if self.currentAnim != anim:
            self.currentAnim = anim
            self.animations[self.currentAnim].start()
        super().move(dt, angle)
    def stop_moving(self):
        if 0 <= self.currentAnim < 4:
            self.animations[self.currentAnim].stop()
            self.currentAnim += 4
            self.animations[self.currentAnim].start()
    def draw(self, surface):
        self.animations[self.currentAnim].update()
        self.animations[self.currentAnim].draw(surface, self.pos)

pygame.init()
screen = pygame.display.set_mode((1200, 700))
clock = pygame.time.Clock()

player = Player()

while True:
    dt = clock.tick(60)/1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_z]:
        player.move(dt, math.pi/2)
    elif pressed[pygame.K_s]:
        player.move(dt, -math.pi/2)
    elif pressed[pygame.K_q]:
        player.move(dt, math.pi)
    elif pressed[pygame.K_d]:
        player.move(dt, 0)
    else:
        player.stop_moving()

    screen.fill((10, 10, 30))
    player.draw(screen)
    pygame.display.update()