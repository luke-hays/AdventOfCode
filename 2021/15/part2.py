#inspiration for improving the dijsktra algo here
#https://bradfieldcs.com/algos/graphs/dijkstras-algorithm/

# text = "./2021/15/sample.txt";
text = "./2021/15/puzzle.txt";

import sys
import numpy as np
import heapq

allRisk = []
baseline = 0
newMapSize = 5

def getNeighbors(graph, i, j):
    neighbors = []

    if i == 0 or i == len(graph)-1 or j == 0 or j == len(graph[i])-1:
        if i != 0:
            neighbors.append((i-1, j))
        if i != len(graph)-1:
            neighbors.append((i+1, j))
        if j != 0:
            neighbors.append((i,j-1))
        if j != len(graph[i])-1:
            neighbors.append((i, j+1))
    else:
        neighbors.append((i-1, j))
        neighbors.append((i, j-1))
        neighbors.append((i+1, j))
        neighbors.append((i, j+1))

    return neighbors

def getNodes(graph):
    nodes = []
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            nodes.append((i,j))
    return nodes

def dijkstra(graph, start):
    shortestPath = {}
    previousNodes = {}

    maxVal = sys.maxsize
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            shortestPath[(i, j)] = maxVal
    shortestPath[start] = 0

    pq = [(0, start)]
    while len(pq) > 0:
        currentDistance, currentVertex = heapq.heappop(pq)

        if currentDistance > shortestPath[currentVertex]:
            continue

        neighbors = getNeighbors(graph, currentVertex[0], currentVertex[1])
        for neighbor in neighbors:
            tentativeValue = shortestPath[currentVertex] + graph[neighbor[0]][neighbor[1]]
            if tentativeValue < shortestPath[neighbor]:
                shortestPath[neighbor] = tentativeValue
                heapq.heappush(pq, (tentativeValue, neighbor))
        
    return previousNodes, shortestPath

def createNewMapSection(caveMap):
    section = np.array(caveMap)
    mapRow = section.copy()

    for i in range(1, newMapSize):
        newSection = section.copy()
        newSection += 1
        newSection[newSection > 9] = 1
        section = newSection.copy()
        mapRow = np.hstack((mapRow, newSection))

    section = mapRow.copy()
    for i in range(1, newMapSize):
        newSection = section.copy()
        newSection += 1
        newSection[newSection>9] = 1
        section = newSection.copy()
        mapRow = np.vstack((mapRow, newSection))
    
    # np.savetxt(fname='./2021/15/matrix.txt', X=mapRow, fmt='%i')

    return mapRow

caveMap = []

with open(text) as file:
    caveMap = [list(map(int, list(x))) for x in [line.strip() for line in file]]

caveMap = createNewMapSection(caveMap).tolist()

x = dijkstra(caveMap, (0, 0))
lastPoint = (len(caveMap)-1, len(caveMap)-1)
print(x[1][lastPoint])
