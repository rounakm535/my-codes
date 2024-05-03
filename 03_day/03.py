# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bmi = weight/height**2
if bmi >18.5:
 print(f"Your bmi is {bmi}. You are underweight")
elif 18.5 < bmi > 25 :
 print(f"Your bmi is {bmi}. You have a normal weight")
elif 25 < bmi > 30 : 
 print(f"Your bmi is {bmi}. You are obese.")
else :
 print(f"Your bmi is {bmi}. You are clinically obese")
 