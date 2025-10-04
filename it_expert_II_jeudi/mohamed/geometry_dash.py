import  pygame

WITDTH, HEIGHT = 1000, 600
BLACK = (0, 0, 0)
PURPLE = (150, 0, 255)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
GRAVITY = -0.8
GROUND_Y = HEIGHT-100

pygame.init()
screen = pygame.display.set_mode((WITDTH, HEIGHT))
pygame.display.set_caption("Geometry Dash")
clock = pygame.time.Clock()

player_y_speed = 0
player_y = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if player_y + 50 == GROUND_Y:
                    player_y_speed = -15

    # Update section
    player_y_speed -= GRAVITY
    player_y += player_y_speed
    if player_y + 50 > GROUND_Y:
        player_y_speed = 0
        player_y = GROUND_Y - 50
    
    # Draw section
    screen.fill(BLACK)
    pygame.draw.line(screen, WHITE, (0, GROUND_Y), (WITDTH, GROUND_Y))
    pygame.draw.rect(screen, BLUE, (20, player_y, 50, 50))

    pygame.display.flip()
    clock.tick(120)