####### modify using return #########

enemies = 1

def increase_enemies():
    print(f"enemies inside function: {enemies}")
    return enemies + 1

print(f"enemies outside function(before modify): {enemies}")
enemies = increase_enemies()
print(f"enemies outside function(after modify): {enemies}")

""" another method is using a keyword global with the variable name inside the function. But that method is avoided because this leads to some change of values and errors unnecessarly"""

