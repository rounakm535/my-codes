# Input a list of student scores
student_scores = input("The scores of students").split()
print(student_scores)
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

# Write your code below this row 👇
highest_score = 0
for score in student_scores:
  if score > highest_score:
    highest_score = score

print(f"The highest score in the class is : {highest_score}")
