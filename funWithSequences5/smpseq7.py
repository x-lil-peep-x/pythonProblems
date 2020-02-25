def check_split(sequence, quantity):
    min_bound = 1
    max_bound = quantity
    for limit in range(min_bound, max_bound - 2):
        first_split = True
        for position in range(0, limit):
            if sequence[position] <= sequence[position + 1]:
                first_split = False
                break
        second_split = True
        for pos in range(limit + 1, max_bound - 1):
            if sequence[pos] >= sequence[pos + 1]:
                second_split = False
                break
        if first_split and second_split:
            print('YES')
            return
    print('NO')


quantity = int(input())
inp = input().split()
sequence = []
for index in range(0, quantity):
    sequence.append(int(inp[index]))
check_split(sequence, quantity)
