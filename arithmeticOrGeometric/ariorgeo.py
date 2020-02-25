def check_arithmetic_sequence(first, medium, last):
    if last - medium == medium - first:
        return True
    return False


def check_geometric_sequence(first, medium, last):
    if last / medium == medium / first:
        return True
    return False


def assign_sequence(first, medium, last):
    is_geometric = check_geometric_sequence(first, medium, last)
    is_arithmetic = check_arithmetic_sequence(first, medium, last)
    if is_arithmetic & is_geometric:
        print('Both')
    else:
        if is_arithmetic:
            print('Arithmetic')
        else:
            if is_geometric:
                print('Geometric')
            else:
                print('None')


loops = int(input())
counter = 0
while loops > counter:
    first, medium, last = map(float, input().split())
    assign_sequence(first, medium, last)
    counter += 1
