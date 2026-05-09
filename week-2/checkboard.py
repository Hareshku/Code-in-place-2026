from karel.stanfordkarel import *


def fill_col():
    
    put_beeper()
    while front_is_clear():
        if front_is_clear():
            move()
        if front_is_clear():
            move()
            put_beeper()
def reset():
    turn_around()
    while front_is_clear():
        move()
    turn_left()
    if beepers_present():

        if front_is_clear():
            move()
            turn_left()
            move()
    else:
        if front_is_clear():
            move()
            turn_left()
        

def turn_around():
    turn_left()
    turn_left()

def come_back_home():
    while not_facing_west():
        turn_left()
    while front_is_clear():
        move()
    turn_around()

def main():
    turn_left()
    while front_is_clear():

        
        fill_col()
        reset()
    come_back_home()


if __name__ == '__main__':
    main()