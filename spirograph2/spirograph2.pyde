# http://andygiger.com/science/harmonograph/index.html
from support import Motor, Hitch, Pendulum
add_library('svg')

H = None
scl = 2.2
step = 0

def setup():
    
    # visual params
    blendMode(MULTIPLY)
    
    global H, scl
    size(1200,900)
    #noLoop()
    
    # motor locations
    x1 = 200 * scl
    x2 = (width-200) * scl
    y1 = 200 * scl
    y2 = 200 * scl
    # motor arm lengths
    al1 = 550 * scl
    al2 = 550 * scl
    
    # angles
    a1 = 0 # motor1
    a2 = PI # motor2
    a3 = PI/1.4 # motor3
    # amplitudes
    r1x = 100 * scl # motor1
    r1y = 200 * scl
    r2x = 100 * scl # motor2
    r2y = 100 * scl
    r3 = 140 * scl # pendulum
    # speeds
    s1 = .0505 # motor1
    s2 = -.05 # motor2
    s3 = -.0251 # pendulum
    # dampening constants
    d1 = .99995 # motor1
    d2 = .99995 # motor2
    d3 = .99993 # motor3
    
    # initiate canvas pendulum
    p = Pendulum(r3, a3, s3, damp=d3)
    # initiate the motors
    M1 = Motor(x1,y1,r1x,r1y,p, angle=a1, speed=s1, armlength=al1, damp=d1)
    M2 = Motor(x2,y2,r2x,r2y,p, angle=a2, speed=s2, armlength=al2, damp=d2)
    # hitch the motors
    H = Hitch(M1, M2)

def draw():
    global H, step
    background(255)
    
    # if step % 1000 == 0:
    #     # vector filename
    #     fn = "spiro_1_{}.svg".format(step)
    #     beginRecord(SVG, fn)
    
    translate(-width/1.7, -height/1.1)
    H.display(traj_only=True)
    H.update()
    step += 1

    # if step % 1000 == 0:
    #     endRecord(SVG, fn)
        
     
     
     
     
     
