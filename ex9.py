import turtle
import math

turtle.shape('turtle')
def pol(n,r) :
    turtle.right(180)
    turtle.right(90 * (n-2) / n)
    for i in range(n) :
        turtle.forward(r)
        turtle.left(180)
        turtle.right(180 * (n-2) /n)
    turtle.penup()
r = 20
n = 3
turtle.goto(0,0)
for i in range(10):
    turtle.penup()
    turtle.goto(0,0)
    turtle.setheading(0)
    turtle.forward(0.5 * r / math.sin(math.pi/n))
    turtle.pendown()
    pol(n,r)
    r = r + 10 
    n = n + 1
