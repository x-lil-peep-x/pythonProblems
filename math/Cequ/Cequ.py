test_cases = int(input())
for case in range(test_cases):
    a, b, c = map(int, input().split())
    has_result = False
    for x in range(c):
        result = x * a
        for y in range(c):
            result += b * y
            if result == c:
                has_result = True
                break
    if has_result:
        print("Yes")
    elif not has_result:
        print("No")