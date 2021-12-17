text = "./2021/16/sample.txt";
# text = "./2021/16/puzzle.txt";

# had to get some inspiration on a solution
# reading from a buffer fixed some of the issues

from io import StringIO

versionsum = 0
packetVals = []

def btoi(val): return int(val, 2)

def htob(val): return bin(int(val, 16))[2:].zfill(4)

def parseBinString(packet):
    global versionsum

    version = packet.read(3)
    typeID = packet.read(3)

    iTypeID = btoi(typeID)
    versionsum+=btoi(version)

    if iTypeID == 4: 
        chunks = []
        bit = ''
        while bit != '0':
            bit = packet.read(1)
            chunks.append(packet.read(4))
        return btoi(''.join(chunks))

    subpackets = []
    if packet.read(1) == '0':
        nBits = btoi(packet.read(15))
        target = packet.tell() + nBits
        while(packet.tell() != target):
            subpackets.append(parseBinString(packet))
    else:
        nBits = btoi(packet.read(11))
        for _ in range(nBits):
            subpackets.append(parseBinString(packet)) 

bstring = ''
with open(text) as file:
    packet = file.readline()
    for c in packet: bstring += htob(c)

parseBinString(StringIO(bstring))

print(f"The first solution is {versionsum}")