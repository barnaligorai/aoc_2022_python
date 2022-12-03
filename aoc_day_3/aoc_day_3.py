from functools import reduce


def read_file(file_name):
    file = open(file_name)
    data = file.read()
    file.close()
    return data


def find_common_item(text1, text2):
    for letter in text1:
        if letter in text2:
            return letter


def item_priority(item):
    ascii_value = ord(item)
    difference = 38
    if ascii_value > 96:
        difference = 96
    return ascii_value - difference


def priority_of_common_item(item):
    divide_at = len(item)/2
    compartment_items = [item[:divide_at], item[divide_at:]]
    common_item = find_common_item(*compartment_items)
    return item_priority(common_item)


def sum_of_priorities(sum, item):
    return sum + priority_of_common_item(item)


raw_input = read_file("./input.txt").splitlines()
sum = reduce(sum_of_priorities, raw_input, 0)
print(sum)
