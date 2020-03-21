#Comparing binary search vs fast search
#                      9780333
# for number in range(0, 10000000000):
#     print(number)
#     if 10000000 == number:
#         break
searched_number = 10000000
max_bound = 10000000000
minBound = 0
while max_bound:
    mid_number = (max_bound + minBound) // 2
    print(mid_number)
    if (searched_number == mid_number):
        break
    else:
        if searched_number < mid_number:
            max_bound = mid_number - 1
        else:
            minBound = mid_number + 1
