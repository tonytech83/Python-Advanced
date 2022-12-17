def is_vip(guest_code):
    """
    This func check if first char in guest_code is digit
    guest_code: str
    return: boolean
    """
    return guest_code[0].isdigit()


# create vip and regular sets for different codes
vip_guests = set()
regular_guests = set()

n = int(input())

for _ in range(n):
    reservation = input()

    # if code starts with digit adds it vip_guests
    if is_vip(reservation):
        vip_guests.add(reservation)
    else:
        regular_guests.add(reservation)

# read codes coming to party and removes from vip or regular guests sets
while True:
    person_code = input()
    if person_code == 'END':
        break

    if is_vip(person_code):
        vip_guests.remove(person_code)
    else:
        regular_guests.remove(person_code)

# calculate total not comes codes
print(len(vip_guests) + len(regular_guests))
# prints vip and guest not comes to the party sorted in ascending order
[print(x) for x in sorted(vip_guests)]
[print(x) for x in sorted(regular_guests)]
