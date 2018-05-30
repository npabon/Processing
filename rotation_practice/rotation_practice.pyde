from support import RLINE

r = None

def setup():
    global r
    size(800,800)
    background(255)
    stroke(0)
    
    r = RLINE(width/2,height/2,0.1,rot_angle=0)
    
def draw():
    global r
    r.update()
    r.display()
    
    
    
