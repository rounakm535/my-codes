import turtle as t
import random

tim = t.Turtle()
t.colormode(255)


def r_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rand_colour = (r, g, b)
    return rand_colour


tim.speed("fastest")


def draw(gap):
    for _ in range(int(360 / gap)):
        tim.color(r_colour())
        tim.circle(100)
        tim.setheading(tim.heading() + gap)


draw(5)

screen = t.Screen()
screen.exitonclick()
