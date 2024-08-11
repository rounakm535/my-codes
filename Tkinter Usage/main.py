from tkinter import  *

window = Tk()
window.title("Developed by Rounak")
window.minsize(width= 600, height= 600)

my_label = Label(text= "Me label", font=("Arial", 24, "bold"))
my_label.pack()


my_label["text"] = "New text"
my_label.config(text = "New Text")


def click():
    print("I got Clicked..")
    new_txt = inpt.get()
    my_label.config(text= new_txt)


button = Button(text="Click Here", command= click)
button.pack()

inpt = Entry(width = 10)
inpt.pack()
ion = inpt.get()
print(ion)


window.mainloop()