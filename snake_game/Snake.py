class Snake():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.xspeed = 1
        self.yspeed = 0
        self.total = 0
        self.tail = [PVector(0,0)]
        
    def update(self,scl):
        #if self.total+1 == len(self.tail):
        if self.xspeed !=0 or self.yspeed != 0:
            for i in range(0,len(self.tail)-1):
                self.tail[i] = self.tail[i+1]
                
            self.tail[self.total-1] = PVector(self.x,self.y)
        
        #if self.xspeed !=0 or self.yspeed != 0:
        self.x = self.x + self.xspeed*scl
        self.y = self.y + self.yspeed*scl
        
        self.x = constrain(self.x, 0, width-scl)
        self.y = constrain(self.y, 0, height-scl)
   
    def dead(self,scl):
        for i in range(0,len(self.tail)-1):
            pos = self.tail[i]     
            if pos.x == self.x and pos.y == self.y:
                self.total = 0
                self.tail = [PVector(0,0)]
                break
                
    def show(self,scl):
        fill(255)
        for i in range(0,len(self.tail)-1):
            rect(self.tail[i].x, self.tail[i].y, scl, scl)
        rect(self.x, self.y, scl, scl)
        
    def dir(self, d_x, d_y):
        self.xspeed = d_x
        self.yspeed = d_y
        
        
    def eat(self, Food,scl):
        if Food.pos.x == self.x and Food.pos.y == self.y:
            self.tail.insert(0,PVector(self.x,self.y))
            self.total +=1
            Food.generate(scl)
                
class Food():
    def __init__(self):
        self.pos = PVector(0,0)
        
    def generate(self,scl):
        rows_x = floor(width/scl)
        cols_y = floor(height/scl)
        self.pos.x = floor(random(rows_x))*scl
        self.pos.y = floor(random(cols_y))*scl
    
    def show(self,scl):
        fill(255,0,100)
        rect(self.pos.x, self.pos.y, scl, scl)            