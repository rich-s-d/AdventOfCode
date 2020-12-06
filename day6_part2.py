

def question_count(group):
    group_set = set(group)
    n_set = set('\n')
    group_set = group_set - n_set
    length = len(group_set)
    return length


def everyone_yes(group):
    persons = group.split('\n')
    set_list = []
    for person in persons:
        person_set = set(person)
        set_list.append(person_set)
    intersection = set_list[-1].intersection(*set_list)
    return len(intersection)


with open('day6.txt', mode='r') as f:
    data = [(x.strip()) for x in f.read().split("\n\n")]
    print(f'Part 1: {sum(question_count(group) for group in data)}')
    print(f'Part 2: {sum(everyone_yes(group) for group in data)}')
