import pygame
import sys

# --- CONSTANTES ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# --- CLASSES ---

# Une classe GameObject crée avec (x, y, width, height, color) avec méthode draw(screen)
"""Classe de base pour tout objet ayant un rectangle et une couleur"""
class GameObject:
    def __init__(self, x, y, width, heigth, color):
        self.x = x
        self.y = y
        self.Width =width
        self. color = color
        self.rect = pygame.Rect(x, y, width, heigth)

        def draw(self, screen):
            pygame.draw.rect(screen, self.color, self.rect)
class Paddle(GameObject):
    def __init__(self, x, y):
        super().__init__(x, y, 15, 100, WHITE)
        self.speed = 5

        def move(self, up_key, down_key, keys):
            if keys[up_key] and self.rect.y > 0:
                self.rect.y -= self. speed
            if keys[down_key] and self.rect.bottom < SCREEN_HEIGHT:
                self.rect.y += self.speed
# Une classe Paddle qui hérite de GameObject crée avec (x, y) de taille (15, 100), couleur (WHITE) et vitesse (5) avec méthode move(up_key, down_key, keys)
"""Raquette qui se déplace verticalement"""
# Une classe Ball qui hérite de GameObject crée avec (x, y) de taille (15, 15) et couleur (WHITE) de vitesse (4, 4) avec une méthode update(paddles, scores): Bouger, Rebondir sur les platformes et le murs, gérer les sorties
"""Balle qui rebondit sur les murs et les raquettes"""


# --- MAIN ---

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 48)

    # TODO crée left_paddle, right_paddle and ball
    left_paddle = paddle(30, SCREEN_HEIGHT//2-5)
    right_paddle.move(pygame.k_)

    scores = [0, 0]  # [gauche, droite]

    running = True
    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        # TODO move the paddles and update the ball
    left_paddle.move(pygame.k_z, pygame.k_s)
    screen.fill(BLACK)

        # ligne centrale
        pygame.draw.line(screen, WHITE, (SCREEN_WIDTH//2, 0), (SCREEN_WIDTH//2, SCREEN_HEIGHT), 2)

        # dessiner objets
        # TODO
        left
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
