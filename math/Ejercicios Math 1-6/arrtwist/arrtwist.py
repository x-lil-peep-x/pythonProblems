def check_twisted_arrays(array_a, array_b):
    max_bound_a = len(array_a)-1
    max_bound_b = len(array_b)-1
    for index_a in range(0, max_bound_a):
        for index_b in range(0, max_bound_b):
            sums_equals = array_a[index_a] + array_a[index_a + 1] == array_b[index_b] + array_b[index_b + 1]
            if sums_equals:
                print('YES')
                return
    print('NO')
    return


length_a, length_b = map(int, input().split())
sequence_a = []
for counter in range(0, length_a):
    sequence_a.append(int(input()))
sequence_b = []
for counter in range(0, length_b):
    sequence_b.append(int(input()))

check_twisted_arrays(sequence_a, sequence_b)