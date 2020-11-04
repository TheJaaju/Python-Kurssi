import pygame

pygame.init()

#Window 
displayWidth = 750
displayHeight = 500
title = "A Really Cool Title"

#Create the window
gameWindow = pygame.display.set_mode((displayWidth,displayHeight))
pygame.display.set_caption(title)

while True:
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
