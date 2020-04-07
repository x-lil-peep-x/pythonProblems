test_cases = int(input())


def is_prime(number):
    for num in range(2,number-1):
        if number % num == 0:
            return False
    return True


for case in range(test_cases):
    length = int(input())
    numbers = [int(num) for num in input().split()]
    has_one = False
    for number in numbers:
        if number == 1:
            print(length)
            has_one = True
            break
        end = False
        if is_prime(number):
            for num in numbers:
                if not num % number == 0:
                    print(length)
                    has_one = True
                    end = True
                    break
        if end:
            break
    if not has_one:
        print(-1)
