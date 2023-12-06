import os
import re
from itertools import islice

os.chdir("/Users/shanerich/AdventOfCode/2023")

with open("./day3.txt") as f:
    data = [x.strip() for x in f.read().splitlines()]


def detect_number(data):
    pattern = r"\d+"
    matches = re.findall(pattern, data[0])
    if matches:
        return True


def detect_symbol(i, length, top_line, bottom_line, middle_line):
    # handle numbers at right hand edge, and numbers with only 2 digits.
    if length == 2:
        if i > 136:
            index_check_list = [i - 1, i, i + 1]
        else:
            index_check_list = [i - 1, i, i + 1, i + 2]
    else:
        if i > 136:
            index_check_list = [i - 1, i, i + 1, i + 2]
        else:
            index_check_list = [i - 1, i, i + 1, i + 2, i + 3]

    pattern = r"[*%@&=\/\-+$#]"

    for ind in index_check_list:
        column_top = top_line[ind]
        column_bottom = bottom_line[ind]
        column_middle = middle_line[ind]
        matches_top = re.search(pattern, column_top)
        matches_bottom = re.search(pattern, column_bottom)
        matches_middle = re.search(pattern, column_middle)
        if matches_top or matches_bottom or matches_middle:
            return True


def get_length(string):
    pattern = r"\d+"
    matches = re.findall(pattern, string)
    return len(matches[0])


def calculate_sum(data):
    sum = 0
    for index, line in enumerate(data):
        if index == 0:
            top_line = "............................................................................................................................................"
        else:
            top_line = data[index - 1]
        if index == 139:
            bottom_line = "............................................................................................................................................"
        else:
            bottom_line = data[index + 1]
        middle_line = data[index]

        lit = iter(enumerate(line))
        for i, column in lit:
            if detect_number(column):
                length = get_length(line[i:i+3])
                result = detect_symbol(i, length, top_line, bottom_line, middle_line)
                if result:
                    sum += int(line[i:i+length])
                next(islice(lit, length, length), None)
    return sum


print(calculate_sum(data))
