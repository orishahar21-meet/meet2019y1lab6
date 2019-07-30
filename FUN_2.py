import turtle
turtle.goto(0,0)

turtle.direction = None
def up():
    turtle.forward(10)
    print("you pressed the up key")
    turtle.direction = "Up"

turtle.onkey(up, "Up")
turtle.listen()

def down():
    
