test_cases = int(input())
for case in range(test_cases):
    m, n = map(int, input().split())
    y = m ** n
    x = 0
    for num in range(n):
        x += m ** num
        x = x % 1000000007
    print(f'{x} {y}')
