# http://andygiger.com/science/harmonograph/index.html
from support import Motor, Hitch

H = None

def setup():
    global H
    size(1200,900)
    #noLoop()
    
    # motor locations
    x1 = 200
    x2 = width-200
    y1 = 200
    y2 = 200
    # motor radii
    r1 = 90
    r2 = 90
    # motor angles
    a1 = PI
    a2 = 0
    # motor arm lengths
    al1 = 500
    al2 = 500
    # motor speeds
    s1 = .101
    s2 = -.1
    
    
    M1 = Motor(x1,y1,r1,angle=a1, speed=s1, armlength=al1)
    M2 = Motor(x2,y2,r2,angle=a2, speed=s2, armlength=al2)
    H = Hitch(M1, M2)
    

def draw():
    global H
    background(255)
    H.display()
    H.spin()
