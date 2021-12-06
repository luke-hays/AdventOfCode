# text = "./2021/06/sample.txt";
text = "./2021/06/puzzle.txt";

fishTime = []
days = 80

with open(text) as file:
    fishTime = file.readline().strip().split(',')
    fishTime = list(map(int, fishTime))

for day in range(1, days):
    #decrement all internal fish timers
    fishTime = list(map(lambda x: x-1, fishTime))

    #if there are any zeros, append an 9
    readyToSpawn = fishTime.count(0)
    for i in range(readyToSpawn):
        fishTime.append(9)

    #reset the zeros to seven
    fishTime = list(map(lambda x: 7 if x == 0 else x, fishTime))

print (len(fishTime))