cases = int(input())


def calculate_time(n, k, m):
    time = m // (n * k)
    print(time)


for case in range(cases):
    n, k, m = map(int, input().split())
    calculate_time(n, k, m)

