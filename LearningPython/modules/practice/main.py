import random

# doc
help(random)
# functions
dir(random)
print(random.random())
print(random.randint(1, 10))
print(random.choice([1, 2, 3]))
my_list = [1, 2, 3, 4]
print(random.shuffle(my_list))
print(my_list)
