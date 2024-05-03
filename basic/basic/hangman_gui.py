from tkinter import *
from tkinter import simpledialog, messagebox
from PIL import Image, ImageTk

main = Tk()
main.title("Hangman")
main.geometry("800x600")

imageList = []
for i in range(1,8):
    imageList.append( Image.open("images/hangman0" + str(i) + ".png"))

#image1 = Image.open("images/hangman01.png")
test = ImageTk.PhotoImage(imageList[0])
label1 = Label(image=test)
label1.image = test
label1.place(x=0, y=0)

MAX_TRIES = 6
no_guess = 0

word = "goodmorning"
word = word.lower()
print(word)

while True:
   key = simpledialog.askstring("Guess", "Guess a letter: ")
   if key in word:
       messagebox.showinfo("Hangman", "word cointains " + key)
       word = word.replace(key,"")
       print(len(word))
       if len(word) == 0:
           messagebox.showinfo("Hangman", "You win")
           break
   else:
       messagebox.showinfo("Hangman", "wrong")
       no_guess = no_guess + 1
       
       test = ImageTk.PhotoImage(imageList[no_guess])
       label1 = Label(image=test)
       label1.image = test
       label1.place(x=0, y=0)

       if no_guess >= MAX_TRIES:
           messagebox.showinfo("Hangman", "You lose")
           break