file = open("day6input")
timeList = []
distanceList = []
for line in file:
    data = line.split(":")
    arr = data[1].strip().split(" ")
    if data[0] == "Time":
        for elem in arr:
            if elem != "":
                timeList.append(int(elem))
    else:
        for elem in arr:
            if elem != "":
                distanceList.append(int(elem))

timeCount = 0
possibleGains = 1
for targetDistance in distanceList:
    print("Target Distance "+str(targetDistance))
    gains = 0
    for accel in range(timeList[timeCount]):
        timeLeft = timeList[timeCount] - accel
        if accel * timeLeft > targetDistance:
            gains+=1
            print("Accel of "+str(accel)+" gives distance "+str(accel*timeLeft))
    possibleGains *= gains
    timeCount += 1

print(possibleGains)


