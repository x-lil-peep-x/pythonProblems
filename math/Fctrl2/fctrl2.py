# Calcular el factorial de un numero Easy

def get_factorial(number):
    value = 1
    for num in range(1, number + 1):
        value *= num
    return value

test_cases = int(input())
for case in range(test_cases):
    number = int(input())
    print(get_factorial(number))