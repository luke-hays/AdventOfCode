# Sub performs a sonar sweeep
#Each line is a measurement of the sea flor depth

#count the number of times a depth measurement increases
#from the previous measurement (non for the first)

text = "./puzzle.txt";
depthMeasurements = []

with open(text) as file:
    depthMeasurements = [int(line.strip()) for line in file] 

ctr = 0
for i in range(1, len(depthMeasurements)):
    if depthMeasurements[i] > depthMeasurements[i-1]:
        ctr += 1

print(ctr)