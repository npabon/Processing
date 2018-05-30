
class Particle(object):
    
    def __init__(self):
        # # OPTION 1
        # self.pos = PVector(random(width),random(height))
        # self.vel = PVector(0,0)
        
        #OPTION 2
        r = random(20)
        a = random(TWO_PI)*4
        self.pos = PVector(width/2 + r*cos(a), height/2 + r*sin(a))
        self.vel = PVector.random2D().limit(4)

        self.acc = PVector(0,0)
        self.maxspeed = 4
        self.prevpos = PVector.random2D()
        
    def update(self):
        self.prevpos = self.pos.copy()
        self.vel.add(self.acc)
        self.vel.limit(self.maxspeed)
        self.pos.add(self.vel)
        self.acc.mult(0)
        self.edges()
        
    def applyForce(self, force):
        self.acc.add(force)
        
    def show(self):
        stroke(0, 5)
        strokeWeight(.8)
        line(self.prevpos.x, self.prevpos.y, self.pos.x, self.pos.y)
        
    def updatePrevious(self):
        self.prevpos = self.pos.copy()
        
    def edges(self):
        if self.pos.x > width: 
            self.pos.x = 0
            self.updatePrevious()
        if self.pos.x < 0:
            self.pos.x = width
            self.updatePrevious()
        if self.pos.y > height:
            self.pos.y = 0
            self.updatePrevious()
        if self.pos.y < 0:
            self.pos.y = height
            self.updatePrevious()
        
    def follow(self, flowfield, scl, numcols):
        x = floor(self.pos.x / scl) 
        y = floor(self.pos.y / scl) 
        idx = floor(x + y * numcols)
        force = flowfield[idx]
        self.applyForce(force)
