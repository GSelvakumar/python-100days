programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again."
    }

#retrieving items from dictionary
print(programming_dictionary["Function"])

#adding new items to dictionary
programming_dictionary["Loop"] = "The action of doing something over and over again."
print(programming_dictionary["Function"])

#create an empty dictionary
empty_dictionary = {}

#delete an existing dictionary
#programming_dictionary = {}

#Edit an item in an dictonary
programming_dictionary["Bug"] = "A moth in your computer."
print(programming_dictionary)

#loop through a dictionary 
for key in programming_dictionary:
    print(key)  # prints the keys
    print(programming_dictionary[key])  # prints the values



