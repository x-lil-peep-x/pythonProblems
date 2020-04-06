test_cases = int(input())
for case in range(test_cases):
    m, n = map(float, input().split())
    value = int(n - m) & int((m - 1)/2)
    print(value)
