#Probabilidad entre 2 tipos de personas que paganas 5bs y 10 bs
while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    if n > m:
        print("0.000000")
    else:
        print('{0:6f}'.format((m - n + 1) / (m + 1)))
