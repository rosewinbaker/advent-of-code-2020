input = []
with open('sample-input.txt') as f:
    for line in f:
        value = line.split()
        input.append(value)
f.close()

lines_visited = {}
lines_we_changed = {}

been_changed = 0
accumulator = 0
acc_temp = 0
i_temp = 0
i=0

# def try_another_change():
#     print("Hey, we've done that before. Stop that.")
#         print("Before: i " + str(i) + " and acc " + str(accumulator))
#         i = i_temp
#         if i == 0:
#             print("Need to break out of 0 loop")
#             i = i_temp + 1
#         accumulator = acc_temp
#         been_changed = 0
#         print("lines_visited before:")
#         print(lines_visited)

#         for key, value in list(lines_visited.items()):
#             if value == 1:
#                 del lines_visited[key]
#             else:
#                 lines_visited[key] -= 1

#         print("lines_visited after:")
#         print(lines_visited)
#         if input[i][0] == 'noc':
#             instruction = 'jmp'
#         if input[i][0] == 'jmp':
#             instruction = 'noc'
#         print("After: i " + str(i) + " and acc " + str(accumulator))

while (i < len(input)): 
# while (i < 500):
    instruction = input[i][0]
    modifier = input[i][1][0]
    number = input[i][1][1:]
    both = input[i][1]
    print("Line #" + str(i) + ": " + instruction + " " + modifier + number)
    lines_visited[i] = 1
    print(lines_visited)

    if (instruction == 'nop' or instruction == 'jmp') and been_changed == 0 and i >= acc_temp and i not in lines_we_changed:
        
        j=0
        for key, value in lines_visited.items():
            print("Before lines visited line #: " + str(j) + " visited " + str(lines_visited[key]) + " times")
            lines_visited[key] += 1
            print("After lines visited line #: " + str(j) + ", " + str(lines_visited[key]))
            j += 1

    
        print("Going to try changing the instruction for line #" + str(i) + " before: " + instruction + " " + both)
        lines_we_changed[i] = True
        if instruction == 'nop':
            instruction = 'jmp'
            print("Hey we reached this conditionnnnnn")
        elif instruction == 'jmp':
            instruction = 'nop'
        print("Line #" + str(i) + " after: " + instruction + " " + both)
        been_changed = 1
        i_temp = i
        acc_temp = accumulator
        print("Saving i_temp " + str(i_temp) + " and acc_temp " + str(acc_temp))

    if instruction == 'acc':
        # print("Accumulate: " + modifier + number)
        accumulator += int(both)
        i += 1
        if i in lines_visited:
            print("Hey, we've done that before. Stop that.")
            print("Before: i " + str(i) + " and acc " + str(accumulator))
            i = i_temp
            if i == 0:
                print("Need to break out of 0 loop")
                i = i_temp + 1
            accumulator = acc_temp
            been_changed = 0
            print("lines_visited before:")
            print(lines_visited)

            for key, value in list(lines_visited.items()):
                if value == 1:
                    del lines_visited[key]
                else:
                    lines_visited[key] -= 1

            print("lines_visited after:")
            print(lines_visited)
            if input[i][0] == 'noc':
                instruction = 'jmp'
            if input[i][0] == 'jmp':
                instruction = 'noc'
            print("After: i " + str(i) + " and acc " + str(accumulator))
    elif instruction == 'nop':
        # print("NOP: Nothing happening. Incrementing by one.")
        i += 1
        if i in lines_visited:
            print("Hey, we've done that before. Stop that.")
            print("Before: i " + str(i) + " and acc " + str(accumulator))
            i = i_temp
            if i == 0:
                print("Need to break out of 0 loop")
                i = i_temp + 1
            accumulator = acc_temp
            been_changed = 0
            print("lines_visited before:")
            print(lines_visited)

            for key, value in list(lines_visited.items()):
                if value == 1:
                    # print("8675380 WE GOT TO THIS CONDITION")
                    del lines_visited[key]
                else:
                    lines_visited[key] -= 1

            print("lines_visited after:")
            print(lines_visited)
            if input[i][0] == 'noc':
                instruction = 'jmp'
            if input[i][0] == 'jmp':
                instruction = 'noc'
            print("After: i " + str(i) + " and acc " + str(accumulator))
    elif instruction == 'jmp':
        # print("Jumping: " + modifier + number)
        # print(lines_visited)
        i += int(both)
        if i in lines_visited:
            print("Hey, we've done that before. Stop that.")
            print("Temp i: " + str(i_temp))
            print("Before: i " + str(i) + " and acc " + str(accumulator))
            i = i_temp
            if i == 0:
                print("Need to break out of 0 loop")
                i = i_temp + 1
            accumulator = acc_temp
            been_changed = 0

            print("lines_visited before:")
            print(lines_visited)

            for key, value in list(lines_visited.items()):
                if value == 1:
                    # print("8675380 WE GOT TO THIS CONDITION")
                    del lines_visited[key]
                else:
                    lines_visited[key] -= 1

            print("lines_visited after:")
            print(lines_visited)

            if input[i][0] == 'noc':
                instruction = 'jmp'
            if input[i][0] == 'jmp':
                instruction = 'noc'
            print("After: i " + str(i) + " and acc " + str(accumulator))




print("Last line visited: " + str(i))
print("Accumulator number: " + str(accumulator))