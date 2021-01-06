student_height = input("Enter a list of student heights").split()
for n in range(0, len(student_height)):
    student_height[n] = int(student_height[n])
print(student_height)

total_height = 0
for height in student_height:
    total_height += height

no_of_students = 0
for student in student_height:
    no_of_students += 1
avg_height = round(total_height / no_of_students)
print(avg_height)




