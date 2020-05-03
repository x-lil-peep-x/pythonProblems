# Operador & interseccion de conjuntos
# 1 1 1 0 1 0     # 58
# & & & & & &
# 1 0 1 0 1 1     # 43
# ⇓ ⇓ ⇓ ⇓ ⇓ ⇓
# 1 0 1 0 1 0     # 42
# formula de paridad de 
test_cases = int(input())
for case in range(test_cases):
    m, n = map(float, input().split())
    print(n-m)
    print((m-1)/2)
    value = int(n - m) & int((m - 1)/2)
    print(value)
