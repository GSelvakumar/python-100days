import turtle as t
import random

sky = t.Turtle()
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb_random = (r, g, b)
    return rgb_random


""" colours = ["firebrick", "dark magenta", "spring green", "medium blue", "orange red", "CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
"""
directions = [0, 90, 180, 270]
sky.pensize(15)
sky.speed("fastest")

for _ in range(200):
    sky.color(random_color())
    sky.forward(30)
    sky.setheading(random.choice(directions))
