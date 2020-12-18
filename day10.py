import itertools


def differences(seq):
    d1, d2, d3 = 1, 0, 1
    for i, num in enumerate(seq):
        if i < len(seq)-1:
            difference = seq[i+1] - num
            if difference == 1:
                d1 += 1
            elif difference == 2:
                d2 += 1
            else:
                d3 += 1

    return d1 * d3


def permutations(data):
    dp = [1]
    for i in range(1, len(data)):
        ans = 0
        for j in range(i):
            if data[j] + 3 >= data[i]:
                ans += dp[j]
        dp.append(ans)
    return dp[-1]


with open('day10.txt') as f:
    data = sorted([int(line.strip()) for line in f.read().split('\n')])
    print(f'Part1: {differences(data)}')
    print(f'Part2: {permutations(data)}')
