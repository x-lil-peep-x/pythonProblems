def calculate_max_money(amounts):
    total_amount = 0
    for index in range(0, len(amounts)):
        total_amount += amounts[index]
    print(total_amount)


amounts = [int(number) for number in input().split()]
number_of_pairs = int(input())
for index in range(0, number_of_pairs):
    member, another_member = map(int, input().split())
    member -= 1
    another_member -= 1
    if amounts[member] > amounts[another_member]:
        amounts[another_member] = 0
    else:
        amounts[member] = 0
calculate_max_money(amounts)
