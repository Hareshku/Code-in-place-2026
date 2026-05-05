from karel.stanfordkarel import *

# File: shelter.py
# -----------------------------
# The warmup program defines a "main"
# function which should make Karel 
# move to the beeper, pick it up, and
# return home.
def main():
    reach_spot()
    pick_beeper()
    move()
    turn_left()
    reach_spot()
    put_beeper()
    turn_around()
    return_to_origin()
    turn_around()

def reach_spot():
    move()
    move()
    
def turn_around():
    turn_left()
    turn_left()

def return_to_origin():
    move_to_wall()
    turn_right()
    move_to_wall()

    

def move_to_wall():
    while front_is_clear():
        move()
def turn_right():
    turn_left()
    turn_left()
    turn_left()

    
    
    
# don't edit these next two lines
# they tell python to run your main function
if __name__ == '__main__':
    main()