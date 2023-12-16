import re
max = 0;
file = open("day1input")
for line in file:
    arr = re.findall("[0-9]",line);
    val = int(arr[0] +""+arr.pop())
    max +=  int(val)
    print(line)
    print(val)

print(max)

