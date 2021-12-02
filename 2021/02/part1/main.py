#horizontal and depth start at 0
#follow directions and units and modify their values according to input
#multiply the two variables together for solution

import os

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

for i in range(len(directions)):
    unit = int(units[i])

    if directions[i] == 'forward':
        horizontal += unit
    elif directions[i] == 'up':
        depth -= unit
    elif directions[i] == 'down':
        depth += unit

print(depth*horizontal)