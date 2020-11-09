#Liikkuvat esteet

import pygame

pygame.init()

window = 1200,720
title = "Liikkuvia esteitä"

screen = pygame.display.set_mode((window))
pygame.display.set_caption(title)

class movingObject:

    def __init__(self,posx,posy):
        self.posx = posx
        self.posy = posy
        self.setObjectSpeed = 0.1
    
    def drawObject(self):
        pygame.draw.rect(screen, (100,0,50), [self.posx,self.posy,100,100])
    
    def moveObject(self):
        self.posx += self.setObjectSpeed
    
    def changeDirection(self):
        if (abs(1280-self.posx) < 100):
            self.setObjectSpeed *= -1
        elif (abs(0-self.posx) < 100):
            self.setObjectSpeed *= -1

block = movingObject(100,100)

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            pygame.quit()

    block.drawObject()
    block.moveObject()

    screen.fill((0,0,0))
    pygame.display.update()