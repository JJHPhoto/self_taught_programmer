"""
Challenge 4:
Take the string 'Where now? Who now? When now?' and call a method that returns a list that looks like: ['Where now?', 'Who now?', 'When now?'].

Feel like I can slice at the 'W' and then shave the extra ' '. However, it does say 'a method' so I think I should look for a specific method. 
"""

str = 'Where now? Who now? When now?'.split('?')
# print(str.split())
# print(str[0:10, 12:20])
# str[0:10]

print(str)

"""
Answer:
lst = "Where now? Who now? When now?".split("?")
print(lst)
"""