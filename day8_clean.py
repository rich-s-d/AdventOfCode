import sys


def accumulator_value(data, j=None):
    acc = 0
    index = 0
    visited = set()
    while index not in visited and index < len(data):
        visited.add(index)
        operation = data[index][0]
        if j == index:
            operation = "nop" if operation == "jmp" else "jmp"
        if operation == 'acc':
            acc += int(data[index][1])
            index += 1
        elif operation == 'jmp':
            index += int(data[index][1])
        elif operation == 'nop':
            index += 1
    return acc, index, visited


def fix_bug(visited, data):
    for j in visited:
        if data[j][0] in ("nop", "jmp"):
            accumulator, i, _ = accumulator_value(data, j)
            if i >= len(data):
                return accumulator
                break


def main():
    with open('day8.txt') as f:
        data = [line.split(' ') for line in f.read().split('\n')]
        acc, index, visited = accumulator_value(data)
        accumulator = fix_bug(visited, data)
        print(f'Part 1: {acc}')
        print(f'Part 2: {accumulator}')


if __name__ == '__main__':
    main()
