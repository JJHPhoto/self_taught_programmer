"""
Print all numbers from 25 to 50. 

I'm guessing there's gonna be an array from 0 - 50 and using a 'while-loop' to print numbers > than 24. 
"""

# i = 1
# while i < 25:
#   if i == 1:
#     i += 1
#     continue
#   print(i)
#   i += 1

for i in range(1, 51):
  if i <= 24:
    continue
  print(i)

"""
needed to adjust the numbers in the range & the <= syntax but basically got it it second try. 
"""


"""
Answer:

for i in range(25,51):
    print(i)

Much simpler... need to remember that simple isn't 'bad'. And complexe doesn't = smarter. 
"""