def counting_sort(unsorted):
    result = [0] * len(unsorted)
    low = min(unsorted)  # we don't care if this is positive or negative any more!
    high = max(unsorted)
    count_array = [0 for i in range(low, high + 1)]
    for i in unsorted:
        count_array[i - low] += 1  # use an offset index
    for j in range(1, len(count_array)):
        count_array[j] += count_array[j - 1]
    for k in reversed(unsorted):
        result[count_array[k - low] - 1] = k  # here too
        count_array[k - low] -= 1  # and here
    return result


test_cases = int(input())
for case in range(test_cases):
    numbers = int(input())
    sequence_1 = [int(number) for number in input().split()]
    sequence_2 = [int(number) for number in input().split()]
    sorted_seq_1 = counting_sort(sequence_1)
    reversed_seq_2 = counting_sort(sequence_2)
    reversed_seq_2.reverse()
    total = 0
    for index in range(len(sorted_seq_1)):
        total += sorted_seq_1[index] * reversed_seq_2[index]
    print(total)
