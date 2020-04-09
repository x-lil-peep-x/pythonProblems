test_cases = int(input())
for case in range(test_cases):
    a, b = map(int, input().split())
    real_a = a
    real_b = b
    # Sacar el minimo comun divisor
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    print(int(real_b/a), int(real_a/b))
