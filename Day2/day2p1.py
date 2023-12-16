import re
file = open("day2input") # Could do solution where you filter max value for each color per line, THEN test highest value (easy in javascript)
total = 0
maxR=12
maxG=13
maxB=14
for line in file:
    print(line)
    possible = True
    game = line.split(":")
    rounds = game[1].split(";")
    for round in rounds:
        pulls = round.split(",")
        print(pulls)
        for pull in pulls:
            vals = pull.split(" ")
            print(pull)
            match(vals[2]):
                case("red"| "red\n"):
                    if(int(vals[1])>12):
                        possible=False

                case("green"|"green\n"):
                    if(int(vals[1])>13):
                        possible=False

                case("blue"|"blue\n"):
                    if(int(vals[1])>14):
                        possible=False
                case _:
                    print(vals,"Did not work!")
    if possible:
        # print(line)
        total+= int(game[0].split(" ").pop())
    # else:
    #     print(line)
print(total)