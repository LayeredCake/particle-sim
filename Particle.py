

import pygame, sys
from pygame.locals import *

from Vector import *
from Window import *
import math

#A particle in the window space with mass, charge, color. Particles move around
#the space, being acted on by forces, and collide with each other.
class Particle():

    def __init__(self, x, y, vx=0, vy=0, r=10, D=1, color=(0, 0, 0), q=0):
        self.color = color
        self.r = r
        self.q = q
        self.m = 4 * D * math.pi * (r ** 3) / 3
        self.d = Vec(x, y)
        self.v = Vec(vx, vy)
        self.a = Vec(0, 0)

    
    #Apply the force vector f to the particle by adding (1 / mass) * f to the particle's acceleration
    def applyForce(self, f):
        self.a += f * (1 / self.m)
        
    #Adjust the position and velocity of the particle to bounce away from a boundary. 
    def bounce(self, axis, limitPos):
        if(axis == 0):
            self.v.x *= -1
            self.d.x = limitPos
        elif(axis == 1):
            self.v.y *= -1
            self.d.y = limitPos
        else:
            raise ValueError("Invalid axis value. Should be 0 for x, or 1 for y.");

    #Returns the distance between this particle and the particle other.
    def distance(self, other):
        return self.d.distance(other.d)
        
    #Handle a collision between this particle and the particle other by adjusting their velocities and positions. 
    def collide(self, other):
        displacement = self.d.displacement(other.d)
        u = displacement.unit()
        aAngle = math.pi - self.v.angle(u)
        bAngle = math.pi - other.v.angle(u * -1)
        ka = (2 * self.v.length() * math.cos(aAngle) + 2 * other.v.length()\
              * math.cos(bAngle)) / (self.m / other.m + 1)
        kb = ka * (self.m / other.m)
        self.v += u * ka
        self.d = self.d + u * ((displacement.length() - self.r - other.r) / 2 - 0.00000001)
     
    #Update the particle by adding its acceleration to its velocity, moving its position by its velocity, keeping it within the window's
    #boundaries, and setting its acceleration to zero.
    def update(self):
        self.v += self.a
        self.d = self.d + self.v
        self.a = Vec(0, 0)

