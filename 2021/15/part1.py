# text = "./2021/15/sample.txt";
text = "./2021/15/puzzle.txt";

import sys

allRisk = []
baseline = 0

def getNeighbors(graph, i, j):
    neighbors = []

    if i == 0 or i == len(graph)-1 or j == 0 or j == len(graph)-1:
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
    unvisitedNodes = getNodes(graph)
    shortestPath = {}
    previousNodes = {}

    maxVal = sys.maxsize
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            shortestPath[(i, j)] = maxVal
    shortestPath[start] = 0

    while unvisitedNodes:
        currentMinNode = None
        for node in unvisitedNodes:
            if currentMinNode == None: currentMinNode = node
            elif shortestPath[node] < shortestPath[currentMinNode]: currentMinNode = node

        neighbors = getNeighbors(graph, currentMinNode[0], currentMinNode[1])
        for neighbor in neighbors:
            tentativeValue = shortestPath[currentMinNode] +  graph[neighbor[0]][neighbor[1]]
            if tentativeValue < shortestPath[neighbor]:
                shortestPath[neighbor] = tentativeValue
                previousNodes[neighbor] = currentMinNode

        unvisitedNodes.remove(currentMinNode)
        
    return previousNodes, shortestPath

caveMap = []

with open(text) as file:
    caveMap = [list(map(int, list(x))) for x in [line.strip() for line in file]]

x = dijkstra(caveMap, (0, 0))
lastPoint = (len(caveMap)-1, len(caveMap)-1)
print(x[1][lastPoint])
