test_cases = int(input())
for case in range(test_cases):
    min_bound, max_bound = map(int, input().split())
    counter = 0
    for number in range(min_bound, max_bound + 1):
        if str(number)[-1] == '2' or str(number)[-1] == '3' or str(number)[-1] == '9':
            counter += 1
    print(counter)
