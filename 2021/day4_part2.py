# This answer came from an answer I liked on Github (cs1201/AOC_2020). Much better than my first attempt (see part 1).
# Example of a passport object(string): ecl:gry byr:1973 iyr:2011 pid:479606625 eyr:2028 hcl:#888785 cid:108 hgt:160cm

import re
passport_file = './day4.txt'


def validate_passport(passport):
    return all(key in passport for key in ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])


def parse_passport(passport):
    # Convert passport to dict
    passport_dict = dict()
    for item in re.split(' |\n', passport):
        passport_dict[item.split(':')[0]] = item.split(
            ':')[1]  # appending to dict in form d[k]=v

    # Validate specific elements
    if validate_passport(passport):
        conditions = [int(passport_dict['byr']) not in range(1920, 2003),
                      int(passport_dict['iyr']) not in range(2010, 2021),
                      int(passport_dict['eyr']) not in range(2020, 2031),
                      passport_dict['hcl'][0] != "#" or len(
            passport_dict['hcl']) != 7 or not passport_dict['hcl'][1:].isalnum(),  # is alfanumneric, string function
            passport_dict['ecl'] not in [
            'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
            len(passport_dict['pid']) != 9,
            not all(x.isdigit() for x in passport_dict['pid']),
            not any(passport_dict['hgt'][-2:] ==
                    measurement for measurement in ["in", "cm"]),
            passport_dict['hgt'][-2:] == "in" and int(
            passport_dict['hgt'][:-2]) not in range(59, 77),
            passport_dict['hgt'][-2:] == "cm" and int(passport_dict['hgt'][:-2]) not in range(150, 194)]
        if any(conditions):
            return False
    else:
        return False
    return True


def part_one(data):
    return sum([validate_passport(passport) for passport in data])


def part_two(data):
    return sum([parse_passport(passport) for passport in data])


with open(passport_file, 'r') as f:
    data = [(x.strip()) for x in f.read().split("\n\n")]
    print(f"Part One: {part_one(data)}")
    print(f"Part Two: {part_two(data)}")

# ecl:gry byr:1973 iyr:2011 pid:479606625 eyr:2028 hcl:#888785 cid:108 hgt:160cm


# Below is a revised condition list under construction.
'''
        conditions = [int(passport_dict['byr']) not in range(1920, 2002),
                      int(passport_dict['iyr']) not in range(2010, 2020),
                      int(passport_dict['eyr']) not in range(2020, 2030),
                      passport_dict['hcl'][0] != '#' or len(
            passport_dict['hcl']) != 7 or not passport_dict['hcl'][1:].isalnum(),
            not isinstance(passport_dict['pid'], (int, float, complex)),
            passport_dict['ecl'] not in 'amb blu brn gry grn hzl oth',
            len(passport_dict['pid']) != 9,
            passport_dict['hgt'][-2:] == 'cm' and int(
                passport_dict['hgt'][:-2]) not in range(150, 193),
            passport_dict['hgt'][-2:] == 'in' and int(passport_dict['hgt'][:-2]) not in range(59, 76)]
'''
