import turtle as t
from doctest import script_from_examples
from turtle import Screen
import random

tim = t.Turtle()
t.colormode(255)
def random_color():
    r = random.randint (0,255)
    g = random.randint (0,255)
    b = random.randint (0,255)
    color = (r, g, b)
    return color

tim.speed("fastest")

def draw_spirograph(size):
    for _ in range(int(360/size)):

        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading()+ size)

draw_spirograph(1)




























screen = Screen()
screen.exitonclick()







