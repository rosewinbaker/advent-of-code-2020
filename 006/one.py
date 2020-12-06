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
all_said_yes_list = []
group_counter = -1
yas = []

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
        group_counter += 1
        # print("This is a blank line / a new group")
        blank_lines.append(i)
        blank_lines.sort()
        if (len(blank_lines) > 1):
            group_size = (blank_lines[-1] - blank_lines[-2]) - 1
            # print("Group #" + str(group_counter) + " size: " + str(group_size))

        k=0
        while (k<len(group_letters)):
            group_count = group_letters.count(group_letters[k])
            if group_size == group_letters.count(group_letters[k]):
                # print("Everyone said yes to: " + group_letters[k])
                yas.append(group_letters[k])
                all_said_yes += 1
            k += 1

        # print("Adding all_said_yes: " + str(len(list(set(yas)))))  
        all_said_yes_list.append(len(list(set(yas))))
        all_said_yes = 0
        yas.clear()
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
print("Questions everyone in group answered yes: " + str(addList(all_said_yes_list)))