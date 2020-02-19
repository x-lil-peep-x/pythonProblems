def decompose_number(number):
    dividend = 2
    while number > 1:
        if number % dividend == 0:
            number //= dividend
            print(dividend, end=' ')
        else:
            dividend += 1


loops = int(input())
counter = 0
while loops > counter:
    decompose_number(int(input()))
    print()
    counter += 1
