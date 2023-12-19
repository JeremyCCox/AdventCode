file = open("day9input")
arr =[]
for line in file:
    arr.append(line.strip().split(" "))

def getVals(vals):
    valCount = len(vals)-1
    newArr=[]
    while valCount > 0:
        newArr.append(int(vals[valCount])-int(vals[valCount-1]))
        valCount-=1
    newArr.reverse()
    return newArr


def allZero(arr):
    for elem in arr:
        if elem != 0:
            return False
    return True


total = 0
for vals in arr:
    valCount = len(vals)-1
    newArr = list(map(int, vals))
    stages = [newArr]
    while not allZero(newArr):
        newArr = getVals(newArr)
        stages.append(newArr)
    stages.reverse()
    incVal = 0
    for stage in stages:
        nextVal = stage[len(stage)-1] + incVal
        stage.append(nextVal)
        incVal = nextVal
    total += incVal
    print(incVal)
print(total)

