import turtle as t

tim = t.Turtle()
tim.shape("turtle")
tim.color("red")

for _ in range(10):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()

screen = t.Screen()
screen.exitonclick()
