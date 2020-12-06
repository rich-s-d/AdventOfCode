in_ = ' '.join(open('day6.txt').read().splitlines()).split('  ')
print(sum(len(set(a.replace(' ', ''))) for a in in_))
print(sum(len(set.intersection(*[set(x) for x in a.split()])) for a in in_))
