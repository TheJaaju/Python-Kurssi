#Liikkuvat esteet

import pygame

pygame.init()

window = 720,1280
title = "Liikkuvia esteitä"

screen = pygame.display.set_mode((window))
pygame.display.set_caption(title)

class MovingObject:
    def __init__(self,posx,posy):
        self.posx = posx
        self.posy = posy
        self.setObjectSpeed = 0.1
    
    def drawObject(self):
        pygame.draw.rect(screen, (100,0,50), (self.posx,self.posy), width=40)

object = MovingObject(100,100)

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            pygame.quit()
            quit()