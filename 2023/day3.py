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


def get_rows_for_analysis(index, line, data):
    if index == 0:
        top_line = "............................................................................................................................................"
    else:
        top_line = data[index - 1]
    if index == 139:
        bottom_line = "............................................................................................................................................"
    else:
        bottom_line = data[index + 1]
    middle_line = data[index]
    return bottom_line, middle_line, top_line


def calculate_sum(data):
    sum = 0
    for index, line in enumerate(data):
        bottom_line, middle_line, top_line = get_rows_for_analysis(index, line, data)

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


#part 2

def detect_gear(data):
    pattern = r"[*]"
    matches = re.findall(pattern, data[0])
    if matches:
        return True
    

def flatten(nested_list):
    flat_list = [element for sublist in nested_list for element in sublist if len(element) > 1]
    return flat_list

def detect_numbers_around_gear(i, top_line, bottom_line, middle_line):
    # handle numbers at right hand edge, and numbers with only 2 digits.
    # if i > 136:
    #     index_check_list = [i - 1, i, i + 1]
    # else:
    #     index_check_list = [i - 1, i, i + 1, i + 2]
    # if i > 136:
    #     index_check_list = [i - 1, i, i + 1, i + 2]
    # else:
    #     index_check_list = [i - 1, i, i + 1, i + 2, i + 3]

    pattern = r"\d+"

    index_left = i - 1
    index_right = i + 1

    column_top_left, column_top_right = top_line[index_left], top_line[index_right]
    column_bottom_left, column_bottom_right = bottom_line[index_left], bottom_line[index_right]
    column_middle_left, column_middle_right = middle_line[index_left], middle_line[index_right]

    matches_top_left, matches_top_right = re.search(pattern, column_top_left), re.search(pattern, column_top_right)
    matches_bottom_left, matches_bottom_right = re.search(pattern, column_bottom_left), re.search(pattern, column_bottom_right)
    matches_middle_left, matches_middle_right = re.search(pattern, column_middle_left), re.search(pattern, column_middle_right)


    index_start = i - 3
    index_stop = i + 4

    matches = []

    if matches_top_left:
        column_top_left = top_line[index_start: i+2]
        matches.append(re.findall(pattern, column_top_left))
    if matches_top_right:
        column_top_right = top_line[i-2: index_stop]
        matches.append(re.findall(pattern, column_top_right))
    if matches_bottom_left:
        column_bottom_left = bottom_line[index_start: i+2]
        matches.append(re.findall(pattern, column_bottom_left))
    if matches_bottom_right:
        column_bottom_right = bottom_line[i-2: index_stop]
        matches.append(re.findall(pattern, column_bottom_right))
    if matches_middle_left:
        column_middle_left = middle_line[index_start: i+2]
        matches.append(re.findall(pattern, column_middle_left))
    if matches_middle_right:
        column_middle_right = middle_line[i-2: index_stop]
        matches.append(re.findall(pattern, column_middle_right))
    
    # column_top = top_line[index_start: index_stop]
    # column_bottom = bottom_line[index_start: index_stop]
    # column_middle = middle_line[index_start: index_stop]

    # matches.append(re.findall(pattern, column_top))
    # matches.append(re.findall(pattern, column_bottom))
    # matches.append(re.findall(pattern, column_middle))
    flattened_list = flatten(matches)
    # remove duplicates
    my_set = set(flattened_list)
    # convert back to list
    my_list = list(my_set)
    return my_list



def calculate_gear_ratio(data):
    sum = 0
    for index, line in enumerate(data):
        bottom_line, middle_line, top_line = get_rows_for_analysis(index, line, data)

        lit = iter(enumerate(line))
        for i, column in lit:
            if detect_gear(column):
                # length = get_length(line[i:i+3])
                result = detect_numbers_around_gear(i, top_line, bottom_line, middle_line)
                if len(result) == 2:
                    sum += int(result[0]) * int(result[1])
    return sum

print(calculate_gear_ratio(data))
