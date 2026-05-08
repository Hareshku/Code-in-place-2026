from karel.stanfordkarel import *

"""
Karel should fill the whole world with beepers.
"""


def main():
    do_one_row()
    move_up()
    go_to_end()
def do_one_row():
    while front_is_clear():
        put_beeper()
        move()
    put_beeper()
    turn_around()
    return_to_base()
    turn_right()

def move_up():
    while front_is_clear():
        move()
        turn_right()
        do_one_row()

def turn_around():
    turn_left()
    turn_left()

def return_to_base():
    while front_is_clear():
        move()

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def go_to_end():
    turn_right()
    while front_is_clear():
        move()


# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()