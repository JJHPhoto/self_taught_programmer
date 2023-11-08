# def f(x = 2):
#   return x ** x

# print(f())
# print(f(4))

# def add_it(x, y = 10):
#   return x + y

# result = add_it(2)
# print(result)

# x = 1
# y = 2
# z = 3

# def f():
#   print(x)
#   print(y)
#   print(z)

# f()

# def f():
#   x = 1
#   y = 2
#   z = 3

# print(x)
# print(y)
# print(z)

# def f():
#   x = 1
#   y = 2
#   z = 3
#   print(x)
#   print(y)
#   print(z)

# f()

# x = 100

# def f():
#   global x
#   x += 1
#   print(x)

# f()

# a = input('type a number:')
# b = input('type another:')
# a = int(a)
# b = int(b)
# print(a/b)

a = input('type a number:')
b = input('type another:')
a = int(a)
b = int(b)
try:
  print(a/b)
except ZeroDivisionError:
  print('b cannot be a zero.')