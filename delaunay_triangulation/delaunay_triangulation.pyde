add_library('ComputationalGeometry')
from support import poisson_sample
import random as rand
from itertools import combinations


# CANVAS PARAMS
cwidth = 600
cheight = 600

# POISSON SAMPLING PARAMS
r = 100 # min distance between points in pixels
n = 2 # number of dimensions
k = 30 # limit of samples to choose before rejection


# # returns params for line between two points: ax + by = c
# def line_from_points(p1, p2):
#     a = p2.y - p1.y
#     b = p1.x - p2.x
#     c = (a * p1.x) + (b * p1.y)
#     return (a,b,c)

# # returns params for a perpendicular bisector of two points
# def perp_bisector_from_points(p1, p2):
#     a1,b1,c1 = line_from_points(p1,p2)
#     a2 = -1 * b1
#     b2 = a1
#     c2 = a2*(p1.x + p2.x)/2 + b2*(p1.y + p2.y)/2
#     return (a2,b2,c2)
    
# # returns the circumcenter of three points
# def circumcenter_from_points(points):
#     p1, p2, p3 = points
#     (a1,b1,c1) = perp_bisector_from_points(p1, p2)
#     (a2,b2,c2) = perp_bisector_from_points(p1, p3)
#     determinant = (a1*b2) - (a2*b1)
#     if determinant == 0: #lines are parallel
#         return None
#     else:
#         x = (b2*c1 - b1*c2)/determinant
#         y = (a1*c2 - a2*c1)/determinant
#         return(x,y)


def setup():
    global cwdith, cheight, r, n, k
    size(cwidth, cheight)
    background(255)
    strokeWeight(4)
    
    # get poisson sampling of points
    points = poisson_sample(r, n, k)
    for p in points:
        point(p.x, p.y)
            
    

    
    
    
    
