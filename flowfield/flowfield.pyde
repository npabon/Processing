from particle import Particle
import math

inc = 0.2
scl = 9  # ratio of cell size to canvas size
numrows = 999
numcols = 999

zoff = 0  # time dimension for noise

num_particles = 10000
particles = []

flowfield = []

def setup():
    global particles, num_particles, flowfield, numrows, numcols
    size(600,600,P2D)
    background(255)

    numcols = int(math.ceil(width / scl)) + 1
    numrows = int(math.ceil(height / scl)) + 1
    print(numrows, numcols)

    for y in range(numrows):
        for x in range(numcols):
            flowfield.append(None)

    for i in range(num_particles):
        particles.append(Particle())


def draw():
    global zoff, particles, flowfield, numrows, numcols
    # background(255)
    stroke(0, 50)
    strokeWeight(.5)

    yoff = 0
    for y in range(numrows):
        xoff = 0
        for x in range(numcols):
            # define flow vector at location
            index = (x + y * numcols)
            angle = noise(xoff, yoff, zoff) * TWO_PI * 3
            v = PVector.fromAngle(angle)
            v.setMag(.8)
            flowfield[index] = v

            # draw vector
            # pushMatrix()
            # translate(x * scl, y * scl)
            # rotate(v.heading())
            # line(0,0,scl,0)
            # popMatrix()

            xoff += inc
        yoff += inc
    zoff += 0.002

    print(floor(frameRate))

    for p in particles:
        p.follow(flowfield, scl, numcols)
        p.update()
        p.show()
        
    saveFrame("frames/flow_####.png")
