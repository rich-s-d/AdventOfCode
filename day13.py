
# Part 2 is not finished.

def next_bus(buses, earliest):
    bus_waittime = [(bus, bus-(earliest % bus)) for _, bus in buses]
    bus, wait = min(bus_waittime, key=lambda x: x[1])
    result = bus*wait
    return result


def earliest_timestamp(buses):
    pass


with open('day13.txt') as f:
    data = [x.strip().split(',') for x in f.read().splitlines() if x != 'x']
    earliest = int(data[0][0])
    buses = [(i, int(x)) for i, x in enumerate(data[1]) if x != 'x']
    # buses2
    #print(f'Part 1: {next_bus(buses, earliest)}')
    print(f'Part 2: {earliest_timestamp(buses)}')
