file = open("day4input")

foundTotal = 0

cardStack = []
cardCount = []

for line in file:
    cardStack.append(line)
    cardCount.append(1)

for i in range(len(cardStack)):
    cardInfo = cardStack[i].split(":")
    values = cardInfo[1].split("|")
    foundCount = 0
    keys = values[0].strip().split(" ")
    locks = " " + values[1].strip() + " "
    # print(locks)
    for val in keys:
        if locks.find(" " + val + " ") > -1:
            if val != "":
                # print("Value: " + val + " |", locks)
                foundCount+= 1
                cardCount[i+foundCount]+= cardCount[i];
    # foundTotal += foundCount

for i in range(len(cardStack)):
    foundTotal+= cardCount[i]
    print(cardStack[i].replace("\n",""),"| Card Count|",cardCount[i])
print(foundTotal)
