# a = input('type a number')
# a = int(a)
# print(a*a)

# a = input('write something:')
# a = str(a)
# print(a)

def req_opp(x, y, z, a = 4, b = 8):
  return x + y - z * a + b

result = req_opp(3, 5, 7)
print(result)