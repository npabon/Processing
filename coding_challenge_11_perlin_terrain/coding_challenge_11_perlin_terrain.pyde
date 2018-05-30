w = 1200
h = 1200
scl = 20
num_rows = h/scl
num_cols = w/scl

#terrain elevation values
terrain = []

# noise params
noise_mag = 140
noiseDetail(3,.4)
xoff = random(10000)
yoff = random(10000)
zoff = random(10000)
dxoff = 0.1
dyoff = 0.1
dzoff = 0.05
    

def setup():
    global terrain
    size(600, 600, P3D)
    frameRate(8)
                
    
def draw():
    global terrain, zoff, dzoff
    background(255)
    stroke(0)
    noFill()
    
    translate(width/2, height/2)
    rotateX(PI/3)
    translate(-w/2, -h/2)
    
    # generate terrain
    terrain = []
    for row in range(0,num_rows):
        row_terrain = []
        for col in range(num_cols):
            z = noise_mag*noise(xoff + col*dxoff, yoff + row*dyoff - zoff) # height / noise
            row_terrain.append(z)
        terrain.append(row_terrain)
    
    # draw terrain
    for row in range(num_rows-1):
        beginShape(TRIANGLE_STRIP)
        for col in range(num_cols-1):
            if row%2 == 0:# even row
                vertex(col*scl, row*scl, terrain[row][col])
                vertex((col+0.5)*scl, (row+1)*scl, terrain[row+1][col])
            else:
                vertex((col+0.5)*scl, row*scl, terrain[row][col])
                vertex((col+1)*scl, (row+1)*scl, terrain[row+1][col+1])
        endShape()
    
    # update terrain
    zoff += dzoff
    
    
