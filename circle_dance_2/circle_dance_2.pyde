rings = 60 # number of circles
dim_init = 50 # radius of first circle
dim_delta = 5 # space between circles

chaos_init = 0.2 
chaos_delta = 0.12
chaos_mag = 20 # noise multiplier

ox = random(10000)
oy = random(10000)
oz = random(10000)

def setup():
    size(800,900)
    strokeWeight(1)
    stroke(0)
    smooth()
    noFill()
    
def draw():
    translate(width/2, height/2)
    background(255)
    display()
    #noLoop()
    
def display():
    global ox, oy, oz
    #ox -= 0.02
    oy -= 0.02
    oz += 0.01
    
    for i in range(0,rings):
        beginShape()
        for angle in range(0,360):
            radian = radians(angle)
            #radius = (chaos_mag * getNoiseWithTime(radian, chaos_delta * i + chaos_init, oz)) + (dim_delta * i + dim_init)
            radius = (chaos_mag * getNoise(radian, chaos_delta * i + chaos_init)) + (dim_delta * i + dim_init)
            vertex(radius * cos(radian), radius * sin(radian))
        endShape(CLOSE)
        
        
def getNoise(radian, dim):
    global ox, oy, oz
    r = radian % TWO_PI
    if r < 0.0: r += TWP_PI
    return noise(ox + cos(r) * dim, oy + sin(r) * dim)
             
def getNoiseWithTime(radian, dim, time):
    global ox, oy, oz
    r = radian % TWO_PI
    if r < 0.0: r += TWP_PI
    return noise(ox + cos(r) * dim, oy + sin(r) * dim, oz + time)
    