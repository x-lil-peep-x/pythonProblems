def print_sequence(sequence):
    for item in sequence:
        print(item, end=' ')


def compare_sequences(sequence_1, sequence_2):
    plus_1 = 0
    plus_2 = 0
    for value in sequence_1:
        plus_1 += value
    for value in sequence_2:
        plus_2 += value
    if plus_1 > plus_2:
        higher_sequence = sequence_1
    else:
        higher_sequence = sequence_2
    print_sequence(higher_sequence)


quantity_1 = int(input())
sequence_1 = input().split()
quantity_2 = int(input())
sequence_2 = input().split()
for index in range(0, quantity_1):
    sequence_1[index] = int(sequence_1[index])
for index in range(0, quantity_2):
    sequence_2[index] = int(sequence_2[index])
compare_sequences(sequence_1, sequence_2)
