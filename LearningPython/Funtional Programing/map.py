from functools import reduce


def multiply_by2(item):
    return item * 2


def only_odd(item):
    return item % 2 != 0


def accumulator(acc, item):
    print(acc, item)
    return acc + item


my_list = [1, 2, 3]
your_list = [10, 20, 30]
their_list = ['a', 'b', 'c']
n1, n2, n3 = map(multiply_by2, my_list)
print(n1)
print(multiply_by2([2, 3, 4]))

print(list(filter(only_odd, my_list)))
zipped_list = list(zip(my_list, your_list, their_list))
print(zipped_list)
print(zipped_list[0][2])
print(reduce(accumulator, my_list, 0))
print(my_list)
