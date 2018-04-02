add_library('pdf')

grid_size = 5
rings = 80
dim_init = 15
dim_delta = 0.1

chaos_init = 0.05
chaos_delta = 0.01
chaos_mag = 80

def setup():
    size(800,800)
    strokeWeight(0.5)
    #colorMode(HSB)
    #blendMode(ADD)
    stroke(150)
    noFill()
    smooth()
    noLoop()
    
def draw():
    background(255)
    translate(-1*width/(2*grid_size), -1*height/(2*grid_size))
    for i in range(grid_size):
        translate(0, height/grid_size)
        pushMatrix()
        for j in range(grid_size):
            translate(width/grid_size, 0)
            display()
        popMatrix()
        
def display():
    ox = random(10000)
    oy = random(10000)
    oz = random(10000)
    
    for i in range(0,rings,2):
        beginShape()
        for angle in range(0,360):
            radian = radians(angle)
            radius = (chaos_mag * getNoiseWithTime(ox, oy, oz, radian, (chaos_delta * i) + chaos_init, oz)) + (i*dim_delta) + dim_init
            vertex(radius * cos(radian), radius * sin(radian))
        endShape(CLOSE)
            
             
def getNoiseWithTime(ox, oy, oz, radian, dim, time):
    r = radian % TWO_PI
    if r < 0.0: r += TWP_PI
    return noise(ox + cos(r) * dim, oy + sin(r) * dim, oz + time)
            
            
            
            