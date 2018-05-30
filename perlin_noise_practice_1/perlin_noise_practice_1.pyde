num_lines = 100
points_per_line = 100
window_buffer = 0

# noise params
noise_mag = 200
xoff = random(10000)
yoff = random(10000)
zoff = random(10000)
dxoff = 0.06 # change in xoff between vertices\
dxoff_t = 0.01 # change in xoff over time (produces scrolling)
dyoff = 0.07 # change in yoff between lines
dzoff = 0.01
noiseDetail(2, .4)

def setup():
    size(800,800)
    noFill()
    stroke(255)
    strokeWeight(3)
    #noLoop()
    
def draw():
    background(0)
    y_ = getY_()
    x_ = getX_()
    drawLines(x_,y_)
   
def getY_():
    inc = ceil(float(height - 2 * window_buffer) / (num_lines + 1))
    y_ = []
    for l in range(0, num_lines):
        y_.append(window_buffer + l * inc)
    return y_


def getX_():
    inc = ceil(float(width - 2 * window_buffer) / (points_per_line + 1))
    x_ = []
    for p in range(0, points_per_line):
        x_.append(window_buffer + p * inc)
    return x_

def drawLines(x_, y_):
    global zoff, xoff
    zoff += dzoff
    xoff += dxoff_t
    
    for i, y in enumerate(y_):
        
        ## POINTS
        for j, x in enumerate(x_):
            n = noise(xoff + j * dxoff, yoff + i * dyoff, zoff) # perlin noise
            n_tot = noise_mag * (n - 0.5) # scaled & offset noise
            stroke(n*255)
            strokeWeight(n*7)
            point(x, y - n_tot)
        
        # ## LINES
        # beginShape()
        # for j, x in enumerate(x_):
        #     n = noise(xoff + j * dxoff, yoff + i * dyoff, zoff) # perlin noise
        #     n_tot = noise_mag * (n - 0.5) # scaled & offset noise
        #     vertex(x, y - n_tot)
        # endShape()
    
