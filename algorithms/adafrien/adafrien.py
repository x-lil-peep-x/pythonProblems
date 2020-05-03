celebrations, max_friends = map(int, input().split())
friends = []
expenses = []


def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)

    for i in range(n, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)


for celebration in range(celebrations):
    friend, expense = input().split()
    if friends.count(friend) > 0:
        expenses[friends.index(friend)] += int(expense)
    else:
        expenses.append(int(expense))
        friends.append(friend)
heap_sort(expenses)
if len(expenses) < max_friends:
    max_friends = len(expenses)
saved_money = 0
counter = -1
for friend in range(max_friends):
    saved_money += expenses[counter]
    counter -= 1
print(saved_money)