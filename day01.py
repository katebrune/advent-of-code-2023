import re

# Part 1

# with open("./data/day01.txt", 'r') as f:
# 	output = 0
# 	for line  in f:
# 		line_no_newlines = line.replace("\n", "")
# 		line_only_numbers = ''.join(re.findall("[0-9]", line_no_newlines))
# 		first = re.search("^[0-9]", line_only_numbers)
# 		last = re.search("[0-9]$", line_only_numbers)
# 		joined = int("{}{}".format(first.group(0), last.group(0)))
# 		print(joined)
# 		output+=joined
# 	print(output)

# Part 2
# with open("./data/day01-sample2.txt", 'r') as f:
# 	output = 0
# 	for line in f:
# 		no_newlines = line.replace("\n", "")
# 		print(no_newlines)
