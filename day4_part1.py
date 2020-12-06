
# My overcomplicated answer for part 1.
# Looked for a better example for part 2 from the the megathread.
# I was relying too much on conditional if statements. Better to use key validation.


def group_passports(txt_file):

    #    Groups passports based on a single blank line of seperation in text file.

    contents = txt_file.read()
    groups = [[line.split(" ") for line in group.split(
        "\n")] for group in contents.split("\n\n")]
    return groups


with open(passport_file, 'r') as f:
    groups = group_passports(f)
    flattened = []
    for group in groups:
        new_group = []
        for sublist in group:
            for item in sublist:
                new_group.append(item)
        flattened.append(new_group)

    password_valid = 0
    password_7fields_but_invalid = 0
    password_invalid = 0

    for group in flattened:
        count = 0
        condition = 'cid'
        if len(group) >= 7:
            for item in group:
                if item[0:3] != condition:
                    count += 1
                    if count == 7:
                        password_valid += 1

    print(password_valid)
