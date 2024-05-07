import turtle as t
import random

tim = t.Turtle()

########### Challenge 3 - Draw Shapes ########

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

def draw(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)

for side_n in range(3, 10):
    tim.color(random.choice(colours))
    draw(side_n)

screen = t.Screen()
screen.exitonclick()