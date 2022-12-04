def read_file(file_name):
    file = open(file_name)
    data = file.read()
    file.close()
    return data


def parse(raw_data):
    data = raw_data.splitlines()
    return map(lambda a: a.split(','), data)


def parse_section(section):
    [section1, section2] = section
    [rangeStart1, range_end1] = section1.split("-")
    [rangeStart2, range_end2] = section2.split("-")
    range1 = set(range(int(rangeStart1), int(range_end1) + 1))
    range2 = set(range(int(rangeStart2), int(range_end2) + 1))
    return [range1, range2]


def is_fully_contained(section):
    [range1, range2] = parse_section(section)
    return range1.issubset(range2) or range2.issubset(range1)


def filter_fully_contained_sections(sections):
    filtered_sections = list(filter(is_fully_contained, sections))
    return len(filtered_sections)


def is_overlapping(section):
    [range1, range2] = parse_section(section)
    return range1.intersection(range2)


def filter_overlapped_sections(sections):
    filtered_sections = list(filter(is_overlapping, sections))
    return len(filtered_sections)


raw_input = read_file("./input.txt")
sections = parse(raw_input)

fully_contained = filter_fully_contained_sections(sections)
print(fully_contained)

overlapped = filter_overlapped_sections(sections)
print(overlapped)
