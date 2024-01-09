"""
Take the items in this list of lists:
[['Top Gun', 'Risky Business', 'Minority Report'], ['Training Day', 'Man on Fire', 'Flight']] and write them to a CSV file. The data from each list should be in a row in the file, with each item in the list separated by a comma.
"""

import csv
movies = [['Top Gun', 'Risky Business', 'Minority Report'], ['Training Day', 'Man on Fire', 'Flight']]

# with open('movie_list.csv', 'w', newline='') as f:
#   w = csv.writer(f, delimiter=',')
#   w.writerow([list])

with open('movies.csv', 'w', newline='') as f:
  w = csv.writer(f, delimiter=',')
  for movie_list in movies:
    w.writerow(movie_list)

"""
Made the csv file but I don't think I did the rows. 

Yeah, I needed to add the for loop like the second example.

Sort of understood it but yeah... struggling. 
"""