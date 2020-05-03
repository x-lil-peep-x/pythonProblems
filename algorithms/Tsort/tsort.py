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


numbers = int(input())
unsorted_list = []
for index in range(numbers):
    unsorted_list.append(int(input()))
sorted_list = counting_sort(unsorted_list)

for item in sorted_list:
    print(item)