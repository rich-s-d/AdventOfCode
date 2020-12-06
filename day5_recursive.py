import math

with open('./day5.txt') as f:
    boardingPasses = [line.rstrip() for line in f]
    for x in boardingPasses:
        print(type(x))
        break


def findSeat(low, high, letters):  # great example of a resursive function.
    if len(letters) == 0:
        return low
    else:
        letter = letters.pop(0)
        mid = math.floor((high + low)/2)
        if letter == 'F' or letter == 'L':
            return findSeat(low, mid, letters)
        elif letter == 'B' or letter == 'R':
            return findSeat(mid, high, letters)


bpIdList = []
for boardingPass in boardingPasses:
    boardingPass = list(boardingPass)
    bpIdList.append(
        findSeat(0, 128, boardingPass[0:7]) * 8 + findSeat(0, 8, boardingPass[7:10]))

print("Part 1:", max(bpIdList))
completeIdList = [x for x in range(min(bpIdList), max(bpIdList))]
print("Part 2:", (set(completeIdList) - set(bpIdList)).pop())
