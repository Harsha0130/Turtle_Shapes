from turtle import Turtle, Screen
from random import choice

colors = ["red", "blue", "green", "black", "pink", "grey", "brown", "orange", "yellow"]
tim = Turtle()
for i in range(8):
    j = 3 + i
    a = 360 / j
    tim.color(choice(colors))
    for _ in range(j):
        tim.forward(100)
        tim.right(a)

tim.forward(100)




scr = Screen()
scr.exitonclick()