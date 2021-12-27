#!/usr/bin/env python

__version__ = '0.0.2'
__author__ = 'Fernandes Macedo'
__email__ = 'masedos@gmail.com'


# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

import random

print(f"{random.choice(names)} is going to buy the meal today!")
