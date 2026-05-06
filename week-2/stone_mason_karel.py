from karel.stanfordkarel import *

"""
File: main.py
--------------------
When you finish writing this file, Karel should have repaired 
each of the columns in the temple
"""

from karel.stanfordkarel import *

def main():
    for i in range(4):          # 4 columns
        build_column()
        if front_is_clear():
            move_to_next_column()

def build_column():
    turn_left()
    for i in range(5):         # height = 5
        put_beeper()
        if front_is_clear():
            move()
    turn_around()
    for i in range(4):         # come back down
        move()
    turn_left()

def move_to_next_column():
    for i in range(4):         # move 4 steps right
        move()

def turn_around():
    turn_left()
    turn_left()

if __name__ == '__main__':
    main()