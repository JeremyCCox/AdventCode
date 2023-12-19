file = open("day8input")

instructions = list(file.readline().strip()+"E")
file.readline()

map = []
for line in file:
    mapVals = line.split("=")
    dirs = mapVals[1].strip().replace("(","").replace(")","").replace(" ","").split(",")
    map.append({"node":mapVals[0].strip(),"L":dirs[0],"R":dirs[1]})

steps=0
lastInstruction="AAA"
instructionCount = 0
while instructionCount <= len(instructions):
    instruction = instructions[instructionCount]
    if instruction == "E":
        instructionCount=0
    else:
        mapIndex = next(location for location in map if location["node"] == str(lastInstruction))
        print(mapIndex[instruction])
        steps +=1
        instructionCount+=1
        if(mapIndex[instruction] == "ZZZ"):
            print(steps)
            exit()
        lastInstruction=mapIndex[instruction]



print(steps)
