from functools import reduce
# square
my_list = [5, 4, 3]

print(list(map(lambda number: number**2, my_list)))
# list sorting
a = [(0, 2), (4, 3), (9, 9), (10, -1)]
a.sort(key=lambda item: item[1])
print(a)