test_cases = int(input())
for case in range(test_cases):
    fancy_number = input()
    counter = 1
    for index in range(len(fancy_number) - 1):
        if fancy_number[index] == fancy_number[index+1]:
            counter *= 2
    print(counter)