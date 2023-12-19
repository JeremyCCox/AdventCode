file = open("day8input")

instructions = list(file.readline().strip()+"E")
file.readline()

lastInstruction=[]
map = []
for line in file:
    mapVals = line.split("=")
    dirs = mapVals[1].strip().replace("(","").replace(")","").replace(" ","").split(",")
    map.append({"node":mapVals[0].strip(),"L":dirs[0],"R":dirs[1]})
    if mapVals[0][2] == "A":
        lastInstruction.append(mapVals[0].strip())

steps=1

instructionCount = 0
while instructionCount <= len(instructions):
    instruction = instructions[instructionCount]
    if instruction == "E":
        instructionCount=0
    else:
        nextInstructions=[]
        allZ=True
        for mapElem in lastInstruction:
            mapIndex = next(location for location in map if location["node"] == str(mapElem))
            nextInstructions.append(mapIndex[instruction])
            if mapIndex[instruction][2] != "Z":
                allZ=False
        if allZ:
            print(steps)
            exit()
        # print(nextInstructions)
        lastInstruction = nextInstructions
        instructionCount+=1
        steps +=1



print(steps)
