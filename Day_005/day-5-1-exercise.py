#!/usr/bin/env python

__version__ = '0.0.1'
__author__ = 'Fernandes Macedo'
__email__ = 'masedos@gmail.com'


# 🚨 Don't change the code below 👇
#student_heights = [180, 124, 165, 173, 189, 169, 146]
student_heights = input("Input a list of student heights ").split()
sum = 0
count = 0
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
  sum += student_heights[n]
  count += 1
average = sum / count
print(int(round(average, 0)))
