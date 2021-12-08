# text = "./2021/08/sample.txt";
text = "./2021/08/puzzle.txt";

def findDifference(segments1, segments2):
    segments1Chars = [char for char in segments1]
    segments2Chars = [char for char in segments2]
    segmentDiff = [i for i in segments1Chars + segments2Chars if i not in segments1Chars or i not in segments2Chars]

    return segmentDiff

ONE = 2
FOUR = 4
SEVEN = 3
EIGHT = 7

totalOutput = 0

with open(text) as file:
    for line in file:
        inputs = []
        outputs = []
        digits = {}
        code = {}
        unknown = {5: [], 6: []}
        for i in range(10): digits[i] = ''
        for c in range(ord('a'), ord('g')+1): code[c] = ''

        io = line.split('|')
        inputs.append(io[0].split())
        outputs.append(io[1].split())

        #Get each unique segment length
        for i in inputs[0]:
            segments = len(i)
            if segments == ONE:
                digits[1] = i
            elif segments == FOUR:
                digits[4] = i
            elif segments == SEVEN:
                digits[7] = i
            elif segments == EIGHT:
                digits[8] = i
            elif segments == 5:
                unknown[5].append(i)
            else:
                unknown[6] .append(i)

        #We can determine the a decoding from 1 and 7
        currDiff = findDifference(digits[1], digits[8])
        for seg in unknown[6]:
            tmpDiff = findDifference(currDiff, seg)
            if len(tmpDiff) == 1: 
                digits[6] = seg
                unknown[6].remove(seg)
                break
        #Now determine decoding for 5
        for seg in unknown[5]:
            tmpDiff = findDifference(digits[6], seg)
            if len(tmpDiff) == 1: 
                digits[5] = seg
                unknown[5].remove(seg)
                break
        #Now determine decoding for 9
        for seg in unknown[6]:
            tmpDiff1 = findDifference(digits[1], digits[5])
            tmpDiff2 = findDifference(digits[1], seg)
            if len(findDifference(tmpDiff1, tmpDiff2)) == 1:
                digits[9] = seg
                unknown[6].remove(seg)
                break
        digits[0] = unknown[6][0]
        #Now determine 2
        for seg in unknown[5]:
            tmpDiff1 = findDifference(digits[1], digits[9])
            tmpDiff2 = findDifference(digits[1], seg)
            if len(findDifference(tmpDiff1, tmpDiff2)) == 1:
                digits[3] = seg
                unknown[5].remove(seg)
                break
        digits[2] = unknown[5][0]

        outputVal = ''
        for i in outputs[0]:
            for k,v in digits.items():
                if len(findDifference(v, i)) == 0:
                    outputVal += str(k)
                    break
        
        totalOutput += int(outputVal)

print(totalOutput)