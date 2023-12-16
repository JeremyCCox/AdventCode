import regex as re
total = 0
nums = ["zero","one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
file = open("day1input")

for line in file:
    arr = re.findall(pattern="[0-9]|two|one|three|four|five|six|seven|eight|nine",string=line,overlapped=True)
    first = arr[0]
    last = arr.pop()
    if len(first) > 1:
        first = str(nums.index(first))
    if len(last) > 1:
        last = str(nums.index(last))
    val = first +last
    print(line," turns to ",val)
    total += int(val)
print(total)