def check_prime(number):
    for index in range(2, number // 2):
        if number % index == 0:
            # return False
            print('NO')
            return
    # return True
    print('YES')


loops = int(input())
for index in range(0, loops):
    number = int(input())
    check_prime(number)
