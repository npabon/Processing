from gaussian_support import init, run
from palettes import nature_palettes_6_color
import random as rand
add_library('svg')

n=10
r=250
points = []
current = []
iter=0

def setup():
    global n, r, points
    size(800,800)
    
    fill(0,22,65,10)
    noStroke()
    frameRate(1)
    blendMode(MULTIPLY)
    #noLoop()
    
    points = init(n,r)
    
    
    
def draw():
    global n, r, points, current, iter
    iter += 1
    
    
    # randomly select colors for background and foreground
    # palette = rand.choice(nature_palettes_6_color.keys())
    # colors = nature_palettes_6_color[palette]
    colors = nature_palettes_6_color["rustic_tones_stone"]
    rand.shuffle(colors)
    background(colors[0])
    
    filename="gaussian_stone_{}.svg".format(iter)
    beginRecord(SVG, filename)
    fill(colors[1],5)
    translate(width/2, height/2)
    run(current, points)
    points = init(n,r)
    
    
    # num_shapes = 3
    # for i in range(num_shapes):
    #     pushMatrix()
    #     translate(random(1)*width,random(1)*height)
    #     # display shape
    #     fill(colors[i+1],10)
    #     run(current, points)
    #     points = init(n,r)
    #     popMatrix()
