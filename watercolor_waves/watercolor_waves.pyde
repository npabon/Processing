from waves_support import init, run
from palettes import nature_palettes_6_color
import random as rand
add_library('svg')

j=0
n=10
r=400
points = []
current = []

def setup():
    global n, r, points
    
    #beer label dimensions
    size(657,477)
    r = width/2
    
    fill(0,22,65,10)
    noStroke()
    frameRate(.2)
    blendMode(MULTIPLY)
    #noLoop()
    
    points = init(n,r)
    
    
    
def draw():
    global n, r, points, current, j
    j += 1
    
    # randomly select colors for background and foreground
    palette = rand.choice(nature_palettes_6_color.keys())
    colors = nature_palettes_6_color[palette]
    rand.shuffle(colors)
    background(colors[0],100)
    
    # vector filename
    fn = "{}_{}.svg".format(palette,j)
    #beginRecord(SVG, fn)
    
    translate(width/2,0)
    num_shapes = 1
    for i in range(num_shapes):
        pushMatrix()
        translate(0,height/2)
        # display shape
        fill(colors[i+1],3)
        run(current, points)
        points = init(n,r)
        popMatrix()
        
    #endRecord()
    
    # png filename for reference
    fn = "{}_{}.png".format(palette,j)
    #save(fn)
