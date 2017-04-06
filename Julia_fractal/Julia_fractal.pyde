from Fractal_class import Julia,Julia_or3

ite = 20
j = Julia(ite)
def setup():
    global ite, j
    size(300,300)
    
    j.generate() 
    
        
def draw():
    global ite, j
    background(255)
    #noStroke()
    translate(width/2,height/2)
    #print(j.ite)
    j.show()
#    j.ite += 1
#    if j.ite > 20:
#        j.ite = 1
    #j.generate()
    #fill(0)

            