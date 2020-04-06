test_cases = int(input())
aux = 1
fac = 1
aux2 = 0
a = 3
for case in range(1,test_cases+1):
    aux = 3 * aux
    aux2 = case -1
    if aux2 != 0:
        fac = fac * aux2
result = aux + (test_cases*(fac-1))
print(result)