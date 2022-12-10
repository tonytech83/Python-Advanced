from collections import deque

# create queue form console input
kids = deque(input().split())

# received number of tosses (skipped kids)
tosses_count = int(input())

current_count = 0

# loop until left only one kid in the queue
while len(kids) > 1:
    # this is the current toss
    current_count += 1

    # take the current kid
    kid = kids.popleft()

    # if current_count is not tosses_count add the kid to the end of queue
    if current_count < tosses_count:
        kids.append(kid)
    # else print the removed kid and reset the current_count
    else:
        print(f'Removed {kid}')
        current_count = 0

print(f'Last is {kids.popleft()}')
