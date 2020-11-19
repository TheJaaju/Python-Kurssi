#Ping Pong Game
import pygame
from random import randint


pygame.init()
 
#Colors
BLACK = (0,0,0)
WHITE = (255,255,255)
ORANGE = (255,100,100)
 
#Ikkunan tiedot
resolution = (700, 500)
screen = pygame.display.set_mode(resolution)
pygame.display.set_caption("Pong")



class Maila(pygame.sprite.Sprite):  #Luo mailat

    
    def __init__(self, color, width, height):
        super().__init__()
        
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
 
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        
        self.rect = self.image.get_rect()

    def moveUp(self, pixels):   # Liikuttaa mailaa ylöspäin
        self.rect.y -= pixels
		
        if self.rect.y < 0:
          self.rect.y = 0
          
    def moveDown(self, pixels):     # Liikuttaa mailaa alaspäin
        self.rect.y += pixels
	
        if self.rect.y > 400:
          self.rect.y = 400

class Ball(pygame.sprite.Sprite):   # Luo pallon
    
    def __init__(self, color, width, height):
        super().__init__()
        
        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)
 
        
        
        
        #pygame.draw.circle(Surface, color, pos, radius, width=0)
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        
        self.velocity = [randint(4,8),randint(-8,8)]
        self.rect = self.image.get_rect()
        
    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
    
    def bounce(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = randint(-8,8)


mailaA = Maila(WHITE, 10, 100)
mailaA.rect.x = 20
mailaA.rect.y = 200
 
mailaB = Maila(WHITE, 10, 100)
mailaB.rect.x = 670
mailaB.rect.y = 200

ball = Ball(ORANGE,10,10)
ball.rect.x = 345
ball.rect.y = 195

# Lista objekien spriteistä
sprites = pygame.sprite.Group()
 
# Työntää mailat spritelistaan
sprites.add(mailaA)
sprites.add(mailaB)
sprites.add(ball)


Running = True
 
clock = pygame.time.Clock() # FPS limitaatiohommeliin kellokone xD

# Pisteet
scoreA = 0
scoreB = 0

# -------- Main Loop -----------
while Running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
              Running = False
        elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE: #Pressing the ESC Key will quit the game
                     Running=False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        mailaA.moveUp(5)
    if keys[pygame.K_s]:
        mailaA.moveDown(5)
    if keys[pygame.K_UP]:
        mailaB.moveUp(5)
    if keys[pygame.K_DOWN]:
        mailaB.moveDown(5)


    # --- Game logic
    sprites.update()
 
    #Display scores:
    font = pygame.font.Font(None, 74)
    text = font.render(str(scoreA), 1, WHITE)
    screen.blit(text, (250,10))
    text = font.render(str(scoreB), 1, WHITE)
    screen.blit(text, (420,10))

    # Pallon tormays reunoihin
    if ball.rect.x>=690:
        scoreA += 1
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.x<=0:
        scoreB +=1
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.y>490:
        ball.velocity[1] = -ball.velocity[1]
    if ball.rect.y<0:
        ball.velocity[1] = -ball.velocity[1]
 
    # --- Drawing code should go here 
    screen.fill(BLACK)
    pygame.draw.line(screen, WHITE, [349, 0], [349, 500], 5)
    sprites.draw(screen)
 
    pygame.display.flip()

    clock.tick(60)   # Asettaa FPS:n rajan lukuun 60

pygame.quit()