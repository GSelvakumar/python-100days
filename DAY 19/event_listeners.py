from turtle import Turtle, Screen

sky = Turtle()
screen = Screen()


def move_forward():
    sky.forward(50)


screen.listen()
screen.onkey(key="space", fun=move_forward)
screen.exitonclick()
