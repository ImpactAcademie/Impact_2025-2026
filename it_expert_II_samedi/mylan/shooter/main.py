import pygame 
from sys import exit
import math


class Entity:
    def __init__(self, pos, angle, speed):
        self.pos = list(pos)
        self.angle = angle
        self.speed = speed

    def move(self, dt):
        self.pos[0]+= math.cos(self.angle)*dt*self.speed
        self.pos[1]-= math.sin(self.angle)*dt*self.speed
    def shoot(self, projectiles):
        projectiles.append(Bullet(self.pos, self.angle))

screen = pygame.display.set_mode((1200,700))


class Player(Entity):
    def __init__(self):
        super().__init__([600, 350], 0, 200)

         
        self.health= 100
        self.name='gon'
        self.max_health = 100
        self.image = pygame.transform.scale_by(pygame.image.load('player_gun.png'),0.5)
        self.current_image= self.image

    
        pass 

    def look_towards(self,point):
       
        
        x = point[0]-self.pos[0]
        y = point[1]-self.pos[1]
        self.angle = math.atan2(-y,x)
    
        self.current_image = pygame.transform.rotate(self.image,math.degrees(self.angle))#self.angle/math.pi*180 )

    def draw(self, surface):
        surface.blit(self.current_image,self.current_image.get_rect(center=self.pos))

class Enemy(Player):
    def __init__(self):
        super().__init__()
        self.pos = [1200, 350]
        self.speed -=20
        self.image = pygame.image.load("monster.png")

class Bullet(Entity):
    def __init__(self, pos, angle):
        super().__init__(pos, angle, 800)

    def draw(self, surface):
        x = self.pos[0] + math.cos(self.angle)*5
        y = self.pos[1] - math.sin(self.angle)*5
        pygame.draw.line(surface, (255, 0, 0), self.pos, ( x, y), 3)
        
        
pygame.init()
clock=pygame.time.Clock()
enemies:list[Enemy] = [Enemy()]
player=Player()
bullets:list[Bullet] = []

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
    for ennemies in ennemies[:]:
        bullet.move(dt)
        if (bullet.pos[0] < 0 or bullet.pos[0] > screen.get.width()) or (bullet.pos[1] < 0 or bullet.pos[1] > screen.get.high()):
    

    
    for bullet in bullets:
        bullet.draw(screen)

    screen.fill((190,200,60))



    player.draw(screen)
    pygame.display.update()



