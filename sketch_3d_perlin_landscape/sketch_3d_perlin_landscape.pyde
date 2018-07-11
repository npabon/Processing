THE_SEED = None
n_particles = 10000
particles = []

# terrain params
dnx = 0.007 # noise step between pixels
dny = 0.007
lower_cutoff = 0.2 # lower noise cutoff
upper_cutoff = 0.8
n_contours = 10.0
contour_width = (upper_cutoff - lower_cutoff) / n_contours
epsilon = 0.0075 # contour line width
alt_sc = 200 # altitude scale

sigmax = 100
sigmay = 100

def setup():
    global THE_SEED, particles, sigmax, sigmay
    THE_SEED = floor(random(9999999))
    randomSeed(THE_SEED)
    
    # canvas params
    size(1600,1000,P3D)
    sigmax = float(width) / 8
    sigmay = float(height) / 8
    
    noiseDetail(3,.4)
    
    #noLoop()
    noFill()
    background(30)
    stroke(200)
    strokeWeight(0.7)
    smooth()
    
    # initialize particles
    for p in range(n_particles):
        particles.append(Particle(width/2 + sigmax*randomGaussian(), 
                                  height/2 + sigmay*randomGaussian(), 
                                  random(TWO_PI)))
        
def draw():
    global particles
    
    translate(width/2, height/2)
    rotateX(PI/4)
    translate(-width/2, -height/2)
    
    for p in particles:
        p.display()
        p.update()

class Particle(object):
    
    def __init__(self, x, y, angle):
        self.pos = PVector(x,y, self.get_z(x,y))
        self.angle = angle # direction of travel
        
    def get_z(self,x,y):
        z = noise(dnx * x, dny * y)
        return z
    
    def update(self):
        speed = 1
        self.pos.x += speed * cos(self.angle)
        self.pos.y += speed * sin(self.angle)
        self.pos.z = self.get_z(self.pos.x, self.pos.y)
        
        # if particle has wandered off canvas, replace it in the middle somewhere
        if (self.pos.x < 0 or self.pos.x > width or
            self.pos.y < 0 or self.pos.y > height):
            self.pos.x = width/2 + sigmax*randomGaussian()
            self.pos.y = height/2 + sigmay*randomGaussian()
            self.angle = random(TWO_PI)
        
        # change direction
        hac = self.pos.z % contour_width # Height Above Contour
        d_angle = 0.5 * map(hac, 0, contour_width, -1, 1)
        self.angle += d_angle
        self.angle = map(self.pos.z, 0, 1, 0, PI)
    
    def display(self):
        if ((self.pos.z > lower_cutoff) and
            (self.pos.z < upper_cutoff) and
            (self.pos.z % contour_width > epsilon)) :
            # c = map(self.pos.z, 0, 1, 0, 255)
            # stroke(c, 10)
            stroke(200,10)
            point(self.pos.x, self.pos.y, alt_sc * self.pos.z)
