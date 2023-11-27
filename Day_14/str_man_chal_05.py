"""
Challenge 5:
Take the list ['The', 'fox', 'jumped', 'over', 'the', 'fence', '.'] and turn it into a crammtically correct string. 
"""


list = ['The', 'fox', 'jumped', 'over','the', 'fence', '.']
# First try
# str = ' '.join(list)
# x = list.strip()
# print(x)

list = ' '.join(list)
list = list[0: -2] + '.'
print(list)

"""
Answer:
fox = ["The", "fox", "jumped", "over", "the", "fence", "."]
fox = " ".join(fox)
fox = fox[0: -2] + "."
print(fox)
"""