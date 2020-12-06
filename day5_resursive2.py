from math import ceil
from time import time

input = open("day5.txt", "r")
result = 0
seats = [[True for i in range(8)] for i in range(128)]


def getSeat(start, end, seat, index):
    if index == len(seat):
        return start
    else:
        if seat[index] in 'FL':
            # could use round() instead of ceil
            return getSeat(start, start + ceil((end-start)/2), seat, index+1)
        else:
            return getSeat(start + ceil((end-start)/2), end, seat, index+1)


for line in input:
    line = line.strip()
    row = line[:7]
    column = line[7:]
    seatRow = getSeat(0, 127, row, 0)
    seatCol = getSeat(0, 7, column, 0)
    seats[seatRow][seatCol] = False
    seatId = seatRow * 8 + seatCol
    if seatId > result:
        result = seatId

t1 = time()

print('Highest seat ID:', result)
t2 = time()
for i in range(len(seats)):
    for j in range(len(seats[0])):
        if seats[i][j] and not seats[i][j-1] and not seats[i][j+1]:
            print('My seat Id:', i * 8 + j)

t3 = time()
print(t2-t1)
print(t3-t2)
