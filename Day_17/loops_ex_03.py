"""
Break
"""

# for i in range(0, 100):
#   print(i)
#   break

qs = ['What is your name?', 'What is your fav. color?', 'What is your quest?']
n = 0
while True:
  print('Type q to quit')
  a = input(qs[n])
  if a == 'q':
    break
  n = (n + 1) % 3

"""
% is assigning the evaluation of the expression
"""