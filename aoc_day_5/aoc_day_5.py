def read_file(file_name):
    file = open(file_name)
    data = file.read()
    file.close()
    return data


def parse_instruction(raw_instruction):
    instruction_set = raw_instruction.split(' ')
    parsed_instruction = {}
    for i in range(0, len(instruction_set), 2):
        parsed_instruction[instruction_set[i]
                           ] = int(instruction_set[i + 1])
    return parsed_instruction


def parse(raw_input):
    [raw_stacks, raw_instructions] = raw_input.split("\n\n")

    instructions = list(
        map(parse_instruction, raw_instructions.split('\n')))
    # stacks = [["Z", "N"], ["M", "C", "D"], ["P"]]

    stacks = [
        ["M", "J", "C", "B", "F", "R", "L", "H"],
        ["Z", "C", "D"],
        ["H", "J", "F", "C", "N", "G", "W"],
        ["P", "J", "D", "M", "T", "S", "B"],
        ["N", "C", "D", "R", "J"],
        ["W", "L", "D", "Q", "P", "J", "G", "Z"],
        ["P", "Z", "T", "F", "R", "H"],
        ["L", "V", "M", "G"],
        ["C", "B", "G", "P", "F", "Q", "R", "J"]
    ]
    return (stacks, instructions)


raw_input = read_file("./input.txt")

(stacks, instructions) = parse(raw_input)

# answer 1

# for instruction in instructions:
#     from_stack = instruction["from"] - 1
#     to_stack = instruction["to"] - 1
#     moves = instruction["move"]

#     for move in range(moves):
#         crate = stacks[from_stack].pop()
#         stacks[to_stack].append(crate)


# answer 2

for instruction in instructions:
    from_stack = instruction["from"] - 1
    to_stack = instruction["to"] - 1
    moves = instruction["move"]

    crates = []
    for move in range(moves):
        crates.insert(0, stacks[from_stack].pop())

    stacks[to_stack].extend(crates)


print(stacks)

l = list(map(lambda s: s[len(s)-1], stacks))
print(l)


# TQRFCBSJJ
# RMHFJNVFP
