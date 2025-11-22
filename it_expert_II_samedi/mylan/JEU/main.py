import pygame 
from sys import exit
import math

from animation import Animation

animation1 = Animation("assets/images/walk", 4, 5)
animation1.start


class Entity:
    def __init__(self, pos, angle, speed):
        self.pos = list(pos)
        self.angle = angle
        self.speed = speed

    def move(self, dt):
        self.pos[0]+= math.cos(self.angle)*dt*self.speed
        self.pos[1]-= math.sin(self.angle)*dt*self.speed

screen = pygame.display.set_mode((1200,700))


class Player(Entity):
    def __init__(self):
        super().__init__([600, 350], 0, 200)


    
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

    dt = clock.tick(60)/1000
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    animation1.update()
    animation1.draw(screen, (600, 350))


    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_z]:
        player.move(dt)    



    # player.draw(screen)
    pygame.display.update()



