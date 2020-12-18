nesting_rules = {}
with open('day7.txt') as f:
    for line in f:
        b, a = line.strip('\n.').split('contain')
        outer = b.rstrip('bags ')
        inners = [b.strip("bags ").split(' ', 1)
                  for b in a.split(',') if not 'no' in b]

        nesting_rules[outer] = inners


def can_contain_shiny_gold(bag_colour):
    if 'shiny gold' in bag_colour:
        print('shiny gold in bag_colour')
        return True
    else:
        return any(can_contain_shiny_gold(colour) for _, colour in nesting_rules[bag_colour])


def number_of_bags_contained(bag_colour):
    if not nesting_rules[bag_colour]:
        return 0
    else:
        return sum(int(num) + int(num) * number_of_bags_contained(colour) for num, colour in nesting_rules[bag_colour])


print(sum(can_contain_shiny_gold(colour)
          for colour in nesting_rules.keys() if colour != 'shiny gold'))
print(number_of_bags_contained('shiny gold'))

#print(nesting_rules['shiny gold'])
#print(nesting_rules['striped gold'])
'''
for x in nesting_rules.keys():
    print(x)
    break

print(nesting_rules['dotted blue'])
print('/n')
print(nesting_rules['wavy bronze'])
'''
