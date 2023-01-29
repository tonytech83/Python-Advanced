from collections import deque

seats = input().split(', ')
first_seq = deque(int(x) for x in input().split(','))
second_seq = deque(int(x) for x in input().split(','))

rotations = 0
seat_matches = []

while rotations != 10:
    rotations += 1
    num_from_first = first_seq.popleft()
    num_from_second = second_seq.pop()

    char = chr(num_from_first + num_from_second)
    first_combination = str(num_from_first) + char
    second_combination = str(num_from_second) + char

    if first_combination not in seats and second_combination not in seats:
        first_seq.append(num_from_first)
        second_seq.appendleft(num_from_second)

    elif first_combination in seats and first_combination not in seat_matches:
        seat_matches.append(first_combination)

    elif second_combination in seats and second_combination not in seat_matches:
        seat_matches.append(second_combination)

    if len(seat_matches) == 3:
        break

print(f'Seat matches: {", ".join([seat for seat in seat_matches])}')
print(f'Rotations count: {rotations}')
