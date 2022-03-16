

import pygame, sys
from pygame.locals import *

from Vector import *
from Window import *
import math

#A particle in the window space with mass, charge, color. Particles move around
#the space, being acted on by forces, and collide with each other.
class Particle():

    def __init__(self, window, x, y, vx=0, vy=0, r=10, D=1, color=(0, 0, 0), q=0):
        self.window = window
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
        
    #Adjust the position and velocity of the particle to keep it within the window's boundaries. 
    def boundaries(self):
        if self.d.x > self.window.w:
            self.d.x = self.window.w
            self.v.x *= -1
        elif self.d.x < 0:
            self.d.x = 0
            self.v.x *= -1
        if self.d.y > self.window.h:
            self.d.y = self.window.h
            self.v.y *= -1
        elif self.d.y < 0:
            self.d.y = 0
            self.v.y *= -1

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
        other.v += u * -kb
        while self.distance(other) <= self.r + other.r:
            self.d = self.d + self.v
            other.d = other.d + other.v
     
    #Update the particle by adding its acceleration to its velocity, moving its position by its velocity, keeping it within the window's
    #boundaries, and setting its acceleration to zero.
    def update(self):
        self.v += self.a
        self.d = self.d + self.v
        self.boundaries()
        self.a = Vec(0, 0)

    def draw(self):
        pygame.draw.circle(self.window.surface, self.color,
                        (round(self.d.x * self.window.zoom - self.window.x),
                        round(self.d.y * self.window.zoom - self.window.y)),
                        round(self.r * self.window.zoom))
