"""
Multiply all the numbers in the list [8, 19, 148, 4] with the numbers in the list[9, 1, 33, 83] and append each result to a third list.

Pretty sure I did this with addition. Should be fine? I feel like I'm already trying to make it complicated by trying to make sure every number is multiplied by every number so that there are 16 numbers. 
"""

# list1 = [8, 19, 148, 4]
# list2 = [9, 1, 33, 83]
# multiplied = []
# for i in list1:
#   for j in list2:
#     multiplied.append(i * j)

# print(multiplied)

"""
The answer has mult in there. Will test to see if results are different. 
"""

list1 = [8, 19, 148, 4]
list2 = [9, 1, 33, 83]
list3 = []

for i in list1:
    for j in list2:
        mult = i * j
        list3.append(i * j)

print(list3)

"""
Nope! I was correct with my own answer. 
"""