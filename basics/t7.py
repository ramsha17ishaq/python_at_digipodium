from turtle import *

speed('fastest')
pencolor('red')
i = 5
while True:
    circle(i,i)
    left(45)
    i += 5
    if i > 1000:
        break

