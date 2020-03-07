
import pygame
from pygame.locals import *
import random

pygame.init()

ecran = pygame.display.set_mode((1080,1080), FULLSCREEN)
pygame.display.set_caption("Island ISN")

source = pygame.image.load("Ile.PNG").convert()
carte = pygame.transform.scale(source, (1080, 1080))
ecran.blit(carte, (0,0))

minimap = pygame.transform.scale(source, (80, 80))
carte.blit(minimap, (1000,1000))

pygame.display.flip()

coords = (0, 0)
continuer = 1

while continuer:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE) :
            continuer = 0
        if event.type == KEYDOWN and  event.key == K_SPACE:
            print("dezoom")
            dezoom = 1
            ecran.blit(source, (0,0))
            pygame.display.flip()
                
            
        

pygame.quit()