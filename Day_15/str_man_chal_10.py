"""
Challenge 10:
Slice the string 'It was a bright cold day in April, and the clocks were striking thirteen.' to only includ ethe characters before the comma.

Pretty sure this is just a slice at ','. Which is pretty easy and probably right since I tend to think its more complicated. 
"""

str = 'It was a bright cold day in April, and the clocks were striking thirteen.'
before_comma = slice(33)
print(str[before_comma])