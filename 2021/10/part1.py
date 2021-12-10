# text = "./2021/10/sample.txt";
text = "./2021/10/puzzle.txt";

#check each line in the navigation system
#corrupted lines close with the wrong character
#some arent corrupted but incomplete, only focusing on corrupted
#stop at first incorrect character and add a score

brackets = {
    ')': ('(', 3),
    ']': ('[', 57),
    '}': ('{', 1197),
    '>': ('<', 25137)
}

totalScore = 0

chunks = []
with open(text) as file:
    chunks = [line.strip() for line in file]

for line in chunks:
    stack = []
    for c in line: 
        corrupted = False
        if c in brackets.keys(): 
            corrupted = brackets[c][0] != stack.pop()
        else: 
            stack.append(c)
            
        if corrupted:
            totalScore += brackets[c][1]
            break

print(totalScore)