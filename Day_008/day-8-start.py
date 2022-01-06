#!/usr/bin/env python

__version__ = '0.0.1'
__author__ = 'Fernandes Macedo'
__email__ = 'masedos@gmail.com'


# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

def greet():
  print("Statement 1")
  print("Statement 2")
  print("Statement 3")

greet()


def greet_with_name(name):
  print(f"Hello {name}")
  print(f"How do you do {name}?")

greet_with_name("Beca")


def greet_with(name, location):
  print(f"Hello {name}")
  print(f"What is it like in {location}?")

greet_with(name="Beca", location="London")