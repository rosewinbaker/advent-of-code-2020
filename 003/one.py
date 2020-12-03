import math
import re

lines = []

f = open('input.txt') 
inputList = []
for line in f:
    value = line.split()
    # print(value[0] * 2)

    lines.append(value[0])
    line = value[0]
    foo = ([pos for pos, char in enumerate(line) if char == '#'])
    # print(foo)
f.close()

# print(lines[0])

trees = []
total_trees = []
line_pos = 1


def find_tree(terrain, line_pos, trees):
    foo = ([pos for pos, char in enumerate(terrain) if char == '#'])
    newfoo = [x+1 for x in foo]
    # print(newfoo)

    if line_pos in newfoo:
        # print("We found a tree at line position " + str(line_pos) + " on line " + str(i))
        trees.append(i)


my_slopes = [[1,1],[3,1],[5,1],[7,1],[1,2]]

j=0
while (j<len(my_slopes)): 
# while (j<2): 
    right = my_slopes[j][0]
    down = my_slopes[j][1]
    print("Checking for slope: " + str(right) + "," + str(down))
    j += 1

    # print("Lines: " + str(len(lines)))

    # print("i #: " + str(i))
    
    i=1
    while (i<len(lines)):                                                                                                                                                              

       
        terrain = lines[i]
        terrain_length = len(terrain)
        i += down
        line_pos += right

        # print("Line # " + str(i) + " + pos # " + str(line_pos))


        find_tree(terrain, line_pos, trees)

        if line_pos >= (terrain_length - (right - 1)):

            remainder = terrain_length - line_pos
            # print("Encountered end of terrain on line " + str(i) + ". Need to add more. " + str(len(terrain)) + " - " + str(line_pos) + " = " + str(remainder))

            line_pos = remainder * -1

    
    print("Total trees encountered: " + str(len(trees)))
    total_trees.append(len(trees))
    # print(total_trees)
    trees.clear()
    i=1
    line_pos = 1

def multiplyList(myList) :
     
    # Multiply elements one by one
    result = 1
    for x in myList:
         result = result * x 
    return result 

print("Final answer: " + str(multiplyList(total_trees)))

   