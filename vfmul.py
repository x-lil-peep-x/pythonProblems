def multiply_numbers(number1, number2):
    return number1 * number2


loops = int(input())
counter = 0
while loops > counter:
    number1, number2 = map(int, input().split())
    print(multiply_numbers(number1, number2))
    counter += 1
