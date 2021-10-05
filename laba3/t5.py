from random import randint
import turtle

a = 200

turtle.penup()
turtle.goto(-a,-a)
turtle.pendown()
turtle.forward(2*a)
turtle.left(90)
turtle.forward(2*a)
turtle.left(90)
turtle.forward(2*a)
turtle.left(90)
turtle.forward(2*a)

number_of_turtles = 20
steps_of_time_number = 200

way = []
pool = [turtle.Turtle(shape='circle') for i in range(number_of_turtles)]
for unit in pool:
    unit.penup()
    unit.speed(50)
    unit.goto(randint(-a, a), randint(-a, a))
    angle = randint(0, 360)
    unit.left(angle)
    way.append(angle)

speed = []
for i in range(number_of_turtles):
    speed.append(randint(2,5))

for i in range(steps_of_time_number):
    for unit in pool:
        ind = pool.index(unit)
        unit.forward(speed[ind])
        if unit.pos()[0] < - a:
            unit.right(2*way[ind] - 180)
            way[ind] = way[ind] - (2*way[ind] - 180)
        if unit.pos()[0] > a:
            unit.left(180 - 2*way[ind])
            way[ind] = way[ind] + (180 - 2*way[ind])
        if unit.pos()[1] > a:
            unit.right(2*way[ind])
            way[ind] = -way[ind]
        if unit.pos()[1] < -a:
            unit.left(-2*way[ind])
            way[ind] = way[ind]-2*way[ind]