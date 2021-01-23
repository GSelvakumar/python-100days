from turtle import Turtle, Screen

sky = Turtle()
screen = Screen()


def move_forward():
    sky.forward(10)


def move_backward():
    sky.backward(10)


def move_left():
    """sky.left(10) another option"""
    new_heading = sky.heading() + 10
    sky.setheading(new_heading)


def move_right():
    """sky.right(10) another option"""
    new_heading = sky.heading() - 10
    sky.setheading(new_heading)


def clear():
    sky.clear()
    sky.penup()
    sky.home()
    sky.pendown()


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="d", fun=move_right)
screen.exitonclick()
