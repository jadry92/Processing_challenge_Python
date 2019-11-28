from Snake import Snake,Food
s = Snake()
scl = 10
food = Food()
record = False
def setup():
    global food
    size(400,400)
    frameRate(scl) 
    food.generate(scl)  

def keyPressed():
    global record
    if keyCode == UP:
        s.dir(0,-1)
    elif keyCode == DOWN:
        s.dir(0,1)        
    elif keyCode == RIGHT:
        s.dir(1,0)
    elif keyCode == LEFT:
        s.dir(-1,0)
    elif key == 'r' or key == 'R':
        record = not record
    else:
        s.dir(0,0)    

def draw():
    global s, food, record
    background(51)
    s.show(scl) 
    s.update(scl)
    s.dead(scl)
    food.show(scl)
    s.eat(food,scl)
    
    if record :
        saveFrame("/Users/johan/gif_img/frame-######.png")
    
