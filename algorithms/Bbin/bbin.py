def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            print(i)
            return
    print(-1)


quantity, searches = map(int, input().split())
numbers = [int(num) for num in input().split()]
numbers.sort()
for index in range(searches):
    search = int(input())
    linear_search(numbers, search)
