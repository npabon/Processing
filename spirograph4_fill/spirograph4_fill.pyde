# http://andygiger.com/science/harmonograph/index.html
from support import Motor, Hitch, Pendulum
add_library('svg')
add_library('pdf')

H = None
scl = 2.5
step = 0

def setup():
    global H, scl
    
    # visual params
    background(255)
    blendMode(MULTIPLY)
    size(1200,900)
    
    # motor locations
    x1 = 200 * scl
    x2 = (width-200) * scl
    y1 = 200 * scl
    y2 = 200 * scl
    # motor arm lengths
    al1 = 600 * scl
    al2 = 600 * scl
    
    # angles
    a1 = 0 # motor1
    a2 = PI # motor2
    a3 = PI # pendulum
    # amplitudes
    r1x = 100 * scl # motor1
    r1y = 175 * scl
    r2x = 100 * scl # motor2
    r2y = 100 * scl
    r3 = 140 * scl # pendulum
    # speeds
    s1 = .0507 # motor1
    s2 = -.05 # motor2
    s3 = s1/2 # pendulum
    # dampening constants
    d1 = .99998 # motor1
    d2 = .99998 # motor2
    d3 = .99997 # motor3
    
    # initiate canvas pendulum
    p = Pendulum(r3, a3, s3, damp=d3)
    # initiate the motors
    M1 = Motor(x1,y1,r1x,r1y,p, angle=a1, speed=s1, armlength=al1, damp=d1)
    M2 = Motor(x2,y2,r2x,r2y,p, angle=a2, speed=s2, armlength=al2, damp=d2)
    # hitch the motors
    H = Hitch(M1, M2)

def draw():
    global H, step
    
    translate(-width/1.3, -height*1.3)
    H.display(traj_only=True)
    H.update()
    step += 1



        
     
     
     
     
     
