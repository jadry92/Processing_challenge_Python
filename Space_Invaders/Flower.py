class Flower():
    def __init__(self,x,y,r):
        self.x = x
        self.y = y
        self.r = r
        self.xsp = 1
        self.ysp = 0
        
    def show(self):
        fill(255,0,100)
        ellipse(self.x,self.y,self.r,self.r)
        
    def grow(self):
        self.r = self.r+1
        
    def move(self):
        self.x = self.x + self.xsp 
        #self.y = self.y + self.ysp 