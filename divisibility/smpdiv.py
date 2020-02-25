def print_divisible_numbers(divider, limit, forbidden_divider):
    counter = 0
    while True:
        counter += 1
        number = counter * divider
        if limit <= number:
            return
        if number % forbidden_divider == 0:
            continue
        print(number, end=" ")


loops = int(input())
for loop in range(0, loops):
    limit, divider, forbidden_divider = map(int, input().split())
    print_divisible_numbers(divider, limit, forbidden_divider)
    print()
