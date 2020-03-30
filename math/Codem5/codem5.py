test_cases = int(input())


def check_combinations(array, value):
    counters = []
    for index in range(len(array)):
        if array[index] == value:
            print(1)
            return
        else:
            sum = 0
            counter = 0
            for sub_index in range(index, len(array)):
                counter += 1
                sum += array[sub_index]
                if sum == value:
                    counters.append(counter)
                if sum > value:
                    break
    if len(counters) == 0:
        print("impossible")
    else:
        counters.sort()
        print(counters[0])





for case in range(test_cases):
    objects_number, objects_weight = map(int, input().split())
    weights = [int(weight) for weight in input().split()]
    check_combinations(weights, objects_weight)