from tkinter import *
from tkinter import simpledialog, messagebox
from functools import partial 

main = Tk()
main.geometry("250x250")
main.title("Tic Tac Toe")

field  = [ ' ', ' ', ' ',
           ' ', ' ', ' ',
           ' ', ' ', ' ' ]

current_player = 1
buttons = []

def btn_click(x):
    global buttons
    global current_player 
    global field

    if current_player == 1:
        buttons[x]["text"] = 'x'
        field[x] = 'x'
        current_player = 0
    else:
        buttons[x]["text"] = 'o'
        field[x] = 'o'
        current_player = 1
    
    check(field)

frame = Frame(main)

index = 0
for x in range(0,3):
    for y in range(0,3):
        b = Button(frame, text=field[index], command=partial(btn_click, index), width=6, height=4)
        b.grid(row=x, column=y)
        buttons.append(b)
        index = index + 1


frame.pack(fill="both")

def endgame(field, player):
    messagebox.showinfo("Winner", player + " wins")
    exit()    

def check(field):
    players = [ 'x', 'o' ]

    for player in players:
        if field[0] == player and field[1] == player and field[2] == player:
            endgame(field, player)
        elif field[3] == player and field[4] == player and field[5] == player:
            endgame(field, player)
        elif field[6] == player and field[7] == player and field[8] == player:
            endgame(field, player)
        elif field[0] == player and field[3] == player and field[6] == player:
            endgame(field, player)
        elif field[1] == player and field[4] == player and field[7] == player:
            endgame(field, player)
        elif field[2] == player and field[5] == player and field[8] == player:
            endgame(field, player)
        elif field[0] == player and field[4] == player and field[8] == player:
            endgame(field, player)
        elif field[2] == player and field[4] == player and field[6] == player:
            endgame(field, player)

main.mainloop()