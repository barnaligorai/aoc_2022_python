from functools import reduce

points = {"X": 1, "Y": 2, "Z": 3, "A": 1, "B": 2, "C": 3}


def read_file(file_name):
    file = open(file_name)
    data = file.read()
    file.close()
    return data

# a z 3 - 1 = 2 --- 3 0
# a y 2 - 1 = 1 --- 2 6


def parse(raw_input):
    return map(lambda a: a.split(' '), raw_input)


def result(move1, move2):
    difference = points[move1] - points[move2]
    if difference == 0:
        return 3
    if difference == -1 or difference == 2:
        return 6
    return 0


def points_of_a_round(sum, moves):
    [move1, move2] = moves
    return sum + points[move2] + result(move1, move2)


def calculate_points(moves):
    return reduce(points_of_a_round, moves, 0)


def calculate_based_on_strategy(sum, moves):
    [move1, move2] = moves
    strategy = {"X": {"A": "Z", "B": "X", "C": "Y"},
                "Y": {"A": "X", "B": "Y", "C": "Z"},
                "Z": {"A": "Y", "B": "Z", "C": "X"}}
    strategic_move = strategy[move2][move1]
    p = points_of_a_round(sum, [move1, strategic_move])
    return p


def strategic_points(moves):
    return reduce(calculate_based_on_strategy, moves, 0)


input = read_file('./input.txt').split('\n')
moves = parse(input)

print(calculate_points(moves))
print(strategic_points(moves))
