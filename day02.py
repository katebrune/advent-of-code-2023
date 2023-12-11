import re
import functools

"""
Part 1
"""
with open("./data/day02.txt", "r") as f:
    data = {}
    for line in f:
        key = int(line.replace("\n", "").split(":")[0].replace("Game ", ""))
        value = line.replace("\n", "").split(":")[1].replace(
            ";", "").replace(",", "").replace("^\s", "")
        data[key] = value
    sum = 0
    for key in data:
        blue = functools.reduce(lambda a, b: a if a > b else b, map(lambda s: int(s), map(
            lambda s: s.replace(" blue", ""), re.findall("([0-9]+\sblue)", data[key]))))
        red = functools.reduce(lambda a, b: a if a > b else b, map(lambda s: int(s), map(
            lambda s: s.replace(" red", ""), re.findall("([0-9]+\sred)", data[key]))))
        green = functools.reduce(lambda a, b: a if a > b else b, map(lambda s: int(s), map(
            lambda s: s.replace(" green", ""), re.findall("([0-9]+\sgreen)", data[key]))))
        if (red <= 12 and green <= 13 and blue <= 14):
            sum += key
    print(sum)


"""
Part 2
"""
with open("./data/day02.txt", "r") as f:
    data = {}
    for line in f:
        key = int(line.replace("\n", "").split(":")[0].replace("Game ", ""))
        value = line.replace("\n", "").split(":")[1].replace(
            ";", "").replace(",", "").replace("^\s", "")
        data[key] = value
    sum = 0
    for key in data:
        blue = functools.reduce(lambda a, b: a if a > b else b, map(lambda s: int(s), map(
            lambda s: s.replace(" blue", ""), re.findall("([0-9]+\sblue)", data[key]))))
        red = functools.reduce(lambda a, b: a if a > b else b, map(lambda s: int(s), map(
            lambda s: s.replace(" red", ""), re.findall("([0-9]+\sred)", data[key]))))
        green = functools.reduce(lambda a, b: a if a > b else b, map(lambda s: int(s), map(
            lambda s: s.replace(" green", ""), re.findall("([0-9]+\sgreen)", data[key]))))
        sum += blue * red * green
    print(sum)
