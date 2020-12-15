numbers = [11, 0, 1, 10, 5, 19]


def game(numbers, turn):
    d = {k: v for v, k in enumerate(numbers)}
    next_number = 0
    round = len(numbers)
    while round < turn:
        current = next_number

        if next_number not in d:
            next_number = 0

        else:
            next_number = round - d[next_number]
        d[current] = round
        round += 1
    return(current)


print(f'Part 1: {game(numbers, 2020)}')
print(f'Part 2: {game(numbers, 30000000)}')
