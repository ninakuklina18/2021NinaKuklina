import turtle

turtle.shape('turtle')
a = 10                                       # Side length of the first square
for i in range(10) :
	for i in range(4) :
		turtle.forward(a)
		turtle.left(90)
	turtle.penup()
	turtle.forward(a+5)
	turtle.right(90)
	turtle.forward(5)
	a = a + 10
	turtle.left(180)
	turtle.pendown()
