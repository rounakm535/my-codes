def turn_around():
    turn_left()
    turn_left()

def turn_right():
     turn_left()
     turn_left()
     turn_left()
    
#draw square
def pass_hurdle():
       
        turn_left()
        move()
        turn_right()
        move()
        turn_right()
        move()
        turn_left()

while at_goal() != True:
            
        if front_is_clear() == True:
            move()

        if wall_in_front() == True:
            pass_hurdle()

    
    