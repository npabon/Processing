# size(400, 400)
# background(192, 64, 0)
# stroke(255, 255, 255, 128)
# line(150, 25, 270, 350)

# the fill/stroke functions (like ALL Processing functions that 
# affect drawing properties) affect all geometries drawn to the screen 
# until the next fill and stroke functions are called


# a program written as a list of statements (like the one above)
# is called a STATIC SKETCH, and creates a single image without
# any interaction or animation

# INTERACTIVE programs are drawn as a series of frames, which you can create
# by adding functions called setup() and draw(). These are built-in functions
# that are called automatically

# def setup():
#     size(700, 700)
#     stroke(255)
#     background(192, 64, 0)

# def draw():
#     line(350, 350, mouseX, mouseY)
#     #ellipse(mouseX, mouseY, 10, 10)
    
# def mousePressed():
#     background(192, 64, 0)
    
# the SETUP block runs once, the DRAW block runs repeatedly. 
# the SIZE function must be the first line inside setup()

# we can also re-draw the background in each frame to get a different
# effect:
    
# def setup():
#     size(700, 700)
#     stroke(255)

# def draw():
#     background(192, 64, 0)
#     line(350, 350, mouseX, mouseY)


# the SIZE() function sets the flobal variables WIDTH and HEIGHT. These variables
# can then be used to specify geometry sizes
size(400,400)
ellipse(width/2, height/2, 100, 100)

# an optional parameter to SIZE() specifies how the graphics are supposed to be 
# rendered. 

# size(400, 400, P2D)
# size(400, 400, P3D)

# in order to export as a PDF, we need to import the PDF library:
add_library('pdf')
# size(400, 400, PDF, "output.pdf")


# LOADING DATA. The loadStrings and loadImage functions expect the files to be contained
# in a folder called 'data'
