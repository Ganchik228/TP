import turtle

turtle.tracer(1)
turtle.penup()
turtle.setposition(-150, 0)
turtle.pendown()

axiom, tempAx, logic, iterations = 'F', '', {'F': 'F-F+F+FF-F-F+F'}, 3

for i in range(iterations):
    for j in axiom:
        tempAx += logic[j] if j in logic else j
    axiom, tempAx = tempAx, ''

for k in axiom:
    if k == '+':
        turtle.left(90)
    elif k == '-':
        turtle.right(90)
    else:
        turtle.forward(5)

turtle.update()
turtle.mainloop()