from turtle import *

speed('fastest')
colors = ['red','blue','pink','green','yellow','black']
s = len(colors)
for i in range(500):
    c = colors[i % s]
    pencolor(c)
    fd(i + 6)
    lt(360/s)
    for j in range(s):
        fd(100)
        lt(360/s)

mainloop()