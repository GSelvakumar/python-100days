import random

test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

nameAsCSV = input("Give me everybody's names, separated by a comma. \n")
names = nameAsCSV.split(", ")

num_items = len(names)

random_choice = random.randint(0, num_items - 1)
random_choice_name = names[random_choice]

print(f"{random_choice_name} is going to buy the meal today!")

# In order to reduce the code this choice method also can be used.
# random_choice = random.choice(names)
# print(f"{random_choice} is going to buy the meal today!")


