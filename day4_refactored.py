# ADVENTOFCODE/day4_refactored.py


import time


def validate_passport(passport):
    return all(key in passport for key in ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])


def sum_of_valid_passports(data):
    return sum([validate_passport(passport) for passport in data])


def main():
    t1 = time.time()
    with open('./day4.txt', 'r') as f:
        data = [(x.strip()) for x in f.read().split("\n\n")]
        print(f"Number of Valid Passports: {sum_of_valid_passports(data)}")
        t2 = time.time()
        print("Time taken to execute: ", round(t2-t1, 4), " seconds")


if __name__ == "__main__":
    main()


# Methods used in production code:
# 1. Being explicit.
# 2. Unitisation for testing.
# 3. Timed: refactored code is faster.