# > color scales range from 0 - 255
# > in greyscale - 0 is black, 255 is white
# > each color scale (0-255) is stored in a byte (8 bits)
# > b/w images use 8 bit color
# > color images use 24 bit color (8 each for R, G, B)

# STROKE and FILL functions set the color of any given shape
# BEFORE it is drawn

# size(400,400)
# background(160)
# stroke(0)
# fill(255)
# rectMode(CENTER)
# rect(width/2, height/2, 100, 100)


# you can make strokes and/or fills invisible using the
# NOSTROKE() and NOFILL() functions

# size(400,400)
# background(160)
# stroke(0)
# line(0, 0, width, height)
# stroke(255)
# noFill()
# rectMode(CENTER)
# rect(width/2, height/2, 100, 100)

# COLOR

# when specifying RGB values, 0 means no color and 255 means as much as possible
# background(255)
# noStroke()
# # bright red
# fill(255,0,0)
# ellipse(20,20,16,16)
# # dark red
# fill(127,0,0)
# ellipse(40,20,16,16)
# # pale red
# fill(255,200,200)
# ellipse(60,20,16,16)



# COLOR TRANSPARENCY
# a fourth color argument gives the alpha

# size(200,200)
# background(0)
# noStroke()

# # No fourth argument means 100% opacity.
# fill(0, 0, 255)
# rect(0, 0, 100, 200)

# # 255 means 100% opacity.
# fill(255, 0, 0, 255)
# rect(0, 0, 200, 40)

# # 75% opacity.
# fill(255, 0, 0, 191)
# rect(0, 50, 200, 40)

# # 55% opacity.
# fill(255, 0, 0, 127)
# rect(0, 100, 200, 40)

# # 25% opacity.
# fill(255, 0, 0, 63)
# rect(0, 150, 200, 40)



# COLOR MODES

# we can customize our color modes, so that they range from 0 - 100 instead of 255
colorMode(RGB,100)
