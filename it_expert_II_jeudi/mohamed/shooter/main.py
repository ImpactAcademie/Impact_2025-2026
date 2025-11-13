import pygame
import math
from sys import exit

class Entity:
    def __init__(self, pos, angle, speed):
        self.pos = list(pos)
        self.angle = angle
        self.speed = speed

    def move(self, dt, angle=None):
        self.pos[0] += math.cos(self.angle if angle == None else angle)*self.speed*dt
        self.pos[1] -= math.sin(self.angle if angle == None else angle)*self.speed*dt

    def set_angle(self, angle):
        self.angle = angle


class Player(Entity):
    def __init__(self):
        super().__init__([600, 350], 0, 200)
        self.health = 100
        self.maxHealth = 100
        self.image = pygame.transform.rotozoom(pygame.image.load("player_gun.png"), 0, 0.5)
        self.currentImage = self.image

    def look_towards(self, point):
        x = point[0]-self.pos[0]
        y = point[0]-self.pos[1]
        self.set_angle(math.atan2(-y, x))
        self.currentImage = pygame.transform.rotate(self.image, self.angle/math.pi*180)

    def shoot(self, projectiles):
        projectiles.append(Bullet(self.pos, self.angle))



    def draw(self, screen):
        screen.blit(self.currentImage, self.currentImage.get_rect(center=self.pos))


class Bullet(Entity):
    def __init__(self, pos, angle):
        super().__init__(pos, angle, 1000)

    def draw(self, screen):
        x = math.cos(self.angle)*5+self.pos[0]
        y = math.cos(self.angle)*5+self.pos[1]
        pygame.draw.line(screen, (255, 0, 0), self.pos, (x, y), 3)

pygame.init()
screen = pygame.display.set_mode((1200, 700))
clock = pygame.time.Clock()
player = Player()
projectiles = []

while True:
    dt =clock.tick(120)/1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.MOUSEMOTION:
            player.look_towards(pygame.mouse.get_pos())
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                player.shoot(projectiles)

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_z]:
        player.move(dt)
        player.look_towards(pygame.mouse.get_pos())
    if pressed[pygame.K_s]:
        player.move(dt, angle=player.angle+math.pi)
        player.look_towards(pygame.mouse.get_pos())
    if pressed[pygame.K_q]:
        player.move(dt, angle=player.angle+math.pi/2)
        player.look_towards(pygame.mouse.get_pos())
    if pressed[pygame.K_d]:
        player.move(dt, angle=player.angle+math.pi/2)
        player.look_towards(pygame.mouse.get_pos())
    for projectile in projectiles:
        projectile.move(dt)

    for projectile in projectiles[:]:
        if projectile.pos[0] < 0 or projectile.pos[0] > screen.get_width():
            projectiles.remove(projectile)
        if projectile.pos[1] < 0 or projectile.pos[1] > screen.get_height():
            projectiles.remove(projectile)

    screen.fill((150, 50, 100))
    for projectile in projectiles:
        projectile.draw(screen)
    player.draw(screen)
    pygame.display.update()