import turtle as t
import random

t.colormode(255)
sky = t.Turtle()
sky.speed("fastest")
"""no need of pen because dot method is used"""
sky.penup()
"""we can hide the turtle in case of look for the drawing"""
sky.hideturtle()
color_list = [(214, 157, 85), (33, 105, 151), (153, 75, 52), (125, 168, 199), (209, 134, 163),
              (156, 60, 81), (22, 39, 54), (212, 85, 61), (176, 162, 47), (200, 85, 119), (135, 184, 150),
              (56, 119, 90), (240, 213, 4), (25, 46, 37), (228, 167, 186), (64, 46, 34), (87, 157, 100), (9, 99, 75),
              (34, 166, 189), (40, 60, 102), (228, 175, 166), (179, 189, 213), (95, 126, 173), (68, 34, 44),
              (105, 42, 60), (170, 205, 179), (113, 43, 37), (156, 206, 217), (78, 69, 35), (3, 90, 115)]

"""angle to bring left side corner"""
sky.setheading(225)
"""bring the turtle forward for the starting point"""
sky.forward(300)
"""make a turn to 0 degree"""
sky.setheading(0)
no_of_dots = 100

for dot_count in range(1, no_of_dots + 1):
    sky.dot(20, random.choice(color_list))
    """distance between each dot"""
    sky.forward(50)

    if dot_count % 10 == 0:
        """dot should end after 10 dots and move to the next line(upwards)"""
        """Turtle should turn to 90 degree from the 0 degree line"""
        sky.setheading(90)
        """Turtle should move 50 in the 90 degree line"""
        sky.forward(50)
        """turn the turtle to 180 degree which is present in the 90 degree"""
        sky.setheading(180)
        """Move to the left corner 50 * 10 = 500"""
        sky.forward(500)
        """This will turn the turtle to right side and continue as mentioned"""
        sky.setheading(0)

screen = t.Screen()
screen.exitonclick()
