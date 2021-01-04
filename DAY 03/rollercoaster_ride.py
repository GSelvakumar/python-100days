print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        print("Please pay ₹10")
    elif age <= 18:
        print("Please pay ₹20")
    else:
        print("Please pay ₹35")
else:
    print("Sorry, you have to grow taller before you can ride.")

