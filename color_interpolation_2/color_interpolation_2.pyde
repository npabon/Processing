import random as rand
from palettes import nature_palettes_6_color

THE_SEED = None

cdimx = 2
cdimy = 2
cgrid = []

dimx = 800
dimy = 500

pad = 0

tick = 1

def setup():
    
    size(1600,1000)
    noStroke()
    #noLoop()
    frameRate(1)
    
    
                
def draw():
    global THE_SEED, cgrid
    
    THE_SEED = floor(random(9999999))
    randomSeed(THE_SEED)
    
    #background(random(34,255))
    background('#222')
    
    # put random colors in a cdimx x cdimy grid    
    cgrid = []
    for i in range(cdimy):       # loop row by row
        crow = []
        for j in range(cdimx):
            c = color(random(255),random(255),random(255),random(255))
            crow.append(c)
        cgrid.append(crow)
    
    
    
    for y in range(dimy):
        for x in range(dimx):
            
            px = (float(x) / dimx) * (cdimx - 1) # a fraction
            py = (float(y) / dimy) * (cdimy - 1)
            
            # cdimx = 2, cdimy = 3
            # px ranges between 0 and 1
            # py ranges between 0 and 2
            
            
            px0 = floor(px)
            py0 = floor(py)
            # px0 and py0 give the floor color index
            
            sx = map(px, px0, px0 + 1, 0, 1) # converts px to range between 0 and 1
            sy = map(py, py0, py0 + 1, 0, 1)
            # 0 < sx < 1 , representing the fraction traveled between color px0 and px0 + 1
            # 0 < sy < 1, representing the fraction traveled between color py0 and py0 + 1

            # lerpColor Calculates a color between two colors at a specific increment.
            cu = lerpColor(cgrid[py0][px0], cgrid[py0][px0 + 1], sigmoid(sx))
            cl = lerpColor(cgrid[py0 + 1][px0], cgrid[py0 + 1][px0 + 1], sigmoid(sx))
            
            c = lerpColor(cu, cl, sigmoid(sy));
            fill(c)
            
            w = (width - pad*2) / (dimx-1)
            h = (height - pad*2) / (dimy-1)

            rect(pad + w * x, pad + h * y, w, h)
    
    filename_png = "img/color_interp_{}.png".format(THE_SEED)
    save(filename_png)
    
    

def sigmoid(x):
    return 1.1 / (1 + exp(-6 * (x - 0.5))) - 0.05
    
    
            
            
    
    
    
    
    
    
