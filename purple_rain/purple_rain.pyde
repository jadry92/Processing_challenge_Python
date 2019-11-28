#colors 
#purple = (138, 43, 226) 
from Drop import Drop
record = False
Rain = []
def setup():
    global Rain
    size(400,400)
    for i in range(0,200):
        Rain.append(Drop())
        Rain[i].star()
    print(Rain)

def keyPressed():
    global record
    if key == 'r' or key == 'R':
        record = not record

def draw():
    global Rain
    background(230, 230, 250) 
    for i in range(0,200):
        #print(Rain[i].x)
        Rain[i].show()
        Rain[i].fall()
    
    if record :
         saveFrame("/Users/johan/gif_img/frame-######.png")
