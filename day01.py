import re

"""
Part 1
"""
with open("./data/day01.txt", 'r') as f:
    output = 0
    for line in f:
        line_no_newlines = line.replace("\n", "")
        line_only_numbers = ''.join(re.findall("[0-9]", line_no_newlines))
        first = re.search("^[0-9]", line_only_numbers)
        last = re.search("[0-9]$", line_only_numbers)
        joined = int("{}{}".format(first.group(0), last.group(0)))
        output += joined
    print(output)


"""
Part 2
"""
with open("./data/day01.txt", 'r') as f:
    output = 0
    for line in f:
        no_newlines = line.replace("\n", "")
        lowercase = no_newlines.lower()
        no_oneight = lowercase.replace("oneight", "oneeight")
        no_twone = no_oneight.replace("twone", "twoone")
        no_threeight = no_twone.replace("threeight", "threeeight")
        no_fiveight = no_threeight.replace("fiveight", "fiveeight")
        no_nineight = no_fiveight.replace("nineight", "nineeight")
        no_sevenine = no_nineight.replace("sevenine", "sevennine")
        no_eightwo = no_sevenine.replace("eightwo", "eighttwo")
        no_eighthree = no_eightwo.replace("eighthree", "eightthree")
        replace_one = no_eighthree.replace("one", "1")
        replace_two = replace_one.replace("two", "2")
        repalce_three = replace_two.replace("three", "3")
        replace_four = repalce_three.replace("four", "4")
        replace_five = replace_four.replace("five", "5")
        replace_six = replace_five.replace("six", "6")
        replace_seven = replace_six.replace("seven", "7")
        replace_eight = replace_seven.replace("eight", "8")
        replace_nine = replace_eight.replace("nine", "9")
        no_letters = ''.join(re.findall("[0-9]", replace_nine))
        first = re.search("^[0-9]", no_letters)
        last = re.search("[0-9]$", no_letters)
        joined = int("{}{}".format(first.group(0), last.group(0)))
        output += joined
    print(output)
