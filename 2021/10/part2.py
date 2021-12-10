# text = "./2021/10/sample.txt";
text = "./2021/10/puzzle.txt";

#check each line in the navigation system
#corrupted lines close with the wrong character
#some arent corrupted but incomplete, only focusing on incomplete

brackets = {
    ')': ('(', 1),
    ']': ('[', 2),
    '}': ('{', 3),
    '>': ('<', 4)
}

scores = []
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
            
        if corrupted: break
    
    #Line is incomplete
    if not corrupted and len(stack) > 0:
        totalScore = 0
        for c in reversed(stack):
            totalScore *= 5
            for k,v in brackets.items():
                if v[0] == c:
                    totalScore += v[1]
                    break
        scores.append(totalScore)

scores.sort()
print(scores[int(len(scores)/2)])