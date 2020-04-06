test_cases = int(input())


def binary(a, b, c):
    limit = 0.000005
    low = 0
    high = 200
    ans2 = 0
    while low < high:
        mid = (low + high) / 2
        ans2 = mid * mid * mid * a + b * mid * mid * c
        if limit > ans2 > -limit:
            return mid
        if ans2 > -limit:
            high = mid
        else:
            low = mid
    return ans2


for case in range(test_cases):
    radius, height = map(float, input().split())
    area = radius * radius
    temp = ((radius * radius) + (height *radius))**(1/2)
    b = 3 * radius * temp
    c = -6 * radius * height * height * temp
    ans = binary(area, b, c)
    if ans > height:
        print('%.6f' % height)
    else:
        print('%.6f' % ans)
