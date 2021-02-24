#with is used to open and close the file
# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)

with open("my_file.txt", mode="a") as file:
    file.write("\n New text.")