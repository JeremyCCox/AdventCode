import re
with open("practiceInput") as filecount:
    for linetotal, line in enumerate(filecount):
        pass
filecount.close()
file = open("day3input")
writeFile = open("day3output","w")
nums = ["0","1","2","3","4","5","6","7","8","9"]

topLine = ""
midline = ""
botline = ""
linecount = 0
partsSum = 0

for line in file:
    line = "..."+line.replace("\n","")+"...\n"
    count = 0
    for i in line:
        if not re.match("[0-9]|\.|,|\\n",i):
            # print(line[count-1],i,line[count+1])
            if line[count-1] in nums:
                numArr = []
                num = 1
                while line[count-num] in nums:
                    numArr.append(line[count-num])
                    lineArr = list(line)
                    lineArr[(count-num)]=","
                    line="";
                    for char in lineArr:
                        line+= char;

                    num+=1
                numArr.reverse()
                numStr =""
                for char in numArr:
                    numStr += char;
                partsSum += int(numStr)
                print("added "+numStr)
                # match(len(numStr)):
                #     case 1:
                #         line.replace(numStr,".")
                #     case 2:
                #         line.replace(numStr,"..")
                #     case 3:
                #         line.replace(numStr,"..")
            if line[count+1] in nums:
                numArr = []
                num = 1
                while line[count+num] in nums:
                    numArr.append(line[count+num])
                    lineArr = list(line)
                    lineArr[(count+num)]=","
                    line="";
                    for char in lineArr:
                        line+= char;
                    num+=1
                # numArr.reverse()
                numStr =""
                for char in numArr:
                    numStr += char;
                partsSum += int(numStr)
                print("added "+numStr)
                # match(len(numStr)):
                #     case 1:
                #         line.replace(numStr,".")
                #     case 2:
                #         line.replace(numStr,"..")
                #     case 3:
                #         line.replace(numStr,"..")
            if topLine != "":
                safeTopline = topLine
                # print(safeTopline[(count+3)-1])
                if safeTopline[count-1] in nums or safeTopline[count] in nums or safeTopline[count+1] in nums:
                    # print("Top 3",(safeTopline[count-1:count+2]))
                    numArr = []
                    num = 1
                    while safeTopline[count-num] in nums:
                        # print("Top 1",safeTopline[(count+3)-num])
                        numArr.insert(0, safeTopline[count - num])
                        topLineArr = list(topLine)
                        topLineArr[count-num]=","
                        topLine="";
                        for char in topLineArr:
                            topLine+= char;
                        topLine += "\n"
                        num+=1
                    num = 1
                    numArr.append(safeTopline[count])
                    while safeTopline[count+num] in nums:
                        numArr.append(safeTopline[count+num])
                        topLineArr = list(topLine)
                        topLineArr[(count+num)]=","
                        topLine="";
                        for char in topLineArr:
                            topLine+= char;
                        topLine += "\n"
                        num+=1
                    numStr =""
                    for char in numArr:
                        numStr += char;
                    trimmedArr=numStr.split(".");
                    # print(trimedArr)
                    for elem in trimmedArr:
                        if len(elem) > 0:
                            partsSum += int(elem)
                            print("added "+elem)




            # if botline != "":
            #     botLine = botline
            #     if botLine[count-1] in nums or botLine[count] in nums or botLine[count+1] in nums:
            #         numArr = []
            #         num = 1
            #         while botLine[count-num] in nums:
            #             numArr.insert(0, botLine[count - num])
            #             botLineArr = list(botline)
            #             botLineArr[(count-num)]=","
            #             botline="";
            #             for char in botLineArr:
            #                 botline+= char;
            #             botline += "\n"
            #             num+=1
            #         num = 1
            #         numArr.append(botLine[count])
            #         while botLine[count+num] in nums:
            #             numArr.append(botLine[count+num])
            #             botLineArr = list(botline)
            #             botLineArr[(count+num)]=","
            #             botline="";
            #             for char in botLineArr:
            #                 botline+= char;
            #             botline += "\n"
            #             num+=1
            #         numStr =""
            #         for char in numArr:
            #             numStr += char;
            #         trimmedArr=numStr.split(".");
            #         for elem in trimmedArr:
            #             if len(elem) > 0:
            #                 partsSum += int(elem)
            #                 print("added "+elem)


                    # match(len(safeTopline[(count+3)-1:(count+3)+2].split("."))):
                    #     case 1:
                    #         print(1,safeTopline[(count+3)-1:(count+3)+2].split("."))
                    #     case 2:
                    #         print(2,safeTopline[(count+3)-1:(count+3)+2].split("."))
                    #     case 3:
                    #         print(3,safeTopline[(count+3)-1:(count+3)+2].split("."))
                    # print(i,"Safe Top line substring: ",safeTopline[((count+3)-3):((count+3)+4)])
                    # print(safeTopline[((count+3)-3):((count+3)+4)].split("."))


                #     numArr = []
                #     num = 1
                #     while safeTopline[(count+3)-num] in nums:
                #         numArr.append(safeTopline[(count+3)-num])
                #         num+=1
                #     numArr.reverse()
                #     numStr =""
                #     for char in numArr:
                #         numStr += char;
                #     # print(numStr+i)
                # if safeTopline[(count+3)+1] in nums:
                #     numArr = []
                #     num = 1
                #     while safeTopline[(count+3)+num] in nums:
                #         numArr.append(safeTopline[(count+3)+num])
                #         num+=1
                #     # numArr.reverse()
                #     numStr =""
                #     for char in numArr:
                #         numStr += char;
                #     # print(i+numStr)

        count = count+1
    if topLine != "":
        topLineCount = 0
        for j in topLine:
            if not re.match("[0-9]|\.|,|\\n",j):
                botLine = line
                if botLine[topLineCount-1] in nums or botLine[topLineCount] in nums or botLine[topLineCount+1] in nums:
                    numArr = []
                    num = 1
                    while botLine[topLineCount-num] in nums:
                        numArr.insert(0, botLine[topLineCount - num])
                        lineArr = list(line)
                        lineArr[(topLineCount-num)]=","
                        line="";
                        for char in lineArr:
                            line+= char;
                        num+=1
                    numArr.append(botLine[topLineCount])
                    if botLine[topLineCount] in nums:
                        lineArr = list(line)
                        lineArr[(topLineCount)]=","
                        line="";
                        for char in lineArr:
                            line+= char
                    num = 1
                    while botLine[topLineCount+num] in nums:
                        numArr.append(botLine[topLineCount+num])
                        lineArr = list(line)
                        lineArr[(topLineCount+num)]=","
                        line="";
                        for char in lineArr:
                            line+= char;
                        num+=1
                    numStr =""
                    for char in numArr:
                        numStr += char;
                    trimmedArr=numStr.split(".");
                    print(trimmedArr)
                    for elem in trimmedArr:
                        if len(elem) > 0:
                            partsSum += int(elem)
                            print("added "+elem)
            topLineCount += 1
    # print(topLine)
    writeFile.write(str(topLine))
    topLine = line
print(partsSum)
print(botLine)
writeFile.write(str(botline))
writeFile.close()
file.close()