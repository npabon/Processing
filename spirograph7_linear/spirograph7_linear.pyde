# http://andygiger.com/science/harmonograph/index.html
from init import get_traj
add_library('svg')


TRAJ = None
STEP = 0

def setup():
    global TRAJ
    
    #blendMode(MULTIPLY)
    background(255)
    size(1200,900)
    frameRate(120)

    TRAJ = get_traj()
    
def draw():
    global TRAJ, STEP
    
    TRAJ.display()
    TRAJ.update()
    
    STEP += 1
    if STEP % 1000 == 0:
        TRAJ.save_svg('triple_hitch_1_step_{}.svg'.format(STEP))


        
     
     
     
     
     
