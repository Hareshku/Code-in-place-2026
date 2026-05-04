from karel.stanfordkarel import *

"""
Karel should finish the puzzle by picking up the last beeper 
(puzzle piece) and placing it in the right spot. Karel should 
end in the same position Karel starts in -- the bottom left 
corner of the world.
"""
def reach_spot():
    for i in range(2):
        move()
def turn_around():
    for i in range(2):
        turn_left()

def turn_right():
    for i in range(3):
        turn_left()

def move_to_wall():
    while front_is_clear():
        move()

def main():
    reach_spot()
    pick_beeper()
    move()
    turn_left()
    reach_spot()
    turn_around()
    put_beeper()
    move_to_wall()
    turn_right()
    move_to_wall()
    turn_around()



# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()