import pygame

pygame.init()

screen_width, screen_height = 1280, 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Mon Zelda avec Pygame")

clock = pygame.time.Clock()





class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        # Charge l'image du joueur
        self.image = pygame.image.load('graphics/player.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.direction = pygame.math.Vector2()
        self.speed = 5

    def input(self):
        keys = pygame.key.get_pressed()
        self.direction.x = 0
        self.direction.y = 0
        if keys[pygame.K_UP]:
            self.direction.y = -1
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
        if keys[pygame.K_LEFT]:
            self.direction.x = -1
        elif keys[pygame.K_RIGHT]:
            self.direction.x = 1

    def move(self, speed):
        # Normalise le vecteur de direction si le joueur se déplace en diagonale
        if self.direction.length() != 0:
            self.direction = self.direction.normalize()
        self.rect.x += self.direction.x * speed
        self.rect.y += self.direction.y * speed

    def update(self):
        self.input()
        self.move(self.speed)




LEVEL_MAP = [
    ['x', 'x', 'x', 'x'],
    ['x', ' ', ' ', 'x'],
    ['x', ' ', ' ', 'x'],
    ['x', 'x', 'x', 'x'],
]
TILE_SIZE = 64

for row_index, row in enumerate(LEVEL_MAP):
    for col_index, cell in enumerate(row):
        if cell == 'x':
            x = col_index * TILE_SIZE
            y = row_index * TILE_SIZE
         
            wall = pygame.Rect(x, y, TILE_SIZE, TILE_SIZE)
            pygame.draw.rect(screen, 'red', wall) 


for wall in walls:
    if self.rect.colliderect(wall):
        print
        
       



running = True

while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



    
    screen.fill("black") 
    

    pygame.display.flip()  
    clock.tick(60) 

pygame.quit()
