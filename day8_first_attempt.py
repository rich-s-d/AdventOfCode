acc = 0
index = 0
instruction_dict = {}


def accumulator_value(data):
    global acc
    global index
    instruction = data[index]
    operation = data[index][0]
    if index in instruction_dict.keys():
        return acc, instruction_dict
    else:
        instruction_dict[index] = instruction
        if operation == 'acc':
            acc += int(data[index][1])
            index += 1
        elif operation == 'jmp':
            index += int(data[index][1])
        elif operation == 'nop':
            index += 1
        return accumulator_value(data)


def accumulator_value_fix(data):
    global acc
    global index
    global instruction_dict
    operation = data[index][0]
    instruction = data[index]
    if index == 640:
        return acc
    elif index in instruction_dict.keys():
        return 'program still broken'
    else:
        instruction_dict[index] = instruction
        if operation == 'acc':
            acc += int(data[index][1])
            index += 1
        elif operation == 'jmp':
            index += int(data[index][1])
        elif operation == 'nop':
            index += 1
        return accumulator_value_fix(data)


def loop_fix(output_dict, data):
    global index
    global instruction_dict
    global acc
    acc_list = []
    for i, instruction in output_dict.items():
        data_copy = data.copy()

        if instruction[0] == 'acc':
            pass
        elif instruction[0] == 'jmp':
            data_copy[i] = ['nop', instruction[1]]
        elif instruction[0] == 'nop':
            data_copy[i] = ['jmp', instruction[1]]

        accumulator = accumulator_value_fix(data_copy)
        acc_list.append(accumulator)
        acc = 0
        index = 0
        instruction_dict = {}

    acc_list = [x for x in acc_list if x != 'program still broken']
    return acc_list[0]


with open('day8.txt') as f:
    data = [line.split(' ') for line in f.read().split('\n')]
    print(f'Part 1: {accumulator_value(data)[0]}')
    output_dict = accumulator_value(data)[1]
    print(f'Part 2: {loop_fix(output_dict, data)}')
