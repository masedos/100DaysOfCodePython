#!/usr/bin/env python

__version__ = '0.0.1'
__author__ = 'Fernandes Macedo'
__email__ = 'masedos@gmail.com'


#Write your code below this line 👇

# to run the code paste in https://reeborg.ca/reeborg.html

while front_is_clear():
    move()
turn_left()
    
while not at_goal():
    if right_is_clear():
        turn_left()
        turn_left()
        turn_left()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()