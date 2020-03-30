test_case = int(input())
for i in range (test_case):
    finish, distance_to_bolt, tiger_acceleration, bolt_speed = map(int, input().split())
    bolt_time = finish / bolt_speed
    tiger_dist = 0.5 * tiger_acceleration * (bolt_time ** 2)
    if tiger_dist >= finish + distance_to_bolt:
        print('Tiger')
    else:
        print('Bolt')