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

    # print(letter + " " + phrase)

    if letter in phrase:
        # print("found the letter")
        count = phrase.count(letter)
        # print(count)
        if range1 <= count <= range2:
            # print("Letter " + letter + " found in range " + str(range1) + "-" + str(range2) + ": " + phrase)
            valid += 1

    j += 3

print("Final answer: " + str(valid))