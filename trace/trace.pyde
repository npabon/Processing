THE_SEED = None
border = 200
n_particles = 3000
n_particle_sets = 8
particle_sets = []
tick = 0

sigma = 110

palette = None

nzoom = 10

def setup():
    global THE_SEED, particle_sets, palette
    
    size(600,600)
    THE_SEED = floor(random(9999999))
    randomSeed(THE_SEED)
    
    noFill()
    background('#e7e7db')
    stroke(20,10)
    strokeWeight(0.7)
    smooth()
    
    palette = [color(80, 55, 83, 20), color(21, 142, 121, 20)]
    
    for j in range(n_particle_sets):
        ps = []
        for i in range(n_particles):
            ps.append(Particle(width/2 + sigma*randomGaussian(), 
                               height/2 + sigma*randomGaussian(), 
                               random(TWO_PI)))
        particle_sets.append(ps)
        
        
def draw():
    global particle_sets
    
    for index, ps in enumerate(particle_sets):
        for p in ps:
            p.update(index)
            p.display(index)
            

class Particle(object):
    
    def __init__(self, x, y, phi):
        self.pos = PVector(x,y)
        self.angle = phi # at construction is random angle between 0 and 2pi
        self.val = 0
        
    def update(self, index):
        
        # update x and y coordinates according to phi (direction of travel)
        self.pos.x += cos(self.angle)
        self.pos.y += sin(self.angle)
        
        # create n vector, which points to particle from center of canvas
        # n indicates where the particle is on the perlin noise landscape
        # a bigger n means that the noise changes more quickly as the 
        # particle moves accross the canvas. a smaller n means less variation
        nx = 1.8 * map(self.pos.x, 0, width, -1, 1)
        ny = 1.8 * map(self.pos.y, 0, height, -1, 1)
        n = PVector(nx,ny)
        noise_field_val = noise(n.x , n.y - 18)
        
        # scaled offset due to the particle set
        sc = 0.05
        dn = (index - n_particle_sets / 2 )
        
        # the nval is determined by the value of the noise field and 
        # which particle set the particle is in
        nval = (noise_field_val + sc*dn) % 1
        
        # so each particle set is offset by a different amount, meaning that they'll
        # each get displayed at different contours
        
        self.angle += PI * map(nval, 0, 1, -1, 1)
        self.val = nval
        
    def display(self, index):
        if self.val > 0.485 and self.val < 0.515:
            pushMatrix()
            translate(self.pos.x, self.pos.y)
            rotate(self.angle)
            point(0,0)
            #ellipse(0,0,3,3)
            popMatrix()       
            
