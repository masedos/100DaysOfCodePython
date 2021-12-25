#!/usr/bin/env python

__version__ = '0.0.1'
__author__ = 'Fernandes Macedo'
__email__ = 'masedos@gmail.com'


num_char = len(input("What is your name? "))
print("Your name has " + str(num_char) + " characters.")



print("""

P E M D A S LR
Parentheses
Exponentes
Multiplication
Division
Addition
Substraction

Left
Rigth

""")

print(3 * 3 + 3 / 3 - 3)

print(3 * (3 + 3) / 3 - 3)

print(round(8 / 3, 2))

print(8 // 3)

# f-String
score = 0
height = 1.8
isWinning = True

print(f"Your score is {score}, your height is {height}, you are winning is {isWinning}")