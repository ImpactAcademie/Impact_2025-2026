import pygame
import sys

# --- CONSTANTES ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# --- CLASSES ---

class GameObject:
    """Classe de base pour tout objet ayant un rectangle et une couleur"""
    def __init__(self, x, y, width, height, color):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)


class Paddle(GameObject):
    """Raquette qui se déplace verticalement"""
    def __init__(self, x, y):
        super().__init__(x, y, 15, 100, WHITE)
        self.speed = 5

    def move(self, up_key, down_key, keys):
        if keys[up_key] and self.rect.top > 0:
            self.rect.y -= self.speed
        if keys[down_key] and self.rect.bottom < SCREEN_HEIGHT:
            self.rect.y += self.speed


class Ball(GameObject):
    """Balle qui rebondit sur les murs et les raquettes"""
    def __init__(self, x, y):
        super().__init__(x, y, 15, 15, WHITE)
        self.vx = 4
        self.vy = 4

    def update(self, paddles, scores):
        self.rect.x += self.vx
        self.rect.y += self.vy

        # rebond murs haut/bas
        if self.rect.top <= 0 or self.rect.bottom >= SCREEN_HEIGHT:
            self.vy = -self.vy

        # rebond sur les paddles
        for paddle in paddles:
            if self.rect.colliderect(paddle.rect):
                self.vx = -self.vx
            while self.rect.colliderect(paddle.rect):
                self.rect.x += self.vx

        # score si sortie gauche/droite
        if self.rect.left < 0:
            scores[1] += 1  # joueur de droite marque
            self.rect.center = (SCREEN_WIDTH//2, SCREEN_HEIGHT//2)
        elif self.rect.right > SCREEN_WIDTH:
            scores[0] += 1  # joueur de gauche marque
            self.rect.center = (SCREEN_WIDTH//2, SCREEN_HEIGHT//2)


# --- MAIN ---

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 48)

    left_paddle = Paddle(30, SCREEN_HEIGHT//2 - 50)
    right_paddle = Paddle(SCREEN_WIDTH - 50, SCREEN_HEIGHT//2 - 50)
    ball = Ball(SCREEN_WIDTH//2, SCREEN_HEIGHT//2)

    scores = [0, 0]  # [gauche, droite]

    running = True
    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        left_paddle.move(pygame.K_z, pygame.K_s, keys)
        right_paddle.move(pygame.K_UP, pygame.K_DOWN, keys)
        ball.update([left_paddle, right_paddle], scores)

        screen.fill(BLACK)

        # ligne centrale
        pygame.draw.line(screen, WHITE, (SCREEN_WIDTH//2, 0), (SCREEN_WIDTH//2, SCREEN_HEIGHT), 2)

        # dessiner objets
        left_paddle.draw(screen)
        right_paddle.draw(screen)
        ball.draw(screen)

        # afficher score
        score_left_text = font.render(str(scores[0]), True, WHITE)
        score_right_text = font.render(str(scores[1]), True, WHITE)
        # collé à gauche et droite de la ligne
        screen.blit(score_left_text, (SCREEN_WIDTH//2 - 40 - score_left_text.get_width(), 20))
        screen.blit(score_right_text, (SCREEN_WIDTH//2 + 40, 20))

        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
