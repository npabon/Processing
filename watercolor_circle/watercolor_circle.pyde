from waves_support import init, run
from palettes import nature_palettes_6_color
import random as rand
add_library('svg')

j=0
n=12
r=300
points = []
current = []

def setup():
    global n, r, points
    
    #beer label dimensions
    size(800,800)
    
    fill(0,22,65,10)
    noStroke()
    frameRate(2)
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
    
    translate(width/2, height/2)
    
    num_shapes = 2
    for i in range(num_shapes):
        r2 = r-i*100
        # display shape
        fill(colors[i+1],5)
        run(current, points)
        points = init(n,r2)
        
    #endRecord()
    
    fn = "{}_{}.png".format(palette,j)
    save(fn)
