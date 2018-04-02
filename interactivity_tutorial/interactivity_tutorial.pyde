# the variables mouseX and mouseY store the coordinates of the mouse

# def draw():
#     frameRate(1) # per second
#     print(str(mouseX) + " : " + str(mouseY))
    
    
# use the mouse to control visual objects

# def setup():
#     size(300, 300)
#     #noStroke()

# def draw():
#     background(126)
#     ellipse(mouseX, 3*height/4, 33, 33)   # Top circle
#     ellipse(mouseX/2, 2*height/4, 33, 33)   # Middle circle
#     ellipse(mouseX*2, 1*height/4, 33, 33)   # Bottom circl

# to INVERT, you can subtract the mouse position

# def setup():
#     size(700, 700)
#     noStroke()

# def draw():
#     x = mouseX
#     y = mouseY
#     ix = width - mouseX   # Inverse X
#     iy = height - mouseY   # Inverse Y
#     background(126)
#     fill(255, 150)
#     ellipse(x, height/2, y, y)
#     fill(0, 159)
#     ellipse(ix, height/2, iy, iy)


# you can track mouse VELOCITY and store PREVIOUS POSITIONS using pmouseX and pmouseY
# def setup():
#     size(500, 500)
#     strokeWeight(10)


# def draw():
#     background(204)
#     line(mouseX, mouseY, pmouseX, pmouseY)




# use the mouse with IF statements to simulate choice selection
# def setup():
#     size(500, 500)
#     noStroke()
#     fill(0)

# def draw():
#     background(204)
#     w = width / 3
#     if (mouseX < w):
#         rect(0, 0, w, height)   # Left
#     elif (mouseX < 2*w):
#         rect(w, 0, w, height)   # Middle
#     else:
#         rect(2*w, 0, 2*w, height)   # Right



# you can also identify when the MOUSE is PRESSED:
    
# def setup():
#     size(100, 100)

# def draw():
#     if (mousePressed == True):
#         if (mouseButton == LEFT):
#             fill(0)   # Black
#         elif (mouseButton == RIGHT):
#             fill(255)   # White
#     else:
#         fill(126)   # Gray

#     rect(25, 25, 50, 50)



# you can sense input from the KEYBOARD
# this one makes a moving line
x = 20
# def setup():
#     size(100, 100)
#     strokeWeight(4)

# def draw():
#     global x
#     background(204)
#     if (keyPressed):  # If the key is pressed
#         x += 1   # add 1 to x 
#     line(x, 20, x-60, 80)



# you can also use WHICH KEY IS PRESSED
# def setup():
#     size(500, 500)
#     textSize(360)

# def draw():
#     background(0)
#     text(key, 100, 375)   # Draw at coordinate (20,75)

# ps fuck you kenny



# The variable keyCode stores the ALT, CONTROL, SHIFT, UP, DOWN, 
# LEFT, and RIGHT keys as constants. 

# y = 35

# def setup():
#   size(100, 100)

# def draw():
#     global y
#     background(204)
#     line(10, 50, 90, 50)
#     if (key == CODED):
#         if (keyCode == UP):
#             y = 20
#         elif (keyCode == DOWN):
#             y = 50
#     else:
#         y = 35
#     rect(25, y, 50, 30)




#  MOUSE EVENTS


