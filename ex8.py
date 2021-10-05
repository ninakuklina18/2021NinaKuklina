import turtle

turtle.shape('turtle')
n = 5
a = 5
for i in range(50) :
	for i in range(2) :
		turtle.forward(n)
		turtle.left(90)
	turtle.right(90)
	turtle.forward(a)
	turtle.left(90)
	n = n + a
