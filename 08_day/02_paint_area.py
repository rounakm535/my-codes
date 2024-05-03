# Write your code below this line 👇
import math

def paint_calc(height, width, cover) :
    area = height * width
    req = area / cover
    print(math.ceil(req))


# Write your code above this line 👆
# Define a function called paint_calc() so the code below works.   

# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall")) # Height of wall (m)
test_w = int(input("Widht of wall")) # Width of wall (m)
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
