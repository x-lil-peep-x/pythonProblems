# Calcular numero de rangos de numeros que cumplan con las condiciones MEdium
# del 2 hasta N cuntos rangos tiene cantidad de primos igual o mayar a k

def is_prime(sub_number):
    if sub_number == 1:
        return False
    for num in range(2, sub_number):
        if sub_number % num == 0:
            return False
    return True


test_cases = int(input())
for case in range(test_cases):
    n, k = map(int, input().split())
    lower_bound = 2
    ranges_counter = 0
    for number in range(lower_bound, n + 1):
        primes_counter = 0
        for sub_number in range(number, n + 1):
            if is_prime(sub_number):
                primes_counter += 1
            if primes_counter >= k:
                ranges_counter += 1
    print(ranges_counter)
