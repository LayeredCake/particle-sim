from Particle import *

import random, math


def drawGrid(size, window):
    x = window.x
    y = window.y
    size *= window.zoom
       
def g(particle1, G, system):
    result = Vec(0, 0)
    for particle2 in system.particles:
        if particle1 is not particle2:
            displacement =  particle2.d.displacement(particle1.d) * -1
            if displacement.length() != 0:
                result += (displacement.unit()) * (G * particle2.m / ((displacement.length())**2))
    return result

def gravity(particle, G, system):
    return g(particle, G, system) * particle.m

def E(particle1, K, system):
    result = Vec(0, 0)
    for particle2 in system.particles:
        if particle1 is not particle2:
            displacement = particle1.d.displacement(particle2.d)
            if displacement.length() != 0:
                result += (displacement.unit()) * (K * particle2.q / ((displacement.length())**2))
    return result

def electric(particle, K, system):
    return E(particle, K, system) * particle.q

#A system of particles, which controls the generation, and mechanics of particles
class System():

    def __init__(self, window, n, vrange=(0, 0.5),
                 rrange=(5, 10), Drange=(0.0001, 0.0001), qrange=(-50, 50), \
                 Gravity=True, G=2, Electric=True, C=5):
        self.window = window
        self.xrange = (0, window.w)
        self.yrange = (0, window.h)
        self.vrange = vrange
        self.rrange = rrange
        self.Drange = Drange
        self.qrange = qrange
        self.particles = []
        self.forces = []
        if Gravity:
            self.forces.append(lambda p: gravity(p, G, self))
        if Electric:
            self.forces.append(lambda p: electric(p, C, self))
        for i in range(n):
            self.newParticle()
            
    #run the main loop for the simulation.
    def run(self):
        
        while True:
    
            for event in pygame.event.get():
        
                if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
          
            self.window.surface.fill((255, 255, 255))
            drawGrid(100, self.window)
            self.update()
            self.draw()
            pygame.display.update()


    #Detect collisions between particles, apply forces to particles, and call their update function.
    def update(self):
        self.findCollisions()
        for particle in self.particles:
            for force in self.forces:
                particle.applyForce(force(particle))
            particle.update()
            
    #Find collisions between any particles in the system
    def findCollisions(self):
        pairs = []
        for particle1 in self.particles:
            for particle2 in self.particles:
                if particle1 is not particle2 and (particle1, particle2) not in pairs:
                    if particle1.distance(particle2) <= particle1.r + particle2.r:
                        particle1.collide(particle2)
                        pairs.append((particle1, particle2))

    def draw(self):
        for particle in self.particles:
            particle.draw()

    #Generate a new particle using the system's ranges
    def newParticle(self):
        r = random.uniform(*self.rrange)
        D = random.uniform(*self.Drange)
        x = random.uniform(*self.xrange)
        y = random.uniform(*self.yrange)
        v = random.uniform(*self.vrange)
        q = random.uniform(*self.qrange)
        vDir = random.uniform(0, 2 * math.pi)
        aDir = random.uniform(0, 2 * math.pi)
        vx = v * math.cos(vDir)
        vy = v * math.sin(vDir)
        color = (random.uniform(0, 255), random.uniform(0, 255), random.uniform(0, 255))
        self.particles.append(Particle(self.window, x, y, vx, vy, r, D, color, q))
