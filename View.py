

import pygame, sys, math
from pygame.locals import *


class View():

    def __init__(self, w=600, h=450):
        self.w = w
        self.h = h
        pygame.init()
        self.surface = pygame.display.set_mode((w, h))
        
    #Return True if the user presses escape or closes the display, otherwise return false.
    def receivedQuit(self):
        
        for event in pygame.event.get():
        
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                return True
                
        return False
                
    def closeView(self):
        pygame.quit()
        
    def update(self, system):
    
                         
        white = (255, 255, 255)
    
        self.surface.fill(white)
        
        for particle in system.particles:
            self.drawParticle(particle)
        pygame.display.update()
        
    def drawParticle(self, particle):
        pygame.draw.circle(self.surface, particle.color, (round(particle.d.x), round(particle.d.y)), round(particle.r))
    