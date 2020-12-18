# from reddit, really nice answer by thomasahle

import sys
import collections

with open('day10.txt') as f:
    js = sorted([int(line.strip()) for line in f.read().split('\n')])
    js = [0] + js + [js[-1] + 3]
cnt = collections.Counter(j2 - j1 for j1, j2 in zip(js, js[1:]))
print(cnt[1] * cnt[3])

dp = [1] + [0] * (len(js) - 1)
print(dp)
for i, j in enumerate(js):
    for l in range(i - 3, i):
        if j - js[l] <= 3:
            dp[i] += dp[l]
print(dp[-1])

print(dp)
