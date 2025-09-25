import pygame

GRAVITER= -0.8

player_size=(50,50)

WIDTH,HEIGHT=1000,700

pygame.init()

GROUND_Y=HEIGHT-100

clock=pygame.time.Clock()

screen=pygame.display.set_mode((WIDTH,HEIGHT))

player_y_speed = 0

player_pos=[100,50]

running=True

while running:

    for event in pygame.event.get():
            
            if event.type==pygame.QUIT:
                  
                  running=False

            if event.type==pygame.KEYDOWN:


                if event.key==pygame.K_UP:
                    player_pos[1]-=10

                if event.key==pygame.K_DOWN:
                    player_pos[1]+=10      
                    
                if event.key==pygame.K_RIGHT:
                    player_pos[0]+=10
                    
                if event.key==pygame.K_LEFT:
                    player_pos[0]-=10

    #update section
    
    screen.fill((255,0,0))
    player_y_speed-=GRAVITER

    player_pos[1]+=player_y_speed

    if player_pos[1]+player_size[1]>GROUND_Y :
        player_pos[1]=GROUND_Y-player_size[1]
        player_y_speed=0

    pygame.draw.rect(screen,(255,255,100),[*player_pos,player_size[0],player_size[1]])

    pygame.draw.line(screen,(255,255,255),(0,GROUND_Y),(WIDTH,GROUND_Y))

    pygame.display.flip()
    clock.tick(60)