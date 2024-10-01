import turtle
 
 
def start(x: float):
    turtle.clear()
    turtle.penup()
    x = x if x < 0 else -x
    turtle.goto(x, 0)
    turtle.pendown()
 
 
def curve_minkowski(length: float, iterations: int): 
    if iterations == 0:
        turtle.forward(length * 4)
    else:
        curve_minkowski(length/4, iterations - 1)
        turtle.left(90)
        curve_minkowski(length/4, iterations - 1)
        turtle.right(90)
        curve_minkowski(length/4, iterations - 1)
        turtle.right(90)
        curve_minkowski(length/4, iterations - 1)
        curve_minkowski(length/4, iterations - 1)
        turtle.left(90)
        curve_minkowski(length/4, iterations - 1)
        turtle.left(90)
        curve_minkowski(length/4, iterations - 1)
        turtle.right(90)
        curve_minkowski(length/4, iterations - 1)
 
 
LENGTH = 100
 
ITERATION = 3
 
start(LENGTH * 2)
 
curve_minkowski(LENGTH, ITERATION)
 
turtle.exitonclick()  