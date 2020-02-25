def reverse_number(number: int):
    reversed_number = 0
    while number > 0:
        last_digit = number % 10
        reversed_number = reversed_number * 10 + last_digit
        number //= 10
    return reversed_number


loops = int(input())
counter = 0
while loops > counter:
    number, number2 = map(int, input().split())
    sumResult = reverse_number(number) + reverse_number(number2)
    sumResult = reverse_number(sumResult)
    print(sumResult)
    counter = counter + 1
