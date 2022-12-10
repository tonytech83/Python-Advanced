numbers_str = input().split()

while numbers_str:
    last_number = numbers_str.pop()
    print(last_number, end=' ')
