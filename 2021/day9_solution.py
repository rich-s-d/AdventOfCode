from collections import *
from functools import lru_cache
import heapq
import itertools
import math
import random
import sys


def main():
    fin = open("day9.txt", "r")
    xs = [int(line.strip()) for line in fin.readlines() if line.strip()]

    sums = set()
    n = len(xs)
    for i, x in enumerate(xs):
        valid = x in sums or i < 25
        if not valid:
            print("part 1", x)
            break
        for j in range(n):
            sums.add(x + xs[j])

    for i in range(n):
        s = 0
        for j in range(i, n):
            s += xs[j]
            if s == 1930745883:
                a = xs[i:j+1]
                print("part 2", a, sum(a), min(a) + max(a))


if __name__ == "__main__":
    main()
