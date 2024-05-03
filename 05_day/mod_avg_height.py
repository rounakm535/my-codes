# Input a Python list of student heights
student_heights = input("The height of students: ").split()

# Check if the input is empty
if not student_heights:
    print("Please enter at least one student height.")
    exit()

# Convert all elements in the list to integers
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

# Calculate the total height and number of students
total_height = 0
number_of_students = len(student_heights)

# Check if the number of students is greater than zero
if number_of_students == 0:
    print("There are no students.")
    exit()

# Calculate the average height
average_height = round(total_height / number_of_students)

# Print the results
print(f"Total height: {total_height}cm")
print(f"Number of students: {number_of_students}")
print(f"Average height: {average_height}cm")
