test_cases = int(input())
for case in range(test_cases):
    number = int(input())
    stack = []
    counter = 1
    while number > 0:
        result = number - counter
        if result < 0:
            stack.append(number)
            number -= number
        else:
            number = result
            stack.append(counter)
        counter += 1
    counter -= 1
    print(counter)