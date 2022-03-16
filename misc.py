

import pygame, sys
from pygame.locals import *
from System import *
from Window import *

 

w = 600
h = 450
pygame.init()
DISPLAYSURF = pygame.display.set_mode((w, h))
window = Window(pygame.display.set_mode((w, h)), w, h)
                         
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
magenta = (255, 0, 255)
cyan = (0, 255, 255)


#
s = System(window, 3, Gravity=True, Electric=False, C=0.01, vrange=(0, 0)\
, rrange=(20, 30), Drange=(0.001, 0.001))
#

while True:
    
    
    for event in pygame.event.get():
        
        if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
            pygame.quit()
            sys.exit()
          
    window.surface.fill(white)
    drawGrid(100, window)
    s.update()
    s.draw()
    pygame.display.update()
