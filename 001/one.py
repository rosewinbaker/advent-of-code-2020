f = open('input.txt') 

inputList = []

for line in f:
    value = line.split()
    inputList.append(value[0])
    # print value[0]
    
f.close()

goal = 2020
sum = 0
anchor = 0
i = 0
val1 = 0
val2 = 0

while (i<(len(inputList) + 1)):
    if i == len(inputList):
        i = 0
        anchor += 1
        print "New anchor: " + str(anchor)
    val1 = int(inputList[anchor])
    val2 = int(inputList[i])
    sum = val1 + val2
    print str(inputList[anchor]) + " + " + str(inputList[i]) + " = " + str(sum)
    i += 1
    if sum == goal:
        print "Hey, we found " + str(goal)
        print str(val1) + " + " + str(val2) + " = " + str(sum)
        break

final_answer = int(val1) * int(val2)
print str(val1) + " * " + str(val2) + " = " + str(final_answer)