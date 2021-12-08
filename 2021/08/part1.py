# text = "./2021/08/sample.txt";
text = "./2021/08/puzzle.txt";

#acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab |
#cdfeb fcadb cdfeb cdbaf

#Each entry consists of ten unique signal patterns - a delimiter and then a four digit output value
#The unique signal patterns correspond to ten different ways to render a digit
#7 is the only digit that uses a three segments - so dab corresponds to 7 (it should be aaaaccfff)
#wire/segment connections are mixed up seperately for each four digit display

#Focus on 1,4,7,8 in the output values
#They use a unique number of digits

inputs = []
outputs = []

ONE = 2
FOUR = 4
SEVEN = 3
EIGHT = 7

with open(text) as file:
    for line in file:
        io = line.split('|')
        inputs.append(io[0].split())
        outputs.append(io[1].split())

ctr = 0
for i in range(len(outputs)):
    for j in range(len(outputs[i])):
        if (len(outputs[i][j]) == ONE or len(outputs[i][j]) == FOUR or
            len(outputs[i][j]) == SEVEN or len(outputs[i][j]) == EIGHT):
            ctr += 1

print(ctr)
