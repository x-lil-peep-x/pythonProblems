def get_sequences_of_zero(sequence):
    length = len(sequence)
    counter = 0
    for index_col in range(0, length):
        sequence_sum = 0
        for sub_index in range(index_col, length):
            sequence_sum += sequence[sub_index]
            if sequence_sum == 0:
                counter += 1
    print(counter)


test_cases = int(input())
for case in range(test_cases):
    length = int(input())
    sequence = [int(num) for num in input().split()]
    get_sequences_of_zero(sequence)
