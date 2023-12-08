"""
Continue
"""

# Using continue, the loop doesn't exit the loop like an break keyword would cause it to do.

# for i in range(1, 6):
#   if i == 3:
#     continue
#   print(i)

# Using a while-loop to do the same thing. 

# i = 1
# while i < 5:
#   if i == 3:
#     i += 1
#     continue
#   print(i)
#   i += 1

  # The while loop does a += to i when it == 3 and continues withouth printing the 3. 

"""
Nested Loops
"""

# for i in range(1, 3):
#   print(i)
#   for letter in ['a', 'b', 'c']:
#     print(letter)

# Nice way to show that the inner loop loops every time the outer loop iterates. 

# list1 = [1, 2, 3, 4]
# list2 = [5, 6, 7, 8]
# added = []
# for i in list1:
#   for j in list2:
#     added.append(i + j)

# print(added)

"""
I saw what it did but didn't understand why it added to the total in list1 and then list2. 

The first loop iterates through every integer in list1. For each item in it, the second loop iterates through each integer in its own iterable, adds it to the integer from list1 and appends the result to the list added. 
"""

while input('y or n') != 'n':
  for i in range(1, 6):
    print(i)