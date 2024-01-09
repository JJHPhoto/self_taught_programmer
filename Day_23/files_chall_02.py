"""
Write a program that asks a user a question, and saves their answer to a file. 
"""

answer = input('What is your favorite sports team?')
with open('fav_team.txt', 'w') as f:
  f.write(answer)

"""
This created a 'fav_team.txt' file in a folder one up from this folder. 
"""