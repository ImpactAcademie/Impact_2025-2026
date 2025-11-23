#je mange du caca et c'est trop bon c'est aussi bon que du +@#[§è{}] sous frosen paf sucré au paf salé giga maxer au ratel fusion pokémon d'un 
#raton laveur et un cambrioleru sour ccrak brrr brrr  patapim tralalelo tralalela ballerina capuchina steal a brainroot c'est nul
# mais blox fruit c'est un super jeux j'y joue  

import pygame 
from sys import exit
import math

screen = pygame.display.set_mode((1200,700))


class Entity:
    def __init__(self,pos,angle,speed):
        self.pos = list(pos) 
        self.angle = angle
        self.speed = speed
    def move(self,dt):
        
        self.pos[0]+= math.cos(self.angle)*dt*self.speed
        self.pos[1]-= math.sin(self.angle)*dt*self.speed



class Bullet(Entity):
    def __init__(self, pos, angle ):
        super().__init__(pos, angle, 800)

    def draw(self,surface):
        x=self.pos[0]+math.cos(self.angle)*5
        y=self.pos [1] -math.sin(self.angle)*5
        pygame.draw.line(surface,(255,133,134),self.pos,(x,y),3)



class Player(Entity):
    def __init__(self):
        super().__init__([600,350],0,200) #super=au dessu

        self.health= 100
        self.name='gon'
        self.max_health = 100
        self.image = pygame.transform.scale_by(pygame.image.load("player_gun.png"),0.5)
        self.current_image= self.image
    def shoot(self,projectils):
        projectils.append(Bullet(self.pos,self.angle))



    def move(self,dt):
        
        self.pos[0]+= math.cos(self.angle)*dt*500
        self.pos[1]-= math.sin(self.angle)*dt*500

class Evemy(Player):
    def __init__(self):

        self.pos=[1200,350]
        self.speed-=100
        self.imag=pygame.transfor.scale_by(pygame.image.load('monstre.png'),1)
         

    def look_towards(self,point):
       
        
        x = point[0]-self.pos[0]
        y = point[1]-self.pos[1]
        self.angle = math.atan2(-y,x)
    
        self.current_image = pygame.transform.rotate(self.image,math.degrees(self.angle))#self.angle/math.pi*180 )

    def draw(self, surface):
        surface.blit(self.current_image,self.current_image.get_rect(center=self.pos))

        

pygame.init()


clock=pygame.time.Clock()

player=Player()
bullets:list[Bullet] = []
enemies:list[Evemy]=[Evemy()]
while True:

    dt=clock.tick(60)/1000

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


        elif event.type == pygame.MOUSEMOTION:
            player.look_towards(pygame.mouse.get_pos())

        elif event.type==pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                player.shoot(bullets)

    


    pressed=pygame.key.get_pressed()
    if pressed[pygame.K_z]:
        player.move(dt)


    screen.fill((190,200,60))

    for bullet in bullets[:]:
        bullet.move(dt)

    for bullet in bullets[:]:
        bullet.move(dt)

        if (bullet.pos[0]<0 
            or bullet.pos[0]>screen.get_width())or(bullet.pos[1]<0
            or bullet.pos[1]>screen.get_height()):
            bullets.remove(bullet)
    


    for bullet in bullets:
        bullet.draw(screen)

    player.draw(screen)
    pygame.display.update()

    clock.tick(60)


