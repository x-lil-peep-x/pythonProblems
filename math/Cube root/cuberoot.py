import math


def sum_of_digits(float_string):
    sum = 0
    for number in float_string:
        if number != '.':
            sum += int(number)
    return sum


test_cases = int(input())
for case in range(test_cases):
    number = int(input())
    number_cube_root = '%.11f' % number ** (1 / 3)
    str_number_cube_root = str(number_cube_root)[0:-1]
    digits_sum = sum_of_digits(str_number_cube_root)
    residual = digits_sum % 10
    print(residual, str_number_cube_root)
