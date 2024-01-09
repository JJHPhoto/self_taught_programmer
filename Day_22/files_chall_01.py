"""
Find a file on your computer and print its contents using Python. 
"""

import os
os.path.join('User', 'joshuahaller/desktop', 'question.txt')

with open('question.txt', 'r') as my_file:
  print(my_file.read())


"""
This code works in IDLE but not in VS Code. Like I thought. 
"""