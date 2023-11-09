# try:
#   a = input('type a number:')
#   b = input('type another:')
#   a = int(a)
#   b = int(b)
#   print(a/b)
# except(ZeroDivisionError,ValueError):
#   print('Invalid input.')


# try: 
#   10/0
#   c = 'I will never get defined.'
# except ZeroDivisionError:
#   print(c)

def add(x,y):
  """
  Return x + y
  :param x: int.
  :param y: int.
  :return: int sum of x and y.
  """
  return x + y