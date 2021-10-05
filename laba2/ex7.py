import turtle
turtle.shape('turtle')
k = 1
fir = 0.1
fid = fir*180/3.1415
for i in range(1000):
    r=k * fir
    turtle.forward(r)
    turtle.left(fid)
    fir=fir+0.1
     
