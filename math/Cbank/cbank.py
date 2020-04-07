test_cases = int(input())
for case in range(test_cases):
    m = 1000000007
    number = int(input())
    f = number * number
    g = f

    f = f * number
    g = g * 6
    y = 11 * number
    f = f + g + y + 6
    f = f * 166666668 % m
    print(f)
