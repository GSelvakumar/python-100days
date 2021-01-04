print("Welcome to the Theme Park")
print("Here is the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 10
        print("Child tickets are ₹10")
    elif age <= 18:
        bill = 20
        print("Youth tickets are ₹20")
    else:
        bill = 35
        print("Adult tickets are ₹35")

    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y":
        bill += 3

    print(f"Your final bill is {bill}") 

else:
    print("Sorry, you have to grow taller before you can ride.")

print("Thank you for coming!")


