r = 10 # min distance between points
n = 2 # number of dimensions
k = 30 # limit of samples to choose before rejection

w = r / sqrt(n) # cell size = r / sqrt(n)
grid = []
active = []

def setup():
    global grid
    size(400,400)
    background(0)
    strokeWeight(4)
    
    ## STEP 0
    num_cols = floor(width / w)
    num_rows = floor(height / w)
    # initialize grid
    grid = [-1] * num_cols * num_rows
    
    
    ## STEP 1
    x = random(width)
    y = random(height)
    pos = PVector(x,y)
    # insert position vector into  array
    i = floor(x / w)
    j = floor(y / w)
    grid[i + j * num_cols] = pos
    active.insert(0,pos)

def draw():
    background(0)
    
    # draw from grid
    for i in range(len(grid)):
        if grid[i] != -1:
            stroke(255)
            strokeWeight(4)
            point(grid[i].x, grid[i].y)
    
    # draw from active
    for i in range(len(active)):
        stroke(255,0,255)
        strokeWeight(4)
        point(active[i].x, active[i].y)
        
    ## STEP 2
        
            
            
            
            
            
            