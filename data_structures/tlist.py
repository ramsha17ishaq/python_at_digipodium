from turtle import *

speed('fastest')
colors = ['red','blue','voilet','pink']

s = len(colors)
for i in range(500):
    c = colors[i % s]
    pencolor(c)
    fd(i + 5)
    lt(360/s)
    for j in range(s):
        fd(100)
        lt(60)

mainloop()