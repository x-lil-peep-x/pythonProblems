import sys
from random import randrange

min_bound = sys.argv[1]
max_bound = sys.argv[2]
number = randrange(int(min_bound), int(max_bound))
while True:
    in_number = int(input())
    if number == in_number:
        print('You are a genius')
        break
    else:
        print('Try again !')
