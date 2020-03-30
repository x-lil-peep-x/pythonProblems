import math
import fractions
while True:
    n, k = map(int, input().split())
    if n == -1 and k == -1:
        break
    down = (n * (n - 1)) // 2
    up = 0
    ans = k - 2
    if k == 2 or k == 1:
        up = 0
    else:
        rest = ans - 2
        if rest < 0:
            rest = 0
        up = ans + rest
    if up == 0:
        print(0)
    else:
        print(fractions.Fraction(up, down))
