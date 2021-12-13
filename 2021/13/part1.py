# text = "./2021/13/sample.txt";
text = "./2021/13/puzzle.txt";

import re
import numpy as np

xCoords = []
yCoords = []

xFolds = []
yFolds = []
folds = []

with open(text) as file:
    for line in file:
        exp = re.search('(\D)=(\d*)', line)
        if exp is not None:
            folds.append((exp.group(1), int(exp.group(2))))
        elif line.strip() == '': continue
        else:
            tmp = line.strip().split(',')
            xCoords.append(int(tmp[0]))
            yCoords.append(int(tmp[1]))

grid = np.zeros((max(yCoords)+1, max(xCoords)+1))
for i in range(len(xCoords)):
    grid[yCoords[i]][xCoords[i]] = 1

# for i in grid:
#     print(''.join(list(str(i))))

#get a subsection of the grid by folding
#flip it accordingly
#use an or condition to layer the grids together

for step in folds:
    folded = []
    if step[0] == 'y':
        folded = grid[step[1]+1:]
        grid = grid[:step[1]]

        folded = np.flip(folded, 0)
        grid = np.logical_or(folded, grid)
    else:
        folded = grid[0:, step[1]+1:]
        grid = grid[0:, :step[1]]

        folded = np.flip(folded, 1)
        grid = np.logical_or(folded, grid)

for i in grid:
    line = ''
    for j in i:
        if j: line += '#'
        else: line += '.'
    print(line)
