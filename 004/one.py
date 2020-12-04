passports = []
with open('input.txt') as f:
    for line in f:
        value = line.split()
        passports.append(value)
f.close()

print("Passports length: " + str(len(passports)))

# print(passports[4])

clean_passports = []
cleaner_passports = []
pass_dict = {}

i=0
while (i<len(passports)):
# while (i<17):
    for field in passports[i]:
        test = field.split(":")
        pass_dict[test[0]] = test[1]
        # print(pass_dict)
    if len(passports[i]) == 0:
        pass_dict_copy = pass_dict.copy()
        clean_passports.append(pass_dict_copy)
        # print("Here is the full Clean passports as of line " + str(i) + ": ")
        # print(clean_passports)
        # print("\n")
        pass_dict.clear()
    i += 1

print("Total number of passports found: " + str(len(clean_passports)))

valid = 0

j=0
for passport in clean_passports:
    # print(str(len(clean_passports[j])))

    if (len(clean_passports[j]) <= 6):
        # print("Found 6 or fewer fields. This passport is invalid.")
        valid += 0
    elif (len(clean_passports[j]) == 7) and "cid" not in clean_passports[j]:
        # print("Only found 7 fields but cid is missing soooo everything's cool, man. Nothing to see here.")
        valid += 1
    elif ((len(clean_passports[j]) == 7)) and "cid" in clean_passports[j]:
        # print("Seven fields and missing something other than cid.. Sorry, man. Invalid.")
        valid += 0
    else: 
        # print("Found all the fields.")
        valid += 1
    j += 1

print("Final Answer / Total valid passports found: " + str(valid))