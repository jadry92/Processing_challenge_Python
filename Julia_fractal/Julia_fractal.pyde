from Fractal_class import Julia,Julia_or3
record = False
ite = 10
j = Julia(ite)
def setup():
    global ite, j
    size(400,400)
    j.generate()
    
def keyPressed():
    global record
    if key == 'r' or key == 'R':
        record = not record

def draw():
    global ite, j, record
    background(255)
    translate(width/2,height/2)
    #print(j.ite)
    j.show()
    if record:
        saveFrame("/Users/johan/gif_img/frame-######.png")

            
