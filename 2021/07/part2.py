# text = "./2021/07/sample.txt";
text = "./2021/07/puzzle.txt";

def calculateFuelCost(start, end):
    distance = abs(start - end)
    return sum(range(1, distance+1))

crabPositions = []

with open(text) as file:
    crabPositions = file.readline().strip().split(',')
    crabPositions = list(map(int, crabPositions))

crabPositions.sort()

fuel = 0
lastPosition = crabPositions[-1]
for position in range(lastPosition+1):
    tempPositions = [x for x in crabPositions]
    tempPositions = list(map(lambda x: abs(calculateFuelCost(x, position)), tempPositions))
    totalFuelCost = sum(tempPositions)
    if fuel == 0: fuel = totalFuelCost
    elif totalFuelCost < fuel: fuel = totalFuelCost

print (fuel)
