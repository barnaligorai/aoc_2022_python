def read_file(file_name):
    file = open(file_name)
    data = file.read()
    file.close()
    return data


def is_all_unique(letters):
    for i in range(len(letters)-1):
        if letters[i] in letters[i+1:]:
            return False
    return True


def first_n_letters(text, length):
    return text[:length]


def find_marker(signal, marker_length):
    marker = ''

    is_marker_found = False
    text = signal
    while not is_marker_found:
        letters = first_n_letters(text, marker_length)
        if is_all_unique(letters):
            marker = letters
            is_marker_found = True
        text = text[1:]

    return marker


signal = read_file("./input.txt")

marker_length = 4
marker = find_marker(signal, marker_length)
start_of_packet = signal.index(marker) + len(marker)

print(marker)
print(start_of_packet)

message_marker_length = 14
message = find_marker(signal, message_marker_length)
start_of_message = signal.index(message) + len(message)

print(message)
print(start_of_message)
