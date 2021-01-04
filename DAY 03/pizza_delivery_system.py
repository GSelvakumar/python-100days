print("Welcome to Python Pizza Deliveries!")

size = input("What size pizza do you want? S, M or L : ")
add_pepperoni = input("Do you want pepperoni? Y or N : ")
extra_cheese = input("Do you want extra cheese? Y or N : ")
bill = 0

if size == "S":
    bill += 150
    if add_pepperoni == "Y":
        bill += 20
elif size == "M":
    bill += 200
    if add_pepperoni == "Y":
        bill += 30
elif size == "L":
    bill += 250
    if add_pepperoni == "Y":
        bill += 20
else:
    print("please select a size for your pizza")

if extra_cheese == "Y":
    bill += 15

print(f"Your final bill is: ₹{bill}")





