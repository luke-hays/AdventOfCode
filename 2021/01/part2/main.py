# Sub performs a sonar sweeep
#Each line is a measurement of the sea flor depth

#Consider sums of three measurement sliding windows.
#So basically need to sum the elements before and after a position
#in the list
#Sum up these numbers into categories A,B,C and compare 
#stop when a three combo cant be made

import os

text = "./2021/01/puzzle.txt";
depthMeasurements = []
sums = []


print(os.getcwd())
with open(text) as file:
    depthMeasurements = [int(line.strip()) for line in file] 

ctr = 0
for i in range(1, len(depthMeasurements)):
    if i == len(depthMeasurements) - 1: break
    sums.append(
        depthMeasurements[i-1] +
        depthMeasurements[i] +
        depthMeasurements[i+1]
    )
    if i > 1 and sums[i-1] > sums[i-2]:
        ctr += 1

print(ctr)