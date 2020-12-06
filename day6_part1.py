

def question_count(group):
    group_set = set(group)
    n_set = set('\n')
    group_set = group_set - n_set
    length = len(group_set)
    return length


with open('day6.txt', mode='r') as f:
    data1 = [(x.strip()) for x in f.read().split("\n\n")]
    print(f'Part 1: {sum(question_count(group) for group in data1)}')
