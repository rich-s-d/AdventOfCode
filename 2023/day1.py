import os
import re

os.chdir("/Users/shanerich/AdventOfCode/2023")


def extract_first_and_last_numbers(text):
    pattern = r"\d+"
    matches = re.findall(pattern, text)
    if len(matches) == 1:
        return ((matches[0]), (matches[0]))
    elif len(matches) >= 2:
        return (matches[0]), (matches[-1])
    else:
        return None
  

def calculate_sum(data):
    sum = 0
    for i in range(len(data)):
        data[i] = [extract_first_and_last_numbers(x) for x in data[i]]
        flattened_data = [item for sublist in data for item in sublist]
        number_to_add = flattened_data[i][0][0] + flattened_data[i][1][-1]
        sum += int(number_to_add)
    return sum

with open("./day1.txt") as f:
    data = [x.strip().split(',') for x in f.read().splitlines()]


print(calculate_sum(data))
