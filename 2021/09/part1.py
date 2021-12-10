# text = "./2021/09/sample.txt";
text = "./2021/09/puzzle.txt";

#find low points - locations lower than adjacent in 4 directions
#edges or corners have only two or three

lowPointRiskSum = 0
floorLength = 0
heightmap = []
with open(text) as file:
    heightmap = [line.strip() for line in file]

rowLen = len(heightmap)
colLen = len(heightmap[0])
for i in range(rowLen):
    for j in range(colLen):
        adj = []
        lowest = int(heightmap[i][j])
        #top
        if i == 0:
            #TopLeft
            if j == 0:
                adj.append(int(heightmap[i+1][j]))
                adj.append(int(heightmap[i][j+1]))
            #TopRight
            elif j == colLen-1:
                adj.append(int(heightmap[i][j-1]))
                adj.append(int(heightmap[i+1][j]))
            #TopEdge
            else:
                adj.append(int(heightmap[i+1][j]))
                adj.append(int(heightmap[i][j-1]))
                adj.append(int(heightmap[i][j+1]))
        #bottom
        elif i == rowLen-1:
            #BottomLeft
            if j == 0:
                adj.append(int(heightmap[i-1][j]))
                adj.append(int(heightmap[i][j+1]))
            #BottomRight
            elif j == colLen-1:
                adj.append(int(heightmap[i-1][j]))
                adj.append(int(heightmap[i][j-1]))
            #BottomEdge
            else:
                adj.append(int(heightmap[i-1][j]))
                adj.append(int(heightmap[i][j-1]))
                adj.append(int(heightmap[i][j+1]))
        else:
            #EdgeLeft
            if j == 0:
                adj.append(int(heightmap[i+1][j]))
                adj.append(int(heightmap[i-1][j]))
                adj.append(int(heightmap[i][j+1]))
            #EdgeRight
            elif j == colLen-1:
                adj.append(int(heightmap[i-1][j]))
                adj.append(int(heightmap[i+1][j]))
                adj.append(int(heightmap[i][j-1]))
            #Everything Else
            else:
                adj.append(int(heightmap[i+1][j]))
                adj.append(int(heightmap[i][j+1]))
                adj.append(int(heightmap[i-1][j]))
                adj.append(int(heightmap[i][j-1]))
        
        foundLowest = True
        for n in adj:
            if n <= lowest: 
                foundLowest = False
                break
        if foundLowest: lowPointRiskSum += lowest+1

print(lowPointRiskSum)