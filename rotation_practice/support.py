# function to rotate a vector around a given point
def rotate_point(p, center, angle):
    newx = center.x + (p.x - center.x)*cos(angle) - (p.y - center.y)*sin(angle)
    newy = center.y + (p.x - center.x)*sin(angle) - (p.y - center.y)*cos(angle)
    return PVector(newx, newy)
    
    



class RLINE(object):
    
    def __init__(self,x,y,rot_speed,rot_angle=0):
        self.traj = [PVector(x,y)]
        self.rot_traj = [PVector(x,y)]
        self.rot_angle = rot_angle
        self.rot_speed = rot_speed
        
    def update(self):
        self.rot_angle += self.rot_speed
        new_point = self.traj[-1] + PVector(0,1)
        center = PVector(width/2, height/2)
        rot_new_point = rotate_point(new_point, center, self.rot_angle)
        self.traj.append(new_point)
        self.rot_traj.append(rot_new_point)
        
    def display(self):
        # rotate canvas
        beginShape()
        for p in self.rot_traj:
            vertex(p.x, p.y)
        endShape()
        
        
        
        
    
        
