class Star():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.z = 0
        self.pz =0
        
    def initiation(self):
        self.x = random(-width/2,width/2)
        self.y = random(-height/2,height/2)
        self.z = random(width)
        self.pz = self.z
        
    def show(self):
        fill(255)
        #noStroke();
        sx = map(self.x/self.z, 0, 1, 0, width)
        sy = map(self.y/self.z, 0, 1, 0, height)
        r = map(self.z , 0, width, 16, 2)
        #ellipse(sx,sy,r,r)
        px = map(self.x/self.pz, 0, 1, 0, width)
        py = map(self.y/self.pz, 0, 1, 0, height)
        stroke(255)
        line(px,py,sx,sy)

    def update(self):
        self.pz = self.z
        self.z -=10
        if self.z < 1:
            self.x = random(-width/2,width/2)
            self.y = random(-height/2,height/2)
            self.z = random(width)
            self.pz = self.z
            
        
         
            