'''
split on \n\n

total count = 0

loop through split vals:
    for chars in splitval[i]:
        count unique characters
    if line is blank:
        compare how many unique in lines since last blank line
        add to total count variable
    restart the count

print final answer: total count
'''

answers = []
with open('input.txt') as f:
    for line in f:
        value = line.split("\n\n")
        answers.append(value)
f.close()

# print(answers)

unique_group_chars = 0
blank_lines = []
group_letters = []
unique_group_answers = []

i=0
# while (i<6):
while (i<len(answers)):
    line_answer = answers[i][0].strip("\n")
    unique_line_chars = len(list(set(line_answer)))

    if unique_line_chars != 0:
        # print("Number of unique characters answered yes: " + str(unique_line_chars))
        j=0
        while (j<len(line_answer)):
            group_letters.append(line_answer[j])
            # print(line_answer)
            j += 1
    elif unique_line_chars == 0:
        # print("This is a blank line / a new group")
        blank_lines.append(i)
        blank_lines.sort()
        if (len(blank_lines) > 1):
            group_size = (blank_lines[-1] - blank_lines[-2]) - 1
            # print("# of entries since last blank line: " + str(group_size))

        unique_answers = len(list(set(group_letters)))
        unique_group_answers.append(unique_answers)
        group_letters.clear()
    i += 1

def addList(unique_group_answers) :
     
    # Multiply elements one by one
    result = 0
    for x in unique_group_answers:
         result = result + x 
    return result 
     
print("Total questions answered yes: " + str(addList(unique_group_answers)))