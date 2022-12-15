from collections import deque


def loading_barrel():
    """
    This func loading barrel with bullets
    return: deque
    """
    global bullets
    barrel = deque()

    # load barbel during hit the barrel_size
    loaded_bullets = 0
    while bullets:
        bullet = bullets.pop()
        barrel.appendleft(bullet)
        loaded_bullets += 1
        if loaded_bullets == barrel_size:
            return barrel
    return barrel


# first line of input receives the price of each bullet – an integer in the range [0-100]
bullet_price = int(input())

# second line receives the size of the gun barrel – an integer in the range [1-5000]
barrel_size = int(input())

# third line receives the bullets – a space-separated integer sequence with [1-100] integers.
# starts shooting bullets back-to-front
bullets = deque([int(x) for x in input().split()])
total_bullets = len(bullets)

# fourth line receives the locks – a space-separated integer sequence with [1-100] integers.
# starts to shoot the locks front-to-back
locks = deque([int(x) for x in input().split()])

# fifth line receives the value of the intelligence – an integer in the range [1-100000]
intelligence = int(input())

# keep the nuber of shouted bullets
used_bullets = 0
current_barrel = loading_barrel()

while locks:

    while current_barrel:
        current_bullet = current_barrel.pop()
        used_bullets += 1
        current_lock = locks[0]

        if current_lock >= current_bullet:
            locks.popleft()
            print('Bang!')
            if not locks:
                break
        else:
            print('Ping!')

    if bullets:
        print('Reloading!')
        current_barrel = loading_barrel()
    else:
        break

if not locks:
    bullets_cost = used_bullets * bullet_price
    money_earned = intelligence - bullets_cost
    print(f'{total_bullets - used_bullets} bullets left. Earned ${money_earned}')
else:
    print(f"Couldn't get through. Locks left: {len(locks)}")
