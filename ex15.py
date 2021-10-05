import tkinter
import math
master = tkinter.Tk()
canvas = tkinter.Canvas(master, bg='white', height=600, width=600)
canvas.pack()
 
r = 100
 
n = int(input('Количество лучей:'))
 
for k in range(n):
    if n % 2 == 0:
        k1 = (k + n / 2 - 1) % n
    else:
        k1 = (k + (n - 1) / 2) % n
 
    p1 = (300 + r * math.cos(2 * 3.14 * k / n), 300 + r * math.sin(2 * 3.14 * k / n))
    p2 = (300 + r * math.cos(2 * 3.14 * k1 / n), 300 + r * math.sin(2 * 3.14 * k1 / n))
    canvas.create_line(p1, p2, fill = 'red')
 
master.mainloop()