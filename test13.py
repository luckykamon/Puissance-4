import time
import pygame
from pygame.locals import *


pygame.init()
fenetre = pygame.display.set_mode((648,604), RESIZABLE)
depart = pygame.image.load("depart.png").convert()
fenetre.blit(depart, (0,0))
pygame.display.flip()

def help():
  help = pygame.image.load("help.png").convert()
  fenetre.blit(help, (0,0))
  pygame.display.flip()
  while True:
    for event in pygame.event.get():
      if event.type==KEYDOWN:
        initialisation()
      if event.type==MOUSEBUTTONDOWN:
        if event.button == 1:
          initialisation()

def initialisation():
  depart = pygame.image.load("depart.png").convert()
  fenetre.blit(depart, (0,0))
  pygame.display.flip()
  while True:
    for event in pygame.event.get():
      if event.type==MOUSEBUTTONDOWN:
        if event.button == 1:
          if 488<event.pos[1]:
            help()
      if event.type==KEYDOWN:
        puissance4()

def puissance4():
  n=0 #nombre de pions poses sur le plateau
  fond = pygame.image.load("plateau2.png").convert()
  fenetre.blit(fond, (0,0))
  pygame.display.flip()
  background=[["     ", "     ", "     ", "     ", "     ", "     "], ["     ", "     ", "     ", "     ", "     ", "     "],["     ", "     ", "     ", "     ", "     ", "     "],["     ", "     ", "     ", "     ", "     ", "     "],["     ", "     ", "     ", "     ", "     ", "     "],["     ", "     ", "     ", "     ", "     ", "     "],["     ", "     ", "     ", "     ", "     ", "     "]] 
  jaune="jaune"
  rouge="rouge"
  rempli=0
  g=0
  player=jaune #jaune commence
  chcol="Colonne jaune ?"
  while True:
    while True:
      utilisateur=True
      if n>41:
          egalite = pygame.image.load("egalite.png").convert()
          fenetre.blit(egalite, (245,100))
          menu = pygame.image.load("menu.png").convert()
          fenetre.blit(menu, (230,200))
          pygame.display.flip()
          while True:
            for event in pygame.event.get():
                if event.key == K_KP0:
                  initialisation()
                if event.key == K_KP1:
                  puissance4()
      if chcol=="Colonne jaune ?":
        fond = pygame.image.load("tjaunes.png").convert()
        fenetre.blit(fond, (500,550))
        pygame.display.flip()
      else:
        fond = pygame.image.load("trouges.png").convert()
        fenetre.blit(fond, (500,550))
        pygame.display.flip()
      while utilisateur:
        for event in pygame.event.get():
          if event.type==MOUSEBUTTONDOWN:
            if event.button == 1:
              
                  
              if 10<event.pos[1]<525:
                if 31<event.pos[0]<103:
                  colj=0
                  utilisateur=False
                if 118<event.pos[0]<187:
                  colj=1
                  utilisateur=False
                if 202<event.pos[0]<272:
                  colj=2
                  utilisateur=False
                if 287<event.pos[0]<357:
                  colj=3
                  utilisateur=False
                if 373<event.pos[0]<443:
                  colj=4
                  utilisateur=False
                if 457<event.pos[0]<527:
                  colj=5
                  utilisateur=False
                if 542<event.pos[0]<612:
                  colj=6
                  utilisateur=False
          if event.type==KEYDOWN:
            if event.key == K_KP1:
              colj=0
              utilisateur=False
            if event.key == K_KP2:
              colj=1
              utilisateur=False
            if event.key == K_KP3:
              colj=2
              utilisateur=False
            if event.key == K_KP4:
              colj=3
              utilisateur=False
            if event.key == K_KP5:
              colj=4
              utilisateur=False
            if event.key == K_KP6:
              colj=5
              utilisateur=False
            if event.key == K_KP7:
              colj=6
              utilisateur=False
      for k in range(6):
        if background[colj][k]=="     ":
          background[colj][k]=player
          plateau(k,colj,player)
          break
        if k==5:
          rempli=1
      if rempli ==0:
        break
      rempli=0
    if player==jaune:
      n+=1
      player=rouge
      chcol="Colonne rouge ?"
    else:
      n+=1
      player=jaune
      chcol="Colonne jaune ?"
    g=gagnant(background)
    if g==1 or g==2:
      time.sleep(1.5) #permet de montrer le resultat sans afficher menu juste devant
      menu = pygame.image.load("menu.png").convert()
      fenetre.blit(menu, (230,200))
      pygame.display.flip()
      while True:
        for event in pygame.event.get():
          if event.type==KEYDOWN:
            if event.key == K_KP0:
              initialisation()
            if event.key == K_KP1:
              puissance4()

def gagnant(b):
  if ligne(b)[0]==1:
    resultat(ligne(b)[1],ligne(b)[2],ligne(b)[3],ligne(b)[4],ligne(b)[5],ligne(b)[6],ligne(b)[7],ligne(b)[8],ligne(b)[9])
    return 1
  if colonne(b)[0]==1:
    resultat(colonne(b)[1],colonne(b)[2],colonne(b)[3],colonne(b)[4],colonne(b)[5],colonne(b)[6],colonne(b)[7],colonne(b)[8],colonne(b)[9])
    return 1
  if diagbghd(b)[0]==1:
    resultat(diagbghd(b)[1],diagbghd(b)[2],diagbghd(b)[3],diagbghd(b)[4],diagbghd(b)[5],diagbghd(b)[6],diagbghd(b)[7],diagbghd(b)[8],diagbghd(b)[9])
    return 1
  if diaghbd(b)[0]==1:
    resultat(diaghbd(b)[1],diaghbd(b)[2],diaghbd(b)[3],diaghbd(b)[4],diaghbd(b)[5],diaghbd(b)[6],diaghbd(b)[7],diaghbd(b)[8],diaghbd(b)[9])
    return 1
  if ligne(b)[0]==2:
    resultat(ligne(b)[1],ligne(b)[2],ligne(b)[3],ligne(b)[4],ligne(b)[5],ligne(b)[6],ligne(b)[7],ligne(b)[8],ligne(b)[9])
    return 2
  if colonne(b)[0]==2:
    resultat(colonne(b)[1],colonne(b)[2],colonne(b)[3],colonne(b)[4],colonne(b)[5],colonne(b)[6],colonne(b)[7],colonne(b)[8],colonne(b)[9])
    return 2
  if diagbghd(b)[0]==2:
    resultat(diagbghd(b)[1],diagbghd(b)[2],diagbghd(b)[3],diagbghd(b)[4],diagbghd(b)[5],diagbghd(b)[6],diagbghd(b)[7],diagbghd(b)[8],diagbghd(b)[9])
    return 2
  if diaghbd(b)[0]==2:
    resultat(diaghbd(b)[1],diaghbd(b)[2],diaghbd(b)[3],diaghbd(b)[4],diaghbd(b)[5],diaghbd(b)[6],diaghbd(b)[7],diaghbd(b)[8],diaghbd(b)[9])
    return 2
  return 0

def ligne(b):
  for l in range(6):
    for k in range(4):
      if b[k][l]==b[k+1][l]==b[k+2][l]==b[k+3][l]=="jaune":
        return [1,b,k,l,k+1,l,k+2,l,k+3,l]
      if b[k][l]==b[k+1][l]==b[k+2][l]==b[k+3][l]=="rouge":
        return [2,b,k,l,k+1,l,k+2,l,k+3,l]
  return [0]

def colonne(b):
  for k in range(7):
    for l in range(3):
      if b[k][l]==b[k][l+1]==b[k][l+2]==b[k][l+3]=="jaune":
        return [1,b,k,l,k,l+1,k,l+2,k,l+3]
      if b[k][l]==b[k][l+1]==b[k][l+2]==b[k][l+3]=="rouge":
        return [2,b,k,l,k,l+1,k,l+2,k,l+3]
  return [0]

def diagbghd(b): #basgauchehautdroit
  for k in range(4):
    for l in range(3):
      if b[k][l]==b[k+1][l+1]==b[k+2][l+2]==b[k+3][l+3]=="jaune":
        return [1,b,k,l,k+1,l+1,k+2,l+2,k+3,l+3]
      if b[k][l]==b[k+1][l+1]==b[k+2][l+2]==b[k+3][l+3]=="rouge":
        return [2,b,k,l,k+1,l+1,k+2,l+2,k+3,l+3]
  return [0]

def diaghbd(b): #gauchehautbasdroit
  for k in range(4):
    for l in range(3):
      if b[k][5-l]==b[k+1][4-l]==b[k+2][3-l]==b[k+3][2-l]=="jaune":
        return [1,b,k,5-l,k+1,4-l,k+2,3-l,k+3,2-l]
      if b[k][5-l]==b[k+1][4-l]==b[k+2][3-l]==b[k+3][2-l]=="rouge":
        return [2,b,k,5-l,k+1,4-l,k+2,3-l,k+3,2-l]
  return [0]

def plateau(coord1,coord2,couleur): #coord1 l'ordonne et coord2 l'abscisse
  col=-85
  lig=85
  pioncollig=[coord1,coord2] #pion colonne numero puis ligne numero
  c=[440+pioncollig[0]*col,28+pioncollig[1]*lig] #centre du pion en bas a gauche
  if couleur=="jaune":
    pionj = pygame.image.load("pionj.png").convert()
    fenetre.blit(pionj, (c[1],c[0]))
    pygame.display.flip()
  if couleur=="rouge":
    pionr = pygame.image.load("pionr.png").convert()
    fenetre.blit(pionr, (c[1],c[0]))
    pygame.display.flip()

def resultat(b,k1,c1,k2,c2,k3,c3,k4,c4):
  fond = pygame.image.load("plateau2.png").convert()
  fenetre.blit(fond, (0,0))
  pygame.display.flip()
  plateau(c1,k1,b[k1][c1])
  plateau(c2,k2,b[k1][c1])
  plateau(c3,k3,b[k1][c1])
  plateau(c4,k4,b[k1][c1])
  if b[k1][c1]=="jaune":
    fond = pygame.image.load("gjaunes.png").convert()
    fenetre.blit(fond, (80,525))
    pygame.display.flip()
  else:
    fond = pygame.image.load("grouges.png").convert()
    fenetre.blit(fond, (80,525))
    pygame.display.flip()

# A laisser a la fin
initialisation()
