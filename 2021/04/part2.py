 
import os

def calcBingoScore(currentDraws, combos):
    lastDrawn =  int(currentDraws[-1])

    numberSet = set(sum(combos, [])).difference(currentDraws)    
    
    n = 0
    for val in numberSet:
        n += int(val)

    return n * lastDrawn

text = "./2021/04/puzzle.txt";

print(os.getcwd())
with open(text) as file:
    bingoSystem = [line.strip() for line in file]

draws = bingoSystem[0].split(',')
boards = []
board = []
rowCtr = 0
gridSize = 5

winningCombos = {}
boardNumber = 0
for i in range(1, len(bingoSystem)):
    if bingoSystem[i] == '':
        continue

    row = bingoSystem[i].split()
    board.append(row)

    if rowCtr >= gridSize-1: 
        winningCombos[boardNumber] = []
        for j in range(len(board)):
            winningCombos[boardNumber].append(board[j])
            winningCombos[boardNumber].append([x[j] for x in board])

        boardNumber += 1
        board = []
        rowCtr = 0
    else:
        rowCtr += 1

boards = [x for x in winningCombos.keys()];
for i in range(5,len(draws)):
    currentDraws = draws[0:i]

    if len(boards) == 1:
        print(calcBingoScore(currentDraws, winningCombos[boards[0]]))
        break

    toRemove = []
    for k,v in winningCombos.items():
        for combo in v:
            if (all(x in currentDraws for x in combo)):
                toRemove.append(k)

    for k in set(toRemove):
        winningCombos.pop(k)
        boards.remove(k)

        