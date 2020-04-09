test_cases = int(input())
for case in range(test_cases):
    number = int(input())
    counter = 0
    while number >= 5:
        number /= 5
        counter += int(number)

    print(counter)