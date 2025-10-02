import pygame
import sys
import random

# --- CONSTANTES ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (200, 0, 0)
GREY = (200, 200, 200)

# --- CLASSES ---

class Paddle:
    def __init__(self, x, y, width=100, height=15, color=WHITE):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.speed = 7

    def move(self, keys):
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.rect.x += self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)


class Ball:
    def __init__(self, paddle, size=12, color=WHITE):
        # commence sur le paddle
        self.rect = pygame.Rect(paddle.rect.centerx - size//2, paddle.rect.top - size, size, size)
        self.color = color
        self.vx = 0
        self.vy = 0
        self.released = False  # pas encore partie

    def release(self):
        if not self.released:
            self.vx = 4 * random.choice([-1, 1])
            self.vy = -4
            self.released = True

    def update(self, paddle, bricks):
        if not self.released:
            # suit le paddle avant le lancement
            self.rect.centerx = paddle.rect.centerx
            self.rect.bottom = paddle.rect.top
            return

        self.rect.x += self.vx
        self.rect.y += self.vy

        # rebonds murs
        if self.rect.left <= 0 or self.rect.right >= SCREEN_WIDTH:
            self.vx = -self.vx
        if self.rect.top <= 0:
            self.vy = -self.vy

        # rebond paddle
        if self.rect.colliderect(paddle.rect):
            self.vy = -abs(self.vy)  # toujours vers le haut
            # optionnel : varier vx selon où elle touche le paddle
            offset = (self.rect.centerx - paddle.rect.centerx) / (paddle.rect.width / 2)
            self.vx = 5 * offset

        # collisions briques
        for brick in bricks[:]:
            if self.rect.colliderect(brick.rect):
                destroyed = brick.hit()
                if destroyed:
                    bricks.remove(brick)
                # simple inversion de vy
                if abs(self.rect.bottom - brick.rect.top) < 10 and self.vy > 0:
                    self.vy = -self.vy
                elif abs(self.rect.top - brick.rect.bottom) < 10 and self.vy < 0:
                    self.vy = -self.vy
                else:
                    self.vx = -self.vx
                break

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)


class Brick:
    def __init__(self, x, y, width, height, color=BLUE):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color

    def hit(self):
        return True

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        pygame.draw.rect(screen, BLACK, self.rect, 1)


class StrongBrick(Brick):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height, color=RED)
        self.hp = 2

    def hit(self):
        self.hp -= 1
        if self.hp <= 0:
            return True
        else:
            self.color = BLUE
            return False


# --- MAIN ---

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 36)

    paddle = Paddle(SCREEN_WIDTH//2 - 50, SCREEN_HEIGHT - 30)
    ball = Ball(paddle)

    lives = 3
    bricks = []

    # briques collées les unes aux autres
    rows = 6
    cols = 10
    brick_width = SCREEN_WIDTH // cols
    brick_height = 25
    for row in range(rows):
        for col in range(cols):
            x = col * brick_width
            y = row * brick_height + 50
            if random.random() < 0.2:
                bricks.append(StrongBrick(x, y, brick_width, brick_height))
            else:
                bricks.append(Brick(x, y, brick_width, brick_height))

    running = True
    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    ball.release()

        keys = pygame.key.get_pressed()
        paddle.move(keys)
        ball.update(paddle, bricks)

        # perdre une vie
        if ball.rect.top > SCREEN_HEIGHT:
            lives -= 1
            if lives <= 0:
                print("Game Over!")
                running = False
            else:
                ball = Ball(paddle)  # remettre balle sur paddle

        screen.fill(BLACK)
        paddle.draw(screen)
        ball.draw(screen)
        for brick in bricks:
            brick.draw(screen)

        # afficher vies
        lives_text = font.render(f"Lives: {lives}", True, WHITE)
        screen.blit(lives_text, (10, 10))

        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
