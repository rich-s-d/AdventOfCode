lines = open('day14.txt').read().split('\n')
msk = 'X' * 36
d = {}


def f(x):
    for i in range(36):
        if msk[36 - 1 - i] == '1':
            x |= (1 << i)
        if msk[36 - 1 - i] == '0':
            x &= (~(1 << i))
    return x


for line in lines:
    if line.startswith('mask'):
        msk = line[len('mask = '):]
        continue
    a, b = line.split(' = ')
    b = int(b)
    a = int(a[a.find('[') + 1:a.find(']')])
    #print(a, b, msk)

    d[a] = f(b)
s = 0
for key in d:
    s += d[key]
print(s)


# part2

lines = open('day14.txt').read().split('\n')
msk = 'X' * 36
d = {}


def f(x, i):
    if i == 36:
        return [0]
    res = f(x, i + 1)
    n = len(res)
    ress = []
    for y in res:
        if msk[36 - 1 - i] == '0':
            ress.append(y | (x & (1 << i)))
        elif msk[36 - 1 - i] == '1':
            ress.append(y | (1 << i))
        elif msk[36 - 1 - i] == 'X':
            ress.append(y)
            ress.append(y | (1 << i))
    return ress


for line in lines:
    if line.startswith('mask'):
        msk = line[len('mask = '):]
        continue
    a, b = line.split(' = ')
    b = int(b)
    a = int(a[a.find('[') + 1:a.find(']')])
    for x in f(a, 0):
        d[x] = b
s = 0
for key in d:
    s += d[key]
# print(s)
