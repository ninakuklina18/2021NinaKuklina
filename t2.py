import turtle as tur
import math

def paint(a):
    for i in a:
        tur.right(i[0])
        tur.forward(i[1])

def one():
    tur.color('blue')
    tur.right(90)
    tur.penup()
    tur.forward(50)
    tur.pendown()

    a =[(-135, math.sqrt(2)*50), (135, 100), (180, 100), (90,0)]
    paint(a)

    tur.penup()
    tur.forward(30)
    tur.pendown()

def four():
    tur.color('blue')

    a = [(90, 50), (-90, 50), (90, 50), (180, 100), (90,0)]
    paint(a)

    tur.penup()
    tur.forward(30)
    tur.pendown()

def seven():
    tur.color('blue')

    a = [(0, 50), (135, math.sqrt(2) * 50), (-45, 50), (-180, 0)]
    paint(a)

    tur.penup()
    tur.forward(100)
    tur.right(90)
    tur.forward(80)
    tur.pendown()

def zero():
    tur.color('blue')

    a = [(90, 100), (-90, 50), (-90, 100), (-90, 50)]
    paint(a)

    tur.penup()
    tur.right(180)
    tur.forward(80)
    tur.pendown()

with open('movies') as f:
    s = list(map(int, f.read().split()))

for i in s:
    if i == 1:
        one()
    if i == 0:
        zero()
    if i == 7:
        seven()
    if i == 4:
        four()