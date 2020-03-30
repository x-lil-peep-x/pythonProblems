test_cases = int(input())
for case in range(test_cases):
    n = int(input())
    f = (pow(34, n)) + (30 * n) + 32
    m = 0
    while f % 11 != 0:
        f += 1
        m += 1
    print(m)