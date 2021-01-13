########### Scope ############

enemies = 1
def increase_enemies():
    enemies = 3
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

######### Local Scope ##########

def drink_potion():
    potion_strength = 2
    print(potion_strength)

drink_potion()
#print(potion_strength) --> it will gives error

######### Global Scope ##########

player_health = 10
def drink_potion1():
    potion_strength = 2
    print(player_health)

drink_potion1()