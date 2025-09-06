import pygame



pygame.init


screen=pygame.display.set_mode((1000,700))

player_pos=[100,50]

running=True

while running:

    for event in pygame.event.get():
            
            if event.type==quit:
                  
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

            

    screen.fill((255,0,0))

    pygame.draw.rect(screen,(255,255,100),[*player_pos,50,50])

    pygame.display.flip()



       