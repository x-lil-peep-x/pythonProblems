num_list = [1, 3, 5, 6, 7, 1, 3, 5]
duplicates = set()
for num in num_list:
    if num_list.count(num) > 1:
        duplicates.add(num)
print(duplicates)
