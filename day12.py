
direction = 90
starting_point = (0, 0)
#instructions = []
with open('day12.txt') as f:
    for line in f:
        line = line.strip('\n')
        direction = line[0]
        value = int(line[1:])
        result = [direction, value]
        # instructions.append(result)


print(instructions)
