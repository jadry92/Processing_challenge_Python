from star import Star
n=600
record = False
star =[Star() for i in range(0,n)]

def setup():
    size(600,600)
    for i in range(0,len(star)):
        star[i].initiation()

def keyPressed():
    global record
    if key == 'r' or key == 'R':
        record = not record

def draw():
    background(0)
    translate(width/2,height/2)
    for i in range(0,len(star)):
        star[i].update()
        star[i].show()
    
    if record :
        saveFrame("/Users/johan/gif_img/frame-######.png")
        
