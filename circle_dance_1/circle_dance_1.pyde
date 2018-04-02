
class WavyCircle(object):
    
    def __init__(self, radius, num_points):
        self.radius = radius
        self.num_points = num_points
        self.x_ = self.get_x_(radius, num_points)
        self.y_ = self.get_y_(radius, num_points)
        self.t = 0.0
        
        
    def get_x_(self, radius, num_points):
        global W, H
        x_ = []
        for p in range(num_points):
            a = p * 2 * PI / num_points
            x = W/2 + radius*cos(a)
            x_.append(x)
        return x_
            
    def get_y_(self, radius, num_points):
        global W, H
        y_ = []
        for p in range(num_points):
            a = p * 2 * PI / num_points
            y = H/2 + radius*sin(a)
            y_.append(y)
        return y_
    
    def display(self):
        stroke(0)
        fill(0)
        self.perturb()
        for i, x in enumerate(self.x_):
            y = self.y_[i]
            ellipse(x, y, 10, 10)
            
    def perturb(self):
        dt = 0.008
        noisemag = 70
        
        self.x_ = self.get_x_(self.radius, self.num_points)
        self.y_ = self.get_y_(self.radius, self.num_points)
        
        newx = []
        newy = []
        for i, x in enumerate(self.x_):
            y = self.y_[i]
            noize = noisemag*(noise(x,y,self.t) - 0.5)
            newx.append(x + noize)
            newy.append(y + noize)
            
        self.x_ = newx
        self.y_ = newy
            
        self.t += dt
            
            
W = 500
H = 500

circle1 = WavyCircle(100,36)

def setup():
    #global W, H
    size(W,H)
    smooth()          
    
def draw():
    background(255)
    circle1.display()