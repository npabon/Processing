


size(600,600)


# POINTS
def y(x):
    return height/2 - height/4*sin(x*PI/20)

# for x in range(2*width):
#     point(x,y(x))


# LINES
# for x in range(2*width):
#     line(x/2, y(x/2), (x/2)+1, y((x/2)+1))


# RECTANGLES
# specified by:
    # 1. top left corner coords <- this is the CORNER mode
    # 2. width
    # 3. height 

# for x in range(width):
#     rect(x, y(x), 8, 8)
    
## OR there's an alternate specification using CENTER, width, and height
# rectMode(CENTER)
# rect(width/2, height/2, 100, 100)


## OR there's an alternate specification using CORNERS
# rectMode(CORNERS)
# rect(width/2, height/2, 100, 100)


## ellipses have the SAME MODES as rectangles: CENTER (default), CORNER, nd CORNERS

# putting it all together:
size(200,200)
rectMode(CENTER)
rect(100,100,20,100)
ellipse(100,70,60,60)
ellipse(81,70,16,32) 
ellipse(119,70,16,32) 
line(90,150,80,160)
line(110,150,120,160)