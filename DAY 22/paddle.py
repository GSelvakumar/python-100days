from turtle import Turtle

class Paddle(Turtle):   #gets the properties of Turtle class

    def __init__(self, position):
        super.__init__()   #used to utilize the properties of Turtle class
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)