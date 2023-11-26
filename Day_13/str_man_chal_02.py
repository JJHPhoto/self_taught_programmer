"""
Challenge 2: Write a program that collects two strings from a user, inserts them into the string 'Yesterday I wrote a [response_one]. I sent it to [response_two]!' and prints a new string. 
"""


r1 = input('What did you write yesterday?')
r2 = input('Where did you send it?')

answer = """Yeseterday I wrote a {}. I sent it to {}!
""".format(r1, r2)
print(answer)

"""
Answer:
answer1 = input("What did you write yesterday?")
answer2 = input("Where did you go yesterday?")

new_string = "Yesterday I wrote a {}. I sent it to {}.".format(answer1, answer2)

print(new_string)
"""