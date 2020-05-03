def binary_search(item_list, item):
    first = 0
    last = len(item_list) - 1
    found = False
    mid = 0
    while first <= last and not found:
        mid = (first + last) // 2
        if item_list[mid] == item:
            found = True
        else:
            if item < item_list[mid]:
                last = mid - 1
            else:
                first = mid + 1
    print('YES')


test_cases = int(input())
for case in range(test_cases):
    quantity = int(input())
    numbers = [int(num) for num in input().split()]
    searched_num = int(input())
    if numbers.count(searched_num) > 0:
        binary_search(numbers, searched_num)
    else:
        print('NO')
