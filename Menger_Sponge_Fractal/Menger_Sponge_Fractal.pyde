from Box import Box

angle=0
 
sponge = []
def setup():
    global sponge
    size(500,500,P3D)
    b = Box(0,0,0,200)
    sponge.append(b)
    translate(width/2,height/2)

def mousePressed():
    global sponge
    next = []
    newBoxes = []
    for i in sponge:
        newBoxes = i.generate()
        next.extend(newBoxes)     
    sponge = next
     
def draw():
    global angle, sponge
    background(50)
    stroke(255)
    noFill()
    lights()
    translate(width/2,height/2)
    angle += 0.01
    rotateX(angle)
    rotateY(angle*0.3)
    rotateZ(angle*0.5)
    for i in sponge:
        i.show()
        #translate(width/2,height/2)