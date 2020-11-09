#Liikkuvat objektit

import pygame

#Values for the screen
window = 500,600
title = "Liikkuvat objektit"

#Creating the screen
screen = pygame.display.set_mode(window)
pygame.display.set_caption(title)

class movingObject:

    def __init__(self,posx,posy,spdx,spdy):
        self.posx = posx
        self.posy = posy
        self.velX = spdx
        self.velY = spdy 

    def drawObject(self):
        pygame.draw.rect(screen, (100,0,50), [self.posx,self.posy,10,100])
    
    def moveObject(self):
        self.posx += self.velX
        self.posy += self.velY


    def changeDirection(self):
        if (abs(400-self.posx) < 50):
            self.velX*= -1
        if (abs(400-self.posy) < 50):
            self.velY*= -1

        elif (abs(0-self.posx) < 100):
            self.velX *= -1
        elif (abs(0-self.posy) < 100):
            self.velY *= -1

este = movingObject(100,100,0,0.1)
este2 = movingObject(200,200,0.2,0)

#Main loop
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            
    #Rendering The Object
    este.drawObject()
    este.moveObject()
    este.changeDirection()

    #Rendering The 2nd Object
    este2.drawObject()
    este2.moveObject()
    este2.changeDirection()

    pygame.display.update()
    screen.fill((0,0,0))

pygame.quit()