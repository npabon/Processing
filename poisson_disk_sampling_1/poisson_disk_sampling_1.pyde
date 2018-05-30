r = 30 # min distance between points in pixels
n = 2 # number of dimensions
k = 30 # limit of samples to choose before rejection
w = float(r) / sqrt(n) # cell size = r / sqrt(n)

# global variables that will be redefined
grid = [] # a 1d array to store a 2d grid
active = []
num_cols = 0
num_rows = 0

def setup():
    global grid, active, num_cols, num_rows
    size(400,400)
    background(0)
    strokeWeight(4)

    
    ## STEP 0
    num_cols = ceil(width / w)
    num_rows = ceil(height / w)
    
    
    # initialize grid with -1
    # these will be replaced by the indeces of the actual samples
    grid = [-1] * num_cols * num_rows
    
    
    ## STEP 1
    # select the initial sample
    x = random(width) 
    y = random(height)
    pos = PVector(x,y)
    # insert position vector into grid array
    i = floor(x / w)
    j = floor(y / w)
    grid_idx = i + (j * num_cols) 
    grid[grid_idx] = pos
    # also insert it into the active array
    active.append(pos)

def draw():
    global grid, active, num_cols, num_rows
    background(0)
    
    ## STEP 2
    # while the active list is not empty, choose a random active point
    # pick ANOTHER random point with distance between r and 2r from
    # this active point
    if len(active) > 0:
        idx = floor(random(len(active)))
        pos = active[idx]
        
        # make k attempts to find the next point
        found_new_point = False
        for j in range(k):
            sample = PVector.random2D() 
            magnitude = random(r, 2*r)
            sample.setMag(magnitude)
            sample.add(pos)
            
            # make sure we're not proposing a point outside the canvas boundary
            if not (sample.x > width or sample.x < 0 or
                    sample.y > height or sample.y < 0):
                    
                #check if the new proposed point is within r of 
                # the points in surrounding grid cells
                sample_col = floor(sample.x / w)
                sample_row = floor(sample.y / w)
                
                ok = True
                for i in range(-1,2):
                    for j in range(-1,2):
                        neighbor_col = sample_col + i
                        neighbor_row = sample_row + j
                        
                        if not (neighbor_col < 0 or neighbor_col >= num_cols or
                                neighbor_row < 0 or neighbor_row >= num_rows):
                            neighbor = grid[neighbor_col + neighbor_row * num_cols]
                            if neighbor != -1:
                                d = PVector.dist(sample, neighbor)
                                if d < r:
                                    ok = False
                
                # if the new sample doesnt collide with
                # existing points, add it to the grid and
                # to the active list
                if ok:
                    found_new_point = True
                    grid_idx = sample_col + (sample_row * num_cols)
                    grid[grid_idx] = sample
                    active.append(sample)
                    break
            
        if not found_new_point:
            print(active)
            print(pos)
            active.remove(pos)                        
                                                   
    
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
        
        
            
            
            
            
            
            
