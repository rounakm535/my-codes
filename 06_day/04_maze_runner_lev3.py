def turn_around():
    turn_left()
    turn_left()

def turn_right():
     turn_left()
     turn_left()
     turn_left()

def pass_hurdle():
        turn_left()
        while wall_on_right(): 
            move()

        turn_right()
        move()
        turn_right()
        
        while front_is_clear():
            move()
            
        turn_left()

while at_goal() != True:
            
        if front_is_clear() == True:
            move()

        if wall_in_front() == True:
            pass_hurdle()  