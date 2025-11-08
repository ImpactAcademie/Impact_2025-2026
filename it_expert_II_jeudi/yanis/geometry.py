import pygame

WIDTH, HEIGHT = 1000, 600
BLACK = (0, 0, 0)
RED = (150, 0, 255)
BLUE = (0, 0, 250)
WHITE = (255, 255, 255)
GRAVITY = 0.8
GROUND_y = HEIGHT-100

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
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
                if player_y + 50 == GROUND_y:
                    player_y_speed = -15

    # Update section 
    player_y_speed += GRAVITY
    player_y += player_y_speed
    if player_y + 50 > GROUND_y:
        player_y = GROUND_y-50
    # Draw section
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, RED, (20, player_y, 50, 50))
    screen.fill(BLACK)
    pygame.draw.line(screen, WHITE, (0, GROUND_y), (WIDTH, GROUND_y))
    pygame.draw.rect(screen, RED, (20, player_y, 50, 50))

    pygame.display.flip()
    clock.tick(60)