def is_prime(number):
    for num in range(2, round(number / 2)+1):
        if number % num == 0:
            return False
    return True


def fun(number):
    if number == 0 or (is_prime(number) and not number % 2 == 0):
        return 0
    elif number == 1:
        return 1
    elif number == 2:
        return 2
    else:
        return fun(number / 2) + fun(number / 2)


number = int(input())
result = fun(number)
print(result)