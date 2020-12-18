def question_count(group):
    group_set = set(group.replace(' ', ''))
    length = len(group_set)
    return length


def everyone_yes(group):
    persons = group.split(' ')
    set_list = []
    for person in persons:
        person_set = set(person)
        set_list.append(person_set)
    intersection = set_list[-1].intersection(*set_list)
    return len(intersection)


with open('day6.txt', mode='r') as f:
    #data = [(x.strip()) for x in f.read().split("\n\n")]
    data = ' '.join(f.read().splitlines()).split('  ')
    print(f'Part 1: {sum(question_count(group) for group in data)}')
    print(f'Part 2: {sum(everyone_yes(group) for group in data)}')
