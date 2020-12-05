passports = []
with open('input.txt') as f:
    for line in f:
        value = line.split()
        passports.append(value)
f.close()

# print("Passports length: " + str(len(passports)))

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

# print("Total number of passports found: " + str(len(clean_passports)))

valid = 0
valid_byr = 0
valid_iyr = 0
valid_eyr = 0
valid_height = 0
valid_eye_color = 0
valid_hair_color = 0
valid_passport_number = 0
total_valid_points = 0
but_like_actually_valid = 0

# def validate_birth_year(clean_passports, valid_byr):
#     # print("Found a birth year field" )
#     if 1920 <= int(clean_passports[j]['byr']) <= 2002:
#         # print("byr between 1920 and 2002: " + str(clean_passports[j]['byr']))
#         valid_byr += 1
#         # print("Number of valid birth years: " + str(valid_byr))
#     else:
#         # print("Not a valid birthyear: " + str(clean_passports[j]['byr']))
#         valid_byr += 0



j=0
for passport in clean_passports:



    # if (len(clean_passports[j]) <= 6):
    #     # print("Found 6 or fewer fields. This passport is invalid.")
    #     valid += 0
    # elif (len(clean_passports[j]) == 7) and "cid" not in clean_passports[j]:
    #     # print("Only found 7 fields but cid is missing soooo everything's cool, man. Nothing to see here.")
    #     valid += 1
    # elif ((len(clean_passports[j]) == 7)) and "cid" in clean_passports[j]:
    #     # print("Seven fields and missing something other than cid.. Sorry, man. Invalid.")
    #     valid += 0
    # else: 
    #     # print("Found all the fields.")
    #     valid += 1
    # # j += 1

    # if ((len(clean_passports[j]) == 7) and "cid" not in clean_passports[j]):
    if ((len(clean_passports[j]) == 7)):
    # if ((len(clean_passports[j]) == 7) and "cid" not in clean_passports[j]) or len(clean_passports[j]) == 8:
        valid += 1

        # print(str(len(clean_passports[j])))

        # if "byr" in clean_passports[j]:
        #     validate_birth_year(clean_passports, valid_byr)

        # Check for valid birth year 
        if "byr" in clean_passports[j]:
            # print("Found a birth year field" )
            if 1920 <= int(clean_passports[j]['byr']) <= 2002:
                # print("byr between 1920 and 2002: " + str(clean_passports[j]['byr']))
                valid_byr += 1
                total_valid_points += 1
            else:
                # print("Not a valid birthyear: " + str(clean_passports[j]['byr']))
                valid_byr += 0

        # Check for issue year 
        if "iyr" in clean_passports[j]:
            # print("Found a issue year field" )
            if 2010 <= int(clean_passports[j]['iyr']) <= 2020:
                # print("byr between 2010 and 2020: " + str(clean_passports[j]['iyr']))
                valid_iyr += 1
                total_valid_points += 1
            else:
                # print("Not a valid issue year: " + str(clean_passports[j]['iyr']))
                valid_iyr += 0
                
        # Check for expiration year 
        if "eyr" in clean_passports[j]:
            # print("Found an expiration year field" )
            if 2020 <= int(clean_passports[j]['eyr']) <= 2030:
                # print("eyr between 2010 and 2020: " + str(clean_passports[j]['eyr']))
                valid_eyr += 1
                total_valid_points += 1
            else:
                # print("Not a valid expiration year: " + str(clean_passports[j]['eyr']))
                valid_eyr += 0
        

        # hgt (Height) - a number followed by either cm or in:
        # If cm, the number must be at least 150 and at most 193.
        # If in, the number must be at least 59 and at most 76.
        # Check for valid height 

        if "hgt" in clean_passports[j]:
            # print("Found a height field" + str(clean_passports[j]['hgt']))
            # print(str(clean_passports[j]['hgt'][:-2]))

            if clean_passports[j]['hgt'][-2:] == "cm":
                if 150 <= int(clean_passports[j]['hgt'][:-2]) <= 193:
                    # print("This is a valid cm height: " + str(clean_passports[j]['hgt']))
                    valid_height += 1
                    total_valid_points += 1
                    # print(clean_passports[j]['hgt'][:-2])
                else:
                    # print("Nooope not a valid cm height sorry: " + str(clean_passports[j]['hgt']))
                    valid_height += 0
                    # print("looks like we could do it")
            elif clean_passports[j]['hgt'][-2:] == "in":
                if 59 <= int(clean_passports[j]['hgt'][:-2]) <= 76:
                    # print("This is a valid in height: " + str(clean_passports[j]['hgt']))
                    valid_height += 1
                    total_valid_points += 1
                    # print(clean_passports[j]['hgt'][:-2])
                else:
                    # print("Wrong number of inches: " + str(clean_passports[j]['hgt']))
                    valid_height += 0
                    # print("looks like we could do it")

            # if 1920 <= int(clean_passports[j]['byr']) <= 2002:
            #     # print("byr between 1920 and 2002: " + str(clean_passports[j]['byr']))
            #     valid_byr += 1
            # else:
            #     # print("Not a valid birthyear: " + str(clean_passports[j]['byr']))
            #     valid_byr += 0

        # Check for valid eye color 
        valid_eyes = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
        if "ecl" in clean_passports[j]:
            if clean_passports[j]['ecl'] in valid_eyes:
                # print("Found a valid eye color: " + clean_passports[j]['ecl'])
                valid_eye_color += 1
                total_valid_points += 1
            else:
                # print("Invalid eyes: " + clean_passports[j]['ecl'])
                valid_eye_color += 0

        # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.

        # Check for vaid hair color 
        if "hcl" in clean_passports[j] and len(clean_passports[j]['hcl']) == 7 and clean_passports[j]['hcl'][0] == "#":
            # print("We found a 7 digit with # first letter")

            hex_value = clean_passports[j]['hcl'][1:]
            # print(hex_value)
            
            ok_chars = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']

            matched_list = [characters in ok_chars for characters in hex_value]
            # print(matched_list)

            if all(matched_list) == True:
                # print("Looks like they were all correct")
                valid_hair_color += 1
                total_valid_points += 1
            
            # foo = ([pos for pos, char in enumerate(hex_value) if char not in ok_chars])
            # # print(foo)
            # if (len(foo) > 0):
            #     print("Found a wrong hex char")

            # try:
            #     int(clean_passports[j]['pid'])
            #     # print("PID can be converted to int.")
            #     if clean_passports[j]['pid'][0] == '0':
            #         # print(clean_passports[j]['pid'][0])
            #         # print("Yaaas this is a valid passport")
            #         valid_passport_number += 1
            #     else:
            #         valid_passport_number += 0
            #         # print("Not valid. First digit not 0")


        # Check for vaid passport number
        if "pid" in clean_passports[j] and len(clean_passports[j]['pid']) == 9:
            # print("We found a 9 digit pid")
            try:
                int(clean_passports[j]['pid'])
                # print("PID can be converted to int.")
                if clean_passports[j]['pid'][0] == '0':
                    # print(clean_passports[j]['pid'][0])
                    # print("Yaaas this is a valid passport")
                    valid_passport_number += 1
                    total_valid_points += 1
                else:
                    valid_passport_number += 0
                    # print("Not valid. First digit not 0")
            except:
                valid_passport_number += 0
                # print("That's like not even a number")

    # if (len(clean_passports[j]) <= 6):
    #     # print("Found 6 or fewer fields. This passport is invalid.")
    #     valid += 0
    # elif (len(clean_passports[j]) == 7) and "cid" not in clean_passports[j]:
    #     # print("Only found 7 fields but cid is missing soooo everything's cool, man. Nothing to see here.")
    #     valid += 1
    # elif ((len(clean_passports[j]) == 7)) and "cid" in clean_passports[j]:
    #     # print("Seven fields and missing something other than cid.. Sorry, man. Invalid.")
    #     valid += 0
    # else: 
    #     # print("Found all the fields.")
    #     valid += 1

    print("Totally valid thoooo: " + str(total_valid_points))    
    if total_valid_points == 8:
        but_like_actually_valid += 1
        print("But like actually valid: " + str(but_like_actually_valid))
    total_valid_points = 0
    j += 1



# print(type(clean_passports[0]['pid']))

# if "pid" in clean_passports[0] and len(clean_passports[0]['pid']) == 9:
#     print("We found a 9 digit pid")
#     try:
#         int(clean_passports[0]['pid'])
#         print("PID can be converted to int.")
#         if clean_passports[0]['pid'][0] == '0':
#             print("Yaaas this is a valid passport")
#             valid_passport_number += 1
#         else:
#             print("Not valid. First digit not 0")
#     except:
#         print("That's like not even a number")
#     print(clean_passports[0]['pid'][0])


    # isinstance(clean_passports[0]['pid'], int)
    # print(isinstance(clean_passports[0]['pid'], int))
    # print(clean_passports[0])

print("Number of valid birth years: " + str(valid_byr))
print("Number of valid issue years: " + str(valid_iyr))
print("Number of valid expiration years: " + str(valid_eyr))
print("Number of valid heights: " + str(valid_height))
print("Number of valid eyes: " + str(valid_eye_color))
print("Number of valid hair: " + str(valid_hair_color))
print("Number of valid passports: " + str(valid_passport_number))

print("\n" + "Total valid number: " + str(but_like_actually_valid))


'''




# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.

# cid (Country ID) - ignored, missing or not.
'''

# print("Final Answer / Total valid passports found: " + str(valid))