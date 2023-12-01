# ADVENTOFCODE/day4.py


import time


def group_passports(txt_file):
    contents = txt_file.read()
    groups = [[line.split(" ") for line in group.split(
        "\n")] for group in contents.split("\n\n")]
    return groups
    

t1 = time.time()
with open('./day4.txt', 'r') as f:
    groups = group_passports(f)
    flattened = []
    for group in groups:
        new_group = []
        for sublist in group:
            for item in sublist:
                new_group.append(item)
        flattened.append(new_group)

    passport_valid = 0
 
    for passport in flattened:
        count = 0
        optional_condition = 'cid'
        if len(passport) >= 7:
            for key in passport:
                if key[0:3] != optional_condition:
                    count += 1
                    if count == 7:
                        passport_valid += 1

    print(passport_valid)
    t2 = time.time()
    print("Time taken to execute: ", round(t2-t1, 4), " seconds")

# Improvements?
# Certainly!
# 1. Validation is not explicit, ie., not easily read.
# 2. Validation is impossible to test, ie., not unitised.
# 3. Unnecessary work nesting and then flattening lists during parsing.