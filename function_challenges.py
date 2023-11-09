"""
Challenge 1
My understanding/attempt was that I needed to take an input and multiply it by itself. I didn't realize that `** 2` would square the number for me.
a = input('type a number')
a = int(a)
print(a*a)

Answer:
def squared(x)
  return x ** 2

print(squared(2))

"""

"""
Challenge 2
Again, I thought I was supposed to take an input and print that out. 
a = input('write something:')
a = str(a)
print(a)

Answer:
def print_string(string):
  print(string)

print_string("Testing, 1, 2, 3.")
"""

"""
Challenge 3
This one I only had part of the concept. I thought correctly about the required paramaters but didn't know I had to define the optional parameters. 

Once I understood that, I 'knew' what to do. 
def req_opp(x, y, z, a = 4, b = 8):
  return x + y - z * a + b

result = req_opp(3, 5, 7)
print(result)
"""