import turtle

turtle.shape('turtle')
n = int(input())
for i in range(n) :
    turtle.forward(90)
    turtle.right(180)
    turtle.stamp()
    turtle.forward(90)
    turtle.right(180)
    turtle.right(360 / n)
     
