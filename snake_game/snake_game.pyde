from Snake import Snake,Food
s = Snake()
scl = 10
food = Food()
def setup():
    global food
    size(400,400)
    frameRate(scl) 
    food.generate(scl)  

def keyPressed():
    if keyCode == UP:
        s.dir(0,-1)
    elif keyCode == DOWN:
        s.dir(0,1)        
    elif keyCode == RIGHT:
        s.dir(1,0)
    elif keyCode == LEFT:
        s.dir(-1,0)
    else:
        s.dir(0,0)    

def draw():
    global s, food
    background(51)
    s.show(scl) 
    s.update(scl)
    s.dead(scl)
    food.show(scl)
    s.eat(food,scl)
    