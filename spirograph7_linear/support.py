# a class for drawing the trajectory of a hinge
class Linear_Traj(object):
    def __init__(self, hinge, dir, draw_hinge=True):
        self.hinge = hinge
        self.dir = dir # the direction of translation
        self.traj_orig = [self.hinge.hinge_pos] # the untranslated trajectory
        self.traj_trans = [self.hinge.hinge_pos] # the translated trajectory
        self.draw_hinge = draw_hinge
        
    def update(self):
        self.hinge.update()
        self.traj_orig.append(self.hinge.hinge_pos)
        self.traj_trans = [ p + self.dir for p in self.traj_trans ]
        self.traj_trans.append(self.hinge.hinge_pos)
        
    def inc_display(self):
        #background(255)
        if self.draw_hinge:
            self.hinge.display()
        stroke(0)
        strokeWeight(0.5)
        noFill()
        beginShape()
        trans = len(self.traj_orig) * -1 * self.dir
        translate(trans.x, trans.y)
        for p in self.traj_orig[-2:]:
            vertex(p.x, p.y)
        endShape()
    
    def display(self):
        background(255)
        if self.draw_hinge:
            self.hinge.display()
        stroke(0)
        strokeWeight(0.5)
        noFill()
        beginShape()
        for p in self.traj_trans:
            vertex(p.x, p.y)
        endShape()
        
    def save_svg(self, filename):
        beginRecord(SVG, filename)
        stroke(0)
        strokeWeight(0.5)
        noFill()
        beginShape()
        for p in self.traj_trans:
            vertex(p.x, p.y)
        endShape()
        endRecord()
        

# a hinge connecting two hinges
class Hinge_Hinge(object):
    def __init__(self, h1, h2, arm1_len, arm2_len):
        self.h1 = h1 # gimbal attachments
        self.h2 = h2
        self.arm1_len = arm1_len # arm lengths
        self.arm2_len = arm2_len
        self.hinge_pos = self.get_hinge_pos()
    
    def get_hinge_pos(self):
        d = (self.h2.hinge_pos - self.h1.hinge_pos).mag() # dist btw attachment pts
        delta = asin((self.h2.hinge_pos - self.h1.hinge_pos).y / d) # angle of vector from g1.arm_pos to g2.arm_pos  
        gamma = acos((self.arm1_len**2 + d**2 - self.arm2_len**2) / (2 * self.arm1_len * d)) # angle btw. vector above and vector from g1.arm_pos to hinge_pos
        angle = delta + gamma # angle from g1.arm_pos to hinge point
        hx = self.h1.hinge_pos.x + self.arm1_len*cos(angle)
        hy = self.h1.hinge_pos.y + self.arm1_len*sin(angle)
        return PVector(hx, hy)

    def display(self):
        self.h1.display() # display child hinges
        self.h2.display()
        strokeWeight(1)
        fill(100)
        line(self.h1.hinge_pos.x, self.h1.hinge_pos.y, self.hinge_pos.x, self.hinge_pos.y) # hinge arms
        line(self.h2.hinge_pos.x, self.h2.hinge_pos.y, self.hinge_pos.x, self.hinge_pos.y)
        ellipse(self.hinge_pos.x, self.hinge_pos.y,5,5) # hinge point point
     
    def update(self):
        self.h1.update() # update gimbals
        self.h2.update()
        self.hinge_pos = self.get_hinge_pos() # update hinge location


# a hinge connecting two gimbals
class Gimbal_Hinge(object):
    def __init__(self, g1, g2, arm1_len, arm2_len, draw_traj=False):
        self.g1 = g1 # gimbal attachments
        self.g2 = g2
        self.arm1_len = arm1_len # arm lengths
        self.arm2_len = arm2_len
        self.hinge_pos = self.get_hinge_pos()
    
    def get_hinge_pos(self):
        d = (self.g2.arm_pos - self.g1.arm_pos).mag() # dist btw attachment pts
        delta = asin((self.g2.arm_pos - self.g1.arm_pos).y / d) # angle of vector from g1.arm_pos to g2.arm_pos  
        gamma = acos((self.arm1_len**2 + d**2 - self.arm2_len**2) / (2 * self.arm1_len * d)) # angle btw. vector above and vector from g1.arm_pos to hinge_pos
        angle = delta + gamma # angle from g1.arm_pos to hinge point
        hx = self.g1.arm_pos.x + self.arm1_len*cos(angle)
        hy = self.g1.arm_pos.y + self.arm1_len*sin(angle)
        return PVector(hx, hy)

    def display(self):
        self.g1.display() # display gimbals
        self.g2.display()
        strokeWeight(1)
        fill(100)
        line(self.g1.arm_pos.x, self.g1.arm_pos.y, self.hinge_pos.x, self.hinge_pos.y) # hinge arms
        line(self.g2.arm_pos.x, self.g2.arm_pos.y, self.hinge_pos.x, self.hinge_pos.y)
        ellipse(self.hinge_pos.x, self.hinge_pos.y,5,5) # hinge point point
     
    def update(self):
        self.g1.update() # update gimbals
        self.g2.update()
        self.hinge_pos = self.get_hinge_pos() # update hinge location


class Gimbal(object):
    def __init__(self, pos, amp, angle=0, speed=.1, damp=1):
        self.pos = pos # center point
        self.amp = amp # amplitudes in x & y directions
        self.angle = angle
        self.arm_pos = self.get_arm_pos() # arm attachment point
        self.speed = speed
        self.damp = damp # dampening coefficient

    def get_arm_pos(self): 
        armx = self.pos.x + self.amp.x*cos(self.angle) 
        army = self.pos.y + self.amp.y*sin(self.angle)
        return PVector(armx, army)
        
    def update(self):
        self.angle += self.speed # apply rotation
        self.amp = self.damp * self.amp # apply dampening
        self.arm_pos = self.get_arm_pos() # update arm position
        
    def display(self):
        strokeWeight(1)
        stroke(100)
        noFill()
        ellipse(self.pos.x, self.pos.y, 2*self.amp.x, 2*self.amp.y) # body
        fill(100)
        ellipse(self.arm_pos.x, self.arm_pos.y,5,5) # arm attachment point

    
