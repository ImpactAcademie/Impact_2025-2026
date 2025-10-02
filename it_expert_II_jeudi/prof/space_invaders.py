import pygame
import random
import sys
from time import time

# --- CONSTANTES ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
YELLOW = (255, 215, 0)

# --- CLASSES DE BASE ---

class GameObject:
    def __init__(self, x, y, width, height, color):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)


class Player(GameObject):
    def __init__(self, x, y):
        super().__init__(x, y, 50, 30, GREEN)
        self.speed = 5
        self.gold = 0
        self.shoot_cooldown = 0.5
        self.shoot_time = time()

    def update(self, keys):
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.rect.x += self.speed

    def shoot(self, bullets):
        if time() - self.shoot_time >= self.shoot_cooldown:
            self.shoot_time = time()
            bullet = Bullet(self.rect.centerx, self.rect.top, -8, RED)
            bullets.append(bullet)


class Enemy(GameObject):
    def __init__(self, x, y, health):
        super().__init__(x, y, 40, 30, RED)
        self.speed = 2
        self.health = health

    def update(self):
        self.rect.x += self.speed
        if self.rect.right >= SCREEN_WIDTH or self.rect.left <= 0:
            self.speed = -self.speed
            self.rect.y += 20
    
    def damage(self):
        self.health -= 5 



class Bullet(GameObject):
    def __init__(self, x, y, speed, color):
        super().__init__(x, y, 5, 10, color)
        self.speed = speed

    def update(self):
        self.rect.y += self.speed


class GoldCoin(GameObject):
    def __init__(self, x, y):
        super().__init__(x, y, 15, 15, YELLOW)
        self.speed = 3

    def update(self):
        self.rect.y += self.speed


# --- FONCTION PRINCIPALE ---

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 36)

    # Joueur
    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 50)

    # Listes
    enemies = []
    bullets = []
    coins = []

    score = 0
    wave = 1
    enemies_left = 0

    def spawn_wave(wave_num):
        """Crée une nouvelle vague d'ennemis proportionnelle à la manche."""
        num_enemies = 5 + wave_num * 2
        new_enemies = []
        for i in range(num_enemies):
            x = random.randint(50, SCREEN_WIDTH - 50)
            y = random.randint(50, 150)
            new_enemies.append(Enemy(x, y, wave))
        return new_enemies

    # Première vague
    enemies = spawn_wave(wave)
    enemies_left = len(enemies)

    # Boucle de jeu
    running = True
    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        player.update(keys)
        if keys[pygame.K_SPACE]:
            player.shoot(bullets)

        # Update bullets
        for bullet in bullets[:]:
            bullet.update()
            if bullet.rect.bottom < 0:
                bullets.remove(bullet)

        # Update enemies
        for enemy in enemies[:]:
            enemy.update()

        # Update coins
        for coin in coins[:]:
            coin.update()
            if coin.rect.top > SCREEN_HEIGHT:
                coins.remove(coin)

        # Collisions balle <-> ennemi
        for bullet in bullets[:]:
            for enemy in enemies[:]:
                if bullet.rect.colliderect(enemy.rect):
                    bullets.remove(bullet)
                    enemy.damage()
                    if enemy.health <= 0:
                        enemies.remove(enemy)
                        score += 10
                        enemies_left -= 1

                        # Chance de drop de gold
                        if random.random() < 0.3:  # 30% de chances
                            coins.append(GoldCoin(enemy.rect.centerx, enemy.rect.centery))

                    break  # éviter double collision avec la même balle

        # Collisions joueur <-> pièce
        for coin in coins[:]:
            if player.rect.colliderect(coin.rect):
                coins.remove(coin)
                player.gold += 1

        # Vérifier si vague finie
        if enemies_left <= 0:
            wave += 1
            enemies = spawn_wave(wave)
            enemies_left = len(enemies)

        # Dessin
        screen.fill(BLACK)
        player.draw(screen)

        for enemy in enemies:
            enemy.draw(screen)
        for bullet in bullets:
            bullet.draw(screen)
        for coin in coins:
            coin.draw(screen)

        # Affichage texte
        score_text = font.render(f"Score: {score}", True, WHITE)
        gold_text = font.render(f"Gold: {player.gold}", True, YELLOW)
        wave_text = font.render(f"Wave: {wave}", True, WHITE)
        screen.blit(score_text, (10, 10))
        screen.blit(gold_text, (10, 40))
        screen.blit(wave_text, (10, 70))

        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
