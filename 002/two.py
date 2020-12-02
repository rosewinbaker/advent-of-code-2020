import re

f = open('input.txt') 
inputList = []
for line in f:
    value = line.split()
    i=0
    while (i<3):
        clean = re.split('\-|:|\*|\n',value[i])
        inputList.append(clean)
        i += 1
f.close()

j = 0
valid = 0

while (j<len(inputList)):
    range1 = int(inputList[j][0])
    range2 = int(inputList[j][1])
    letter = inputList[j+1][0]
    phrase = inputList[j+2][0]

    if letter in phrase:

        foo = ([pos for pos, char in enumerate(phrase) if char == letter])
        newfoo = [x+1 for x in foo]

        if (range1 in newfoo) != (range2 in newfoo):
            # print(newfoo)
            # print(letter + " in " + phrase + " " + str(range1) + " or " + str(range2))
            valid += 1

    j += 3

print("Final answer: " + str(valid))