# #line of vents is given as a line segment x1,y1 -> x2,y2
# #x1,y1 are coordinates of one end of the line segment, x2,y2 are the other
# #These include the point at both end

# #ex 1,1 -> 1,3 covers 1,1 1,2 and 1,3
# #for now only condsider horizontal and vertical (x1=x2 or y1=y2)

import re
import math

def markCoords(coordinates, x, y):
    if y not in coordinates:
        coordinates[y] = {}

    if x not in coordinates[y].keys():
        coordinates[y][x] = 1
    else:
        coordinates[y][x] += 1
        if coordinates[y][x] == 2:
            return 1
    return 0


text = "./2021/05/puzzle.txt";
# text = "./2021/05/sample.txt";

coordinates = {}

overlapCtr = 0
with open(text) as file:
    for line in file:
        matches = re.findall('\d+', line)

        x1 = int(matches[0]) 
        x2 = int(matches[2])
        y1 = int(matches[1])
        y2 = int(matches[3])
        step = 1

        if y1 == y2:
            start = x1
            stop = x2 + 1

            if x1 > x2:
                step = -1
                stop = x2 - 1

            for i in range(start, stop, step):   
                overlapCtr += markCoords(coordinates, i, y1)
        elif x1 == x2:
            start = y1
            stop = y2 + 1

            if y1 > y2:
                step = -1
                stop = y2 - 1

            for i in range(start, stop, step):
                overlapCtr += markCoords(coordinates, x1, i)
        else:
            #Only need diagnols if they are a 45 degree angle
            dist = math.degrees(math.atan2(y2-y1,x2-x1))
            if dist % 45.0 == 0: 
                #Just need to figure out the direction we are moving
                xStep = yStep = 1
                xStart = x1
                yStart = y1
                xStop = x2 + 1
                yStop = y2 + 1

                if x1 > x2:
                    xStep = -1
                    xStop = x2 - 1
                if y1 > y2:
                    yStep = -1
                    yStop = y2 - 1

                m = [i for i in range(xStart, xStop, xStep)]
                n = [i for i in range(yStart, yStop, yStep)]
                index = 0
                while(index < len(m)):
                    overlapCtr += markCoords(coordinates, m[index], n[index])
                    index += 1

print(overlapCtr)
