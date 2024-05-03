
field  = [ '1', '2', '3',
           '4', '5', '6',
           '7', '8', '9' ]

current_player = 1

def draw(field):
    print(f"{field[0]} {field[1]} {field[2]}")
    print(f"{field[3]} {field[4]} {field[5]}")
    print(f"{field[6]} {field[7]} {field[8]}")
    #print("\n")

def endgame(field, player):
    draw(field)
    print(player + " wins")
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

def get_input():
    global current_player
    print("\n")
    x = input(f"Player {current_player}, where? ")
    x = int(x)
    print(x)
    return x

def switch_player():
    global current_player
    if current_player == 1:
        field[ (x-1) ] = 'x'
        current_player = 0
    else:
        field[ (x-1) ] = 'o'
        current_player = 1

draw(field)

while True:
    x = get_input()
    switch_player()
    check(field)
    draw(field)
