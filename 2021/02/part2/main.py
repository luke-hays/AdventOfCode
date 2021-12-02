#horizontal and depth start at 0
#follow directions and units and modify their values according to input
#multiply the two variables together for solution

import os

# text = "./2021/02/sample.txt";
text = "./2021/02/puzzle.txt";

units = []
directions = []

print(os.getcwd())
with open(text) as file:
    directions = [line.strip().split(' ', 1)[0] for line in file]
    file.seek(0)
    units = [line.strip().split(' ', 1)[1] for line in file]

horizontal = 0
depth = 0
aim = 0 #need to track aim at this point

#down and up modify the aim now
#forward increase horizontal and depth with aim * X

for i in range(len(directions)):
    unit = int(units[i])

    if directions[i] == 'forward':
        horizontal += unit
        depth += aim * unit
    elif directions[i] == 'up':
        aim -= unit
    elif directions[i] == 'down':
        aim += unit

print(depth*horizontal)