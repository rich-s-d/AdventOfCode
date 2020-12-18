import copy

# Notes: This solution needs to be debugged still. Returning 7417. Conditions need to be heavily simplified.

with open('day11.txt') as f:
    new_seatplan = [list('.' + line.strip() + '.')
                    for line in f if line.strip()]
    # Buffer the seats to prevent out of bounds checks.
    # new_seatplan = [['.', '#', '#', 'L', 'L', '.'], ['.', 'L', '#', '#', '#', '.'], ['.', '#', '#', 'L', 'L', '.'], ['.', 'L', '#', '#', '#', '.']]
    new_seatplan = [['.'] * len(new_seatplan[0])] + \
        new_seatplan + [['.'] * len(new_seatplan[0])]


data = None
while new_seatplan != data:
    data = copy.deepcopy(new_seatplan)
    for i, seatrow in enumerate(data):
        for j, seat in enumerate(seatrow):
            count = 0
            if seat == '.':
                continue
            if seat == 'L' and data[i][j-1] == 'L' or '.':
                count += 1
            if seat == 'L' and data[i][j+1] == 'L' or '.':
                count += 1
            if seat == 'L' and data[i-1][j] == 'L' or '.':
                count += 1
            if seat == 'L' and data[i-1][j-1] == 'L' or '.':
                count += 1
            if seat == 'L' and data[i-1][j+1] == 'L' or '.':
                count += 1
            if seat == 'L' and data[i+1][j] == 'L' or '.':
                count += 1
            if seat == 'L' and data[i+1][j-1] == 'L' or '.':
                count += 1
            if seat == 'L' and data[i+1][j+1] == 'L' or '.':
                count += 1

            if (seat == '#' and data[i][j-1] == '#' or '.'
                and (data[i][j+1] == '#' or '.')
                and (data[i-1][j] == '#' or '.')
                and (data[i-1][j-1] == '#' or '.')
                and (data[i-1][j+1] == '#' or '.')
                and (data[i+1][j] == '#' or '.')
                and (data[i+1][j-1] == '#' or '.')
                    and (data[i+1][j+1] == '#' or '.')):
                new_seatplan[i][j] = 'L'

            if count >= 4:
                new_seatplan[i][j] = '#'


#print(sum(x.count('L') for x in data))
# return " ".join(data).count('L')
print(sum(row.count('#') for row in new_seatplan))

# 2346 is answer to part1
# print(data)
