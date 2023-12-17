import re
import numpy
"""
Part 1
"""
with open("./data/day08.txt", "r") as f:
	steps = None
	network = {}
	for i, line in enumerate(f):
		line = line.strip()
		if i == 0:
			steps = [*line]
		elif not len(line): continue
		else:
			line = line.split(' = ')
			rl = line[1].replace('(', '').replace(')', '').split(', ')
			network[line[0]] = tuple((rl[0], rl[1]))
	count = 0
	cur = 'AAA'
	while cur != 'ZZZ':
		for step in steps:
			count+=1
			if step == 'R':
				cur = network[cur][1]
			elif step == 'L':
				cur = network[cur][0]
	print(count)

"""
Part 2
"""
with open("./data/day08.txt") as f:
	steps = None
	network = {}
	for i, line in enumerate(f):
		line = line.strip()
		if i == 0:
			steps = [*line]
		elif not len(line): continue
		else:
			line = line.split(' = ')
			rl = line[1].replace('(', '').replace(')', '').split(', ')
			network[line[0]] = tuple((rl[0], rl[1]))

	def get_count(cur):
		count = 0
		while not re.match(r'.*Z$', cur):
			for step in steps:
				count += 1
				if step == 'R':
					cur = network[cur][1]
				elif step == 'L':
					cur = network[cur][0]
		return count
	
	start_list = list(filter(lambda s: re.match(r'.*A$', s) ,list(network.keys())))
	counts = list(map(get_count, start_list))
	lcm = numpy.lcm.reduce(counts)
	print(lcm)
