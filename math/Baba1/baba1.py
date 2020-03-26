import math


def print_sides(hypotenuse, area):
    a = 1
    b = - (area * area)
    c = (hypotenuse * 2)
    c = c * c
    try:
        side_a = math.sqrt((-b + math.sqrt(float(b ** 2 - 4 * a * c))) / 2)
        side_b = math.sqrt((-b - math.sqrt(float(b ** 2 - 4 * a * c))) / 2)
        if side_a != 0 and side_b != 0:
            print(side_b, ' ', side_a, ' ', hypotenuse)
        else:
            print('-1')
    except:
        print('-1')


cases = int(input())
for case in range(cases):
    hypotenuse, area = map(int, input().split())
    print_sides(hypotenuse, area)
