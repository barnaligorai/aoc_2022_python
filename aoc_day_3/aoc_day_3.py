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
    compartment_items = partition(item, len(item)/2)
    common_item = find_common_item(*compartment_items)
    return item_priority(common_item)


def sum_of_priorities(sum, item):
    return sum + priority_of_common_item(item)


def partition(items, size):
    groups = []
    for i in range(0, len(items), size):
        groups.append(list(items[i:i+size]))
    return groups


def find_badge(group):
    for letter in group[0]:
        if letter in group[1]:
            if letter in group[2]:
                return letter


def sum_of_badges(sum, group):
    badge = find_badge(group)
    return sum + item_priority(badge)


rucksacks = read_file("./input.txt").splitlines()
sum = reduce(sum_of_priorities, rucksacks, 0)
print(sum)

groups = partition(rucksacks, 3)
sum = reduce(sum_of_badges, groups, 0)

print(sum)
