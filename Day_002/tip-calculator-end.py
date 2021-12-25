#!/usr/bin/env python

__version__ = '0.0.1'
__author__ = 'Fernandes Macedo'
__email__ = 'masedos@gmail.com'


#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator")
bill = float(input('What was the total bill? $'))
people = int(input('How many people to split the bill? '))
tip = float(input('What the percentage tip would you like to give? 10, 12, or 15? '))

each = ((bill  * tip / 100) + bill) / people

print(f"Each person should pay: ${round(each, 2)}")