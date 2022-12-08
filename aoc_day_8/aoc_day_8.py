
def read_file(file_name):
    file = open(file_name)
    data = file.read()
    file.close()
    return data


def parse_size(sizes_as_string):
    sizes = list(map(int, list(sizes_as_string)))
    return sizes


def parse_sizes(input_sizes):
    return list(map(parse_size, input_sizes))


def is_visible_from_left(tree_index, row):
    height = row[tree_index]
    trees_on_left = row[:tree_index]
    for tree in trees_on_left:
        if height <= tree:
            return False

    return True


def is_visible_from_right(tree_index, row):
    height = row[tree_index]
    trees_on_right = row[tree_index + 1:]

    for tree in trees_on_right:
        if height <= tree:
            return False
    return True


def is_visible_from_up(tree_index, col):
    return is_visible_from_left(tree_index, col)


def is_visible_from_down(tree_index, col):
    return is_visible_from_right(tree_index, col)


def is_tree_visible(tree, row, col, grid):
    return is_visible_from_left(tree[1], row) or is_visible_from_right(tree[1], row) or is_visible_from_up(tree[0], col) or is_visible_from_down(tree[0], col)


def visible_trees(grid):
    visible = []
    for i in range(len(grid)):
        row = grid[i]
        for j in range(len(row)):
            e = grid[i][j]
            col = []
            for k in range(len(grid)):
                col.append(grid[k][j])
            if is_tree_visible([i, j], row, col, grid):
                visible.append([i, j, row, col])
    return visible


def left_score(pos, row):
    tree = row[pos]
    view = 0
    for i in range(len(row[:pos]), 0, -1):
        if row[i-1] >= tree:
            view += 1
            break
        else:
            view += 1
    return view


def right_score(pos, row):
    tree = row[pos]
    view = 0
    for i in row[pos + 1:]:
        if tree > i:
            view += 1
        else:
            view += 1
            break
    return view


def up_score(pos, col):
    return left_score(pos, col)


def down_score(pos, col):
    return right_score(pos, col)


def scenic_score(tree_data):
    [r, c, row, col] = tree_data
    return left_score(c, row) * right_score(c, row) * up_score(r, col) * down_score(r, col)


input_data = read_file("./input.txt").splitlines()
tree_sizes = parse_sizes(input_data)

v = visible_trees(tree_sizes)
# print(v)
print(len(v))

scores = list(map(scenic_score, v))
# print(scores)

m = max(scores)
print(m)
