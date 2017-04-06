class Box():
    def __init__(self,x,y,z,radio_r):
        self.pos = PVector(x,y,z)
        self.r = radio_r
        
    def show(self):
        pushMatrix()
        translate(self.pos.x,self.pos.y,self.pos.z)
        noStroke()
        fill(255)
        box(self.r)
        popMatrix()
        
    def generate(self):
        boxes = []
        for x in range(-1,2):
            for y in range(-1,2):
                for z in range(-1,2):
                    sum = abs(x) + abs(y) + abs(z)
                    newR = self.r/3
                    if sum > 1 :
                        b = Box(self.pos.x+x*newR,self.pos.y+y*newR,self.pos.z+z*newR,newR)
                        boxes.insert(len(boxes),b) 
        return boxes