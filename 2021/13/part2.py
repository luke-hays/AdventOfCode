# text = "./2021/12/sample.txt";
text = "./2021/12/puzzle.txt";

#Find all paths - looks like a graph as well
#Input is a map containing a format node1-node2
#find the number of distinct paths that start at start 
#dont visit small caves more than once - small is lowercase, big is upper

#going to need to use a dfs with some modifications
#undirected graph
#This needs to be reworked, duplicates get in but removing them gets the right answer

totalPaths = 0
graph = {}
twiceVisit = set()
hasVisited = set()
paths = []

def dfs(node, destination, visited, path):
    global totalPaths
    global twiceVisit
    global hasVisited

    twiceState = False
    if node == 'start' or node == 'end':
        visited.add(node)
    elif node in hasVisited:
        visited.add(node)
    elif node == node.lower() and len(twiceVisit) == 0:
        twiceVisit.add(node)
        twiceState = True
    elif node == node.lower():
        visited.add(node)

    path.append(node)

    if node == destination:
        paths.append(','.join(path))
        totalPaths += 1
    else:
        for i in graph[node]:
            if i not in visited:
                dfs(i, destination, visited, path)
    
    path.pop()
    if node == node.lower():
        if not twiceState:
            visited.remove(node)
        else:
            twiceVisit = set()
            hasVisited.add(node)
            dfs(node, destination, visited, path)
            hasVisited.remove(node)

with open(text) as file:
    for line in file:
        caves = line.strip().split('-')
        if caves[0] not in graph: graph[caves[0]] = []
        if caves[1] not in graph: graph[caves[1]] = []
        graph[caves[0]].append(caves[1])
        graph[caves[1]].append(caves[0])

dfs('start', 'end', set(), [])

paths.sort()
paths = set(paths)

print(len(paths))