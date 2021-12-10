# text = "./2021/09/sample.txt";
text = "./2021/09/puzzle.txt";

#find low points - locations lower than adjacent in 4 directions
#edges or corners have only two or three

lowPointRiskSum = 0

heightmap = []
basins = []

def getNeighbors(i, j):
    rowLen = len(heightmap)
    colLen = len(heightmap[0])
    adj = []
    #top
    if i == 0:
        #TopLeft
        if j == 0:
            adj.append((i+1, j))
            adj.append((i, j+1))
        #TopRight
        elif j == colLen-1:
            adj.append((i,j-1))
            adj.append((i+1,j))
        #TopEdge
        else:
            adj.append((i+1,j))
            adj.append((i,j-1))
            adj.append((i,j+1))
    #bottom
    elif i == rowLen-1:
        #BottomLeft
        if j == 0:
            adj.append((i-1,j))
            adj.append((i,j+1))
        #BottomRight
        elif j == colLen-1:
            adj.append((i-1,j))
            adj.append((i,j-1))
        #BottomEdge
        else:
            adj.append((i-1,j))
            adj.append((i,j-1))
            adj.append((i,j+1))
    else:
        #EdgeLeft
        if j == 0:
            adj.append((i+1,j))
            adj.append((i-1,j))
            adj.append((i,j+1))
        #EdgeRight
        elif j == colLen-1:
            adj.append((i-1,j))
            adj.append((i+1,j))
            adj.append((i,j-1))
        #Everything Else
        else:
            adj.append((i+1,j))
            adj.append((i,j+1))
            adj.append((i-1,j))
            adj.append((i,j-1))
    return adj

def isLowest(point, adj):
    foundLowest = True
    for n in adj:
        if heightmap[n[0]][n[1]] <= point: 
            foundLowest = False
            break
    return foundLowest

def getBasinSize(visited, queue, node):
    currentBasinSize = 0
    visited.append(node)
    queue.append(node)

    while queue:
        currNode = queue.pop(0)
        currentBasinSize += 1
        adj = getNeighbors(currNode[0], currNode[1])
        
        for node in adj:
            n = heightmap[node[0]][node[1]]
            if n != '9' and node not in visited:
                visited.append(node)
                queue.append(node)
    return currentBasinSize

def checkPoints():
    rowLen = len(heightmap)
    colLen = len(heightmap[0])
    for i in range(rowLen):
        for j in range(colLen):
            point = heightmap[i][j]
            adj = getNeighbors(i, j)
            if isLowest(point, adj):
                basins.append(getBasinSize([], [], (i, j)))


with open(text) as file:
    heightmap = [line.strip() for line in file]

checkPoints()
basins.sort()
product = basins[-1] * basins[-2] * basins[-3]

print(product)