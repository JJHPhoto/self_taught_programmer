author = 'Kafka'
author[0]
author[1]
author[2]
author[3]
author[4]
K
a
f
k
a


author[5]
# would cause an IndexError: string index out of range 

author[-1]
a

author[-2]
author[-3]
k
f

ff = 'F. Fitzgerald'
ff = 'F. Scott Fitzgerald'
ff
'F. Scott Fitzgerald'

'cat' + 'in' + 'hat'
'catinhat'

'cat' + ' in' + ' the' + ' hat'
'ca in the hat'

'Sawyer' * 3
'SawyerSawyerSawyer'

'We hold these truths...'.upper()
'WE HOLD THESE TRUTHS...'

'SO IT GOES.'.lower()
'so it goes.'

'four score and...'.capitalize()
'Four score and...'

'William {}'.format('Faulkner')
'William Faulkner'

author = 'William Faulkner'
year_born = '1897'

'{} was born in {}.'.format(author, year_born)
'William Faulkner was born in 1897'