import functools
"""
Part 1
"""
with open('./data/day09.txt', 'r') as f:
	predication_sum = 0
	for line in f:
		line = line.strip()
		line = line.split(' ')
		vault = []
		cur = line
		all_zero = False
		while not all_zero:
			vault.append(cur)
			temp = []
			for i in range(len(cur) - 1):
				temp.append(int(cur[i+1]) - int(cur[i]))
			all_zero = all(x == 0 for x in temp)
			cur = temp
		vault.append(cur)
		vault = list(reversed(vault))
		res = []
		for i in range(len(vault)):
			if i == 0:
				res.append(0)
			else:
				res.append(int(res[-1]) + int(vault[i][-1]))
		predication = res[-1]
		predication_sum+=predication
	print(predication_sum)

"""
Part 2
"""
with open('./data/day09.txt', 'r') as f:
	prediction_sum = 0
	for line in f:
		line = line.strip()
		line = line.split(' ')
		vault = []
		cur = line
		all_zero = False
		while not all_zero:
			vault.append(cur)
			temp = []
			for i in range(len(cur) - 1):
				temp.append(int(cur[i+1]) - int(cur[i]))
			all_zero = all(x == 0 for x in temp)
			cur = temp
		vault.append(cur)
		vault = list(reversed(vault))
		res = []
		for i in range(len(vault)):
			if i == 0:
				res.append(0)
			else:
				res.append(int(vault[i][0]) - int(res[-1]))
		prediction = res[-1]
		prediction_sum += prediction
	print(prediction_sum)
		