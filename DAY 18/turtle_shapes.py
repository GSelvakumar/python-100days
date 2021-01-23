import turtle as t
import random

sky = t.Turtle()
colours = ["firebrick", "dark magenta", "spring green", "medium blue", "orange red", "CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        sky.forward(100)
        sky.right(angle)

for shape_side_num in range(3, 11):
    sky.color(random.choice(colours))
    draw_shape(shape_side_num)
