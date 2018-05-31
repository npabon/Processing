grid = []
next = []

# reaction params
Da = 1 # diffusion constant for a
Db = 0.5 # diffusion constant for b
feed = 0.05 # feed rate for a
k = 0.062 # kill rate for b
dt = 1 # timestep


time = 0

def setup():
    global grid, next
    size(512,512)
    
    for x in range(width):
        grid.append([])
        next.append([])
        for y in range(height):
            grid[x].append({ 'a': 1, 'b': 0 })
            next[x].append({ 'a': 1, 'b': 0 })
            
    # seed some b at random locations
    num_seeds = 4
    r = 5
    for i in range(num_seeds):
        cx = floor(random(100,width-100))
        cy = floor(random(100, height-100))
        for x in range(cx-r,cx+r):
            for y in range(cy-r,cy+r):
                if (x-cx)**2 + (y-cy)**2 <= r**2:
                    grid[x][y]['b'] = 1
     
def draw():
    global grid, next, time
    time += 1
    background(51)
    
    # update 'next'
    for x in range(1,width-1):
        for y in range(1,height-1):
            a = grid[x][y]['a']
            b = grid[x][y]['b']
            next[x][y]['a'] = a + (Da*laplaceA(x,y) - a*b*b + feed*(1-a))*dt
            next[x][y]['b'] = b + (Db*laplaceB(x,y) + a*b*b - (k+feed)*b)*dt
            
    
    # color the pixels by 'next'
    loadPixels()
    for x in range(width):
        for y in range(height):
            a = grid[x][y]['a']
            b = grid[x][y]['b']
            c = floor((a-b)*255)
            c = constrain(c,0,255)
            colorr = color(c,c,c)
            idx = x + y * width
            pixels[idx] = colorr
    updatePixels()
    
    # replace 'grid' with 'next'
    # a deep copy takes far too long
    swap()
    
    if time < 40000 and time % 2 == 0:
        frame_num = str(time/2).zfill(5)
        file_name = "frames/react_diff_{}.png".format(frame_num)
        save(file_name)
    
def swap():
    global grid, next
    tmp = grid
    grid = next
    next = tmp
    
def laplaceA(x,y):
    sum = 0
    sum += grid[x][y]['a'] * -1
    sum += grid[x-1][y]['a'] * 0.2
    sum += grid[x+1][y]['a'] * 0.2
    sum += grid[x][y-1]['a'] * 0.2
    sum += grid[x][y+1]['a'] * 0.2
    sum += grid[x-1][y-1]['a'] * 0.05
    sum += grid[x-1][y+1]['a'] * 0.05
    sum += grid[x+1][y-1]['a'] * 0.05
    sum += grid[x+1][y+1]['a'] * 0.05
    return sum

def laplaceB(x,y):
    sum = 0
    sum += grid[x][y]['b'] * -1
    sum += grid[x-1][y]['b'] * 0.2
    sum += grid[x+1][y]['b'] * 0.2
    sum += grid[x][y-1]['b'] * 0.2
    sum += grid[x][y+1]['b'] * 0.2
    sum += grid[x-1][y-1]['b'] * 0.05
    sum += grid[x-1][y+1]['b'] * 0.05
    sum += grid[x+1][y-1]['b'] * 0.05
    sum += grid[x+1][y+1]['b'] * 0.05
    return sum
