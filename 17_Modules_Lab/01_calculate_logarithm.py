from math import log

number = int(input())
base = input()

if base == 'natural':
    print(f'{log(number):.2f}')
print(f'{log(number, int(base)):.2f}')
