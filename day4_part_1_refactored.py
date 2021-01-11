
def validate_passport(passport):
    return all(key in passport for key in ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])


def part_one(data):
    return sum([validate_passport(passport) for passport in data])


with open('./day4.txt', 'r') as f:
    data = [(x.strip()) for x in f.read().split("\n\n")]
    print(f"Part One: {part_one(data)}")
