f = open('input.txt') 

prac_list = []

for line in f:
    value = line.split()
    prac_list.append(value[0])
    # print value[0]
    
f.close()

goal = 2020
sum = 0
a1 = 0
a2 = a1 + 1
a3 = a1 + 2

while (a3<=(len(prac_list))):
    if a3 == len(prac_list):
        a3 = a1 + 2
        a2 += 1
        if a2 == len(prac_list):
            a1 += 1
            a2 = a1 + 1
        # if a1 == len(prac_list):
        #     break
        # # print "New a2: " + str(prac_list[a2])
    val1 = int(prac_list[a1])
    val2 = int(prac_list[a2])
    val3 = int(prac_list[a3])
    sum = val1 + val2 + val3
    # print sum
    a3 += 1
    if sum == goal:
        print "Hey, we found " + str(goal)
        print str(val1) + " + " + str(val2) + " + " + str(val3) + " = " + str(sum)
        break


final_answer = int(val1) * int(val2) * int(val3)
print str(val1) + " + " + str(val2) + " + " + str(val3) + " = " + str(final_answer)