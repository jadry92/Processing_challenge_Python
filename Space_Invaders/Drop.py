class Drop():
    def __init__(self,x,y,r):
        self.x = x
        self.y = y
        self.r = r
        self.Del_st = False
        
    def show(self):
        noStroke()
        fill(150,0,200)
        ellipse(self.x,self.y,self.r,self.r)
        
    def move(self):
        self.y = self.y -  5 
        
    def hits(self,Flower):
        dis = dist(self.x, self.y, Flower.x, Flower.y)
        if dis < self.r + Flower.r/2 :
            Re = True
        else:
            Re = False
        return Re
    
    def evaporate(self):
        self.Del_st = True