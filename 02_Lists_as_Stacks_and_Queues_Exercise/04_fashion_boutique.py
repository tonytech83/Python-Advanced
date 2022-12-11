# stack of clothes boxes
clothes_boxes = [int(x) for x in input().split()]
rack_capacity = int(input())

current_rack = rack_capacity
racks_count = 1

while clothes_boxes:
    # peek element from stack (access last element)
    current_box = clothes_boxes[-1]

    if current_box > current_rack:
        racks_count += 1
        current_rack = rack_capacity
    else:
        current_rack -= clothes_boxes.pop()

print(racks_count)
