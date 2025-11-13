#je mange du caca et c'est trop bon c'est aussi bon que 
import pygame 
from sys import exit
import math

screen = pygame.display.set_mode((1200,700))


class Player:
    def __init__(self):

        self.pos = [600,350]
        self.angle=0 
        self.health= 100
        self.name='gon'
        self.max_health = 100
        self.image = pygame.transform.scale_by(pygame.image.load('player_gun.png'),0.5)
        self.current_image= self.image

    def move(self,dt):
        
        self.pos[0]+= math.cos(self.angle)*dt*50
        self.pos[1]+= math.sin(self.angle)*dt*50

        pass 

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

while True:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


        elif event.type == pygame.MOUSEMOTION:
            player.look_towards(pygame.mouse.get_pos())

    screen.fill((190,200,60))
    player.draw(screen)
    pygame.display.update()

    clock.tick(60)


