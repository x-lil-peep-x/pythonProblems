def print_near_value_index(sequence_1, sequence_2, scope):
    for index in range(0, len(sequence_1)):
        for value in range(-scope, scope):
            near_index = index + value
            if 0 <= near_index and near_index < len(sequence_1):
                if sequence_1[index] == sequence_2[near_index]:
                    print(index + 1,end=' ')
                    break



quantity, x = map(int,input().split())
sequence_1 = [int(number) for number in input().split()] 
sequence_2 = [int(number) for number in input().split()]
print_near_value_index(sequence_1, sequence_2, x)
