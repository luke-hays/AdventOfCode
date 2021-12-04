#verify life support = oxygen generator * C02 scrubber

#consider first bit of numbers
#keep only numbers selected by the bit criteria, discard otherwise
#If only one number left, stop - thats the rating
#Otherwise go to next bit in numbers and continue search

#bit criteria depends on typ of rating to find

#oxygen generator - determine the most common value for the bit positon
#if 0 and 1 are equally common, keep values with 1

#c02 scrubber - determine the least common value in bit pos
#keep only numbers with that bit in that positon. 0 is taken if equal
 
import os

text = "./2021/03/puzzle.txt";

print(os.getcwd())
with open(text) as file:
    binNumbers = [line.strip() for line in file]

oxygenNumbers = [num for num in binNumbers]
co2Numbers = [num for num in binNumbers]

#calc oxygen generator rating
bitCriteria = 0
while (len(oxygenNumbers) > 1):
    bits = [n[bitCriteria] for n in oxygenNumbers]
    zeroCount = bits.count('0')
    oneCount = bits.count('1')

    if oneCount > zeroCount or oneCount == zeroCount:
        oxygenNumbers = [x for x in oxygenNumbers if x[bitCriteria] == '1']
    else:
        oxygenNumbers = [x for x in oxygenNumbers if x[bitCriteria] == '0']

    bitCriteria += 1
oxygenGeneratorRating = oxygenNumbers[0]

bitCriteria = 0
while (len(co2Numbers) > 1):
    bits = [n[bitCriteria] for n in co2Numbers]
    zeroCount = bits.count('0')
    oneCount = bits.count('1')

    if zeroCount < oneCount or oneCount == zeroCount:
        co2Numbers = [x for x in co2Numbers if x[bitCriteria] == '0']
    else:
        co2Numbers = [x for x in co2Numbers if x[bitCriteria] == '1']

    bitCriteria += 1
co2ScrubberRating = co2Numbers[0]

lifeSupportRating = int(oxygenGeneratorRating, 2) * int(co2ScrubberRating, 2)
print(lifeSupportRating)