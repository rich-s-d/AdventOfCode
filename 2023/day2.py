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


def sum_of_ids(data):
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
    return sum_of_ids


def highest(numbers_as_strings):
    numbers = [int(x) for x in numbers_as_strings]
    highest = max(numbers)
    return highest


def sum_of_powers(data):
    sum_of_powers = 0
    for game in data:
        red = extract_numbers(game, "red")
        highest_red = highest(red)
        blue = extract_numbers(game, "blue")
        highest_blue = highest(blue)
        green = extract_numbers(game, "green")
        highest_green = highest(green)
        sum_of_powers += highest_red * highest_blue * highest_green
    return sum_of_powers

# Solution Part One
print(sum_of_ids(data))

# Solution Part Two
print(sum_of_powers(data))
