num_lines = 100
points_per_line = 100
window_buffer = 50

# noise params
noise_mag = 400
xoff = random(10000)
yoff = random(10000)
zoff = random(10000)
dxoff = 0.06
dyoffa = 0.07 # change in yoff between lines
dyoffb = 0.005 # change in yoff over time
dzoff = 0.005
noiseDetail(3, .4)
dmag = noise_mag / (num_lines+40)


def getY_():
    inc = (height - (2 * window_buffer)) / (num_lines+100)
    y_ = []
    for l in range(0, num_lines):
        y_.append(height - window_buffer - l*inc)
    return y_

def getX_():
    inc = (width - (2 * window_buffer)) / (points_per_line)
    x_ = []
    for p in range(0, points_per_line):
        x_.append(window_buffer + p * inc)
    return x_

def setup():
    size(800,800)
    noFill()
    stroke(255)
    strokeWeight(.6)
    #noLoop()
    
def draw():
    background(0)
    y_ = getY_()
    x_ = getX_()
    drawLines(x_, y_)
        
def drawLines(x_, y_):
    global yoff, zoff
    for i, y in enumerate(y_):
        nmag =  i * dmag
        beginShape()
        for j, x in enumerate(x_):
            noize = nmag * noise(xoff + j*dxoff, yoff + i*dyoffa, zoff)
            vertex(x,y - (noise_mag/2) - noize)
            #point(x,y - (noise_mag/2) - noize)
        endShape()
    yoff += dyoffb
    zoff += dzoff