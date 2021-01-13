"""Python has no blockscope, means the variables created in the conditional and looping stmts can be used as a global scope"""

game_level = 3
enemies = ["Skeleton", "Zombie", "Alien"]
if game_level < 5:
    new_enemy = enemies[0]

print(new_enemy)
