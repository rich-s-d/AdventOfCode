import os
import re

os.chdir("/Users/shanerich/AdventOfCode/2023")

number_map = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

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
        #comment out replace_words_with_numbers for part 1
        replace_words_with_numbers(i, data)
        data[i] = [extract_first_and_last_numbers(x) for x in data[i]]
        flattened_data = [item for sublist in data for item in sublist]
        number_to_add = flattened_data[i][0][0] + flattened_data[i][1][-1]
        sum += int(number_to_add)
    return sum


def replace_words_with_numbers(i, data):
    for key in number_map:
        # replacement adds the key back either side of the number so that spelling is not broken on other number words.
        replacement = key + str(number_map[key]) + key
        data[i] = [x.replace(key, replacement) for x in data[i]]

with open("./day1.txt") as f:
    data = [x.strip().split(',') for x in f.read().splitlines()]


print(calculate_sum(data))
