

def bag_colours(data, adjective, colour):
    primary_list = []
    for group in data:
        combined = adjective + ' ' + colour
        if combined in group:
            colour_list.append(group)
    for group in primary_list:
        splitted = group.split()
        if splitted[0] == adjective and splitted[1] == colour:
            colour_list.remove(group)
        if splitted[0] != adjective or splitted[1] != colour:

    return splitted


with open('day7.txt', mode='r') as f:
    data = [x for x in f.read().split('\n')]


print(bag_colours(data, 'shiny', 'gold'))


# print('shiny gold bags contain no other bags' in data) # returned False
