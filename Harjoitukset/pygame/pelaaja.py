#Tehdään liikkuva pelaaja

import pygame

pygame.init()

displayWidth = 750
displayHeight = 500
title = "Player Movement"

screen = pygame.display.set_mode((displayWidth, displayHeight))
pygame.display.set_caption(title)

class Player:

    def __init__(self, posX, posY):
        self.posX = posX
        self.posY = posY
        self.playerSpeed = 0.1
        

    #Pelaajan piirto
    def displayPlayer(self):
        pygame.draw.circle(screen, (100,0,200),(int(self.posX),int(self.posY)), 10)
    
    #Pelaajan liikkuminen eri suuntiin
    def movePlayerDown(self):
        self.posY += self.playerSpeed
    
    def movePlayerUp(self):
        self.posY -= self.playerSpeed
    
    def movePlayerLeft(self):
        self.posX -= self.playerSpeed

    def movePlayerRight(self):
        self.posX += self.playerSpeed

#Alustetaan Player-luokka
plr = Player(0.5*displayWidth, 0.5*displayHeight)



#Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(0)
            quit()
        

    keys = pygame.key.get_pressed()


    if event.type == pygame.KEYDOWN:
        if keys == pygame.K_LEFT or keys == ord('a'):
            plr.movePlayerLeft
        if keys == pygame.K_RIGHT or keys == ord('d'):
            plr.movePlayerRight
        if keys == pygame.K_UP or keys == ord('w'):
            plr.movePlayerUp
        if keys == pygame.K_DOWN or keys == ord('s'):
            plr.movePlayerDown

    if(keys[pygame.K_UP]):
        plr.movePlayerUp()
    elif(keys[pygame.K_DOWN]):
        plr.movePlayerDown()
    elif(keys[pygame.K_LEFT]):
        plr.movePlayerLeft()
    elif(keys[pygame.K_RIGHT]):
        plr.movePlayerRight() 

    screen.fill((0,0,0))

    plr.displayPlayer()
    pygame.display.update()
