import pygame
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((640, 480))

continuer = 1
while continuer:
	for event in pygame.event.get(): 
		if event.type==MOUSEBUTTONDOWN:
			if event.button == 1:
				if event.pos[0]<100:
					print "ok1"
					
