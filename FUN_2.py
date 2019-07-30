import turtle
turtle.goto(0,0)

turtle.direction = None
def up():
    x,y = turtle.pos()
    turtle.goto(x,y+50)
    print("you pressed the up key")

turtle.onkey(up, "Up")
turtle.listen()

def down():
    x, y = turtle.pos()
    turtle.goto(x,y-50)

turtle.onkey(down, "Down")
turtle.listen()
    
def left():
    x,y = turtle.pos()
    turtle.goto(x-50,y)

turtle.onkey(left, "Left")
turtle.listen()

def right():
    x, y = turtle.pos()
    turtle.goto(x+50, y)

turtle.onkey(right, "Right")
turtle.listen()
