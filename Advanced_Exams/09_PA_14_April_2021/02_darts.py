# Exam: 02. Darts
# From: Python Advanced Retake Exam - 14 April 2021
# URL: https://judge.softuni.org/Contests/Practice/Index/2828#1
from collections import deque


def throw(current_throw, player):
    global player_one_score
    global player_two_score
    global is_bull_eye

    row, col = current_throw

    try:
        if dartboard[row][col] == 'B':
            is_bull_eye = True

        elif dartboard[row][col] == 'D' or dartboard[row][col] == 'T':
            multiplier = 3 if dartboard[row][col] == 'T' else 2

            if player == 'player_one':
                points = (int(dartboard[0][col]) + int(dartboard[6][col]) + int(dartboard[row][0]) + int(
                    dartboard[row][6])) * multiplier
                player_one_score -= points
            else:
                points = (int(dartboard[0][col]) + int(dartboard[6][col]) + int(dartboard[row][0]) + int(
                    dartboard[row][6])) * multiplier
                player_two_score -= points

        else:
            if player == 'player_one':
                player_one_score -= int(dartboard[row][col])
            else:
                player_two_score -= int(dartboard[row][col])

    except IndexError:
        pass


def check_win_conditions():
    if player_one_score <= 0 or player_two_score <= 0 or is_bull_eye:
        return True

    return False


player_one_throws = 0
player_two_throws = 0
player_one_score = 501
player_two_score = 501
players = deque(input().split(', '))
size = 7
dartboard = [input().split() for _ in range(size)]

is_bull_eye = False

win_throws_count = 0
throw_idx = 0
while True:

    players.append(players.popleft())

    if throw_idx % 2 == 0:
        current_player = 'player_one'
        player_one_throws += 1
    else:
        current_player = 'player_two'
        player_two_throws += 1

    throw_idx += 1

    player_throw = tuple(int(x) for x in input().strip('()').split(', '))
    throw(player_throw, current_player)

    if check_win_conditions():
        win_throws_count = player_one_throws if current_player == 'player_one' else player_two_throws
        break

print(f'{players[1]} won the game with {win_throws_count} throws!')
