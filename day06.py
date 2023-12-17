import re
import functools

"""
Part 1
"""
times = None
distances = None
with open("./data/day06.txt", "r") as f:
	for i, line in enumerate(f):
		line = line.strip()
		line = list(filter(lambda s: re.match('[0-9]', s), line.split(':')[1].split(' ')))
		if i == 0: times = line
		elif i == 1: distances = line
totals = []
for i in range(len(times)):
	time = int(times[i])
	distance = int(distances[i])
	race_sum = 0
	for i in range(time):
		real_distance = i * (time - i)
		if real_distance > distance: race_sum += 1
	totals.append(race_sum)
result = functools.reduce(lambda a, b: a * b, totals)
print(result)

"""
Part 2
"""
with open("./data/day06.txt", "r") as f:
	time = None
	distance = None
	for i, line in enumerate(f):
		line = line.strip()
		line = line.split(':')[1].replace(' ', '')
		if i == 0: time = int(line)
		elif i == 1: distance = int(line)
	sum = 0
	for i in range(time):
		real_distance = i * (time - i)
		if real_distance > distance: sum += 1
	print(sum)