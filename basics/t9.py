from turtle import *

speed('normal')

side = 5
shapesize(2,2)
for i in range(side):
    dot(25,'black')
    forward(100)
    pensize(side*i)
    left(360/side)
    dot(50,'red')

mainloop()
