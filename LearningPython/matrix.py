# Matrix
matrix = [
    [1, 0, 1],
    [0, 1, 0],
    [1, 0, 1]
]
numbers = [1, 2, 3, 4, 5]
# Adding
numbers.append(6)
numbers.insert(6, 100)
numbers.extend([101, 102, 103])
print(matrix[0][1])
print(matrix[1][1])
print(numbers)

# Removing
lastNumber = numbers.pop()
numbers.pop(0)
numbers.remove(5)
print('Last number: ' + str(lastNumber))
print(numbers)
numbers.clear()
print(numbers)
