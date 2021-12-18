# text = "./2021/17/sample.txt";
text = "./2021/17/puzzle.txt";

import re

steps = 300
hits = {}
maxY = 0
x1 = x2 = y1 = y2 = 0
with open(text) as file:
    x1, x2, y1, y2 = re.findall(r'-?\d+?\d*', file.readline())

x1 = int(x1)
x2 = int(x2)
y1 = int(y1)
y2 = int(y2)

target = []
for i in range(x1, x2+1):
    for j in range(y2, y1-1, -1):
        target.append((i, j))

def probe(v):
    global x1, x2, y1, y2
    maxY = x = y = 0
    while(True):
        #incease x positon by x velocity
        x += v[0]
        #increase y position by y velocity
        y += v[1]
        if y > maxY: maxY = y
        #x velocity changes by 1 towards the value 0
        if v[0] != 0: v[0] = v[0]-1 if v[0] > 0 else v[0]+1
        #y velocity decreases by 1
        v[1] -= 1

        #Check position when x velocity is stalled
        if v[0] == 0 and x < x1: 
            break
        #Check if we've over shot x
        if x > x2: 
            break
        #Check if we've over shot y, y must be negative
        if y < y1: 
            break
        # #Check if our position is in target range
        if (x, y) in target: 
            return maxY
    return -1

def fire(x):
    #Now increment y until its velocity returns -1
    res = y = 0
    while (res >= 0 or y <= steps):
        y += 1
        res = probe([x,y])
        if res >= 0: hits[(x,y)] = res

    #Now decrement y until its velocity returns -1
    res = y = 0
    while (res >= 0 or y >= -steps):
        y -= 1
        res = probe([x,y])
        if res >= 0: hits[(x,y)] = res  

#find the first x velocity, leaving y velocity at 0
x = 1
res = probe([x, 0])
while (x < steps):
    x += 1
    res = probe([x, 0])
    if res >= 0: hits[(x+1,0)] = res
x += 1

while(x > 0):
    fire(x)
    x-=1

print(max(hits.values()))