stats = {'Height': 'Six Feet', 'Color': 'Purple', 'Favorite Author': 'Brandon Sanderson'}

n = input('Ask a question about me: ')
if n in stats:
  stat = stats[n]
  print(stat)
else:
  print('Not available')

"""
Sort of got it but should give better instruction to the user. Especially considering it is case sensitive. 
"""