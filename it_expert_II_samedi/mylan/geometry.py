import pygame

WIDTH, HEIGHT = 1000, 700
GRAVITY =  -0.8
GROUND_Y = 700
pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))

clock = pygame.time.Clock()
player_pos = [100, 50]
player_y_speed = 0
player_size = (50, 50)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player_pos[1] -= 10
            if event.key == pygame.K_DOWN:
                player_pos[1] += 10
            if event.key == pygame.K_LEFT:
                player_pos[0] -= 10
            if event.key == pygame.K_RIGHT:
                player_pos[0] += 10
    #uptade section
    player_y_speed -= GRAVITY
    player_pos[1] += player_y_speed
    if player_pos[1] + player_size[1]> GROUND_Y:
        player_pos[1] = GROUND_Y - player_size[1]
        player_y_speed = 0
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (125,0,255), [*player_pos, player_size[0], player_size[1]])
    pygame.display.flip()
    clock.tick(60)
    pygame.draw.line (screen, (255, 255, 255), (0, GROUND_Y), (WIDTH, GROUND_Y))