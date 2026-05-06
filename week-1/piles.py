from karel.stanfordkarel import *

# File: piles.py
# -----------------------------
# The warmup program defines a "main"
# function which should make Karel
# pick up all the beepers in the world.
def main():
    move()
    while front_is_clear():
        if beepers_present():
            pick_all_beepers()
    safe_move()

def pick_all_beepers():
    while beepers_present():
        pick_beeper()

    two_move()

def two_move():
    safe_move()
    safe_move()


def safe_move():
    if front_is_clear():
        move()


   
# don't edit these next two lines
# they tell python to run your main function
if __name__ == '__main__':
    main()