file = open("day2input") # Could do solution where you filter max value for each color per line, THEN test highest value (easy in javascript)
total = 0

for line in file:
    # print(line)
    possible = True
    game = line.split(":")
    rounds = game[1].split(";")
    maxR=0
    maxG=0
    maxB=0
    for round in rounds:
        pulls = round.split(",")
        for pull in pulls:
            vals = pull.split(" ")
            match(vals[2]):
                case("red"| "red\n"):
                    if(int(vals[1])>maxR):
                        maxR=int(vals[1])

                case("green"|"green\n"):
                    if(int(vals[1])>maxG):
                        maxG=int(vals[1])

                case("blue"|"blue\n"):
                    if(int(vals[1])>maxB):
                        maxB=int(vals[1])
                case _:
                    print(vals,"Did not work!")
    print(line,maxR, maxG, maxB)
    power = maxR*maxG*maxB
    total+= power
    # else:
    #     print(line)
print(total)