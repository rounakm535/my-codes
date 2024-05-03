# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
num_person = len(names)
name_choice = random.randint(0, num_person-1)
paying_person = names[name_choice]
print(paying_person + " is going to buy the meal today")