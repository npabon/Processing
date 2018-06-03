from gaussian_support import init, run
from palettes import nature_palettes_6_color
import random as rand
add_library('svg')

n=10
points = []
current = []

def setup():
    size(800,500)
    background(255,255,255)
    noStroke()
    #blendMode(MULTIPLY)
    noLoop()
        
    
    
def draw():
    global points, current
    
    #background(255,255,255)
    
    # aztek sunset colors: http://www.color-hex.com/color-palette/21517
    darkred = color(62,2,0)
    medred = color(255,0,0)
    aqua = color(64,244,208)
    orange = color(245,158,4)
    
    #filename="gaussian_stone_{}.svg".format(iter)
    #beginRecord(SVG, filename)
    
    
    hy = 0
    fill(orange,5)
    points = init(n,hy)
    run(current, points)
    
    hy = height/4
    fill(aqua,5)
    points = init(n,hy)
    run(current, points)
    
    hy = height/2
    fill(medred,5)
    points = init(n,hy)
    run(current, points)
    
    hy = 3*height/4
    fill(darkred,5)
    points = init(n,hy)
    run(current, points)
    
