import imageio
import matplotlib.pyplot as plt
im = imageio.imread("plateau.png")
print(im.shape) #taille de l'image
print(tuple(im[0][0])) #couleur en ordonne puis abscisse, on commence en haut a gauche
c=[960,135] #centre du pion en bas a gauche
t=70 #rayon du pion
col=-170
lig=170
pioncollig=[0,0] #pion colonne numero puis ligne numero
c=[960+pioncollig[0]*col,135+pioncollig[1]*lig] #centre du pion en bas a gauche
for o in range(-t,t+1):
  for a in range(-t,t+1):
    if o*o+a*a<t*t:
      im[c[0]+o,c[1]+a] = (255,255,0) 


imageio.imsave("img2.png", im)
plt.imshow(im)
plt.show()
