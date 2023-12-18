file = open("day6practiceInput")
timeList = []
distanceList = []
for line in file:
    data = line.split(":")
    arr = data[1].strip().split(" ")
    if data[0] == "Time":
        for elem in arr:
            if elem != "":
                timeList.append(elem)
    else:
        for elem in arr:
            if elem != "":
                distanceList.append(elem)
