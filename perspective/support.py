class Particle(object):
    
    def __init__(self, x, y, phi):
        self.pos = PVector(x,y)
        self.angle = phi
        self.val = 0
        
    def update(index, pTransform):
        self.pos.x += cos(self.angle)
        self.pos.y += sin(self.angle)
        
        # map x and y values to between 0 and 1.8
        nx = 1.8 * map(self.pos.x, 0, width, -1, 1)
        ny = 1.8 * map(self.pos.y, 0, height, -1, 1)
        
        np = pTransform.transformInverse(nx,ny)
        
        n = PVector(nx,ny)
        
        self.altitude = noise(n.x + 423.2, n.y - 231.1) + 0.05 * noise(n.x * 15 - 113.3, n.y * 15 + 221.1)
        nval = (self.altitude + 0.045 * (index - number_of_particle_sets / 2)) % 1
        
    

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
        
        
