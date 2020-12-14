
# counter, Day 10
from itertools import product
import copy
import collections
cnt = collections.Counter(j2 - j1 for j1, j2 in zip(js, js[1:]))

# Deep copy, Day 11
new_seatplan = None
while new_seatplan != data:
    new_seatplan = copy.deepcopy(data)

# Below snippet from Day 11, counting occupied seat in the 8 positions around any point in a grid.
occupied_count = sum(
    old_seats[row + x][col + y] == '#'
    for x, y in itertools.product((-1, 0, 1), repeat=2)
    if (x, y) != (0, 0)
)


