"""
Challenge 4
I knew that I needed to take in an int and then divide it. I then needed to pass that to a result and then use that result as a parameter in the second function. I thought I should label the 'result' and the 'combin'(final) result. I didn't realize I could wait till the end to divide and then multiply until I saw the answer.  
def div_int(x):
  return x / 2

result = div_int(4)
print(result)

def combine(y):
  return y * 4

final = combine(result)
print(final)
"""


"""
My pseudocode for Challenge 5
float('12.8')

def str_float(x):
  return str(float(x))

str_float('this is a string')
"""


"""
Challenge 5
Again, got caught up in want to have an input as opposed to the brief of the challenge. It did attempt to convert the string to a float, but my except was wrong. Among other things. 
try:
  a = input('write something:')
  a = str(a)
  b = float(a)
  print(b)
except(FloatingPointError):
  print("Can't do that.")
"""

def convert(string):
  try:
    return float(string)
  except ValueError:
    print('Could not convert the string to a float.')

c = convert('55.0')
print(c)