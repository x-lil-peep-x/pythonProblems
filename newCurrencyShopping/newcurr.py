def calculate_combinations(amount):
    combinations = 1
    combinations += amount // 2
    print(combinations)


loops = int(input())
# 0 , 1
for index in range(0, loops):
    amount = int(input())
    calculate_combinations(amount)
