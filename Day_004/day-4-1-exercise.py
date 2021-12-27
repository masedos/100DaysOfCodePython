#!/usr/bin/env python

__version__ = '0.0.2'
__author__ = 'Fernandes Macedo'
__email__ = 'masedos@gmail.com'


#Write your code below this line 👇
#Hint: Remember to import the random module first. 🎲
"""
e.g.
1 means Heads
0 means Tails
"""

import random

coin = random.randint (0, 1)

if coin == 0:
  print("Tails")
else:
  print("Heads")
