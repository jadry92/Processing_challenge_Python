class Drop():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.yspeed = 1
        self.lengt = 10
        
    def star(self):
        self.x = random(0,width)
        self.y = random(-400,-50)
        self.yspeed = random(4,10)
        self.lengt = random(4,10)
        
    def fall(self):
        self.y += self.yspeed
        self.yspeed += 0.1
        if self.y > height:
            self.y = random(-400,-50)
            self.yspeed = random(4,10)
        
    def show(self):
        line(self.x,self.y,self.x,self.y+self.lengt) 
        stroke(138, 43, 226)