file = open("day5input")
fileArr = []
mapInf = [[]]
mapInfCount = 0


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
        newArr.append([int(vals[0]), int(vals[1]), int(vals[2])])
    newArr.sort(key=sortRules, reverse=True)
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
print(len(condensedPairs))
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

seeds = []
locations = []
iterCount = 0


def mapRange(seed, mapData):
    for inf in mapData[1:len(mapData)]:
        if seed >= inf[1] <= inf[1] + inf[2]:
            if seed <= inf[1] + inf[2]:
                return inf[0] - (inf[1] - seed)
    return seed


for seedPair in condensedPairs:
    print((iterCount / len(seedPairs) * 100), "% Completed!")

    seedRange = list(range(seedPair[0], seedPair[1]))
    seedFile = open("seedFile-" + str(iterCount), "w")
    seedLocations = []
    for seed in seedRange:
        seedFile.write(str(
            mapRange(  # Humidity To location
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
                mapInf[7])
        ) + ",")
    iterCount += 1
    seedFile.close()
locations.sort()
for loc in locations:
    print(loc)

# mapRange(98,0,98,2)
