
import pygame
from pygame.locals import *
import random

pygame.init()

ecran = pygame.display.set_mode((1080,1080), FULLSCREEN)
pygame.display.set_caption("Island ISN")

source = pygame.image.load("Ile.PNG").convert()
carte = pygame.transform.scale(source, (1080, 1080))
ecran.blit(carte, (0,0))

#chargement
chateau = pygame.image.load("Chateau.png").convert_alpha()
chateau = pygame.transform.scale(chateau, (31,31))

mainbarre = pygame.image.load("mainbarre.png").convert_alpha()

minimap = pygame.transform.scale(source, (80, 80))
carte.blit(minimap, (1000,1000))

pygame.display.flip()






continuer = True
terrain=[[]]



def Verification(x, y):
    if terrain[y][x]==0 or terrain[y][x]==1:
        return False
    else:
        return True

while continuer:

    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE) :
            continuer = False
        
        if event.type == pygame.MOUSEBUTTONUP and event.button ==1 :
            x = event.pos[0]
            y = event.pos[1]
            if Verification(x, y) == True:
                ecran.blit(chateau, (x-17, y-20))
            else:
                ecran.blit(mainbarre, (x-15, y-15))
        

    pygame.display.flip()
                
            
        

pygame.quit()