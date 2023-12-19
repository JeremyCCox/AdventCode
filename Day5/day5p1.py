
file = open("day5input")
fileArr = []
mapInf = [[]]
mapInfCount = 0
for line in file:
    if line== "\n":
        mapInfCount += 1
        mapInf.append([])
    else:
        item = mapInf[mapInfCount]
        mapInf[mapInfCount].append(line.strip())


def sortRules(e):
    return e[1]



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

def mapRange(seed,mapData):
    print(mapData[0],seed)
    seed = int(seed)
    lower = seed
    for inf in mapData[1:len(mapData)]:
        # print(inf,"|",seed)
        # infArr = inf.split(" ")
        dest = int(inf[0])
        source = int(inf[1])
        quant = int(inf[2])
        if seed >= source:
            if seed <= source+quant:
                # print(((dest+quant)-(source+quant-seed)))
                return ((dest+quant)-(source+quant-seed))
                # lower = ((dest+quant)-(source+quant-seed))
        # source = int(infArr[0])
        # dest = int(infArr[1])
        # quant = int(infArr[2])
        # sourceRange = list(range(source,source+quant))
        # destRange = list(range(dest,dest+quant))
        # if seed in sourceRange:
        #     lower = destRange.index(seed)
    # print("Lower for seed "+str(seed)+" is: ",lower)
    return lower

seeds = mapInf[0][0].split(":")[1].strip().split(" ")
locations = []
for seed in seeds:
    locations.append(
        mapRange( #Humidity To location
            mapRange(   #Temp to Humidity
                mapRange(   #Light to Temp
                    mapRange(   #Water to Light
                        mapRange(   #Fertilizer to Water
                            mapRange(   #Soil to Fertilizer
                                mapRange(   #Seed to Soil
                                    seed
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
    )
locations.sort()
for loc in locations:
    print(loc)

# mapRange(98,0,98,2)