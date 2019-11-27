from Fractal_class import Julia,Julia_or3

ite = 90
j = Julia(ite)
def setup():
    global ite, j
    size(600,600)
    j.generate()
    
        
def draw():
    global ite, j
    background(255)
    translate(width/2,height/2)
    #print(j.ite)
    j.show()
    #j.ite += 1
    #if j.ite > 20:
    #j.ite = 1
    #j.generate()
    #fill(0)

            