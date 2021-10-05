import turtle as tur
dt = 0.01
Vx = 30
Vy = 40
x = -200
y = 0
ay = -10
ax = 0
tur.goto(200,0)
for i in range(10000):
    tur.goto(x, y)
    x += Vx*dt + ax*dt**2
    y += Vy*dt + ay*dt**2
    ay = -10 - Vy*0.1
    ax = -Vx*0.1
    Vy += ay*dt
    Vx += ax*dt
    if y < 0:
        Vy = -Vy