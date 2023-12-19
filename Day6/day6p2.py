file = open("day6input")
time=0
distance=0
leadZeros = 0;
for line in file:
    data = line.split(":")
    arr = data[1].replace(" ","").strip()
    if data[0] == "Time":
        time=int(arr)
    else:
        distance=int(arr)

# if time[len(time)-1] == '0' and distance[len(distance)-1] == "0":
#     time = int(time[0:len(time)-1])
#     distance = int(distance[0:len(distance)-1])
possibleGains = 1

gains = 0
for accel in range(int(time)):
    timeLeft = time - accel
    if accel * timeLeft > distance:
        gains+=1


# for targetDistance in distanceList:
#     print("Target Distance "+str(targetDistance))
#
#             print("Accel of "+str(accel)+" gives distance "+str(accel*timeLeft))


print(gains)


