quantity = int(input())
numbers = [int(num) for num in input().split()]
plus = 0
for num in numbers:
    plus += num
print(plus)