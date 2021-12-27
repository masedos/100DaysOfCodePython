#!/usr/bin/env python

__version__ = '0.0.1'
__author__ = 'Fernandes Macedo'
__email__ = 'masedos@gmail.com'


import random
import my_module

random_integer = random.randint(1, 10)
print(random_integer)

print(my_module.pi)

# 0.000000 - 0.999999
random_float = random.random()
print(random_float)

# 0.000000 - 4.999999
print(random_float * 5)


love_score = random.randint(1, 100)
print(f"Your love score is {love_score}")