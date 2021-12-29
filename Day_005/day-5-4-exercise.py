#!/usr/bin/env python

__version__ = '0.0.1'
__author__ = 'Fernandes Macedo'
__email__ = 'masedos@gmail.com'


#Write your code below this row 👇

for number in range(1, 101):
  if number % 3 == 0 and number % 5 == 0:
    print(f"FizzBuzz")
  elif number % 3 == 0:
    print(f"Fizz")
  elif number % 5 == 0:
    print(f"Buzz")
  else:
    print(number)