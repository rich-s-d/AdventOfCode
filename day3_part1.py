import os

'''
# this duplicated the lines in the day3.text into a new file. I multiplied by 1500 to make sure that is was at least 3 times wider than it was long, as the tobogan trajectory is 3 to the right, 1 down.
with open('day3.txt', mode='r') as f, open('new.txt', mode='w') as f2:
    for i, line in enumerate(f):
        line = line.strip('\n')
        f2.write(line*2400)
        f2.write('\n')
'''

slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

results = [85, 272, 66, 73, 35]
n = 2
with open('day3_transformed.txt', mode='r') as f:
    x_count = 0
    trees = 0
    for i, line in enumerate(f):
        if i % n == 0:
            if line[x_count] == '#':
                trees += 1
            x_count += 1
    print(trees)


'''
# below calculates line count, which is 323 
with open('new.txt') as f:
    line_count = 0
    for line in f:
        line_count += 1

print(line_count)
'''
