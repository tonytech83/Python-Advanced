from collections import deque

eggs = deque(int(x) for x in input().split(', '))
papers = [int(x) for x in input().split(', ')]

filled_boxes = 0
BOX_SIZE = 50

while eggs and papers:
    egg = eggs.popleft()

    if egg <= 0:
        continue

    if egg == 13:
        papers[0], papers[-1] = papers[-1], papers[0]
        continue

    paper = papers.pop()

    if egg + paper <= BOX_SIZE:
        filled_boxes += 1

if filled_boxes > 0:
    print(f'Great! You filled {filled_boxes} boxes.')
else:
    print("Sorry! You couldn't fill any boxes!")

if eggs:
    print(f'Eggs left: {", ".join([str(x) for x in eggs])}')
if papers:
    print(f'Pieces of paper left: {", ".join([str(x) for x in papers])}')
