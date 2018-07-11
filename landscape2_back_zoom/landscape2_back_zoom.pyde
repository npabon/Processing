THE_SEED = None
n_particles = 5000
n_particle_sets = 8
particle_sets = []

# initial distribution of particles
sigmax = 180
sigmay = 200


def setup():
    global THE_SEED, particle_sets
    
    size(1600,1000)
    THE_SEED = floor(random(9999999))
    randomSeed(THE_SEED)
    
    noFill()
    background(30)
    stroke(200,10)
    strokeWeight(0.7)
    smooth()
    
    # initialize the particle sets
    for j in range(n_particle_sets):
        ps = []
        for i in range(n_particles):
            ps.append(Particle(width/2 + sigmax*randomGaussian(), 
                               height/2 + sigmay*randomGaussian(), 
                               random(TWO_PI)))
        particle_sets.append(ps)


def keyPressed():
    if (keyCode == 80):
        filename_png = "img/trace_{}.png".format(THE_SEED)
        save(filename_png)

    
def draw():
    global particle_sets
    
    for index, ps in enumerate(particle_sets):
        for p in ps:
            p.update(index)
            p.display(index)    
        
        
class Particle(object):
    
    def __init__(self, x, y, angle):
        self.pos = PVector(x,y)
        self.angle = angle # direction of travel, at construction is random
        self.val = 0
        
    def update(self, index):
        
        # update x and y coordinates according to phi (direction of travel)
        speed = 1
        self.pos.x += speed * cos(self.angle)
        self.pos.y += speed * sin(self.angle)
        
        # if particle has wandered off canvas, replace it in the middle somewhere
        if (self.pos.x < 0 or self.pos.x > width or
            self.pos.y < 0 or self.pos.y > height):
            self.pos.x = width/2 + sigmax*randomGaussian()
            self.pos.y = height/2 + sigmay*randomGaussian()
            self.angle = random(TWO_PI)
            
        # we want to be able to make the noise field symmetric, so we 
        # create n vector, which points to particle from center of canvas
        
        ## NOISE 1
        # nmagx = 1.8 # scales the ZOOM
        # nmagy = 1.8
        # nx = nmagx * map(self.pos.x, 0, width, -1, 1)
        # ny = nmagy * map(self.pos.y, 0, height, -1, 1)
        
        ## NOISE 2
        # the height on the canvas scales the zoom level
        # higher up is further away
        nx = map(self.pos.y, 0, height, 3, 0.5) * map(self.pos.x, 0, width, -1, 1)
        ny = 2 * map(self.pos.y, 0, height, 3, 0.5) * map(self.pos.y, 0, width, -1, 1)
        
        n = PVector(nx,ny)
        noise_field_val = noise(n.x - 93, n.y - 23)
        
        # perlin noise is always between 0 and 1, with most values around 0.5
        
        # scaled offset due to the particle set
        sc = 0.045 # MANIPULATE TO CHANGE APPEARANCE
        set_idx = index - float(n_particle_sets) / float(2)
        noise_offset = sc * set_idx
        
        # so each particle set is offset by a different amount, meaning that they'll
        # each get displayed at different contours
        nval = (noise_field_val + noise_offset) % 1

        # adjust angle of travel based on nval
        self.angle += PI * map(nval, 0, 1, -1, 1)
        self.val = nval
        
    def display(self, index):
        if self.val > 0.482 and self.val < 0.518:
            pushMatrix()
            translate(self.pos.x, self.pos.y)
            rotate(self.angle)
            point(0,0)
            popMatrix()      
