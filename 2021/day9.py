# solution from a reddit/github answer for this one.


PREAMBLE = 25


def check_valid(seq):
    return any((a != b and a+b == seq[-1]) for a in seq[:-1] for b in seq[:-1])
    # the above is a generator expression and they are an efficient way to check conditions in a list!


def part1(data):
    for i, num in enumerate(data):
        if i > PREAMBLE:
            if not check_valid(data[i-PREAMBLE-1:i]):
                return data[i-1]


def part2(data):
    invalid_val = part1(data)
    for i, val_a in enumerate(data):
        window = []
        j = 1
        window.append(val_a)
        while sum(window) <= invalid_val:
            window.append(data[i+j])
            if sum(window) == invalid_val:
                return max(window) + min(window)
            j += 1


def main():
    with open('day9.txt') as f:
        data = [int(line.strip()) for line in f.read().split('\n')]
        print(part1(data))
        print(part2(data))


if __name__ == '__main__':
    main()
