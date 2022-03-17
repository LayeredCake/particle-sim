

import pygame, sys
from pygame.locals import *
from System import *
from Window import *

 

w = 600
h = 450
pygame.init()
DISPLAYSURF = pygame.display.set_mode((w, h))
window = Window(pygame.display.set_mode((w, h)), w, h)
             


#
s = System(window, 3, Gravity=True, Electric=False, C=0.01, vrange=(0, 0)\
, rrange=(20, 30), Drange=(0.001, 0.001))
#

s.run()