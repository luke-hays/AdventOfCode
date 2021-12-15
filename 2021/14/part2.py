#AB -> C
#pair insertion rules means that when elements A and B are adjacent, C is inserted between them
#So NNCB, you would insert three elements, between NN, NC, CB
#repeat this process
#subtract the quantity of the least common element from most common
#40 steps meant part 1's solution was too inefficient

# text = "./2021/14/sample.txt";
text = "./2021/14/puzzle.txt";

polymerTemplate = ''
pairInsertion = {}
steps = 40
keys = []
counts = {}

with open(text) as file:
    polymerTemplate = file.readline().strip()
    file.readline()
    for line in file:
        parseLine = line.strip().split(' -> ')
        keys.append(parseLine[0])
        pairInsertion[parseLine[0]] = parseLine[1]
        counts[parseLine[1]] = 0

pairCounts = dict(zip(keys, [0]*len(keys)))
newPairCounts = dict(zip(keys, [0]*len(keys)))

for i in range(len(polymerTemplate)-1):
    c1 = polymerTemplate[i]
    c2 = polymerTemplate[i+1]
    pairCounts[c1+c2] += 1

for i in range(steps):
    newPairCounts = dict(zip(keys, [0]*len(keys)))

    for k,v in pairCounts.items():
        element = pairInsertion[k]
        newPairCounts[k[0] + element] += v
        newPairCounts[element + k[1]] += v
        counts[element] += v

    pairCounts = newPairCounts.copy()

for c in polymerTemplate:
    counts[c] += 1

print(max(counts.values()) - min(counts.values()))