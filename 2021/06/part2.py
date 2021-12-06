# text = "./2021/06/sample.txt";
text = "./2021/06/puzzle.txt";

fishTime = []
days = 256
fishState = []

for i in range(9): fishState.append(0)

with open(text) as file:
    fishTime = file.readline().strip().split(',')
    fishTime = list(map(int, fishTime))

for i in range(len(fishTime)):
    fishState[fishTime[i]] += 1

#part1 was naive aprpaoch
#There are only 8 days to keep track of
#maintain a list with 8 elements keeping track of number of fish on each day

for day in range(days):
    #on a new day we'll shift all the numbers down a day
    #the number for 0 will need to be stored in temporarily
    readyToSpawn = fishState[0]
    for i in range(1, len(fishState)):
        fishState[i-1] = fishState[i]
    
    fishState[8] = readyToSpawn
    fishState[6] += readyToSpawn

print (sum(fishState))
