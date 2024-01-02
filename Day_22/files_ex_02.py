"""
Automatically Closing Files

Second way to open files that doesn't require you to remember to close the file. It will automatically close the file as soon as Python finishes running the file. 
"""

# with open('st.txt', 'w') as f:
#   f.write('Hi from Python!')

"""
Reading from Files

Not sure where to put the 'st.txt' file. Its not in the repo and I don't know if I should be putting it on my desktop? 
"""

with open('st.txt', 'r') as my_file:
  print(my_file.read())



my_list = list()

with open('st.txt', 'r') as f:
  my_list.append(f.read())

print(my_list)

# ['Hi from Python!']