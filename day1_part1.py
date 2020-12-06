numbers = []
target_number = 2020

with open('day1.txt', mode='r') as f:
    for line in f:
        line = line.rstrip('\n')
        line = int(line)
        numbers.append(line)


for i, number in enumerate(numbers):
    complementary = target_number - number
    if complementary in numbers[i+1:]:
        print("Solution Found: {} and {}".format(number, complementary))
        print(f'sum of numbers is {number*complementary}')
        break
else:  # note 3
    print("No solutions exist")
