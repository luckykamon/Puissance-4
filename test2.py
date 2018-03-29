
def puissance4():
  background=[[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
  jaune=1
  rouge=2
  rempli=0
  print background
  while True:
    colj=input("colonne jaune ?")-1
    if colj==1 or colj==2 or colj==3 or colj==4 or colj==5 or colj==6 or colj==0:
      test=0
    else:
      test=1
      print "veuillez choisir un entier entre 1 et 7"
    if test==0:
      for k in range(6):
        print background[colj][k]
        if background[colj][k]==0:
          background[colj][k]=1
          break
        if k==5:
          rempli=1
      if rempli ==0:
        break
      if rempli==1:
        rempli=0
        print "Colonne rempli, veuillez en choisir une autre"
  print background
  print affichage(background,5)
  print affichage(background,4)
  print affichage(background,3)
  print affichage(background,2)
  print affichage(background,1)
  print affichage(background,0)

def affichage(p,l):
  return ([p[0][l],p[1][l],p[2][l],p[3][l],p[4][l],p[5][l],p[6][l]])
