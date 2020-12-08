input = []
with open('input.txt') as f:
    for line in f:
        value = line.split()
        input.append(value)
f.close()

lines_visited = []

accumulator = 0
i=0
for items in input:
    instruction = input[i][0]
    modifier = input[i][1][0]
    number = input[i][1][1:]
    # print("Line #" + str(i) + ": " + instruction + " " + modifier + number)
    lines_visited.append(i)
    # print(lines_visited)



    if instruction == 'acc':
        # print("Accumulate: " + modifier + number)
        if modifier == "+":
            accumulator += int(number)
        elif modifier == "-":
            accumulator -= int(number)
        # print("New accumulator number: " + str(accumulator))
        i += 1
        if i in lines_visited:
            print("Hey, we've done that before. Stop that.")
            print("Accumulator number: " + str(accumulator))
            break
    elif instruction == 'nop':
        # print("NOP: Nothing happening. Incrementing by one.")
        i += 1
        if i in lines_visited:
            print("Hey, we've done that before. Stop that.")
            print("Accumulator number: " + str(accumulator))
            break
    elif instruction == 'jmp':
        # print("Jumping: " + modifier + number)
        if modifier == "+":
            # print("Jumping into the future by " + number + " to line #" + str(i+int(number)) + " from line " + str(i))
            i += int(number)
            if i in lines_visited:
                print("Hey, we've done that before. Stop that.")
                print("Accumulator number: " + str(accumulator))
                break
        elif modifier == "-":
            # print("Going back in time by  " + number + " to line #" + str(i-int(number)) + " from line " + str(i))
            i -= int(number)
            if i in lines_visited:
                print("Hey, we've done that before. Stop that.")
                print("Accumulator number: " + str(accumulator))
                break