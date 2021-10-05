import turtle as t

def l(n):
     for i in range(n):
        t.forward(100)
        t.left(180-180/n)
t.goto(0,0)
n=int(input())
zvezda(n)
if n%2==0:
     t.goto(0,0)
	
