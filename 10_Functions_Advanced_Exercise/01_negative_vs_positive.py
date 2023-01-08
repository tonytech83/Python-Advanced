def find_positive_and_negative_sums(*args):
    p_sum = sum(x for x in args if x > 0)
    n_sum = -sum(-x for x in args if x < 0)
    return p_sum, n_sum


numbers = [int(x) for x in input().split()]

positive_sum, negative_sum = find_positive_and_negative_sums(*numbers)

print(negative_sum)
print(positive_sum)

if positive_sum > abs(negative_sum):
    print('The positives are stronger than the negatives')
else:
    print('The negatives are stronger than the positives')
