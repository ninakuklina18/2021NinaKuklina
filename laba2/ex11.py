import turtle

turtle.shape('turtle')
def okr(r) :
	for i in range(100) :
    		turtle.forward(r)
    		turtle.left(180 - (180* (100-2) / 100))
turtle.right(90)
r=2
for i in range(10) : 
	for i in range(2) :
		okr(r)
		turtle.right(180)
	r = r + 0.5
