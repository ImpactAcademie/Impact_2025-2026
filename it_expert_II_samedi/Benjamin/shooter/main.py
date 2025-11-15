import pygame
from sys import exit
import math

class Entity:
    def __init__(self, pos, angle, speed):
        self.pos = list(pos)
        self.angle = angle
        self.speed = speed
    def move(self, dt):
        self.pos[0] += math.cos(self.angle) * dt * self.speed
        self.pos[1] -= math.sin(self.angle) * dt * self.speed     

class Player(Entity):
    def __init__ (self):
        super().__init__([600, 350], 0, 200)
        self.health = 100
        self.maxHealth = 100
        self.name = "Bob"
        self.image = pygame.transform.scale_by(pygame.image.load("player_riffle.png"),0.5)
        self.currentImage = self.image
    
    def shoot(self, projectiles):
        projectiles.append(Bullet(self.pos, self.angle))


    def look_towards(self, point):
        x = point[0] - self.pos[0]
        y = point[1] - self.pos[1]
        self.angle = math.atan2(-y,x)
        self.currentImage = pygame.transform.rotate(self.image,  math.degrees(self.angle))
    def draw(self, surface):
        surface.blit(self.currentImage, self.currentImage.get_rect(center = self.pos))
class Enemy(Player):
    def __init__(self):
        super().__init__()
        self.pos = [1200, 350]
        self.speed -= 100
        self.image = pygame.transform.scale_by(pygame.image.load("monster.png"),0.5)
        self.image = pygame.transform.rotate(self.image, 270)


class Bullet(Entity):
    def __init__(self, pos, angle):
        super().__init__(pos,angle, 800)

    def draw(self, surface):
        x = self.pos[0] + math.cos(self.angle)*5
        y = self.pos[1] + math.sin(self.angle)*5
        pygame.draw.line(surface, (255,0,0), self.pos, (x,y), 5)
pygame.init()
screen = pygame.display.set_mode((1200,700))
clock = pygame.time.Clock()
player = Player()
bullets:list[Bullet] = []
ennemies:list[Enemy] = [Enemy()]
while True:
    dt = clock.tick(60)/1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.MOUSEMOTION:
            player.look_towards(pygame.mouse.get_pos())
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                player.shoot(bullets)

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_z]:
        player.move(dt)
    
   
    for bullet in bullets[:]:
        bullet.move(dt)
        if (bullet.pos[0] < 0 or bullet.pos[0] > screen.get_width()) or (bullet.pos[1] < 0 or bullet.pos[1] > screen.get_height()):
            bullets.remove(bullet)

    for enemy in ennemies:
        enemy.look_towards(player.pos)
        enemy.move(dt)

    screen.fill((175,100,50))
    for bullet in bullets:
        bullet.draw(screen)

    for enemy in ennemies:
        enemy.draw(screen)
    player.draw(screen)
    pygame.display.update()
    

