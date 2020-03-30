import math
import fractions
while True:
    n, k = map(int, input().split())
    if n == -1 and k == -1:
        break
    down = (n * (n - 1)) // 2
    print(down)
    up = 0
    ans = k - 2
    if ans % 2 == 0:
        num = ans // 2
        up = ((num + 1) * ans) // 2
    else:
        num = (ans - 1) // 2
        up = ((num + 1) * (ans + 1)) // 2
    print(num)
    print(ans)
    print(up)
    if up == 0:
        print(0)
    else:
        print(fractions.Fraction(up, down))
