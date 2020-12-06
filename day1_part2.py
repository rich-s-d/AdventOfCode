

numbers = []
target_number = 2020

with open('day1.txt', mode='r') as f:
    for line in f:
        line = line.rstrip('\n')
        line = int(line)
        numbers.append(line)


for i, number in enumerate(numbers):
    for j, number2 in enumerate(numbers[i+1:]):
        complementary = target_number - number - number2
        if complementary in numbers[i+1:]:
            print("Solution Found: {}, {} and {}".format(
                number, number2, complementary))
            print(f'sum of numbers is {number*number2*complementary}')
            break
