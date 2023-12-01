"""
Challenge 7:
Use a method to find the first index of the character 'm' in the string 'Hemingway'.

I think I need to write a function that uses the try/except logic. Just need to review how to write a function in Python.

Ok... at first I thought that didn't work, but it 'works'. Its just not necessary to do the try/except logic.  
"""

def index(string):
  try:
    return string.index('m')
  except:
    print('not found')

m = index('Hemingway')
print(m)

# first_m = 'Hemingway'.index('m')
# print(first_m)

"""
Answer:
first_index = "Hemingway".index("H")
print(first_index)
"""