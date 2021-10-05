import turtle

turtle.shape('turtle')
def okr(r) :
	for i in range(100) :
    		turtle.forward(r)
    		turtle.left(180 - (180* (100-2) / 100))
n = int(input())
for i in range(n) :
	okr(2)
	turtle.right(360 / n)