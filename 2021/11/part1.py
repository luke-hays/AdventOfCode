# text = "./2021/11/sample.txt";
text = "./2021/11/puzzle.txt";

import numpy as np

#map octopus, each one has an energy level
#each step raises an octopus' energy by 1
#if the energy is over 9 then it flashes
#this resets the energy to 0 and raises the energy
#of adjacent octopuses by 1. this can cause a chain

totalFlashes = 0
grid = []
steps = 100

def getNeighbors(i, j):
    rowLen = len(grid)
    colLen = len(grid[0])
    adj = []
    #top
    if i == 0:
        #TopLeft
        if j == 0:
            adj.append((i+1, j))
            adj.append((i, j+1))
            adj.append((i+1, j+1))
        #TopRight
        elif j == colLen-1:
            adj.append((i,j-1))
            adj.append((i+1,j))
            adj.append((i+1, j-1))
        #TopEdge
        else:
            adj.append((i+1,j))
            adj.append((i,j-1))
            adj.append((i,j+1))
            adj.append((i+1, j-1))
            adj.append((i+1, j+1))
    #bottom
    elif i == rowLen-1:
        #BottomLeft
        if j == 0:
            adj.append((i-1,j))
            adj.append((i,j+1))
            adj.append((i-1, j+1))
        #BottomRight
        elif j == colLen-1:
            adj.append((i-1,j))
            adj.append((i,j-1))
            adj.append((i-1, j-1))
        #BottomEdge
        else:
            adj.append((i-1,j))
            adj.append((i,j-1))
            adj.append((i,j+1))
            adj.append((i-1, j-1))
            adj.append((i-1, j+1))
    else:
        #EdgeLeft
        if j == 0:
            adj.append((i+1,j))
            adj.append((i-1,j))
            adj.append((i,j+1))
            adj.append((i+1, j+1))
            adj.append((i-1, j+1))
        #EdgeRight
        elif j == colLen-1:
            adj.append((i-1,j))
            adj.append((i+1,j))
            adj.append((i,j-1))
            adj.append((i+1, j-1))
            adj.append((i-1, j-1))
        #Everything Else
        else:
            adj.append((i+1,j))
            adj.append((i,j+1))
            adj.append((i-1,j))
            adj.append((i,j-1))
            adj.append((i+1, j+1))
            adj.append((i-1, j-1))
            adj.append((i+1, j-1))
            adj.append((i-1, j+1))
    return adj

def bfs(nodes):
    flashes = 0
    queue = []
    for i in range(len(nodes[0])): queue.append((nodes[0][i], nodes[1][i]))
    flashed = []

    while queue:
        node = queue.pop(0)
        flashed.append(node);
        flashes += 1

        #we need to increment all neighbors by 1
        for n in getNeighbors(node[0], node[1]):
            grid[n[0]][n[1]] += 1

            if grid[n[0]][n[1]] >= 10 and n not in flashed and n not in queue:
                queue.append(n)
    
    for n in flashed:
        grid[n[0]][n[1]] = 0

    return flashes


with open(text) as file:
    grid = np.array([list(map(int, list(x))) for x in [line.strip() for line in file]])

for i in range(steps):
    #add 1 energy to each octopus
    grid += 1
    
    #see if any are greater than 9
    #if so begin the energy flashing to adjacent octopuses at that coordinate

    if grid.max() > 9:
        totalFlashes += bfs(np.where(grid >= 10))
    
print(totalFlashes)