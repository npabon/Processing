class Hitch(object):
    
    def __init__(self, motor1, motor2):
        self.m1 = motor1
        self.m2 = motor2
        # angle of vector from the arm attachment point of m1
        # to the hitch point
        self.angle = self.getAngle(self.m1, self.m2)
        self.x = self.m1.armx + self.m1.armlength*cos(self.angle)
        self.y = self.m1.army + self.m1.armlength*sin(self.angle)
        
        # store the initial point in the trajectory
        p0 = PVector(self.x, self.y)
        self.traj = [p0]
        
    def display(self, traj_only=True):
        if not traj_only:
            # motors
            self.m1.display()
            self.m2.display()
            # motor arms
            strokeWeight(1)
            line(self.m1.armx, self.m1.army, self.x, self.y)
            line(self.m2.armx, self.m2.army, self.x, self.y)
            # hitch point
            noFill()
            strokeWeight(2)
            ellipse(self.x, self.y,10,10)
        
        # trajectory
        strokeWeight(0.5)
        stroke(0)
        throwaway = 7
        if len(self.traj) > throwaway:
            beginShape()
            for p in self.traj[-2:]:
                vertex(p.x, p.y)
            endShape()
            
    def save_svg(self):
        background(255)
        strokeWeight(0.5)
        stroke(0)
        throwaway = 7
        if len(self.traj) > throwaway:
            fn = "spiro_params_.svg".format(len(self.traj))
            beginRecord(SVG, fn)
            beginShape()
            for p in self.traj[throwaway:]:
                vertex(p.x, p.y)
            endShape()
            endRecord()
        
        
    def update(self):
        self.m1.update()
        self.m2.update()
        self.angle = self.getAngle(self.m1, self.m2)
        self.x = self.m1.armx + self.m1.armlength*cos(self.angle)
        self.y = self.m1.army + self.m1.armlength*sin(self.angle)
        # store the new point in the trajectory
        p = PVector(self.x, self.y)
        self.traj.append(p)
        
    def getAngle(self, m1, m2):
        x1, y1, l1 = m1.armx, m1.army, m1.armlength
        x2, y2, l2 = m2.armx, m2.army, m2.armlength
        l3 = sqrt( (y2-y1)**2 + (x2-x1)**2 )
        
        # angle of vector from m1 to m2
        delta = asin( (y2-y1)/l3 )
        
        # angle between vector from m1 to m2 and vector
        # from m1 to hitch point
        gamma = acos( (l1**2 + l3**2 - l2**2)/(2*l1*l3) )
        
        return delta + gamma
        

class Motor(object):
    
    def __init__(self, x, y, rx, ry, pendulum, angle=0, speed=.1, armlength=100, damp=0.9999):
        self.x = x
        self.y = y
        self.rx = rx
        self.ry = ry
        self.angle = angle
        self.speed = speed
        self.armlength = armlength
        # arm attachment point
        self.armx = self.x + self.rx*cos(self.angle)
        self.army = self.y + self.ry*sin(self.angle)
        # the third pendulum, adds motion in x direction
        self.pendulum = pendulum
        self.dx = self.pendulum.x
        self.damp = damp
        
    # display the motor
    def display(self):
        #body
        strokeWeight(1)
        stroke(100)
        noFill()
        ellipse(self.x+self.dx, self.y, 2*self.rx, 2*self.ry)
        # arm attachment point
        strokeWeight(2)
        ellipse(self.armx, self.army,10,10)
        
    
    def update(self):
        self.pendulum.update()
        self.dx = self.pendulum.x
        self.angle += self.speed
        self.rx = self.damp * self.rx
        self.ry = self.damp * self.ry
        self.armx = self.x + self.dx + self.rx*cos(self.angle)
        self.army = self.y + self.ry*sin(self.angle)
        
# a pendulum class to move the motors in the x direction
class Pendulum(object):
    
    def __init__(self, amplitude, angle, speed, damp=0.9999):
        self.amplitude = amplitude
        self.speed = speed
        self.angle = angle
        self.x = 0
        self.damp = damp
        
    def update(self):
        self.angle += self.speed
        self.amplitude = self.damp * self.amplitude
        self.x = self.amplitude * cos(self.angle)
