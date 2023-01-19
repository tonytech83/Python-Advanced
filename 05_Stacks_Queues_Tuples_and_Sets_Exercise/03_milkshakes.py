from collections import deque


def output():
    """
    This function print the final result as is requested.
    """
    if milkshakes == 5:
        print('Great! You made all the chocolate milkshakes needed!')
    else:
        print('Not enough milkshakes.')

    print(f'Chocolate: {", ".join(map(str, chocolates)) or "empty"}')
    print(f'Milk: {", ".join(map(str, milk_cups)) or "empty"}')


# read chocolates input in stack
chocolates = [int(x) for x in input().split(', ')]
# read milk cups input in queue
milk_cups = deque(int(x) for x in input().split(', '))

milkshakes = 0

empty = False

while chocolates and milk_cups and milkshakes < 5:

    chocolate = chocolates.pop()
    milk = milk_cups.popleft()

    # If any of the values are equal to or below 0,
    # you should remove them from the records right before mixing them with the other ingredient.
    if chocolate <= 0 and milk <= 0:
        continue

    if chocolate <= 0:
        milk_cups.appendleft(milk)
        continue

    if milk <= 0:
        chocolates.append(chocolate)
        continue

    # if both are equal increase milkshakes
    # else move the cup of milk at the end of the sequence and
    # decrease the value of the chocolate by 5 without moving it from its position
    if chocolate == milk:
        milkshakes += 1
    else:
        milk_cups.append(milk)
        chocolates.append(chocolate - 5)

output()
