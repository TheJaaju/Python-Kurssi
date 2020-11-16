#A simple program for controlling a player and adding moving objects
# + collision

# not functional YET


import pygame
import math

from pygame import draw

pygame.init()
Running = True

xd = "VITUN RUNKKARI SAATANA"

#display
resolution = 400,400
title = "playerCollision"

gameDisplay = pygame.display.set_mode(resolution)
pygame.display.set_caption(title)

#Canvas
def drawSurfRect(rectWidth,rectHeight):
    #border = pygame.Rect((rectWidth,rectHeight))
    borderSurface = pygame.Surface((rectWidth,rectHeight))
    borderSurface.fill((200,100,12))
    return borderSurface

#Player
class Player:
    def __init__(self,posX,posY,r):
        self.posx = posX
        self.posy = posY
        self.plrSpeed = 0.2
        self.r = r

        #Unit Vector
        self.length = math.sqrt(posX*posX + posY*posY)
        self.unitVector = [posX / self.length, posY / self.length]









    
    def drawPlayer(self):
        pygame.draw.rect(gameDisplay, (255,255,255),(int(self.posX),int(self.posY)),20)

    def moveLeft(self):
        self.posX -= self.plrSpeed

    def moveRight(self):
        self.posX += self.plrSpeed

class Ball:
    def __init__(self, posx, posy, velx, vely, r):
        self.position = [posx, posy]
        self.speedMagnitude = 0.5   
        self.dirx, self.diry = velx, vely

        self.r = r

        #Unit vector
        self.length = math.sqrt(velx*velx + vely*vely)
        self.unitVector = [velx / self.length, vely / self.length]

        self.speed = [0,0]

        def calcSpeed(self):
            self.speed[0] = self.unitVector[0]*self.speedMagnitude
            self.speed[1] = self.unitVector[1]*self.speedMagnitude

        def displayBall(self):
            pygame.draw.circle(gameDisplay,(200,0,200),(int(self.position[0],self.position[1])),self.r)

        def moveBall(self):
            self.position[0] += self.speed[0]
            self.position[1] += self.speed[1]
        
borderTop = drawSurfRect(400,10)
borderLeft = drawSurfRect(10,400)
borderRight = drawSurfRect(10,400)

topX,topY = 0,0
leftX,leftY = 0,0
rightX,rigthY = 400,0


plr = Player(100,-300)
ball = Ball(0,0,0,0,10)


def checkPlayerCollision(plr):
    print(xd)

def checkBallPlayerCollision(plr,ball):
    print(xd)

while Running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False
            pygame.quit()
            quit()

    gameDisplay.fill((0,0,0))

    keys = pygame.key.get_pressed()

    if(keys[pygame.K_a] or keys[pygame.K_LEFT]):
        plr.moveLeft()
    if(keys[pygame.K_d] or keys[pygame.K_RIGHT]):
        plr.moveRight()

    plr.drawPlayer()
    pygame.display.update()