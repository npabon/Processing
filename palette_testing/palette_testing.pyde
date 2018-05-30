from palettes import nature_palettes_6_color
import random

def setup():

    size(600, 600)
    background(240)
    noStroke()
    
    num_rows = 6
    num_cols = 6
    
    rh = float(height) / (num_rows + 1)
    cw = float(width) / (num_cols + 1)
    r = cw/1.4
    
    for row in range(num_rows):
        translate(0,rh)
        # choose a row color
        row_palette = random.choice(nature_palettes_6_color.keys())
        row_colors = nature_palettes_6_color[row_palette]
        random.shuffle(row_colors)
        
        pushMatrix()
        for col in range(num_cols):
            translate(cw,0)
            fill(row_colors[col])
            ellipse(0,0,r,r)
        popMatrix()
        
    
    
