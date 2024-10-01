import turtle


def minkowski_curve(rank: int, length: float) -> None:
    if rank > 0:
        turtle.right(30)
        minkowski_curve(rank - 1, length / 2)
        turtle.left(90)
        minkowski_curve(rank - 1, length / 2)
        turtle.right(90)
        minkowski_curve(rank - 1, length / 2)
        turtle.left(30)
    else:
        turtle.forward(length)


def minkowski_sausage(rank: int, length: float) -> None:
    for i in range(0, 4):
        minkowski_curve(rank, length)
        turtle.right(90)


turtle.speed(0)
turtle.penup()
turtle.back(150)
turtle.pendown()
minkowski_sausage(10, 1000)
turtle.done()