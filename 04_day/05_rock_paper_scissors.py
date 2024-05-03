rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

import random

choice0 = input("Type 0 for rock, 1 for paper, 2 for scissors")
choice = int(choice0)

if choice == 0 :
    print ("You have selected rock")
    print(rock)
elif choice == 1 :
    print("You have selected paper")
    print(paper)
elif choice == 2 :
    print("You have selected scissors")
    print(scissors)
else :
    print("enter a valid choice")


comp_choice = random.randint(0,2)


if comp_choice == 0 :
    print ("Computer has selected rock")
    print(rock)
elif comp_choice == 1 :
    print("Computer has selected paper")
    print(paper)
elif comp_choice == 2 :
    print("Computer has selected scissors")
    print(scissors)
else :
    print("enter a valid choice")



if comp_choice == choice : 
    print("It is officially a draw")

elif comp_choice == 0 and choice == 1 : 
    print("You won")

elif comp_choice == 1 and choice == 0 :
    print("Computer won")

elif comp_choice == 2 and  choice == 1 :
    print("Computer won")

elif comp_choice == 1 and choice == 2 :
    print("You won")

