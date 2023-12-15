import re
import numpy as np
import functools

"""
Part 1
"""
with open("./data/day04.txt", "r") as f:
    sum = 0
    for line in f:
        numbers = line.strip().split(":")[1].split("|")
        winners = filter(lambda s: re.match(
            '[0-9]+', s), numbers[0].split(' '))
        yours = filter(lambda s: re.match('[0-9]+', s), numbers[1].split(' '))
        matches = list(set(winners) & set(yours))
        if len(matches) > 1:
            sum += 2**(len(matches) - 1)
        else:
            sum += len(matches)
    print(sum)

"""
Part 2
"""
number_of_lines = 0
with open("./data/day04.txt", "r") as f:
    for count, line in enumerate(f):
        pass
    number_of_lines = count
with open("./data/day04.txt", "r") as f:
    cards = np.array([1] * (number_of_lines+1))
    for index, line in enumerate(f):
        numbers = line.strip().split(":")[1].split("|")
        winners = filter(lambda s: re.match(
            '[0-9]+', s), numbers[0].split(' '))
        yours = filter(lambda s: re.match('[0-9]+', s), numbers[1].split(' '))
        matches = list(set(winners) & set(yours))
        if len(matches):
            cards[index+1:index + 1 + len(matches)] += cards[index]
    sum = functools.reduce(lambda a, b: a + b, cards)
    print(sum)
