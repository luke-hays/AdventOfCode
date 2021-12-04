#diagnositic report is a list of binary numbers
#decode to get paramerts
#power consumption
#gamma rate
#epsilon rate

#use the binary numbers to generate the gamma and epsilon rate
#power consumption can be found by multiplying the two rates

#gamma rate is determined by finding most common bit in corresponding pos
#of all numbers

#find gamma by taking all the bits in a column - the most common ones in each will make a binary
#the epsilon rate is the least common bit - so it will be the complement of the gamma number
#multiply the two rates in decimal to get the power consumption

import os

text = "./2021/03/puzzle.txt";

print(os.getcwd())
with open(text) as file:
    binNumbers = [line.strip() for line in file]

gammaRate = ''
epsilonRate = ''
for i in range(len(binNumbers[0])):
    bits = [x[i] for x in binNumbers]
    zeroCount = bits.count('0')
    oneCount = bits.count('1')
    if zeroCount > oneCount:
        gammaRate += '0'
        epsilonRate += '1'
    else:
        gammaRate += '1'
        epsilonRate += '0'

powerConsumption = int(gammaRate, 2) * int(epsilonRate, 2)
print(powerConsumption)