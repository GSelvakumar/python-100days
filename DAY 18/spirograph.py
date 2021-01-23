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


sky.speed("fastest")


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        sky.color(random_color())
        sky.circle(100)
        sky.setheading(sky.heading() + size_of_gap)


draw_spirograph(5)
screen = t.Screen()
screen.exitonclick()
