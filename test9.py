import imageio
import matplotlib.pyplot as plt
im = imageio.imread("pionr.png")
print(im.shape) #taille de l'image
print(tuple(im[0][0])) #couleur en ordonne puis abscisse, on commence en haut a gauche
c=[72,72] #centre du pion en bas a gauche
t=70 #rayon du pion
col=-170
lig=170
pioncollig=[0,0] #pion colonne numero puis ligne numero
for o in range(-t,t+1):
  for a in range(-t,t+1):
    if o*o+a*a<t*t:
      im[c[0]+o,c[1]+a] = (255,0,0)
    else:
      im[c[0]+o,c[1]+a] = (0,0,255)


imageio.imsave("pionr.png", im)
plt.imshow(im)
plt.show()
