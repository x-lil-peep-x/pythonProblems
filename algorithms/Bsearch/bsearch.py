def binary_search(seq, t):
    min = 0
    max = len(seq) - 1
    while True:
        if max < min:
            return -1
        mid = (min + max) // 2
        if seq[mid] < t:
            min = mid + 1
        elif seq[mid] > t:
            max = mid - 1
        else:
            return mid


quantity, searches = map(int, input().split())
numbers = [int(num) for num in input().split()]
for search in range(searches):
    searched_num = int(input())
    print(binary_search(numbers, searched_num))
