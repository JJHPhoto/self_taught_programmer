"""
Write a program with an infinite loop(with the option to type q to quit) and a list of numbers. Each time through the loop ask the user to guess a number on the list and tell them whether or not they guess correctly.

I feel like I need to use an inner loop to loop over the numbers in my list and then return True if the answer is one of those numbers. 
"""

# numbers = ['5', '23', '33']
# n = 0
# while True:
#   print('Type q to quit')
#   a = input('Guess a number')
#   if a == 'q':
#     break
#   if a == numbers[]:
#     print('That is correct!')

"""
Answer:

numbers = [11, 32, 33, 15, 1]

while True:
    answer = input("Guess a number or type q to quit.")
    if answer == "q":
        break
    try:
        answer = int(answer)
    except ValueError:
        print("please type a number or q to quit.")
    if answer in numbers:
        print("You guessed correctly!")
    else:
        print("You guessed incorrectly!")

My thoughts:

So, I didn't need them to be strings. 
I needed to convert the answer from a str to an int and use a ValueError to type a number. 

At least I 'got' the while True part....
"""

numbers = [5, 23, 33]
# n = 0
while True:
  # print('Type q to quit')
  # a = input('Guess a number')
  # if a == 'q':
  #   break
  # if a == numbers[]:
  #   print('That is correct!')
  answer = input('Guess a number between 1 and 100 or type q to quit.')
  if answer == 'q':
    break
  try:
    answer = int(answer)
  except ValueError:
    print('Please us a number or type q to quit')
  if answer in numbers:
    print('That is correct!')
  else:
    print('Nope! Try again!')