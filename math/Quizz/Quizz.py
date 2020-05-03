def check_winner(team1, team2, reds1, reds2):
    if team1 >= 9 and (reds1 != 0 or reds2 != 0):
        print('Team 1 wins and the point is', ((9 - team2) + reds1 * 5))
    elif team2 >= 9 and (reds1 != 0 or reds2 != 0):
        print('Team 2 wins and the point is', ((9 - team1) + reds2 * 5))
    else:
        print('Incomplete game')


def carrhim():
    team1 = 0
    team2 = 0
    reds1 = 0
    reds2 = 0
    while True:
        player = input()
        if player == "#":
            check_winner(team1, team2, reds1, reds2)
            carrhim()
        white, black, red = map(int, input().split())
        if player == 'A' or player == 'C':
            team1 += white
            team2 += black
            reds1 += red
        else:
            team2 += white
            team1 += black
            reds2 += red


carrhim()
