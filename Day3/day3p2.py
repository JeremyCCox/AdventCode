import re
file = open("day3input")
followFile = open("practiceInput2")
writeFile = open("practiceOutput2","w")
nums = ["0","1","2","3","4","5","6","7","8","9"]

topLine = ""
midline = ""
botline = ""
linecount = 0
partsSum = 0

gearRatioTotal=0

twoDArray = [[]]

for line in file:
    line = "..."+line.replace("\n","")+"...\n"
    twoDArray.append(list(line))

arrCount = 0
for arr in twoDArray:
    charCount = 0
    print(arr)
    for char in arr:
        gears=[]
        if char == "*":
            if arrCount>0:
                # print(twoDArray[arrCount-1][charCount-1:charCount+2])
                numArr=[]
                num=1
                while twoDArray[arrCount-1][charCount-num] in nums:
                    numArr.insert(0, twoDArray[arrCount-1][charCount-num])
                    num+=1
                if twoDArray[arrCount-1][charCount] in nums:
                    numArr.append(twoDArray[arrCount-1][charCount])
                else:
                    numArr.append(".")
                num=1
                while twoDArray[arrCount-1][charCount+num] in nums:
                    numArr.append(twoDArray[arrCount-1][charCount+num])
                    num+=1
                numStr =""
                for char in numArr:
                    numStr += char;
                trimmedArr=numStr.split(".");
                for elem in trimmedArr:
                    if len(elem) > 0:
                        gears.append(elem)
                        print(elem)
            # print(twoDArray[arrCount][charCount-1:charCount+2])
            if twoDArray[arrCount][charCount-1] in nums:
                numArr = []
                num = 1
                while twoDArray[arrCount][charCount-num] in nums:
                    numArr.insert(0,twoDArray[arrCount][charCount-num])
                    num+=1
                numStr =""
                for char in numArr:
                    numStr += char;
                # currentGears.append(numStr);
                trimmedArr=numStr.split(".");
                for elem in trimmedArr:
                    if len(elem) > 0:
                        gears.append(elem)
                        print(elem)
            if twoDArray[arrCount][charCount+1] in nums:
                numArr = []
                num = 1
                while twoDArray[arrCount][charCount+num] in nums:
                    numArr.append(twoDArray[arrCount][charCount+num])
                    num+=1
                numStr =""
                for char in numArr:
                    numStr += char;
                # currentGears.append(numStr);
                trimmedArr=numStr.split(".");
                for elem in trimmedArr:
                    if len(elem) > 0:
                        gears.append(elem)
                        print(elem)
            # print(twoDArray[arrCount][charCount-1:charCount+2])
            if arrCount<=len(twoDArray):
                # print(twoDArray[arrCount+1][charCount-1:charCount+2])
                numArr=[]
                num=1
                while twoDArray[arrCount+1][charCount-num] in nums:
                    numArr.insert(0, twoDArray[arrCount+1][charCount-num])
                    num+=1
                if twoDArray[arrCount+1][charCount] in nums:
                    numArr.append(twoDArray[arrCount+1][charCount])
                else:
                    numArr.append(".")
                num=1
                while twoDArray[arrCount+1][charCount+num] in nums:
                    numArr.append(twoDArray[arrCount+1][charCount+num])
                    num+=1
                numStr =""
                for char in numArr:
                    numStr += char;
                trimmedArr=numStr.split(".");
                for elem in trimmedArr:
                    if len(elem) > 0:
                        gears.append(elem)
                        print(elem)
            print(gears)
        charCount+=1
        if len(gears)>1:
            print(gears)
            gearRatio=1
            for num in gears:
                gearRatio*=int(num)
            gearRatioTotal +=  gearRatio
    arrCount+=1
print(gearRatioTotal)
# for line in file:
#     line = "..."+line.replace("\n","")+"...\n"
#     print("line",line)
#     count = 0
#     for i in line:
#         if re.match("[*]",i):
#             if line[count-1] in nums:
#                 numArr = []
#                 num = 1
#                 while line[count-num] in nums:
#                     numArr.append(line[count-num])
#                     num+=1
#                 numArr.reverse()
#                 numStr =""
#                 for char in numArr:
#                     numStr += char;
#                 currentGears.append(numStr);
#                 print("added "+numStr)
#             if line[count+1] in nums:
#                 numArr = []
#                 num = 1
#                 while line[count+num] in nums:
#                     numArr.append(line[count+num])
#                     num+=1
#                 numStr =""
#                 for char in numArr:
#                     numStr += char;
#                 currentGears.append(numStr);
#                 print("added "+numStr)
#             if topLine != "":
#                 safeTopline = topLine
#                 if safeTopline[count-1] in nums or safeTopline[count] in nums or safeTopline[count+1] in nums:
#                     numArr = []
#                     num = 1
#                     while safeTopline[count-num] in nums:
#                         numArr.insert(0, safeTopline[count - num])
#                         # topLine += "\n"
#                         num+=1
#                     num = 1
#                     numArr.append(safeTopline[count])
#                     while safeTopline[count+num] in nums:
#                         numArr.append(safeTopline[count+num])
#                         topLineArr = list(topLine)
#                         topLineArr[(count+num)]=","
#                         topLine="";
#                         for char in topLineArr:
#                             topLine+= char;
#                         # topLine += "\n"
#                         num+=1
#                     numStr =""
#                     for char in numArr:
#                         numStr += char;
#                     trimmedArr=numStr.split(".");
#                     # print(trimedArr)
#                     for elem in trimmedArr:
#                         if len(elem) > 0:
#                             currentGears.append(numStr);
#                             print("added "+numStr)
#         count = count+1
#     if topLine != "":
#         topLineCount = 0
#         for j in topLine:
#             if re.match("\*",j):
#                 botLine = line
#                 print(botLine)
#                 if botLine[topLineCount-1] in nums or botLine[topLineCount] in nums or botLine[topLineCount+1] in nums:
#                     numArr = []
#                     num = 1
#                     while botLine[topLineCount-num] in nums:
#                         numArr.insert(0, botLine[topLineCount - num])
#                         num+=1
#                     numArr.append(botLine[topLineCount])
#                     num = 1
#                     while botLine[topLineCount+num] in nums:
#                         numArr.append(botLine[topLineCount+num])
#                         num+=1
#                     numStr =""
#                     for char in numArr:
#                         numStr += char;
#                     trimmedArr=numStr.split(".");
#                     print(trimmedArr)
#                     for elem in trimmedArr:
#                         if len(elem) > 0:
#                             currentGears.append(numStr);
#                             print("added "+numStr)
#             topLineCount += 1
#         botLine=line
#         print(currentGears)
#     else:
#         print(currentGears)
#     writeFile.write(str(topLine))
#     topLine = line
# print(partsSum)
# print(botLine)
# writeFile.write(str(botLine))
# writeFile.close()
# file.close()