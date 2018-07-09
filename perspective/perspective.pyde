import matfunc as mt

THE_SEED = None
n_particles = 3000
n_particle_sets = 8
particle_sets = []
tick = 0

palette = None

nzoom = 10
pTransform = None
invpTransform = None

def setup():
    global THE_SEED, particle_sets, pTransform, invpTransform
    
    size(600,600)
    THE_SEED = floor(random(9999999))
    randomSeed(THE_SEED)
    
    noFill()
    background('#e7e7db')
    stroke(20,10)
    strokeWeight(0.7)
    smooth()
    
    srcCorners = [(0, 0), (width, 0), (width, height), (0, height)]
    dstCorners = [(200, 300), (width - 200, 300), (width, height - 300), (0, height - 300)];
    pTransform = PerspectiveTransform(srcCorners, dstCorners)
    invpTransform = PerspectiveTransform(dstCorners, srcCorners)

    for j in range(n_particle_sets):
        ps = []
        for i in range(n_particles):
            ps.append(Particle(width/2 + 140*randomGaussian(), 
                               height/2 + 140*randomGaussian(), 
                               random(TWO_PI)))
        particle_sets.append(ps)
   
             
def draw():
    global particle_sets
    
    for index, ps in enumerate(particle_sets):
        for p in ps:
            p.update(index)
            p.display()
            
            
            
            

            
                        
##### SUPPORT            
            
            
class Particle(object):
    
    def __init__(self, x, y, phi):
        self.pos = PVector(x,y)
        self.angle = phi
        self.val = 0
        
    def update(self, index):
        self.pos.x += cos(self.angle)
        self.pos.y += sin(self.angle)
        
        # map x and y values to between 0 and 1.8
        nx = 1.8 * map(self.pos.x, 0, width, -1, 1)
        ny = 1.8 * map(self.pos.y, 0, height, -1, 1)
        
        np = invpTransform.transform(nx,ny)
        
        n = PVector(nx,ny)
        
        self.altitude = noise(n.x + 423.2, n.y - 231.1) + 0.05 * noise(n.x * 15 - 113.3, n.y * 15 + 221.1)
        nval = (self.altitude + 0.065 * (index - n_particle_sets / 2 )) % 1
        self.angle += 1.8 + map(nval, 0, 1, -1, 1)
        self.val = nval
        
    def display(self):
        stroke(0)
        fill(0)
        if self.val > 0.47 and self.val < 0.53:
            np = pTransform.transform(self.pos.x, self.pos.y + 350 - self.altitude * 700)
            print(np[0], np[1])
            point(np[0], np[1])

class PerspectiveTransform(object):
    
    def __init__(self, srcCorners, dstCorners):
        self.srcCorners = srcCorners
        self.dstCorners = dstCorners
        self.coeffs = self.perspective_coefficients(self.srcCorners, self.dstCorners)

    def transform(self, x, y):
        a,b,c,d,e,f,g,h = self.coeffs
        new_x = float(a*x + b*y + c) / (g*x + h*y + 1)
        new_y = float(d*x + e*y + f) / (g*x + h*y + 1)
        return new_x, new_y

    def perspective_coefficients(self, oldplane, newplane):
        """
        Calculates and returns the transform coefficients needed for a perspective 
        transform, ie tilting an image in 3D.
        Note: it is not very obvious how to set the oldplane and newplane arguments
        in order to tilt an image the way one wants. Need to make the arguments more
        user-friendly and handle the oldplane/newplane behind the scenes.
        Some hints on how to do that at http://www.cs.utexas.edu/~fussell/courses/cs384g/lectures/lecture20-Z_buffer_pipeline.pdf
    
        | **option** | **description**
        | --- | --- 
        | oldplane | a list of four old xy coordinate pairs
        | newplane | four points in the new plane corresponding to the old points
    
        """
        # first find the transform coefficients, thanks to http://stackoverflow.com/questions/14177744/how-does-perspective-transformation-work-in-pil
        pb,pa = oldplane,newplane
        grid = []
        for p1,p2 in zip(pa, pb):
            grid.append([p1[0], p1[1], 1, 0, 0, 0, -p2[0]*p1[0], -p2[0]*p1[1]])
            grid.append([0, 0, 0, p1[0], p1[1], 1, -p2[1]*p1[0], -p2[1]*p1[1]])
    
        # then do some matrix magic
        A = mt.Matrix(grid)
        B = mt.Vec([xory for xy in pb for xory in xy])
        AT = A.tr()
        ATA = AT.mmul(A)
        gridinv = ATA.inverse()
        invAT = gridinv.mmul(AT)
        res = invAT.mmul(B)
        a,b,c,d,e,f,g,h = res.flatten()
    
        # finito
        return a,b,c,d,e,f,g,h
            
