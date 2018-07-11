THE_SEED = None
n_particles = 5000
particles = []

# terrain params
dnx = 0.003 # noise step between pixels
dny = 0.003
lower_cutoff = 0.1 # lower noise cutoff
upper_cutoff = 0.9
n_contours = 8.0
contour_width = (upper_cutoff - lower_cutoff) / n_contours
epsilon = 0.0075 # contour line width
alt_sc = 200 # altitude scale
rotation_angle = PI/3

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
                                  random(TWO_PI), 1
                                  ))
        
def draw():
    global particles
    
    translate(width/2, height/2)
    rotateX(rotation_angle)
    translate(-width/2, -height/2)
    
    for p in particles:
        p.display()
        p.update()

class Particle(object):
    
    def __init__(self, x, y, angle, speed):
        self.pos = PVector(x,y, self.get_z(x,y))
        self.angle = angle # direction of travel
        self.speed = speed
        
    def get_z(self,x,y):
        z = noise(dnx * x, dny * y)
        return z
    
    def update(self):
        self.pos.x += self.speed * cos(self.angle)
        self.pos.y += self.speed * sin(self.angle)
        self.pos.z = self.get_z(self.pos.x, self.pos.y)
        
        # if particle has wandered off canvas, replace it in the middle somewhere
        if (self.pos.x < 0 or self.pos.x > width or
            self.pos.y < 0 or self.pos.y > height):
            self.pos.x = width/2 + sigmax*randomGaussian()
            self.pos.y = height/2 + sigmay*randomGaussian()
            self.angle = random(TWO_PI)
        
        # change direction
        # try to remain at the same altitude
        self.angle = self.change_direction()
    
    def change_direction(self):
        cur_z = self.pos.z
        new_angle = 0
        
        done = False
        while not done:
            # propose new angle
            new_angle = random(-1,1)
            new_x = self.speed * cos(new_angle)
            new_y = self.speed * cos(new_angle)
            new_z = self.get_z(new_x, new_y)
            # if it's downhill, accept
            if new_z <= cur_z:
                done = True
            # if it's uphill, accept with some probability
            else:
                # with speed 1 the average diff is .33
                diff = new_z - cur_z
                if random(1) <= 0.1:
                    done=True
        return new_angle
                
                
            
    def display(self):
        if ((self.pos.z > lower_cutoff) and
            (self.pos.z < upper_cutoff) and
            (self.pos.z % contour_width > epsilon)) :
            # c = map(self.pos.z, 0, 1, 0, 255)
            # stroke(c, 10)
            stroke(200,10)
            point(self.pos.x, self.pos.y, alt_sc * self.pos.z)
            
            
