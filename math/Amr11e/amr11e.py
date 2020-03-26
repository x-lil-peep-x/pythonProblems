def print_prime_by_position(pos):
    less_number = 5
    while True:
        if pos == 0:
            print(6 * (less_number - 1))
            return
        is_prime = True
        for number in range(less_number - 1, 1, -1):
            if less_number % number == 0:
                is_prime = False
        if is_prime:
            pos -= 1
        less_number += 1


cases = int(input())
for case in range(cases):
    position = int(input())
    print_prime_by_position(position)
