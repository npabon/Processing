inc = 0.11
scl = 20 # ratio of cell size to canvas size


def setup():
    size(400,400)
    stroke(0)
    strokeWeight(.5)


def draw():
    background(255)
    numcols = width / scl
    numrows = height / scl
    
    yoff = 0
    for y in range(numrows):
        xoff = 0
        for x in range(numcols):
            index = (x + y * width) * 4
            
            # define flow vector at location
            angle = noise(xoff, yoff) * TWO_PI
            v = PVector.fromAngle(angle)

            # draw vector
            pushMatrix()
            translate(x * scl, y * scl)
            rotate(v.heading())
            line(0,0,scl,0)
            popMatrix()
            
            xoff += inc
        yoff += inc
        
    print(floor(frameRate))