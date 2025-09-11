import pygame

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400
GRAVITY = -0.8
JUMP_STRENGTH = -13
GROUND_Y = SCREEN_HEIGHT-100
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (150, 100, 255)

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Mini Geometry Dash")
clock = pygame.time.Clock()

# Variables
player_size = (50, 50)
player_center = [100, GROUND_Y-player_size[1]//2]
player_y_speed = 0

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Jump
                player_y_speed = JUMP_STRENGTH

    # Apply gravity
    player_y_speed -= GRAVITY
    player_center[1] += player_y_speed
    if player_center[1]+player_size[1]//2 >= GROUND_Y:
        player_center[1] = GROUND_Y-player_size[1]//2
        player_y_speed = 0

    # Draw background
    screen.fill(BLACK)
    # Draw floor
    pygame.draw.line(screen, WHITE, (0, GROUND_Y), (SCREEN_WIDTH, GROUND_Y))
    # Draw player
    pygame.draw.rect(screen, BLUE, [player_center[0]-player_size[0]//2, player_center[1]-player_size[1]//2, *player_size])

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
