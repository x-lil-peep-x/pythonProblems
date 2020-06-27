from functools import reduce


# lambda parameter: func(param)

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
print('Multiply by 2 with lambda')
n1, n2, n3 = map(lambda number: number * 2, my_list)
print(n1, n2, n3)

print(list(filter(lambda number: number % 2 != 0, my_list)))
zipped_list = list(zip(my_list, your_list, their_list))
print(zipped_list)
print(zipped_list[0][2])
print(reduce(lambda accumulator, number: accumulator + number, my_list, 0))
print(my_list)
