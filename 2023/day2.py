import os
import re

os.chdir("/Users/shanerich/AdventOfCode/2023")

with open("./day2.txt") as f:
    data = [x.strip().split("\n") for x in f.read().splitlines()]

def extract_numbers(data, colour):
    pattern = rf"(\d+)\s+{(colour)}"
    matches = re.findall(pattern, data[0])
    return matches

def possible(red, threshold):
    possible = True
    for round in red:
        as_number = int(round)
        if as_number > threshold:
            possible = False
    return possible

sum_of_ids = 0

for index, game in enumerate(data):
    red = extract_numbers(game, "red")
    red_result = possible(red, 12)
    blue = extract_numbers(game, "blue")
    blue_result = possible(blue, 14)
    green = extract_numbers(game, "green")
    green_result = possible(green, 13)
    if red_result and blue_result and green_result:
        sum_of_ids += index + 1

print(sum_of_ids)