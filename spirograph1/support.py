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
        
    def display(self):
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
        strokeWeight(0.8)
        stroke(0)
        noFill()
        beginShape(POINTS)
        for p in self.traj:
            vertex(p.x, p.y)
        endShape()
        
    def spin(self):
        self.m1.spin()
        self.m2.spin()
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
    
    def __init__(self, x, y, r, angle=0, speed=.1, armlength=100):
        self.x = x
        self.y = y
        self.r = r
        self.angle = angle
        self.speed = speed
        self.armlength = armlength
        # arm attachment point
        self.armx = self.x + self.r*cos(self.angle)
        self.army = self.y + self.r*sin(self.angle)
        
    # display the motor
    def display(self):
        #body
        strokeWeight(1)
        stroke(100)
        noFill()
        ellipse(self.x,self.y,2*self.r,2*self.r)
        # arm attachment point
        strokeWeight(2)
        ellipse(self.armx, self.army,10,10)
        
    # spin the motor
    def spin(self):
        self.angle += self.speed
        self.armx = self.x + self.r*cos(self.angle)
        self.army = self.y + self.r*sin(self.angle)
