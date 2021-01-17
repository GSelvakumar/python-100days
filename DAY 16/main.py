# from turtle import Turtle, Screen
#
# tim = Turtle()
# print(tim)
# tim.shape("turtle")
# tim.color("coral")
# tim.forward(100)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

# -----------------------------------------

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"
print(table)
