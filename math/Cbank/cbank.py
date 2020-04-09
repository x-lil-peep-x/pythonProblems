test_cases = int(input())
for case in range(test_cases):
    m = 1000000007
    number = int(input())
    counter = number
    branches = [number]
    is_end = False
    while True:
        if is_end:
            break
        for index in range(len(branches)):
            value = branches[index]
            # print(branches)
            if branches[-1] == 0.25:
                print(counter)
                is_end = True
                break
            if branches[index] == 0.5:
                counter += 1
                branches.pop(index)
                branches.insert(index, value / 2)
                branches.insert(index + 1, value / 2)
                break
            elif branches[index] == 1:
                counter += 1
                branches.pop(index)
                branches.insert(index, value / 2)
                branches.insert(index + 1, value / 2)
                break
            elif branches[index] % 2 == 0:
                counter += 2
                branches.pop(index)
                branches.insert(index, value/2)
                branches.insert(index+1, value/2)
                break
            elif not branches[index] % 2 == 0 and branches[index] > 1:
                counter += 1
                value = branches[index] - 1
                branches.pop(index)
                branches.insert(index, value)
                branches.insert(index, 1)
                break



