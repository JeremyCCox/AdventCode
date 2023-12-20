import datetime

file = open("practiceInput")
fileArr = []
mapInf = [[]]
mapInfCount = 0


def log(message):
    logfile = open("logfile.txt","a")
    logfile.write(str(datetime.datetime.now())+" LOG: "+message+"\n")
    print(str(datetime.datetime.now())+" LOG: "+str(message)+"\n")
    logfile.close()


log("Program Running! \n")

def sortRules(e):
    return e[1]


for line in file:
    if line == "\n":
        mapInfCount += 1
        mapInf.append([])
    else:
        item = mapInf[mapInfCount]
        mapInf[mapInfCount].append(line.strip())

mapInfCount = 1
for inf in mapInf[1:len(mapInf)]:
    # print(inf)
    newArr = []
    for val in inf[1:len(inf)]:
        vals = val.split(" ")
        newArr.append([int(vals[0]), int(vals[1]), int(vals[2])+int(vals[1])])
    # newArr.sort(key=sortRules, reverse=True)
    newArr.insert(0, inf[0])
    mapInf[mapInfCount] = newArr
    mapInfCount += 1

almanacList = mapInf[0][0].split(":")[1].strip().split(" ")
seedPairs = []
seedCount = 0
pairCount = -1
for val in almanacList:
    if seedCount % 2 == 0:
        pairCount += 1
        seedPairs.append([])
    seedPairs[pairCount].append(int(val))
    seedCount += 1


def sortSmallest(e):
    return e[0]


seedPairs.sort(key=sortSmallest)
print(seedPairs)

condensedPairs = [[seedPairs[0][0], seedPairs[0][0] + seedPairs[0][1]]]
# print(len(condensedPairs))
condensedCount = 0
# def condensePairs(start,rnge):
#     if condensedPairs[condensedCount][1] >= start:
#         if condensedPairs[condensedCount][1] < (start + range):
#             condensedPairs[condensedCount][1] = (start+range)
#     else:
#         condensedPairs.append([start,start+range])
#         condensedCount+= 1



for pair in seedPairs:
    if condensedPairs[condensedCount][1] >= pair[0]:
        if condensedPairs[condensedCount][1] < (pair[0] + pair[1]):
            condensedPairs[condensedCount][1] = (pair[0] + pair[1])
    else:
        condensedPairs.append([pair[0], pair[0] + pair[1]])
        condensedCount += 1

print(condensedPairs)

seedPairs = []
almanacList=[]


seeds = []
locations = []
iterCount = 0

def mapRange(seed, mapData):
    for inf in mapData[1:len(mapData)]:
        if seed >= inf[1]:
            if seed <= inf[2]:
                return inf[0] - (inf[1] - seed)
    return seed


lowestVals = []

for seedPair in condensedPairs:
    log(str((iterCount / len(condensedPairs) * 100))+"% Completed!")
    lowestLocation = seedPair[0]*seedPair[1]
    # seedRange = list(range(seedPair[0], seedPair[1]))
    seed = seedPair[0]
    seedMax = seedPair[1]-1
    while seed < seedMax:
    # for seed in seedRange:
        seedLocation = mapRange(  # Humidity To location
            mapRange(  # Temp to Humidity
                mapRange(  # Light to Temp
                    mapRange(  # Water to Light
                        mapRange(  # Fertilizer to Water
                            mapRange(  # Soil to Fertilizer
                                mapRange(  # Seed to Soil
                                    int(seed)
                                    ,
                                    mapInf[1])
                                ,
                                mapInf[2])
                            ,
                            mapInf[3])
                        ,
                        mapInf[4])
                    ,
                    mapInf[5])
                ,
                mapInf[6])
            ,
            mapInf[7])# seedFile.write(str(
        if seedLocation < lowestLocation:
            lowestLocation = seedLocation
        seed += 1
        # ) + ",")
    iterCount += 1
    log("Lowest was "+str(lowestLocation))
    lowestVals.append(lowestLocation)
    # seedFile.close()

lowestVals.sort()

log("Overall Lowest was "+str(lowestVals[0]))
log("All Lower Values are:")
for val in lowestVals:
    log("Val " + str(val))
log("Program Finished Running! \n")


# mapRange(98,0,98,2)
