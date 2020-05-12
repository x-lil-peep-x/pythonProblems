from collections import deque


test_cases = int(input())
scores = deque()
for case in range(test_cases):
    quantity = int(input())
    data = dict()
    scores = deque()

    for index in range(quantity):
        problem, score = input().split(' ')
        problem, score = int(problem), int(score)
        if problem in [9, 10, 11]:
            continue
        else:
            if problem not in data or data[problem] < score:
                data[problem] = score
                scores = data.values()
    print(sum(scores))
