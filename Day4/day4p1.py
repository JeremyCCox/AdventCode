
file = open("day4input")

foundTotal = 0
for line in file:
    card = line.split(":")
    values = card[1].split("|")
    foundCount = 0
    keys = values[0].strip().split(" ")
    locks = " "+values[1].strip() + " "
    # print(locks)
    for val in keys:
        if locks.find(" "+val+" ") > -1:
            if val != "":
                print("Value: "+val+" |", locks)
                if foundCount > 0:
                    foundCount = foundCount * 2
                else:
                    foundCount = 1
    foundTotal += foundCount
print(foundTotal)