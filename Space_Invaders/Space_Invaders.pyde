from Ship import Ship
from Flower import Flower
from Drop import Drop
record = False
D = []

def setup():
    global S,flowers,D
    size(600,400)
    S = Ship(width/2)
    #D = Drop(width/2,360) 
    flowers = [Flower((width/6)*i+(width/12),100,35) for i in range(0,6)]
     
def draw():
    #global S,flowers
    background(51)
    S.show()
    for bols in D:
        bols.show()
        bols.move()
        for flo in flowers:
            if bols.hits(flo) == True:
                flo.grow()
                bols.evaporate()
                print("Boom x = ",bols.Del_st)
                 
            
    for flo in flowers:
        flo.show()
        flo.move()
        if flo.x+flo.r/2 > 600:
            flo.x = (width/6)+(width/12)
        
    for bols in D:
        if bols.Del_st == True:
            D.remove(bols)
            
    if record :
        saveFrame("/Users/johan/gif_img/frame-######.png")    
################################################    
def keyPressed():
    global record
    if keyCode == UP:
        print('nothing')
    elif key == 'r' or key == 'R':
        record = not record
    elif key == ' ':
        tm = Drop(S.x,height-60,8)
        D.append(tm)
    elif keyCode == DOWN:
        print('nothing')
    elif keyCode == RIGHT:
        S.move(1)
    elif keyCode == LEFT:
        S.move(-1)
    else:
        S.move(0) 
