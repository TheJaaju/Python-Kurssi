import pygame

pygame.init()

#clock = pygame.time.Clock()
#fps = 60


#Window 
displayWidth = 750
displayHeight = 500
title = "A Really Cool Title"

#Create the window
gameWindow = pygame.display.set_mode((displayWidth,displayHeight))
pygame.display.set_caption(title)

#Create a slab
slab = pygame.draw.rect(gameWindow, (100,100,100),(100,100,100,25))

#Create a circle
circle = pygame.draw.circle(gameWindow, (50,10,200),(200,200),10)


#The loop that keeps the game alive
while True:
    #clock.tick()
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()