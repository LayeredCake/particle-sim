
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
            self.new()

    def update(self):
        self.findCollisions()
        for particle in self.particles:
            for force in self.forces:
                particle.applyForce(force(particle))
            particle.update()
            
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

    def new(self):
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