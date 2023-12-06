"""
For-Loops
"""

# for-loop iterating through string
# name = 'Ted'
# for character in name:
#   print(character)

# for-loop iterating through the items in a list
# shows = ['GOT', 'Narcos', 'Vice']
# for show in shows:
#   print(show)

# for loop iterating through items in a tuple 
# coms = ('A. Development', 'Friends', 'Always sunny')
# for show in coms:
#   print(show)

# for-loop iterating through the keys in a dictionary
# people = {'G. Bluth II', 'Barney', 'HIMYM', 'Dennis', 'Always Sunny'}
# for character in people:
#   print(character)

# for-loop changing items in a mutable iterable
# tv = ['GOT', 'Narcos', 'Vice']
# i = 0
# for show in tv:
#   new = tv[i]
#   new = new.upper()
#   tv[i] = new
#   i += 1

# print(tv)

# other syntax to changing items in a mutable iterable 
# tv = ['GOT', 'Narcos', 'Vice']
# for i, show in enumerate(tv):
#   new = tv[i]
#   new = new.upper()
#   tv[i] = new

# print(tv)

# for-loop to take all the strings from two different lists, capitalize each character in them and put them into a new list

tv = ['GOT', 'Narcos', 'Vice']
coms = ['Arrested Development', 'friends', 'Always Sunny']
all_shows = []

for show in tv:
  show = show.upper()
  all_shows.append(show)

for show in coms:
  show = show.upper()
  all_shows.append(show)

print(all_shows)
