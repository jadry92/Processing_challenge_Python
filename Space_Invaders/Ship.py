class Ship():
    def __init__(self,x):
        self.x = x
        
    def show(self):
        fill(255)
        rectMode(CENTER)
        rect(self.x,height-20,20,60)
        
        
    def move(self,dir):
        self.x += dir*5