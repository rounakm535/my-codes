from random import randint
from tkinter import *
from tkinter import simpledialog, messagebox

main = Tk()
main.withdraw()

random_number = randint(0,10)
print(random_number)

x = -1
while x != random_number:
    if x != -1:
        messagebox.showinfo("Wrong", "Wrong guess")

    x = simpledialog.askstring("Guess", "Enter a number: ")
    x = int(x)

    if x == random_number:
        messagebox.showinfo("Right", "You guessed correctly") 
        exit()

main.mainloop() 