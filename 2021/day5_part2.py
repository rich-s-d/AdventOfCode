from time import time
import math
NUM_ROWS = 128
NUM_COLUMNS = 8


def bsp(sector, valid_range):
    if sector == "F" or sector == "L":
        valid_range = valid_range[:round(len(valid_range)/2)]
    if sector == "B" or sector == "R":
        valid_range = valid_range[round(len(valid_range)/2):]
    return valid_range


def get_seat_info(boarding_number):
    row_info = boarding_number[:-3]
    column_info = boarding_number[-3:]
    valid_row_range = range(0, 128)
    valid_column_range = range(0, 8)

    # ROW
    for i, sector in enumerate(row_info):
        valid_row_range = bsp(row_info[i], valid_row_range)
        if valid_row_range[0] == valid_row_range[-1]:
            row = valid_row_range[0]
    # COLUMN
    for i, sector in enumerate(column_info):
        valid_column_range = bsp(column_info[i], valid_column_range)
        if valid_column_range[0] == valid_column_range[-1]:
            column = valid_column_range[0]

    seat_id = row * 8 + column

    return seat_id


def find_missing(list_of_seats):
    missing_seats = [x for x in range(list_of_seats[0], list_of_seats[-1]+1)
                     if x not in list_of_seats]
    return missing_seats


def find_seat(data):
    list_of_seats = []
    for seat in data:
        seat_id = get_seat_info(seat)
        list_of_seats.append(seat_id)
        missing_seats = find_missing(sorted(list_of_seats))
    return missing_seats


def part_one(data):
    return max([get_seat_info(boarding_pass) for boarding_pass in data])


def part_two(data):
    return find_seat(data)


t1 = time()
with open("./day5.txt") as f:
    data = [x.strip() for x in f]
    print(f"Part One: {part_one(data)}")
    t2 = time()
    print(f"Part Two: {part_two(data)}")
    t3 = time()

print(t2-t1)
print(t3-t2)
