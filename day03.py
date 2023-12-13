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

"""
Part 2
"""
with open("./data/day03.txt", "r") as f:
    data = []
    for line in f:
        data.append([*line.strip()])
    sum = 0
    for i, row in enumerate(data):
        for j, value in enumerate(row):
            if re.match('\*', value):
                neighbors = []
                if i > 0 and re.match('[0-9]', data[i-1][j]):
                    left = re.search(r'\d+$', ''.join(data[i-1][0:j]))
                    right = re.search(r'^\d+', ''.join(data[i-1][j+1:]))
                    neighbors.append("{}{}{}".format(
                        left.group(0) if left != None else "", data[i-1][j], right.group(0) if right != None else ""))
                else:
                    if i > 0 and j > 1 and re.match('[0-9]', data[i-1][j-1]):
                        left = re.search(r'\d+$', ''.join(data[i-1][0:j]))
                        neighbors.append("{}".format(left.group(0)))
                    if i > 0 and j < len(data[i]) and re.match('[0-9]', data[i-1][j + 1]):
                        right = re.search(r'^\d+', ''.join(data[i-1][j+1:]))
                        neighbors.append("{}".format(right.group(0)))
                if j > 0 and re.match('[0-9]', data[i][j-1]):
                    left = re.search(r'\d+$', ''.join(data[i][0:j]))
                    neighbors.append('{}'.format(left.group(0)))
                if j < len(data[i]) and re.match('[0-9]', data[i][j+1]):
                    right = re.search(r'^\d+', ''.join(data[i][j+1:]))
                    neighbors.append("{}".format(right.group(0)))
                if i < len(data) and re.match("[0-9]", data[i+1][j]):
                    left = re.search(r'\d+$', ''.join(data[i+1][0:j]))
                    right = re.search(r'^\d+', ''.join(data[i+1][j+1:]))
                    neighbors.append("{}{}{}".format(
                        left.group(0) if left != None else "", data[i+1][j], right.group(0) if right != None else ""))
                else:
                    if i < len(data) and j > 1 and re.match('[0-9]', data[i+1][j-1]):
                        left = re.search(r'\d+$', ''.join(data[i+1][0:j]))
                        neighbors.append("{}".format(left.group(0)))
                    if i < len(data) and j < len(data[i]) and re.match('[0-9]', data[i+1][j+1]):
                        right = re.search(r'^\d+', ''.join(data[i+1][j+1:]))
                        neighbors.append("{}".format(right.group(0)))
                if (len(neighbors) == 2):
                    sum += int(neighbors[0])*int(neighbors[1])
    print(sum)
