import copy
z_noise = 1
num_interps = 7

def init(n, r):
    global z_noise, num_interps
    points = []
    for i in range(n):
        rads = (float(i)/n) * TWO_PI # goes around the circle in n steps
        v_x = r * cos(rads)
        v_y = r * sin(rads)
        #initially the corners have the most noise
        v_z = random(z_noise) # noise control
        v = PVector(v_x, v_y, v_z)
        points += [v]
    for j in range(n):
        rads = (float(j)/n) * TWO_PI # goes around the circle in n steps
        v_x = r * cos(rads)
        v_y = -1 * r * sin(rads)
        #initially the corners have the most noise
        v_z = random(z_noise) # noise control
        v = PVector(v_x, v_y, v_z)
        points += [v]   
    
    for b in range(num_interps):
        points = interpolate(points)
    return points

    
# function to add midpoints between every two points
def interpolate(points):
    for i in range(len(points)-1, 0, -1):
        p1 = points[i-1]
        p2 = points[i]
        p3 = generate_midpoint(p1,p2)
        points = splice(points, i, p3)
    # close the gap btw beginning & end
    p1 = points[len(points)-1]
    p2 = points[0]
    p3 = generate_midpoint(p1,p2)
    points = splice(points, 0, p3)
    return points

# insert element into array at specified index
def splice(arr, index, elem):
    a1 = arr[:index]
    a2 = arr[index:]
    a1.append(elem)
    return a1 + a2

# find the midpoint between two vectors
def generate_midpoint(p1,p2):
    p3_x = (p1.x + p2.x) / 2
    p3_y = (p1.y + p2.y) / 2
    p3_z = ((p1.z + p2.z) / 2) * .27 * random(.3, 1.5) # ADJUST THIS RANDOM
    p3 = PVector(p3_x, p3_y, p3_z)
    p3 = move_nearby(p3, 150) # add noise
    return p3

def run(current, points):
    for i in range(80):
        current = update(current, points) # this returns a noisy shape
        display(current)
        
def update(current, points):
    # initiallize current to points
    current = copy.deepcopy(points) 
    # five cycles of noise
    for b in range(5): 
        for i in range(len(current)): # loop through points
            current[i] = move_nearby(current[i], 150) # add noise
    return current

def move_nearby(pnt, sd):
    sigma = pnt.z * sd
    pnt.x += sigma*randomGaussian()
    pnt.y += sigma*randomGaussian()
    return pnt

def display(current):
    beginShape()
    for i in range(len(current)):
        vertex(current[i].x, current[i].y)
    endShape()
    
    
