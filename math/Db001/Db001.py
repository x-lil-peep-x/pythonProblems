test_cases = int(input())
for case in range(test_cases):
    length = int(input())
    numbers = [int(num) for num in input().split()]
    has_one = False
    for number in numbers:
        if number == 1:
            print(length)
            has_one = True
            break
    if not has_one:
        print(-1)
