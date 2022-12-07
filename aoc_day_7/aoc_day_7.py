from functools import reduce


def read_file(file_name):
    file = open(file_name)
    data = file.read()
    file.close()
    return data


input_data = read_file("./input.txt").splitlines()


def parse(raw_input):
    path = []
    dir_data = {}
    for i in range(len(input_data)):
        command = input_data[i]
        if "$ cd .." in command:
            path.pop()
        elif "$ cd" in command:
            [_, _, dir_name] = command.split(' ')

            if dir_name != '/':
                dir_name = dir_name + '/'

            path.append(dir_name)
            pwd = "".join(path)
            if dir_name == '/':
                dir_data[pwd] = {"dir": pwd, "size": 0}
        elif not "$ ls" in command:
            if "dir" in command:
                [_, dir_name] = command.split(' ')
                if dir_name != '/':
                    dir_name = dir_name + '/'

                dir_name = "".join(path) + dir_name
                dir_data[dir_name] = {"dir": dir_name, "size": 0}
            else:
                [size, name] = command.split(' ')
                for i in range(len(path), 0, -1):
                    dir_name = "".join(path[:i])
                    dir_data[dir_name]["size"] += int(size)
    return dir_data


def sum_size_lesser_than_100000(sum, dir_data):
    size = dir_data["size"]
    sizes.append(size)
    if size < 100000:
        sum += size

    return sum


def closest_to(sizes, free_space):
    size_lesser_than = []
    for s in sizes:
        if s + free_space > 30000000:
            size_lesser_than.append(s)
    size_lesser_than.sort()
    return size_lesser_than[0]


dir_data = parse(input_data)

sizes = []
sum_lesser_than_100k = reduce(
    sum_size_lesser_than_100000, dir_data.values(), 0)

print(sum_lesser_than_100k)


sizes.sort()
print(sizes)

free_space = 70000000 - sizes[-1]
print(free_space)

print("ans---", closest_to(sizes, free_space))
