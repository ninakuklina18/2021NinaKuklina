import turtle

turtle.shape('turtle')
n = 360
for i in range(n) :
    turtle.forward(1)
    turtle.left(180 - (180* (n-2) / n))
    
