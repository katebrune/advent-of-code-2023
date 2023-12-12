import re

"""
Part 1
"""
with open("./data/day03.txt", "r") as f:
    data = []
    for line in f:
        data.append(line.strip())
    sum = 0
    for i, row in enumerate(data):
        temp_row = row
        numbers = re.findall("[0-9]+", row)
        for number in numbers:
            has_symbol_in_bounding_box = False
            upper_bound = tuple((temp_row.find(number) - 1, i - 1))
            lower_bound = tuple((temp_row.find(number) + len(number), i + 1))
            bounding_box_coordinates = []
            for x in range(upper_bound[0], lower_bound[0] + 1):
                for y in range(upper_bound[1], lower_bound[1] + 1):
                    bounding_box_coordinates.append(tuple((x, y)))
            bounding_box = ''.join(map(
                (lambda t: data[t[1]][t[0]] if t[0] >= 0 and t[1] >= 0 and t[0] < len(data) and t[1] < len(data[0]) else '.'), bounding_box_coordinates))
            filtered = re.sub('\d', '', bounding_box).replace('.', '')
            print(filtered)
            if len(filtered):
                sum += int(number)
            temp_row = temp_row[0: temp_row.find(
                number)] + '.'*len(number) + temp_row[temp_row.find(number) + len(number):]
    print(sum)
