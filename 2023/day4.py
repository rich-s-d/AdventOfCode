import os
import re

os.chdir("/Users/shanerich/AdventOfCode/2023")

with open("./day4.txt") as f:
    data = [x.strip().split("|") for x in f.read().splitlines()]


points = 0

for card in data:
    pattern = r"\d+"
    matches_winning_numbers = re.findall(pattern, card[0][-31:])
    matches_my_numbers = re.findall(pattern, card[1])

    # now check if any of the matches_my_numbers are in matches_winning_numbers, and if they are, make a count and add by 1 for every match
    count = 0
    for number in matches_my_numbers:
        if number in matches_winning_numbers:
            count += 1

    if count != 0:
        number = 1
        for i in range(count - 1):
            number *= 2
        points += number
    

print(points)