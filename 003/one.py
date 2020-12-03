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
line_pos = 1
i=1

def find_tree(terrain, line_pos, trees):
    foo = ([pos for pos, char in enumerate(terrain) if char == '#'])
    newfoo = [x+1 for x in foo]
    # print(newfoo)

    if line_pos in newfoo:
        print("We found a tree at line position " + str(line_pos) + " on line " + str(i))
        trees.append(i)

while (i<len(lines)):

    terrain = lines[i]

    i += 1
    line_pos += 3

    print("Line # " + str(i) + " + pos # " + str(line_pos))

    if line_pos >= (len(terrain) - 2):

        remainder = len(terrain) - line_pos
        print("Encountered end of terrain on line " + str(i) + ". Need to add more. " + str(len(terrain)) + " - " + str(line_pos) + " = " + str(remainder))

        if remainder == 0:
            find_tree(terrain, line_pos, trees)
            line_pos = 0
            print("Setting new line_pos to 0: " + str(line_pos))
        elif remainder == 1:
            find_tree(terrain, line_pos, trees)
            line_pos = -1
            print("Setting new line_pos to 2: " + str(line_pos))
        elif remainder == 2:
            find_tree(terrain, line_pos, trees)
            line_pos = -2
            print("Setting new line_pos to 2: " + str(line_pos))
        elif remainder == -1:
            line_pos = 3
            print("Setting new line_pos to 2: " + str(line_pos))
            find_tree(terrain, line_pos, trees)
        elif remainder == -2:
            line_pos = 2
            print("Setting new line_pos to 1: " + str(line_pos))
            find_tree(terrain, line_pos, trees)
    else:
        find_tree(terrain, line_pos, trees)
        # print("New line position: " + str(line_pos))

print("Total trees encountered: " + str(len(trees)))
    
   