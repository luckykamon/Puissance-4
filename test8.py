import pygame
from pygame.locals import *
pygame.init()
fenetre = pygame.display.set_mode((1296,1084), RESIZABLE)
fond = pygame.image.load("plateau.png").convert()
fenetre.blit(fond, (0,0))
pygame.display.flip()

def plateau(coord1,coord2,couleur): #coord1 l'ordonne et coord2 l'abscisse
  if couleur=="jaune":
    pionj = pygame.image.load("pionj.png").convert()
    col=-170
    lig=170
    pioncollig=[coord1,coord2] #pion colonne numero puis ligne numero
    c=[960+pioncollig[0]*col,135+pioncollig[1]*lig] #centre du pion en bas a gauche
    fenetre.blit(pionj, (c[1],c[0]))
    pygame.display.flip()
    
  if couleur=="rouge":
    pionr = pygame.image.load("pionr.png").convert()
    col=-170
    lig=170
    pioncollig=[coord1,coord2] #pion colonne numero puis ligne numero
    c=[960+pioncollig[0]*col,135+pioncollig[1]*lig] #centre du pion en bas a gauche
    fenetre.blit(pionr, (c[1],c[0]))
    pygame.display.flip()
  

