#AB -> C
#pair insertion rules means that when elements A and B are adjacent, C is inserted between them
#So NNCB, you would insert three elements, between NN, NC, CB
#repeat this process
#subtract the quantity of the least common element from most common

text = "./2021/14/sample.txt";
# text = "./2021/14/puzzle.txt";

import pandas as pd

polymerTemplate = ''
pairInsertion = {}
steps = 10

with open(text) as file:
    polymerTemplate = file.readline().strip()
    file.readline()
    for line in file:
        parseLine = line.strip().split(' -> ')
        pairInsertion[parseLine[0]] = parseLine[1]

for i in range(steps):
    newPolymer = ''
    for j in range(len(polymerTemplate)-1):
        c1 = polymerTemplate[j]
        c2 = polymerTemplate[j+1]

        element = pairInsertion[c1+c2]
        if j == 0: newPolymer += c1 + element + c2
        else:newPolymer += element + c2
    polymerTemplate = newPolymer

counts = pd.Series(list(polymerTemplate)).value_counts()
print(counts[0] - counts[-1])