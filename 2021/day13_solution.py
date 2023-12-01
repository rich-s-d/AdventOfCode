line_1, line_2 = open('day13.txt').readlines()
target = int(line_1)
buses = [(i, int(t)) for i, t in enumerate(line_2.split(',')) if t != 'x']
bus, time_wait = (min([(bus, bus-(target % bus))
                       for _, bus in buses], key=lambda t: t[1]))
print(bus*time_wait)


offsets = [(time_after % bus, bus) for time_after, bus in buses]
candidate = 0
increment = 1
for time_after, bus in offsets:
    while True:
        if candidate % bus == (bus-time_after if time_after > 0 else 0):
            print(candidate % bus)
            break
        candidate += increment
    increment *= bus
print(candidate)  # Part 2: 1012171816131114
