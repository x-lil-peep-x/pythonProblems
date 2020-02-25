def compare_sequences(short_sequence, large_sequence):
    for index in range(0, len(short_sequence)):
        if short_sequence[index] == large_sequence[index]:
            print(index + 1)


num_quantity = int(input())
sequence = list(input().split())
num_quantity_2 = int(input())
sequence_2 = list(input().split())
compare_sequences(sequence, sequence_2)