test_cases = int(input())
for case in range(test_cases):
    max_bound = int(input())
    max = 2 ** max_bound
    counter = 0
    for num in range(0, max):
        if num % 3 == 0:
            counter += 1

    print(counter)
