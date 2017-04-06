from star import Star
n=600
star =[Star() for i in range(0,n)]

def setup():
    size(600,600)
    for i in range(0,len(star)):
        star[i].initiation()


def draw():
    background(0)
    translate(width/2,height/2)
    for i in range(0,len(star)):
        star[i].update()
        star[i].show()
    
        