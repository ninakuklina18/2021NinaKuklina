import turtle

turtle.shape('turtle')
def dug(r) :
	for i in range(50) :
    		turtle.forward(r)
    		turtle.right(180 - (180* (100-2) / 100))
turtle.left(90)
r_big = 2
r_small = 0.5
for i in range(5) :
	dug(r_big)
	dug(r_small)
dug(r_big)