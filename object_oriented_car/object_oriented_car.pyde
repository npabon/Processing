class Car(object):
    
    def __init__(self, c, xpos, ypos, xspeed):
        self.c = c   
        self.xpos = xpos
        self.ypos = ypos
        self.xspeed = xspeed

        
    def display(self):
        stroke(0)
        fill(self.c)
        rectMode(CENTER)
        rect(self.xpos, self.ypos, 20, 10);
        
    def drive(self):
        self.xpos += self.xspeed
        if self.xpos > width:
            self.xpos = 0
            
            
            
myCar1 = Car(color(255, 0, 0), 0, 100, 2)
myCar2 = Car(color(0, 255, 255), 0, 10, 1)

def setup():
    size(200,200)

def draw(): 
  background(255)
  myCar1.drive()
  myCar1.display()
  myCar2.drive()
  myCar2.display()