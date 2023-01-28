from collections import deque


def try_clime_peak(supply: int, stamina: int, difficult: int):
    """
    This func check if current supply and stamina are enough to clime the peak with current difficult.
    """
    if supply + stamina >= difficult:
        return True
    return False


# set of supplies
supplies = [int(x) for x in input().split(', ')]

# queue of stamina
stamina = deque(int(x) for x in input().split(', '))

mountain_peaks = deque([
    ('Vihren', 80),
    ('Kutelo', 90),
    ('Banski Suhodol', 100),
    ('Polezhan', 60),
    ('Kamenitza', 70),
])

# stored all climbed peaks
conquered_peaks = []

while mountain_peaks:
    if not supplies or not stamina:
        break

    current_supply = supplies.pop()
    current_stamina = stamina.popleft()
    current_peak, current_difficult = mountain_peaks.popleft()

    if try_clime_peak(current_supply, current_stamina, current_difficult):
        conquered_peaks.append(current_peak)
    else:
        mountain_peaks.appendleft((current_peak, current_difficult))

if not mountain_peaks:
    print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
else:
    print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")

if conquered_peaks:
    print('Conquered peaks:')
    print(*conquered_peaks, sep='\n')
