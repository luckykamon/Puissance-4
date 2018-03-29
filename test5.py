import imageio
import matplotlib.pyplot as plt

def plateau(coord1,coord2,couleur): #coord1 l'ordonne et coord2 l'abscisse
  if couleur=="jaune":
    couleur=(255,255,0)
  if couleur=="rouge":
    couleur=(255,0,0)
  im = imageio.imread("img2.png")
  c=[960,135] #centre du pion en bas a gauche
  t=70 #rayon du pion
  col=-170
  lig=170
  pioncollig=[coord1,coord2] #pion colonne numero puis ligne numero
  c=[960+pioncollig[0]*col,135+pioncollig[1]*lig] #centre du pion en bas a gauche
  for o in range(-t,t+1):
    for a in range(-t,t+1):
      if o*o+a*a<t*t:
        im[c[0]+o,c[1]+a] = couleur
  imageio.imsave("img2.png", im)

def puissance4():
  im = imageio.imread("plateau.png")
  imageio.imsave("img2.png", im)
  background=[["     ", "     ", "     ", "     ", "     ", "     "], ["     ", "     ", "     ", "     ", "     ", "     "],["     ", "     ", "     ", "     ", "     ", "     "],["     ", "     ", "     ", "     ", "     ", "     "],["     ", "     ", "     ", "     ", "     ", "     "],["     ", "     ", "     ", "     ", "     ", "     "],["     ", "     ", "     ", "     ", "     ", "     "]] 
  jaune="jaune"
  rouge="rouge"
  rempli=0
  g=0
  player=jaune #jaune commence
  chcol="Colonne jaune ?"
  print affichage(background,5)
  print affichage(background,4)
  print affichage(background,3)
  print affichage(background,2)
  print affichage(background,1)
  print affichage(background,0)
  while True:
    while True:
      colj=input(chcol)-1
      if colj==1 or colj==2 or colj==3 or colj==4 or colj==5 or colj==6 or colj==0:
        test=0
      else:
        test=1
        print "Veuillez choisir un entier entre 1 et 7"
      if test==0:
        for k in range(6):
          print background[colj][k]
          if background[colj][k]=="     ":
            background[colj][k]=player
            plateau(k,colj,player)
            break
          if k==5:
            rempli=1
        if rempli ==0:
          break
        if rempli==1:
          rempli=0
          print "Colonne rempli, veuillez en choisir une autre"
    print affichage(background,5)
    print affichage(background,4)
    print affichage(background,3)
    print affichage(background,2)
    print affichage(background,1)
    print affichage(background,0)
    if player==jaune:
      player=rouge
      chcol="Colonne rouge ?"
    else:
      player=jaune
      chcol="Colonne jaune ?"
    g=gagnant(background)
    if g==1:
      return "Les jaunes ont gagnes !!!"
    if g==2:
      return "Les rouges ont gagnes !!!"

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

def resultat(b,k1,c1,k2,c2,k3,c3,k4,c4):
  new=[["     ", "     ", "     ", "     ", "     ", "     "], ["     ", "     ", "     ", "     ", "     ", "     "],["     ", "     ", "     ", "     ", "     ", "     "],["     ", "     ", "     ", "     ", "     ", "     "],["     ", "     ", "     ", "     ", "     ", "     "],["     ", "     ", "     ", "     ", "     ", "     "],["     ", "     ", "     ", "     ", "     ", "     "]]
  new[k1][c1]=b[k1][c1]
  new[k2][c2]=b[k2][c2]
  new[k3][c3]=b[k3][c3]
  new[k4][c4]=b[k4][c4]
  print affichage(new,5)
  print affichage(new,4)
  print affichage(new,3)
  print affichage(new,2)
  print affichage(new,1)
  print affichage(new,0)

def affichage(p,l):
  return ([p[0][l],p[1][l],p[2][l],p[3][l],p[4][l],p[5][l],p[6][l]])

def credit():
  print "Lucas Bodin"
