import functools

"""
Part 1
"""
def counts(arr):
	aces = functools.reduce(lambda acc, cur: acc + 1 if cur == 'A' else acc, arr, 0)
	kings = functools.reduce(lambda acc, cur: acc + 1 if cur == 'K' else acc, arr, 0)
	queens = functools.reduce(lambda acc, cur: acc + 1 if cur == 'Q' else acc, arr, 0) 
	jacks = functools.reduce(lambda acc, cur: acc + 1 if cur == 'J' else acc, arr, 0)
	tens = functools.reduce(lambda acc, cur: acc + 1 if cur == 'T' else acc, arr, 0)
	nines = functools.reduce(lambda acc, cur: acc + 1 if cur == '9' else acc, arr, 0)
	eights = functools.reduce(lambda acc, cur: acc + 1 if cur == '8' else acc, arr, 0)
	sevens = functools.reduce(lambda acc, cur: acc + 1 if cur == '7' else acc, arr, 0)
	sixes = functools.reduce(lambda acc, cur: acc + 1 if cur == '6' else acc, arr, 0)
	fives = functools.reduce(lambda acc, cur: acc + 1 if cur == '5' else acc, arr, 0)
	fours = functools.reduce(lambda acc, cur: acc + 1 if cur == '4' else acc, arr, 0)
	threes = functools.reduce(lambda acc, cur: acc + 1 if cur == '3' else acc, arr, 0)
	twos = functools.reduce(lambda acc, cur: acc + 1 if cur == '2' else acc, arr, 0)
	return [aces, kings, queens, jacks, tens, nines, eights, sevens, sixes, fives, fours, threes, twos]
data = []
with open('./data/day07.txt', 'r') as f:
	data = []
	for line in f:
		line = line.strip().split(' ')
		data.append({"hand": line[0], "bid": line[1], "counts": counts([*line[0]])})

def compare_strength(a, b):
	strength = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3','2']
	i = 0
	while a[i] == b[i]:
		i=i+1
	return 1 if strength.index(a[i]) < strength.index(b[i]) else -1

def comparator(a, b):
	# check 5 of a kind
	if 5 in a["counts"] and 5 not in b["counts"]:
		return 1
	elif 5 not in a["counts"] and 5 in b["counts"]:
		return -1
	elif 5 in a["counts"] and 5 in b["counts"]:
		return compare_strength(a['hand'], b['hand'])
	# check 4 of a kind
	elif 4 in a["counts"] and 4 not in b["counts"]:
		return 1
	elif 4 not in a["counts"] and 4 in b["counts"]:
		return -1
	elif 4 in a["counts"] and 4 in b["counts"]:
		return compare_strength(a['hand'], b['hand'])
	# check full house
	elif 3 in a["counts"] and 2 in a["counts"]:
		if 3 in b["counts"] and 2 in b["counts"]:
			return compare_strength(a['hand'], b['hand'])
		else:
			return 1
	elif 3 in b["counts"] and 2 in b["counts"]:
		return -1
	# check 3 of a kind
	elif 3 in a["counts"] and 3 not in b["counts"]:
		return 1
	elif 3 not in a["counts"] and 3 in b["counts"]:
		return -1
	elif 3 in a["counts"] and 3 in b["counts"]:
		return compare_strength(a['hand'], b['hand'])
	# check two pair
	elif len(list(filter(lambda n: n == 2, a['counts']))) == 2 and len(list(filter(lambda n: n == 2, b['counts']))) != 2:
		return 1
	elif len(list(filter(lambda n: n == 2, a['counts']))) != 2 and len(list(filter(lambda n: n == 2, b['counts']))) == 2:
		return -1
	elif len(list(filter(lambda n: n == 2, a['counts']))) == 2 and len(list(filter(lambda n: n == 2, b['counts']))) == 2:
		return compare_strength(a['hand'], b['hand'])
	# check one pair
	elif 2 in a['counts'] and 2 not in b['counts']:
		return 1
	elif 2 not in a['counts'] and 2 in b['counts']:
		return -1
	elif 2 in a['counts'] and 2 in b['counts']:
		return compare_strength(a['hand'], b['hand'])
	else:
		return compare_strength(a['hand'], b['hand'])
	
comparator_key = functools.cmp_to_key(comparator)
data.sort(key=comparator_key)
winnings = [ (i + 1) * int(x['bid']) for i,x in enumerate(data)] 
winnings_sum = functools.reduce(lambda a,b: a + b, winnings)
print(winnings_sum)

"""
Part 2
"""
def counts(arr):
	aces = functools.reduce(lambda acc, cur: acc + 1 if cur == 'A' else acc, arr, 0)
	kings = functools.reduce(lambda acc, cur: acc + 1 if cur == 'K' else acc, arr, 0)
	queens = functools.reduce(lambda acc, cur: acc + 1 if cur == 'Q' else acc, arr, 0) 
	jacks = functools.reduce(lambda acc, cur: acc + 1 if cur == 'J' else acc, arr, 0)
	tens = functools.reduce(lambda acc, cur: acc + 1 if cur == 'T' else acc, arr, 0)
	nines = functools.reduce(lambda acc, cur: acc + 1 if cur == '9' else acc, arr, 0)
	eights = functools.reduce(lambda acc, cur: acc + 1 if cur == '8' else acc, arr, 0)
	sevens = functools.reduce(lambda acc, cur: acc + 1 if cur == '7' else acc, arr, 0)
	sixes = functools.reduce(lambda acc, cur: acc + 1 if cur == '6' else acc, arr, 0)
	fives = functools.reduce(lambda acc, cur: acc + 1 if cur == '5' else acc, arr, 0)
	fours = functools.reduce(lambda acc, cur: acc + 1 if cur == '4' else acc, arr, 0)
	threes = functools.reduce(lambda acc, cur: acc + 1 if cur == '3' else acc, arr, 0)
	twos = functools.reduce(lambda acc, cur: acc + 1 if cur == '2' else acc, arr, 0)
	return [aces, kings, queens, tens, nines, eights, sevens, sixes, fives, fours, threes, twos, jacks]
data = []
with open('./data/day07.txt', 'r') as f:
	data = []
	for line in f:
		line = line.strip().split(' ')
		data.append({"hand": line[0], "bid": line[1], "counts": counts([*line[0]])})

def apply_jokers(o):
	c = o["counts"]
	if c[len(c) - 1] == 5:
		return o
	elif c[len(c) - 1] == 4:
		c[c.index(1)] += 4
		c[len(c) - 1] = 0
		o["counts"] = c
		return o
	elif c[len(c) - 1] == 3:
		c[len(c) - 1] = 0
		if 2 in c:
			c[c.index(2)] += 3
			o["counts"] = c
			return o
		else:
			c[c.index(1)] += 3
			o["counts"] = c
			return o
	elif c[len(c) - 1] == 2:
		c[len(c) - 1] = 0
		if 3 in c:
			c[c.index(3)] += 2
			o["counts"] = c
			return o
		elif 2 in c:
			c[c.index(2)] += 2
			o["counts"] = c
			return o
		else:
			c[c.index(1)] += 2
			o["counts"] = c
			return o
	elif c[len(c) - 1] == 1:
		c[len(c) - 1] = 0
		if 4 in c:
			c[c.index(4)] += 1
			o["counts"] = c
			return o
		elif 3 in c:
			c[c.index(3)] += 1
			o["counts"] = c
			return o
		elif 2 in c:
			c[c.index(2)] += 1
			o["counts"] = c
			return o
		else:
			c[c.index(1)] += 1
			o["counts"] = c
			return o
	else:
		return o

def compare_strength(a, b):
	strength = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3','2', 'J']
	i = 0
	while a[i] == b[i]:
		i=i+1
	return 1 if strength.index(a[i]) < strength.index(b[i]) else -1

def comparator(a, b):
	# check 5 of a kind
	if 5 in a["counts"] and 5 not in b["counts"]:
		return 1
	elif 5 not in a["counts"] and 5 in b["counts"]:
		return -1
	elif 5 in a["counts"] and 5 in b["counts"]:
		return compare_strength(a['hand'], b['hand'])
	# check 4 of a kind
	elif 4 in a["counts"] and 4 not in b["counts"]:
		return 1
	elif 4 not in a["counts"] and 4 in b["counts"]:
		return -1
	elif 4 in a["counts"] and 4 in b["counts"]:
		return compare_strength(a['hand'], b['hand'])
	# check full house
	elif 3 in a["counts"] and 2 in a["counts"]:
		if 3 in b["counts"] and 2 in b["counts"]:
			return compare_strength(a['hand'], b['hand'])
		else:
			return 1
	elif 3 in b["counts"] and 2 in b["counts"]:
		return -1
	# check 3 of a kind
	elif 3 in a["counts"] and 3 not in b["counts"]:
		return 1
	elif 3 not in a["counts"] and 3 in b["counts"]:
		return -1
	elif 3 in a["counts"] and 3 in b["counts"]:
		return compare_strength(a['hand'], b['hand'])
	# check two pair
	elif len(list(filter(lambda n: n == 2, a['counts']))) == 2 and len(list(filter(lambda n: n == 2, b['counts']))) != 2:
		return 1
	elif len(list(filter(lambda n: n == 2, a['counts']))) != 2 and len(list(filter(lambda n: n == 2, b['counts']))) == 2:
		return -1
	elif len(list(filter(lambda n: n == 2, a['counts']))) == 2 and len(list(filter(lambda n: n == 2, b['counts']))) == 2:
		return compare_strength(a['hand'], b['hand'])
	# check one pair
	elif 2 in a['counts'] and 2 not in b['counts']:
		return 1
	elif 2 not in a['counts'] and 2 in b['counts']:
		return -1
	elif 2 in a['counts'] and 2 in b['counts']:
		return compare_strength(a['hand'], b['hand'])
	else:
		return compare_strength(a['hand'], b['hand'])
	
comparator_key = functools.cmp_to_key(comparator)
mapped_data = list(map(apply_jokers, data))
mapped_data.sort(key=comparator_key)
winnings = [ (i + 1) * int(x['bid']) for i,x in enumerate(mapped_data)] 
winnings_sum = functools.reduce(lambda a,b: a + b, winnings)
print(winnings_sum)